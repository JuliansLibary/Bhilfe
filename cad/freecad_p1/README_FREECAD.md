# ConeTip P1 in FreeCAD

Parametrischer Versuchsstand mit vorgerolltem Tip, äußerer Tip-Kassette,
stumpf anschließendem Vollkern und breitwärts ausziehbarem Schlitten.
Geprüft mit **FreeCAD 1.0.0**. Keine Zusatz-Workbench erforderlich.

**Geometrisch geprüft; Wickelqualität, tatsächliche Klemmkraft und
beschädigungsfreie Entnahme sind noch am gedruckten Prototyp zu prüfen.**
Die frühere OpenSCAD-P0 enthält diese Tip-Integration nicht.

## Direkt öffnen

1. `exports/ConeTip_P1.FCStd` herunterladen beziehungsweise das ZIP entpacken.
2. In FreeCAD **Datei → Öffnen** oder **Strg+O** wählen und die FCStd laden.
3. Im Modellbaum stehen vier nummerierte Druckteile, das Spreadsheet `Parameter`
   und die Gruppe `Referenzen`.
4. Falls nötig axonometrische Ansicht wählen und **Alles einpassen** verwenden.

Die Datei enthält native Skizzen, Rotationen, Pads und Pockets. Sie benötigt das
Makro nach dem Öffnen nicht. Alle 22 Skizzen sind vollständig bestimmt.

## Parameter und Bewegungsstellungen

`Parameter` doppelt anklicken. **Grüne Zellen sind Eingaben**, blaue Werte werden
berechnet. Werte mit Einheit eingeben, etwa `6.5 mm`, und anschließend das
Dokument neu berechnen, üblicherweise mit **F5**.

| Eingabe | Bedeutung / Ausgangswert |
|---|---|
| `TipDiameter` | 6 mm; tatsächlichen Außendurchmesser messen |
| `TipLength` | 18 mm |
| `TipExposed` | 3 mm papierfreier Überstand als Anlegeanforderung |
| `ClampLength` | 2 mm äußere Haltezone |
| `JointGap` | 0,15 mm zwischen Tip und Kern |
| `CoveredTarget` | 68 mm nominelle papierbedeckte Zielzone |
| `WideDiameter` | 12 mm am Ende der nominalen Körperzone |
| `ClampCompression` | 0,04 mm radiale Zustellung nur der oberen Sitzkontur; Versuchsmaß |
| `GuideClearance` | 0,4 mm nominales Führungsspiel; Druckprobe nötig |
| `EdgeChamfer` | nur 0,08 mm am Kernanfang; nicht großzügig nachschleifen |

Die untere Halbkreisaufnahme bleibt im Nominalmaß. Die obere Kontur hat ein
kleines Übermaß zum nominellen Tip-Hüllkörper. **Diese absichtliche Überschneidung
beschreibt eine zu erprobende elastische Klemmung, keine bereits bekannte Kraft.**
Bei `ClampCompression = 0` gibt es im idealen Modell keine Klemmvorspannung.
Druckabweichungen können größer als das vorgesehene Zustellmaß sein: Backen vor
dem Einsatz nachmessen und an Probetips prüfen. Eine kleinere Bohrung nicht durch
kräftiges Zudrehen kompensieren. Die Flächen begrenzen den maximalen Schließweg.

Die folgenden Zustandszellen verändern die Bauteilpositionen direkt:

| Stellung | `Extraction` B17 | `JawLift` B18 | `JawSide` B19 |
|---|---|---|---|
| Wickeln | `0 mm` | `0 mm` | `0 mm` |
| Kern herausgezogen | `=Stroke` | `0 mm` | `0 mm` |
| Produkt entnehmen | `=Stroke` | `12 mm` | `30 mm` |

Die Backe erst hochheben und anschließend seitlich ablegen; bei geschlossenem
Zustand verhindern zwei Stifte seitliches Verschieben. Zum Zurücksetzen zuerst
`JawSide = 0 mm`, dann `JawLift = 0 mm`, zuletzt `Extraction = 0 mm` setzen.
Die mitgelieferte Datei öffnet in Wickelstellung. Keine Antriebssimulation und
keine bewegten Schrauben sind enthalten; diese werden real vorher gelöst.

Die Makroerzeugung validiert die Eingaben. Nach manuellen Spreadsheet-Änderungen
sind Geometrie, Maße und Bewegungen neu zu prüfen. Die FCStd führt keinen
versteckten Python-Code aus und validiert die physikalische Papierpassung nicht
automatisch. Insbesondere `GlueWidth` ist ein dokumentierter Versuchsparameter,
keine implementierte Klebenaht-Simulation.

