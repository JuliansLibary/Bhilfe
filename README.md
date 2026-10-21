# Cone-Rolling-Tool

Mechanische Hilfe zum Formen **leerer Papier-Cones**. Aktuell liegt ein
parametrischer **FreeCAD-P1 mit Tip-Integration** vor. Die ältere OpenSCAD-P0
enthält noch keine Tip-Aufnahme. Physische Funktionstests stehen noch aus.

- [FreeCAD-P1 direkt öffnen](cad/freecad_p1/exports/ConeTip_P1.FCStd)
- [FreeCAD-P1-Komplettpaket als ZIP](dist/ConeTip_FreeCAD_P1.zip)
- [FreeCAD-Anleitung, Montage und Druckgrenzen](cad/freecad_p1/README_FREECAD.md)
- [FreeCAD-Makro zur Neuerzeugung](cad/freecad_p1/ConeTip_P1.FCMacro)
- [OpenSCAD-Datei](cad/ConeRolling_P0.scad)
- [Älteres OpenSCAD-P0-Komplettpaket als ZIP](dist/ConeRolling_OpenSCAD_P0.zip)
- [Neue mechanische Konzeptstudie mit Tip-Integration](docs/tip-integration-konzept.md)
- [Öffnen, Parameter ändern und STL exportieren](cad/README_OPENSCAD.md)
- [STL-Dateien für beide Formatvorgaben](cad/exports)
- [Konzeptstudie und Prototypplan](docs/konzeptstudie.md)
- [Abwicklungsstudie, A4 quer, Maßstab 1:1](docs/abwicklung.svg)

Die Papierformate und Materialwerte sind ausdrücklich Annahmen. Die
Geometrieberechnung benötigt nur Python 3.10 oder neuer, keine Zusatzpakete:

```sh
python3 tools/cone_geometry.py
python3 tools/cone_geometry.py --svg docs/abwicklung.svg
```

Die Rechnung prüft die ideale Papierabdeckung. Sie simuliert weder den
Wickelvorgang noch Reibung, Klebung oder reales Materialverhalten.

Die STL-Dateien im älteren Ordner `cad/exports` enthalten keine Tip-Aufnahme.
Die neuen vier P1-Druckteile stehen in `cad/freecad_p1/exports`. Geometrieprüfung
und reale Wickelfunktion werden ausdrücklich getrennt betrachtet.
