# Konzeptstudie: Werkzeug für leere Papier-Cones

Stand: 21. Oktober 2026. Entwicklungsstand A–C und Versuchsplanung P0.
Auf Nutzerwunsch erfolgt die CAD-Umsetzung jetzt in OpenSCAD. Ein erstes
parametrisches P0-Modell liegt in `../cad/ConeRolling_P0.scad`; die nachfolgenden
Funktionsannahmen bleiben bis zu physischen Versuchen unbestätigt.

**Empfehlung:** Zuerst einen glatten Wechsel-Formdorn mit offener Anlegestation
entwickeln. P0 soll zeigen, ob Papieraufnahme, Wickeln, Kleben und Entformen
reproduzierbar funktionieren. Ein mechanischer Zwangsvorschub ist erst sinnvoll,
wenn der reale Papierbewegungsablauf bekannt ist. Die Bewertung ist eine
technische Vorauswahl, kein Nachweis eines marktreifen Produkts.

## 1. Funktionsanalyse und Abgrenzung

Das Werkzeug formt handelsübliches Papier zu einem leeren Kegelstumpf mit offenem
schmalem Ende. Befüllen, Stopfen und Filterherstellung gehören nicht zu diesem
Projekt. Ein eingelegter Filter wird für P0 nicht vorausgesetzt.

Der Arbeitsablauf umfasst sechs Teilfunktionen:

1. Papier und Klebestreifen erkennen, positionieren und ausrichten.
2. Eine erste, noch unverklebte Überdeckung um die Form anlegen.
3. Das Papier unter geringer, verteilter Spannung aufwickeln. Dabei muss es seine
   Richtung ändern und auf der Ablage gleiten können.
4. Den Klebestreifen freilegen, befeuchten und auf die Papierüberdeckung drücken.
5. Die Naht entsprechend dem verwendeten Papier ausreichend anziehen lassen.
6. Den Formdorn herausziehen und den fertigen Hohlkörper ablegen.

Beim freien Rollen fehlen eine definierte Innenkontur und eine reproduzierbare
Referenz für den Anlegewinkel. Zu hohe oder ungleichmäßige Spannung verzieht das
Papier; eine bereits fixierte falsche Lage erzeugt Falten. Feuchte Klebung,
unterschiedliche Papiersteifigkeit und die Bewegung beim Entnehmen verändern das
Ergebnis zusätzlich. Ein Werkzeug muss deshalb Geometrie und Orientierung
vorgeben, ohne das Blatt während des Wickelns zu überbestimmen.

Erfolgsfaktoren sind eine glatte Formfläche, eine freie Klebenaht, genügend
Papierüberdeckung, eine bewegliche Papierzuführung und ein freier Entformungsweg.
Ein trichterförmiger Hohlraum allein löst diese Aufgaben nicht: Beim Einschieben
des rechteckigen Blatts ist weder dessen Lage noch die Überlappung festgelegt.

## 2. Geometrische Machbarkeit

### Annahmen für den ersten Vergleich

Die folgenden Werte sind **Arbeitsannahmen**, keine vermessenen Angaben eines
bestimmten Papierherstellers. Vor CAD-Freigabe müssen reale Blätter einschließlich
Gummierung vermessen werden. Die Formatbezeichnung allein reicht nicht.

| Parameter | 1¼ | King Size Slim | Bedeutung |
|---|---:|---:|---|
| Papierlänge P | 78 mm | 110 mm | entlang des Klebestreifens |
| Papierbreite H | 44 mm | 44 mm | quer zum Klebestreifen |
| Klebestreifen g | 4 mm | 4 mm | angenommene Breite, durchgehend |
| Vollständig umschlossene axiale Zielzone L | 68 mm | 98 mm | keine zugesicherte fertige Gesamtlänge |
| Dorn-Durchmesser an Anfang/Ende dieser Zone | 6 / 12 mm | 6 / 12 mm | Innenkontur auf dem Dorn |
| Papierdicke | 0,03 mm | 0,03 mm | Startannahme; nicht in der Abwicklungsrechnung |