## Vier Druckteile und zwei Schraubverbindungen

| Datei | Funktion | STL-Druckabmessungen X × Y × Z |
|---|---|---|
| `Base.stl` | Basis, gefangene Führung, Parkanschlag, Kassettenaufnahme | 214,96 × 64 × 27 mm |
| `CoreCarriage.stl` | glatter Kern, Griff, integrierter Schlitten | 40,77 × 22,25 × 106,40 mm |
| `TipCassette.stl` | unterer Sitz, hinterer Tipanschlag, Schiebeanschluss | 12 × 18 × 14,8 mm |
| `UpperJaw.stl` | geführte abnehmbare Oberbacke | 12 × 24 × 8 mm |

Zusätzlich **2 × M3×16-Schrauben mit gut greifbarem Kopf bis Ø10 mm und 2 × M3-Muttern**.
Eine Verbindung klemmt die Backe, die andere parkt den Schlitten. M3×12 ist hier
zu kurz. Muttertaschen berücksichtigen ungefähr 5,7 mm Schlüsselweite; reale
Muttern und Druckmaße prüfen. Die Parkschraube liegt 10,5 mm über der Grundebene,
damit ein Ø10-mm-Kopf den 5-mm-Boden freigibt. Größere Köpfe erfordern eine neue
Kollisionsprüfung. Oberbacke mit Stiften und Schraube ersetzt das
zuvor erwogene Scharnier. Es gibt keinen Scharnierstift und keine FDM-Dauerfeder.

### Drucken

- Einheit **Millimeter**, Slicermaßstab **100 %**. Die vorhandenen STL stehen
  bereits auf Z = 0 in den angegebenen Druckorientierungen.
- Die Basis braucht mindestens etwa **215 mm nutzbare Drucklänge**. Auf einem
  220-mm-Bett bleiben nur etwa 2,5 mm je Seite; ein breiter Brim passt dann nicht.
- PLA ist ein erster Geometriewerkstoff; PETG und Materialeignung werden später
  verglichen. Passungen und Oberflächen sind noch nicht druckverifiziert.
- Kernachse vertikal, breite Griffseite unten: etwa 0,08–0,12 mm Schichthöhe als
  Versuchswert. **Lokale Stützen unter dem seitlich versetzten Schlitten und
  seiner Anbindung sind in dieser einteiligen Drucklage erforderlich.** Die
  konische Papierkontaktfläche bleibt ohne Stützkontakt.
- Auch die untere Kassette hat in der gelieferten Lage Schulterüberhänge neben
  dem schmalen Schiebeanschluss. Dort lokale Stützen verwenden; Nut-Tasche und
  Kontaktfläche anschließend säubern. Die Oberbacke liegt mit der äußeren
  Fläche unten, ihre Sitzkontur öffnet nach oben.
- Führung, Pins, Muttertaschen und Tip-Sitz zuerst an Druckproben prüfen.
  Keine Passung gewaltsam zusammenpressen. Kernfläche glätten und fertig messen.

Für ein späteres supportärmeres Produkt kann Kern und Schlitten zu zwei Teilen
getrennt werden; P1 hält bewusst vier Druckteile bei und dokumentiert den nötigen
lokalen Support. Die mitgelieferten STL gelten nur für die Standardparameter.
Nach Änderungen neu exportieren und im Slicer ausrichten; ein normaler manueller
FreeCAD-Export übernimmt sonst die Baugruppenlage.

### Montage

1. M3-Mutter von unten in die untere Tip-Kassette einsetzen.
2. Kassette von der Mundseite in die Basis schieben, bis der gefangene
   Schiebeanschluss am vorderen Anschlag sitzt. Er nimmt die axiale Last auf.
3. Kern-Schlitten von der breiten Seite in die Führung einsetzen und zum
   Parkanschlag schieben. Die breite Führung trägt das Werkzeug ohne Tip.
4. Zweite M3-Mutter von oben in den seitlichen Parkboss einsetzen. M3×16 von
   außen eindrehen und den Schlitten nur leicht parken.
5. Vorgerollten Tip an seinen hinteren Anschlag legen. Oberbacke über die beiden
   Pins aufsetzen und mit der anderen M3×16-Schraube vorsichtig klemmen.
6. Rundheit, tatsächliche Koaxialität und Stirnspalt prüfen. Führungsspiel und
   Druckschrumpfung sind nicht durch die nominelle CAD-Achse ausgeschlossen.

