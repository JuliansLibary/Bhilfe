# In OpenSCAD öffnen

1. **ConeRolling_P0.scad** herunterladen. Es ist eine vollständige, eigenständige
   Datei; keine Bibliotheken, Python-Installation oder FreeCAD-Dateien nötig.
2. In OpenSCAD **Datei → Öffnen** wählen und die `.scad`-Datei laden.
3. **F5** startet die Vorschau. Zunächst erscheint die Baugruppe aus Dorn und
   offener Ablage.
4. Im **Customizer** `part` und `paper_format` auswählen. Falls die Seitenleiste
   ausgeblendet ist, unter **Ansicht** den Customizer einblenden. Alternativ die
   gleichnamigen Variablen ganz oben im Quelltext ändern und F5 drücken.
5. Zum Drucken `part = "mandrel"` oder `part = "station"` auswählen, **F6** zum
   vollständigen Rendern drücken, dann **Datei → Exportieren → STL**. Beide Teile
   separat exportieren. Änderungen können auch vor dem Export mit F5 geprüft
   werden. Die Datei selbst mit Strg+S speichern.

Beispiel für die ersten beiden Einstellungen direkt im Quelltext:

```scad
part = "mandrel";
paper_format = "one_quarter";
```

Die vorhandenen Vorgaben **ersetzen**, diese Zeilen nicht zusätzlich anfügen.
Der Customizer kann eigene Werte vorgeben; beim Bearbeiten im Texteditor dieselben
Werte im Customizer kontrollieren.

| `part` | Ergebnis |
|---|---|
| `"assembly"` | gemeinsame Ansicht zur Erklärung, keine Druckorientierung |
| `"mandrel"` | Formdorn mit breitem Griff auf der Druckplatte |
| `"station"` | offene Anlegestation, flach auf der Druckplatte |
| `"print_layout"` | beide Teile getrennt in Drucklage; einzelne STL sind einfacher |

| `paper_format` | Ausgangsannahme |
|---|---|
| `"one_quarter"` | Papier 78 × 44 mm, Zielzone 68 mm, Formkern etwa 90 mm |
| `"king_size_slim"` | Papier 110 × 44 mm, Zielzone 98 mm, Formkern etwa 120 mm |

## Maße ändern

Die übrigen Variablen im oberen Dateibereich sind die zentralen Eingaben.
Papierlänge und Zielzonenlänge verwenden bei **0** die Formatvorgabe. Für ein
anderes tatsächliches Papier `paper_length_override_mm`, `paper_width_mm` und
`glue_width_mm` setzen; die gewünschte Zielzone bei Bedarf über
`zone_length_override_mm` anpassen.

Nach **F5/F6** werden Konizität, Papierhülle, notwendige Kernverlängerung,
Aufnahmen und Basis neu berechnet. Bei zu kleinem Papier stoppt eine
`assert`-Meldung die Erzeugung. Diese Meldung durch Anpassen der Maße beheben;
die Machbarkeitsprüfung nicht entfernen. Der Bereich unter `[Hidden]` enthält
abgeleitete Werte und Module.

6→12 mm sind Durchmesser **innerhalb der Zielzone**. Der verlängerte gesamte
Kern hat andere Enddurchmesser. Die fertige Papiergesamtlänge und ebenen
Endränder sind bei rechteckigem Papier nicht garantiert. Die Abwicklung ignoriert
Papierdicke und Materialverhalten.

## Was dieser Prototyp macht

Der glatte Dorn bestimmt die Innenform. Sein breites Ende besitzt Griff und
Schaft; die schmale Spitze bleibt frei. Die Ablage hält den Schaft in zwei nach
oben offenen U-Aufnahmen. Sie dient dem Anlegen und Ablegen. Die waagerechte
Papierauflage liegt unterhalb des Kerns; sie ist kein tangentialer Rollkanal und
erzwingt keinen Papiervorschub. Eine empirisch ermittelte Anlegekarte kann später
auf der Fläche befestigt werden.

Zum Wickeln den Dorn herausheben, das Papier von Hand herumführen und die freie
Naht schließen. Nach ausreichendem Anziehen der Naht den Dorn am breiten Griff
herausziehen: Das Papier bewegt sich relativ zum Dorn zur schmalen Spitze.
Die Handhabung und die passende Startposition müssen am realen P0 ermittelt werden.

## Drucken und Nacharbeiten

- Einheit **Millimeter**, Importmaßstab **100 %**. Im Slicer die Abmessungen prüfen.
- Dorn mit breiter Griffseite nach unten, wie in `mandrel` vorgegeben; zunächst
  PLA, etwa 0,08–0,12 mm Schichthöhe und ohne Support auf der Formfläche. Der
  gesamte Dorn ist ungefähr 134 beziehungsweise 164 mm hoch.
- Schmale hohe Drucke benötigen ein geeignetes Druckprofil; Brim nach Bedarf.
- Basis flach, als Ausgangspunkt 3 mm Boden und 3 mm Material neben den
  Schaftaufnahmen. Der offene U-Ausschnitt benötigt keine geschlossene Brücke.
- Papierkontaktfläche glätten, sorgfältig reinigen und die fertigen Durchmesser
  messen. Entformen über raue Schichtringe ist ausdrücklich noch zu testen.
- `journal_clearance_mm = 0.5` bezeichnet die Zugabe **am Durchmesser**.
  Vor dem kompletten Druck eine kleine Passungsprobe für den eigenen Drucker machen.
- Vorhandene STL-Dateien verwenden die Standardparameter. Nach Parameteränderungen
  die STL neu exportieren; die alten STL ändern sich nicht automatisch.

Geometriegültigkeit und Mesh-Prüfung belegen keine zuverlässige Wickelfunktion.
Der physische Versuchsplan steht in `../docs/konzeptstudie.md`.

## Geometrisch geprüft

Beide Formatvorgaben wurden mit OpenSCAD 2021.01 ohne Warnungen als binäre STL
exportiert. Alle vier Druckteilnetze sind geschlossen, konsistent orientiert,
haben positives Volumen und bestehen jeweils aus genau einem zusammenhängenden
Körper. Ihre Unterseite liegt bei Z = 0.

| Standardexport | Abmessungen X × Y × Z |
|---|---|
| 1¼-Dorn | 24 × 24 × 134 mm |
| 1¼-Station | 120 × 60 × 23 mm |
| King-Size-Slim-Dorn | 24 × 24 × 164 mm |
| King-Size-Slim-Station | 150 × 60 × 23 mm |

Die gerenderte 1¼-Baugruppe enthält zwei getrennte geschlossene Körper; ihr
Volumen entspricht der Summe der Einzelteile. Ein zusätzlicher Parametersatz
mit geändertem Papier, Zielzone und Durchmessern ließ sich rendern. Zu schmales
Papier, zu kurzes Papier und gleiche Enddurchmesser wurden wie vorgesehen
abgewiesen. Diese Ergebnisse gelten für die geprüften Einstellungen.

## Kommandozeile, optional

Aus dem Repository-Hauptverzeichnis:

```sh
openscad --hardwarnings --export-format binstl -o cad/exports/one_quarter_mandrel.stl -D 'part="mandrel"' cad/ConeRolling_P0.scad
openscad --hardwarnings --export-format binstl -o cad/exports/one_quarter_station.stl -D 'part="station"' cad/ConeRolling_P0.scad
```

Für King Size Slim zusätzlich `-D 'paper_format="king_size_slim"'` verwenden.
Geprüfte Version: OpenSCAD 2021.01. Das Modell benötigt keine externen Module.