Die kleinen Durchmesser bieten einen handhabbaren offenen Auslass. Die breite
Seite bleibt bei 12 mm unter dem verfügbaren Papierumfang. Diese Wahl soll zuerst
die Mechanik prüfen; sie ist keine Optimierung für eine bestimmte Füllmenge.
L wird zunächst kürzer als P gewählt, um der nicht geraden Papierendkontur Raum
zu lassen. Die beiden Längen benötigen bei gleichen Enddurchmessern verschiedene
Kegelwinkel und damit getrennte Formdorne.

### Warum ein rechteckiges Blatt keine exakten ebenen Endränder ergibt

Die Abwicklung eines Kegelstumpfs ist ein Kreisringsektor. Ein Rechteck kann diese
Fläche überdecken, erzeugt dabei aber örtlich unterschiedliche Überdeckung und
ungleichmäßige Endränder. Am schmalen Ende können mehrere Papierlagen entstehen.
Zwei exakt ebene Stirnkanten und eine exakt festgelegte Gesamtlänge sind bei
diesem Vorgehen nicht zugesichert. Dafür wäre Beschnitt oder ein angepasster
Sektorzuschnitt erforderlich. P0 soll mit unverändertem Standardpapier arbeiten;
das Endrandverhalten wird gemessen.

Die einfache Rechnung „Umfang plus Klebenaht kleiner als Papierbreite“ ist eine
nützliche Vorprüfung. Sie berücksichtigt die Abwicklung und die Lage der Naht
jedoch nicht vollständig.

### Nachvollziehbare Abwicklungsrechnung

Mit r0 = 3 mm, r1 = 6 mm und dr = r1 − r0 gelten:

```text
s = sqrt(L² + dr²)             Mantellänge der Zielzone
alpha = atan(dr / L)           halber Öffnungswinkel
k = sin(alpha)
R0 = r0 / k; R1 = r1 / k       Radien in der ebenen Abwicklung
beta = 2*pi*k                  Winkel des vollständigen Sektors, in Radiant
```

Für die flachen Kegel dieser Studie liegt der Sektor zwischen theta = −beta und
0. Die innere Grenze des Klebestreifens liegt auf der radialen Linie y = 0;
der Klebestreifen belegt 0 ≤ y ≤ g. Der übrige Papierbereich liegt darunter.
Dann genügt für Zielsektor plus Klebestreifen folgendes Rechteck:

```text
P_min = R1 − R0*cos(beta)
H_min = R1*sin(beta) + g
```

Die Formeln setzen hier beta < 90° voraus. Die Implementierung weist andere
Fälle zurück. Die Zeichnung zeigt die Abwicklung, **keine bereits validierte
Startlage oder Steuerkurve des Wickelvorgangs**.

| Rechnerisches Ergebnis | 1¼ | King Size Slim |
|---|---:|---:|
| Halber Öffnungswinkel alpha | 2,526° | 1,753° |
| Voller Öffnungswinkel | 5,052° | 3,507° |
| Abwicklungswinkel beta | 15,867° | 11,015° |
| Mantellänge s | 68,066 mm | 98,046 mm |
| Benötigtes Rechteck P_min × H_min | 70,660 × 41,219 mm | 99,852 × 41,467 mm |
| Verbleibende Papierreserve längs / quer | 7,340 / 2,781 mm | 10,148 / 2,533 mm |

Damit ist die vollständige Überdeckung der Zielzone einschließlich vorhandenem
Klebestreifen im idealen Modell ohne Papierdicke rechnerisch möglich. Die
Querreserve ist relativ klein. Sie ist keine pauschale zulässige Positionier-
oder Fertigungstoleranz. Andere Papierbreiten oder größere Durchmesser erfordern
eine erneute Rechnung.

Das gesamte Rechteck muss unterstützt werden, auch außerhalb dieser Zielzone.
Für die in der Zeichnung verwendete, längs zentrierte Lage gilt:

