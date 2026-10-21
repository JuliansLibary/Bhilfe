"""Developer geometry checks. Run with FreeCAD's Python, not required to open FCStd.

Linux package example:
env -u PYTHONHOME -u PYTHONPATH /usr/bin/python3 cad/freecad_p1/check_model.py
"""

from collections import Counter
from pathlib import Path
import json
import math
import runpy
import struct
import sys
import tempfile

for location in ("/usr/lib/freecad-python3/lib", "/usr/share/freecad/Mod"):
    if Path(location).is_dir():
        sys.path.insert(0, location)

import FreeCAD as App
import Part


def set_parameter(doc, alias, setting):
    doc.Parameters.set(doc.Parameters.getCellFromAlias(alias), str(setting) + " mm")
    doc.recompute()


def sweep_solid(shape, displacement):
    """Exact straight sweep from boundary prisms plus initial/final volumes."""
    final = shape.copy()
    final.translate(displacement)
    pieces = [shape, final]
    for face in shape.Faces:
        swept = face.extrude(displacement)
        if swept.Volume > 1e-7:
            assert swept.isValid(), "Invalid swept boundary"
            pieces.append(swept)
    result = pieces[0].multiFuse(pieces[1:]).removeSplitter()
    assert result.isValid() and len(result.Solids) == 1
    return result


def no_intersection(first, second):
    volume = first.common(second).Volume
    assert volume < 1e-5, "Unexpected overlap: %.8f mm3" % volume


def vertical_round_sweep(x0, x1, r0, r1, z0, travel):
    """Exact capsule-section sweep of a cylinder/frustum perpendicular to X.

    Extruding a whole periodic lateral face can self-intersect. Matching capsule
    wires avoid that failure of the general boundary-prism construction.
    """
    def capsule(x, r):
        a = App.Vector(x, -r, z0)
        b = App.Vector(x, -r, z0 + travel)
        c = App.Vector(x, r, z0 + travel)
        d = App.Vector(x, r, z0)
        return Part.Wire([
            Part.makeLine(a, b),
            Part.Arc(b, App.Vector(x, 0, z0 + travel + r), c).toShape(),
            Part.makeLine(c, d),
            Part.Arc(d, App.Vector(x, 0, z0 - r), a).toShape(),
        ])
    swept = Part.makeLoft([capsule(x0, r0), capsule(x1, r1)], True, True)
    assert swept.isValid() and len(swept.Solids) == 1
    return swept


def check_stl(path):
    data = path.read_bytes()
    count = struct.unpack_from("<I", data, 80)[0]
    # FreeCAD Mesh.write() normally writes ASCII STL; accept both encodings.
    if len(data) == 84 + 50 * count:
        triangles = []
        for i in range(count):
            values = struct.unpack_from("<12fH", data, 84 + 50 * i)
            triangles.append([tuple(values[j:j + 3]) for j in (3, 6, 9)])
    else:
        vertices = [tuple(map(float, line.split()[1:]))
                    for line in data.decode("ascii").splitlines()
                    if line.strip().startswith("vertex ")]
        assert len(vertices) % 3 == 0
        triangles = [vertices[i:i + 3] for i in range(0, len(vertices), 3)]
        count = len(triangles)
    points = {}
    edges = Counter()
    signs = Counter()
    parent = []
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    volume = 0
    for tri in triangles:
        ids = []
        for xyz in tri:
            assert all(math.isfinite(v) for v in xyz)
            if xyz not in points:
                points[xyz] = len(points)
                parent.append(len(parent))
            ids.append(points[xyz])
        assert len(set(ids)) == 3
        a, b, c = tri
        volume += (a[0] * (b[1] * c[2] - b[2] * c[1])
                   + a[1] * (b[2] * c[0] - b[0] * c[2])
                   + a[2] * (b[0] * c[1] - b[1] * c[0])) / 6
        for first, second in zip(ids, ids[1:] + ids[:1]):
            edge = tuple(sorted((first, second)))
            edges[edge] += 1
            signs[edge] += 1 if first < second else -1
            parent[find(first)] = find(second)
    assert set(edges.values()) == {2}, "Non-manifold/open mesh"
    assert set(signs.values()) == {0}, "Inconsistent mesh orientation"
    assert len({find(i) for i in parent}) == 1, "Disconnected print mesh"
    assert volume > 0
    coordinates = list(points)
    lower = [min(p[k] for p in coordinates) for k in range(3)]
    upper = [max(p[k] for p in coordinates) for k in range(3)]
    assert abs(lower[2]) < 1e-4, "Print does not sit at Z=0"
    return {"triangles": count, "size_mm": [round(b - a, 4) for a, b in zip(lower, upper)]}