## Wickeln und Entformen

Tip und Kern bleiben stationär. Das Paper von Hand um beide führen, Klebestreifen
zugänglich halten und die Paper-Naht schließen. Der Paper-Tip wird dadurch nicht
automatisch verklebt: Sein Halt muss durch Umwicklung und Reibung nachgewiesen
werden. Die Positionierkarte beziehungsweise reale Startlage wird erst im
Versuch ermittelt; es ist kein automatischer Rollmechanismus vorhanden.

Nach ausreichendem Anziehen der Naht zuerst die Parkschraube so weit lösen, dass
sie den Schlitten vollständig freigibt. Kern breitwärts herausziehen. Dann
Backenschraube lösen, Oberbacke über die Stifte heben und seitlich ablegen.
Produkt nach oben entnehmen. Nicht nur die Oberbacke direkt über dem Tip schweben
lassen: Sie würde dem späteren Ausheben im Weg stehen.

## Was geometrisch geprüft ist

- Vier gültige Druckkörper mit positivem Volumen, jeweils genau ein Solid und
  ohne gegenseitige Volumenüberschneidungen.
- 22 vollständig bestimmte native Skizzen; FCStd gespeichert und wieder geöffnet.
- Durchgehender Kern-Auszugshub von **78,40 mm** mit einem kontinuierlichen
  Sweepkörper gegen Basis, Backen, nominellen Tip und angenommene Papierhülle.
- Nach Auszug und seitlichem Ablegen der Backe kollisionsfreies Ausheben um
  30 mm; dabei wurden auch gefüllte konservative Produkt-Hüllkörper geprüft.
- Vier geschlossene, konsistent orientierte STL-Netze; STEP-Reimport mit vier
  Solids. Ein geänderter Tip von 6,5 × 20 mm mit angepasster Haltezone und
  Überstand wurde nach dem Wiederöffnen ebenfalls geprüft.
- King-Size-Slim-Vorgabe lässt sich erzeugen, braucht aber eine **272,80 mm lange
  Basis**. Sie ist nicht auf einem üblichen 220-mm-Bett einteilig druckbar.

`validation_report.json` dokumentiert den Testlauf. Die Entwicklertests in
`check_model.py` setzen eine verfügbare FreeCAD-Python-Installation voraus.

## Noch offene Funktionsnachweise

Die Paper-Referenz ist eine ideale Bauraumhülle. Die konservative axiale Grenze
aus der Blattdiagonale setzt eine kontrollierte Startreferenz voraus und ist
**kein Abwicklungs- oder Wickelnachweis** für Zylinder plus Kegel. Ein unbeschnittenes
Blatt kann ungleichmäßige Endränder und lokale Mehrlagen erzeugen. An jeder
Umfangsposition müssen die 3 mm Tip-Überstand und der freie Klemmbereich erhalten
bleiben; die CAD-Hülle erzwingt das nicht.

Pflichtversuche: Tip kippt/ovalisiert nicht beim Wickeln; Paper liegt am
Tip-Kern-Übergang ausreichend sauber; Naht hält; Kern lässt sich herausziehen,
ohne Paper vom Tip zu lösen. Vorläufige Kraftreserve:

```text
kleinste Paper-Tip-Haltekraft >= 2 × größte Kern-Abzugskraft
```

Die obere Sitzkontur überschneidet den unverformten nominalen Tip absichtlich um
etwa 0,75 mm³. Das ist kein starrer kollisionsfreier Einlegezustand, sondern der
geometrische Platzhalter für eine noch ungemessene Klemmverformung. Auch die reale
Freigabe nach dem Öffnen ist physisch zu prüfen. Es wurden keine Druck- oder
Wickelergebnisse erfunden.

## Makro zur Neuerzeugung

`ConeTip_P1.FCMacro` ist eine eigenständige Datei. In FreeCAD **Makro → Makros…**
öffnen, den Makropfad auf den heruntergeladenen Ordner setzen, Datei auswählen
und **Ausführen** wählen. Alternativ ein neues Makro anlegen und den vollständigen
Inhalt einfügen. Jeder Lauf erzeugt ein neues Dokument und bewahrt vorhandene.

Für King Size Slim oben `PAPER_FORMAT = "king_size_slim"` setzen. Das Makro
speichert und überschreibt standardmäßig keine Dateien. Das neue Dokument über
**Datei → Speichern unter** sichern. Native FCStd ist das editierbare Hauptformat;
STEP ist ein Geometrieaustausch und enthält nicht die vollständige Parametrik.