```text
x0 = R0*cos(beta) − (P − P_min)/2
rho_min = x0
rho_max = sqrt((x0 + P)² + max(g, H − g)²)
z_min/max = (rho_min/max − R0)*cos(alpha)
```

| Vollständige Papierhülle, relativ zum Beginn der Zielzone | 1¼ | King Size Slim |
|---|---:|---:|
| Axialer Bereich | −6,258 bis 77,271 mm | −6,877 bis 107,008 mm |
| Notwendige Formfläche inklusive 2 mm Reserve je Ende | 87,529 mm | 117,885 mm |
| Vorläufig aufgerundete Formkernlänge | ca. 90 mm | ca. 120 mm |

Die Verlängerungen folgen derselben Konizität. Der vollständige Dorn hat deshalb
andere Enddurchmesser als die innerhalb liegende 6→12-mm-Zielzone. Ein nur 68 oder
98 mm langer Dorn würde das unbeschnittene Papier nicht vollständig unterstützen.
Die Hüllrechnung gilt für die abschließende ideale Lage; zusätzlichen Bewegungs-
raum während des Wickelns muss P0 prüfen.

Der Außendurchmesser des fertigen Cones ist wegen Papierdicke, örtlich mehreren
Lagen und Rückstellung nicht gleich dem Dorn-Durchmesser. Glatte Geometrie allein
beweist weder Entformbarkeit noch Faltenfreiheit.

## 3. Drei mechanische Konzepte

### A — Wechsel-Formdorn mit offener Anlegestation

**Prinzip:** Eine offene Ablage erleichtert Orientierung und erste Überdeckung.
Der glatte Dorn wird anschließend mit dem Papier herausgehoben und von Hand
weitergedreht. Das Papier darf dabei frei schwenken. Die Klebenaht bleibt offen
zugänglich. Nach dem Anziehen der Naht wird der Kern am breiten Griff entnommen.

**Bauteile:** ein Formdorn mit integriertem Griff; eine Ablage mit Papierauflage,
Orientierungsmarkierungen und offener Griffaufnahme. Für eine zweite Geometrie
wird nur der Dorn gewechselt. Markierungen zunächst auf austauschbarer Karte,
damit sich die Anlegeposition ohne Neudruck korrigieren lässt.

**Vorteile:** wenige Teile, freie Sicht, kein enger Papierkanal, einfache
Reinigung, keine Trennfuge auf der Formfläche. Die relevante Geometrie ist direkt
messbar. Der breite Griff bietet eine sichere Handposition.

**Schwachstellen:** Das Anlegen bleibt teilweise eine Handfertigkeit. Eine
Anfänger-Eignung und eine passende Startmarkierung sind noch nicht nachgewiesen.
Eine Karte ist eine Hilfe zur Ausgangslage, keine Zwangsführung der gesamten
Bewegung. Einhandbedienung wird für P0 nicht versprochen.

**Aufwand / erwartetes Ergebnis:** niedrig; präzise Innenkontur bei gelungener
Wicklung, aber zunächst bedienerabhängige Naht und Endränder.

### B — Formdorn mit aufklappbarer Negativschale

**Prinzip:** Das Papier wird um den Dorn vorgelegt und mit zwei öffnenden
Schalensegmenten gestützt. Die Schale glättet beziehungsweise hält; sie ersetzt
das vorherige Anlegen nicht. Eine ausreichend breite Längsöffnung hält die
Klebenaht erreichbar. Nach dem Kleben werden beide Segmente vollständig geöffnet.

**Bauteile:** Dorn, zwei Schalenteile, Scharnier und begrenzter Verschluss; eine
integrierte elastische Verbindung wäre gesondert auf Dauerhaltbarkeit zu prüfen.

**Vorteile:** mehr Unterstützung bei geringer Fingerfertigkeit; ruhige Lage beim
Andrücken der Naht; eventuell gleichmäßigerer Anpressdruck.