def main():
    root = Path(__file__).resolve().parent
    api = runpy.run_path(str(root / "ConeTip_P1.FCMacro"))
    doc = api["create_document"]()
    report = {"freecad": ".".join(App.Version()[:3]), "preset": "one_quarter"}
    report["fully_constrained_sketches"] = sum(o.TypeId == "Sketcher::SketchObject" for o in doc.Objects)
    report["base_size_mm"] = [doc.Base.Shape.BoundBox.XLength, doc.Base.Shape.BoundBox.YLength, doc.Base.Shape.BoundBox.ZLength]
    report["extraction_stroke_mm"] = api["value"](doc.Parameters, "Stroke")
    no_intersection(doc.TipCassette.Shape, doc.NominalTip.Shape)
    no_intersection(doc.CoreCarriage.Shape, doc.NominalTip.Shape)
    report["intentional_upper_jaw_nominal_tip_overlap_mm3"] = doc.UpperJaw.Shape.common(doc.NominalTip.Shape).Volume
    assert report["intentional_upper_jaw_nominal_tip_overlap_mm3"] > 0
    # Nominal Ø10 mm, 4 mm high thumb heads; larger heads need a new check.
    park_head = Part.makeCylinder(5, 4, App.Vector(api["value"](doc.Parameters, "ParkStart") + 9, 20, 10.5), App.Vector(0, 1, 0))
    tip_head = Part.makeCylinder(5, 4, App.Vector(-5, 0, api["value"](doc.Parameters, "AxisHeight") + 8))
    for body in (doc.Base, doc.CoreCarriage, doc.TipCassette, doc.UpperJaw, doc.NominalTip):
        no_intersection(park_head, body.Shape)
        no_intersection(tip_head, body.Shape)
    report["nominal_10mm_thumb_head_clearance"] = "passed"
    swept = sweep_solid(doc.CoreCarriage.Shape, App.Vector(report["extraction_stroke_mm"], 0, 0))
    for name in ("Base", "TipCassette", "UpperJaw", "NominalTip", "PaperEnvelope"):
        no_intersection(swept, doc.getObject(name).Shape)
    report["continuous_core_extraction"] = "passed"
    for fraction in (0, .1, .25, .5, .75, 1):
        set_parameter(doc, "Extraction", fraction * report["extraction_stroke_mm"])
        api["validate_document"](doc)
    set_parameter(doc, "JawLift", 12)
    set_parameter(doc, "JawSide", 30)
    api["validate_document"](doc)
    # Sweep the full nominal cylindrical tip upwards, conservatively solid.
    p = doc.Parameters
    radius = api["value"](p, "TipDiameter") / 2
    tip_sweep = vertical_round_sweep(0, api["value"](p, "TipLength"), radius, radius,
                                     api["value"](p, "AxisHeight"), 30)
    for body in (doc.Base, doc.CoreCarriage, doc.TipCassette, doc.UpperJaw):
        no_intersection(tip_sweep, body.Shape)
    # Filled paper outer cone is a conservative envelope for the hollow product.
    product_sweep = vertical_round_sweep(
        api["value"](p, "CoreStart"), api["value"](p, "PaperEndBound"), radius + .04,
        api["value"](p, "CoreEndRadius") - api["value"](p, "Slope") * api["value"](p, "EndAllowance") + .04,
        api["value"](p, "AxisHeight"), 30)
    paper_tip_sweep = vertical_round_sweep(api["value"](p, "TipExposed"),
        api["value"](p, "CoreStart"), radius + .04, radius + .04,
        api["value"](p, "AxisHeight"), 30)
    for body in (doc.Base, doc.CoreCarriage, doc.TipCassette, doc.UpperJaw):
        no_intersection(product_sweep, body.Shape)
        no_intersection(paper_tip_sweep, body.Shape)
    report["upward_release_with_jaw_set_aside"] = "passed"
    set_parameter(doc, "JawSide", 0)
    set_parameter(doc, "JawLift", 0)
    set_parameter(doc, "Extraction", 0)
    with tempfile.TemporaryDirectory(prefix="conetip-p1-") as tmp:
        api["export_bundle"](doc, tmp)
        report["print_meshes"] = {path.name: check_stl(path) for path in Path(tmp).glob("*.stl")}
        path = str(Path(tmp) / "ConeTip_P1.FCStd")
        App.closeDocument(doc.Name)
        doc = App.openDocument(path)
        api["validate_document"](doc)
        report["native_reopen"] = "passed"
        import Import
        step_doc = App.newDocument("StepRoundtrip")
        Import.insert(str(Path(tmp) / "ConeTip_P1_assembly.step"), step_doc.Name)
        step_doc.recompute()
        solids = sum(len(obj.Shape.Solids) for obj in step_doc.Objects if hasattr(obj, "Shape") and obj.TypeId != "App::Part")
        assert solids == 4, "STEP must contain exactly four print solids"
        report["step_roundtrip_solids"] = solids
        App.closeDocument(step_doc.Name)
    for alias, setting in (("TipDiameter", 6.5), ("TipLength", 20), ("ClampLength", 2.5), ("TipExposed", 3.5)):
        set_parameter(doc, alias, setting)
    api["validate_document"](doc)
    report["live_parameter_change_after_reopen"] = "passed"
    other = api["create_document"]("king_size_slim")
    api["validate_document"](other)
    report["king_size_base_length_mm"] = other.Base.Shape.BoundBox.XLength
    App.closeDocument(other.Name)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
