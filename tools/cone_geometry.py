"""Ideal, zero-thickness paper development; no CAD or physical process simulation.

Run from the repository root: python3 tools/cone_geometry.py
Use --svg docs/abwicklung.svg to regenerate the concept illustration.
All dimensions are millimetres. Defaults are unverified concept assumptions.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import html
import json
import math
from pathlib import Path


@dataclass(frozen=True)
class PaperCone:
    name: str
    paper_length: float
    paper_width: float
    zone_length: float
    small_diameter: float = 6.0
    large_diameter: float = 12.0
    glue_width: float = 4.0
    core_end_allowance: float = 2.0


ASSUMPTIONS = (
    PaperCone("1¼", 78.0, 44.0, 68.0),
    PaperCone("King Size Slim", 110.0, 44.0, 98.0),
)


def calculate(p: PaperCone) -> dict:
    """Contain one complete sector plus glue in a centred paper rectangle.

    The glue's inner boundary lies on y=0, the strip occupies 0<=y<=g.
    The complete frustum sector occupies -beta<=theta<=0. Its bounding
    box formulas below apply to the intended shallow cones (beta<pi/2).
    The paper's x margins are equal about that bounding box.
    """
    numbers = [v for v in asdict(p).values() if isinstance(v, (int, float))]
    if not all(math.isfinite(v) and v > 0 for v in numbers):
        raise ValueError("All numeric dimensions must be positive and finite")
    if p.large_diameter <= p.small_diameter:
        raise ValueError("This study requires a widening frustum")
    if p.glue_width >= p.paper_width:
        raise ValueError("Glue must leave a non-glued paper area")
    r0, r1 = p.small_diameter / 2, p.large_diameter / 2
    slope = (r1 - r0) / p.zone_length
    alpha = math.atan(slope)
    slant = math.hypot(p.zone_length, r1 - r0)
    k = math.sin(alpha)
    radius0, radius1 = r0 / k, r1 / k
    beta = 2 * math.pi * k
    if beta >= math.pi / 2:
        raise ValueError("Sector wider than supported by these bounding formulas")
    need_length = radius1 - radius0 * math.cos(beta)
    need_width = radius1 * math.sin(beta) + p.glue_width
    x0 = radius0 * math.cos(beta) - (p.paper_length - need_length) / 2
    if x0 <= 0:
        raise ValueError("Paper crosses the virtual apex; this layout is unsuitable")
    maximum_y = max(p.glue_width, p.paper_width - p.glue_width)
    rho_min = x0
    rho_max = math.hypot(x0 + p.paper_length, maximum_y)
    paper_z_min = (rho_min - radius0) * math.cos(alpha)
    paper_z_max = (rho_max - radius0) * math.cos(alpha)
    # Extend the forming surface, so raw rectangular paper does not hang
    # beyond the nominal 68/98 mm target zone. Grip is outside this area.
    core_z_min = paper_z_min - p.core_end_allowance
    core_z_max = paper_z_max + p.core_end_allowance
    return {
        "assumptions": asdict(p),
        "fits_ideal_target_zone": (
            p.paper_length >= need_length and p.paper_width >= need_width
        ),
        "half_angle_deg": math.degrees(alpha),
        "sector_angle_deg": math.degrees(beta),
        "slant_length": slant,
        "development_small_radius": radius0,
        "development_large_radius": radius1,
        "required_rectangle": [need_length, need_width],
        "paper_reserve": [p.paper_length - need_length, p.paper_width - need_width],
        "paper_x0": x0,
        "paper_axial_envelope": [paper_z_min, paper_z_max],
        "minimum_extended_core_length": core_z_max - core_z_min,
        "extended_core_end_diameters": [
            2 * (r0 + core_z_min * slope),
            2 * (r0 + core_z_max * slope),
        ],
        "radial_release_after_3mm": 3 * slope,
    }


def write_svg(path: Path, studies: list[dict]) -> None:
    """A4 landscape, true-scale developments, not a cutting template."""
    blocks = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="210mm" viewBox="0 0 297 210">',
        '<rect width="297" height="210" fill="white"/>',
        '<style>text{font-family:Arial,sans-serif;fill:#15283b} .small{font-size:3.2px} .title{font-size:6px;font-weight:bold}</style>',
        '<text x="14" y="17" class="title">Cone-Rolling-Tool · Abwicklungsstudie</text>',
        '<text x="14" y="25" class="small">Annahmen, kein Prototypnachweis · Maßstab 1:1 bei Ausdruck ohne Seitenanpassung</text>',
        '<text x="14" y="32" class="small">Kein Zuschnitt: Blau zeigt eine vollständig umschlossene Zielzone im rechteckigen Papier.</text>',
    ]
    for paper_x, study in zip((16, 148), studies):
        p = study["assumptions"]
        paper_y = 62
        radius0 = study["development_small_radius"]
        radius1 = study["development_large_radius"]
        beta = math.radians(study["sector_angle_deg"])
        def point(radius: float, theta: float) -> str:
            x = paper_x + radius * math.cos(theta) - study["paper_x0"]
            y = paper_y + p["glue_width"] - radius * math.sin(theta)
            return f"{x:.4f},{y:.4f}"
        # Sample the circular arcs for a portable vector illustration.
        points = [point(radius1, -beta * i / 160) for i in range(161)]
        points += [point(radius0, -beta * i / 160) for i in range(160, -1, -1)]
        blocks += [
            f'<text x="{paper_x}" y="49" font-size="4.5" font-weight="bold">{html.escape(p["name"])}</text>',
            f'<text x="{paper_x}" y="55" class="small">Papier {p["paper_length"]:g} × {p["paper_width"]:g} mm; Zielzone {p["zone_length"]:g} mm</text>',
            f'<rect x="{paper_x}" y="{paper_y}" width="{p["paper_length"]}" height="{p["paper_width"]}" fill="#f4f6f8" stroke="#44546a" stroke-width="0.25"/>',
            f'<rect x="{paper_x}" y="{paper_y}" width="{p["paper_length"]}" height="{p["glue_width"]}" fill="#fde8ad"/>',
            f'<polygon points="{" ".join(points)}" fill="#b6dfe8" fill-opacity="0.75" stroke="#156c80" stroke-width="0.25"/>',
            f'<line x1="{paper_x}" y1="{paper_y+p["glue_width"]}" x2="{paper_x+p["paper_length"]}" y2="{paper_y+p["glue_width"]}" stroke="#ae6d00" stroke-width="0.25" stroke-dasharray="1 1"/>',
            f'<text x="{paper_x}" y="116" class="small">Blau: Innengeometrie Ø6 → Ø12 mm</text>',
            f'<text x="{paper_x}" y="123" class="small">Gelb: angenommener Klebestreifen, 4 mm</text>',
            f'<text x="{paper_x}" y="130" class="small">Benötigt: {study["required_rectangle"][0]:.2f} × {study["required_rectangle"][1]:.2f} mm</text>',
        ]
    blocks += [
        '<text x="14" y="148" class="small">Die übrigen Papierzonen wickeln zusätzlich mit: variable Überdeckung und ungleichmäßige Endränder.</text>',
        '<text x="14" y="155" class="small">Die Zeichnung beschreibt die Abwicklung, nicht die Startlage oder den Vorschub des realen Rollvorgangs.</text>',
        '<text x="14" y="162" class="small">Papierdicke, Klebung, Reibung und elastische Rückstellung sind hier nicht modelliert.</text>',
        '<line x1="16" y1="180" x2="66" y2="180" stroke="#15283b" stroke-width="0.4"/>',
        '<path d="M16,178 v4 M66,178 v4" stroke="#15283b" stroke-width="0.4"/>',
        '<text x="16" y="188" class="small">Kontrollmaß: 50 mm</text>',
        '</svg>',
    ]
    path.write_text("\n".join(blocks), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--svg", type=Path, help="Write the concept development drawing")
    args = parser.parse_args()
    studies = [calculate(p) for p in ASSUMPTIONS]
    if args.svg:
        write_svg(args.svg, studies)
    print(json.dumps(studies, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