**Schwachstellen:** Einklemmen und Quetschfalten an Schließkanten, verdeckte
Fehllagen, erschwerte Reinigung. Ein starrer FDM-Spalt kann eine wenige
Hundertstelmillimeter dicke, unterschiedlich mehrlagige Papierhülle nicht präzise
regeln. Nachgiebigkeit ist wichtiger als ein vermeintlich exakt papierdicker Spalt.

**Aufwand / erwartetes Ergebnis:** mittel; potenziell bessere Haltefunktion,
zusätzliche Fehlermöglichkeiten beim Schließen. Kein Nachweis automatischen Rollens.

### C — Rotierender Dorn mit unabhängig nachgiebigen Druckrollen

**Prinzip:** Ein einseitig gelagerter Dorn wird am Handrad gedreht. Mehrere schmale,
unabhängig frei laufende Rollen drücken lokal an. Eine offene, nachgiebige
Papierauflage erlaubt Schwenken. Zum Kleben werden Rollen angehoben; anschließend
wird zum schmalen, freien Dornende entformt.

**Bauteile:** Dorn/Handrad, Lagerbasis, beispielsweise drei Rollen mit separaten
Achsen und nachgiebigen Haltern, gemeinsamer Öffnungsbügel und offene Auflage.

**Vorteile:** potenziell kontrollierbarer Druck, weniger unmittelbarer
Fingerkontakt und ein geführter Drehvorgang.

**Schwachstellen:** Einzug und erster Wickelkontakt bleiben anspruchsvoll.
Unterschiedliche Rollenlasten können schräg ziehen. Klebstoff kann Rollen
verschmutzen. Der Aufbau verlangt mehr Justage, Bauraum und Reinigung.

**Kinematische Grenze:** Es gilt v(z) = omega*r(z). Bei 3→6 mm Radius variiert die
Umfangsgeschwindigkeit entlang der Zielzone um Faktor zwei. Eine parallel
festgehaltene Papierkante oder ein überall gleich schnell laufendes Band ist
damit nicht als schlupffreier Vorschub geeignet. Das Blatt muss sich in seiner
Ebene drehen können; bei idealem Abrollen ist der virtuelle Kegelscheitel der
Bezugspunkt. Separate frei laufende Rollen lösen die unterschiedlichen örtlichen
Geschwindigkeiten, beweisen aber noch keinen zuverlässigen Papiereinzug.

**Aufwand / erwartetes Ergebnis:** hoch; interessantes Ausbaukonzept, dessen
Bedienvorteil erst am Versuch bewiesen werden muss.

## 4. Gewichtete Vorauswahl

Punkte 1 = ungünstig bis 5 = günstig. Alle Punkte sind **begründete
Entwicklungseinschätzungen**, keine Messwerte. Herstellungsaufwand bewertet
einfache Fertigung und geringe Teilezahl positiv.

| Kriterium | Gewicht | A | B | C |
|---|---:|---:|---:|---:|
| Erwartete Formqualität | 25 % | 4 | 4 | 4 |
| Einfache Bedienung | 20 % | 3 | 4 | 4 |
| Reproduzierbarkeit | 20 % | 3 | 4 | 4 |
| Mechanische Zuverlässigkeit | 15 % | 5 | 3 | 3 |
| Herstellungsaufwand | 10 % | 5 | 3 | 2 |
| Ergonomie | 10 % | 4 | 4 | 4 |
| **Gewichtete Summe** | **100 %** | **3,85** | **3,75** | **3,65** |

A erhält die Vorzugsempfehlung für P0, weil offene Zugänglichkeit und wenige
Fehlerquellen derzeit besonders wertvoll sind. B und C erhalten höhere
Bedienpunkte wegen ihrer möglichen Halte-/Druckunterstützung. Die Unterschiede
sind klein: Schon ein zusätzlicher Bedienpunkt für B würde dessen Rang ändern.
Die Matrix begründet den günstigsten Lernschritt, keinen sicheren Seriensieger.

## 5. Vorzugsarchitektur und konstruktive Leitplanken

- Griff und Aufnahme liegen ausschließlich hinter dem breiten Ende der gesamten
  Papierhülle. Die Spitze bleibt frei. Keine Nut, Federklemme, umlaufende Schulter
  oder Erhebung liegt auf der Formfläche oder im Abzugsweg.
- Beim Entformen bewegt sich das Papier relativ zum Dorn zur schmalen Spitze;
  entsprechend wird der Dorn am breiten Griff aus dem Papier gezogen. Das Papier
  wird nur sanft und verteilt gehalten, nicht am kleinen Ende zusammengeklemmt.
- Konizität schafft beim Abziehen Spiel: 3 mm Axialbewegung ergeben radial
  0,132 mm bei L = 68 beziehungsweise 0,092 mm bei L = 98. Reibung oder anhaftender
  Klebstoff können die Entformung trotzdem verhindern.
- Die offene Aufnahme dient dem Einlegen und Ablegen. Für P0 ist kein dauerhaft
  gefesselter Drehvorgang erforderlich. Papieranschläge dürfen nach dem Anlegen
  keine Kante während des Wickelns festhalten.
- Orientierung von Klebestreifen, großer und kleiner Seite durch sichtbare
  Markierungen. Keine erhabenen Logos, Rändelungen oder Linien auf der
  Papierkontaktfläche. Eine runde Griffkontur mit zwei flachen Fingerflächen kann
  Handhabung und Ablegen verbessern.
- Ein geteilter oder kollabierender Kern wird erst bei nachgewiesenem Bedarf
  verfolgt. Eine zusätzliche Trennfuge ist zunächst ein unnötiges Oberflächenrisiko.

### FDM-Ausgangswerte, sämtlich vorläufig

| Merkmal | P0-Ausgangswert / Vorgehen |
|---|---|
| Material | zunächst PLA für Geometrie und Nacharbeit; PETG anschließend vergleichend |
| Dorn | vorzugsweise massiv; bei diesen kleinen Durchmessern überschaubarer Materialbedarf |
| Basis | 2,4 mm tragende Wand als Startwert für 0,4-mm-Düse; Druckprofil tatsächlich prüfen |
| Druckrichtung Dorn | Achse vertikal, breite Griffseite unten; Kontaktfläche ohne Support |
| Schichthöhe | 0,08–0,12 mm als Startbereich; Qualität des konkreten Drucks entscheidet |
| Oberfläche | sorgfältig glätten und reinigen; fertige Durchmesser nachmessen |
| Griff | vorläufig Ø22–26 mm, 20–25 mm lang; anhand Handhabung prüfen |
| Spiel einer offenen Griffaufnahme | 0,3 / 0,5 / 0,7 mm Durchmesserzugabe mit Probekörper vergleichen |
| Übergänge | kleine, verrundete Endkanten außerhalb der Zielzone; etwa 0,5 mm Startwert |

Ringförmige Schichtstufen des vertikalen Drucks wirken dem axialen Entformen
entgegen. Deshalb ist feine Schichthöhe allein kein Oberflächennachweis. Nacharbeit
verändert die Maße; entscheidend sind fertig gemessene Dornkontur und tatsächliche
Abzugskraft. Horizontaler Druck bringt auf der Kontaktfläche leichter Support-
oder Abflachungsfehler. Die Basis wird flach und der Dorn separat gedruckt.

Für Papierkontakt werden keine ungetesteten Schmiermittel oder Beschichtungen
vorausgesetzt. Geometrieprototypen belegen noch keine Materialeignung für ein
später angebotenes Endprodukt. Zerlegbarkeit und offene Flächen unterstützen die
Reinigung; konkrete Reinigungsmittel müssen zum gewählten Material passen.

## 6. Konkreter Versuchsplan

### P0a — Papierbewegung und Oberfläche, zunächst nur 1¼

1. Mindestens zehn reale Blätter eines konkreten Papiers vermessen: P, H,
   Klebestreifen, Streuung und Faserverhalten dokumentieren. Dicke bei Bedarf an
   einem trockenen Blattstapel messen und durch Blattzahl teilen.
2. Zunächst den vollständigen 1¼-Dorn mit etwa 90 mm Formfläche und eine offene
   Ablage herstellen. Vor dem vollständigen Druck die Griffpassung an einem
   kleinen Probekörper prüfen.
3. Anlegekarte mit korrigierbaren Markierungen verwenden. Die Abwicklung liefert
   die zulässige Endlage; den tatsächlichen Startwinkel und Schwenkweg im Versuch
   ermitteln. Nichts durch einen festen Anschlag erzwingen.
4. Zehn vollständige Wickel-, Klebe- und Entformvorgänge durchführen. Kamera von
   oben, dann seitlich; Klebevorgang und Wartezeit getrennt protokollieren.
5. Knicke, örtliche Mehrlagen, Papierreste auf dem Kern, Nahtlage und beschädigte
   Endränder festhalten. Bei Fehlschlag zuerst unterscheiden: falsches Format,
   falsche Anlegeposition, raue Oberfläche, zu hohe Spannung oder Klebstoffkontakt.

Vorläufiger Übergang zu P0b: mindestens 9 von 10 Versuchen ohne Riss, bleibenden
Querknick, offene durchgehende Naht oder Beschädigung beim Abziehen. Das ist eine
Entwicklungsgrenze, keine statistische Absicherung. Beim Scheitern genau eine
plausible Einflussgröße ändern und den betroffenen Versuch wiederholen.

### P0b — Vergleich mit und ohne Anlegehilfe

Fünf unerfahrene Personen erhalten dieselbe kurze Anleitung und je zwei nicht
gewertete Übungsversuche. Danach je sechs Durchgänge mit und sechs ohne Ablage,
abwechselnde Reihenfolge zwischen Personen. Das ergibt 30 gewertete Versuche pro
Variante. Derselbe fertig gemessene Dorn und dasselbe Papierlos dienen als
Vergleichsbasis. Die Ablage soll einen messbaren Vorteil gegenüber dem Dorn allein
bringen; ihre bloße Existenz rechtfertigt sie nicht.

| Eigenschaft | Messung | Vorläufiges Entwicklungsziel |
|---|---|---|
| Fehlerfreies Ergebnis | Riss, bleibender Querknick, Nahtöffnung, Entformschaden einzeln erfassen | mindestens 27/30 je Variante; Verbesserung der Ablage gesondert ausweisen |
| Anlegen | Video und Anzahl nötiger Neuansätze | höchstens ein Neuansatz bei mindestens 27/30 |
| Klebekante | Sichtprüfung über der gesamten Zielzone | vollständig erreichbar, kein notwendiges Öffnen der schon geformten Wicklung |
| Entformen | Video, Schäden, optional niedrige Zugkraftmessung an Dorn und flächiger Papierhalterung | keine Risse/Quetschung; Kraftziel zunächst ≤2 N als zu prüfende Annahme |
| Formtreue | Konturfotos mit Maßstab, zwei um 90° versetzte Ansichten, definierte Längsreferenz an der Naht | vorläufig maximal ±0,5 mm Abweichung zur papierdickenkorrigierten Soll-Außenkontur |
| Naht | Aufnahme unmittelbar und 60 s nach Entnahme | keine sichtbare Wiederöffnung der Zielzone |
| Zeit | aktive Zeit und Klebe-Wartezeit getrennt; Median und Streuung | Lerntrend und Vorteil der Ablage zeigen; zunächst kein unbelegtes Geschwindigkeitsversprechen |
| Reinigung | 20 Zyklen und anschließende Sicht-/Funktionsprüfung | keine verbleibende klebrige Stelle auf der Formfläche |

Eine Schieblehre kann den weichen Cone zusammendrücken; Konturfotos sind zunächst
die bessere Messmethode. Für Fotovergleiche eine definierte Stelle der Klebenaht
als Längsreferenz markieren und die Sollkontur darauf beziehen. Messunsicherheit
und örtliche Mehrlagigkeit dokumentieren. Ein 30er Versuch belegt keine
Serienzuverlässigkeit und sagt noch nichts über andere Papiersorten.

### P0c — Skalierung und Entscheidung

Nach erfolgreicher kurzer Variante den zweiten Dorn mit eigener Konizität
herstellen und die kritischen Versuche wiederholen. PETG, eine zweite Papiersorte
und Links-/Rechtshandbedienung anschließend vergleichen. Den langen Dorn nicht
einfach durch Verlängern des kurzen erzeugen: gleiche Enddurchmesser verlangen
einen neuen Winkel.

Bei hoher Streuung ausschließlich im Anlegen wird die Karte verbessert. Bei
instabiler Handhaltung kann B als Halteschale helfen. Erst wenn Fingerandruck und
kontrollierte Drehung nachweislich die Begrenzung sind, wird C mit Druckrollen
weiterentwickelt. Raue Oberflächen werden zuerst bearbeitet; sie sind kein
Argument für einen komplexeren Mechanismus.

## 7. Umsetzung in OpenSCAD

Das erste P0-Modell steht als eigenständige `.scad`-Datei bereit. Es enthält:

- Zentrale Eingaben für Papierformat, Klebestreifen, Zielzone, Durchmesser,
  Griffmaße und Spiel. Kegelwinkel, Papierhülle und notwendige Kernverlängerung
  werden bei jeder Neuerzeugung berechnet. Der Winkel ist keine zusätzliche,
  widersprüchliche unabhängige Eingabe.
- Benannte Module für Formdorn, offene Schaftaufnahmen, Basis und Drucklagen.
  Das Dornprofil wird rotationssymmetrisch erzeugt, seine äußeren Kanten werden
  im Profil gerundet. Die Aufnahmen bleiben nach oben vollständig offen.
- Eine Baugruppenansicht und getrennte Ausgaben für jedes Druckteil. Der Dorn
  steht in seiner Drucklage auf dem breiten Griff; die Station liegt flach.
- Eingabeprüfungen mit `assert`, insbesondere für zu kleines Papier und ungeeignete
  Geometrie. Ein Neuaufbau erzeugt die Geometrie direkt aus den aktuellen Eingaben.

Die reale Anlegebewegung bleibt eine Versuchsaufgabe. Deshalb enthält die Station
keinen starren Vorschub und keine behauptete tangentiale Führung des Papiers.
Die horizontale Ablage liegt unter dem Kern; der Dorn wird zum Wickeln ausgehoben.

Die editierbare Quelle ist SCAD. Pro Druckteil werden STL-Dateien in Millimetern
ausgegeben. Ein STEP-Export ist mit diesem OpenSCAD-Workflow nicht bereitgestellt.
Vor Druck sind Maßstab, Passung und Oberfläche am konkreten Drucker zu prüfen.

## 8. Nachweisstand

Die Formeln wurden mit Python numerisch ausgewertet und die beiden Abwicklungen
als maßstäbliche SVG erzeugt. Die idealen Zielzonen passen unter den genannten
Annahmen in die jeweiligen Rechtecke. Die Berechnung ist mit
`python3 tools/cone_geometry.py` reproduzierbar und benötigt keine Fremdpakete.
Eine unabhängige numerische Gegenprüfung hat pro Format 40.401 Sektorpunkte und
8.241 Punkte des Klebestreifens samt unterliegender Papierlage auf Einschluss im
Rechteck geprüft. Die Flächenidentität des Sektors mit der Kegelmantelfläche und
die Erkennung zu schmaler beziehungsweise zu kurzer Papierbeispiele wurden
ebenfalls geprüft. Die SVG-Datei ist gültiges XML.

Noch nicht geprüft: physische Wicklung, Bedienerstreuung, Reibung, Klebung,
Entformkräfte, Oberflächenhaltbarkeit, reales Papier und Druck. Die geometrische
Prüfung des OpenSCAD-P0 ist von diesen Funktionsnachweisen zu unterscheiden.
