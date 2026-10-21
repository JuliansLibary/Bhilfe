# Neukonzeption mit Tip-Integration — mechanische Vorzugsarchitektur

Stand: 21. Oktober 2026. Konzeptentscheidung ohne neuen CAD-Code.
Nach Freigabe umgesetzt als FreeCAD-P1: siehe `../cad/freecad_p1/README_FREECAD.md`.
Die nachfolgende Studie dokumentiert die vorausgehende Konzeptentscheidung.
Die vorhandene OpenSCAD-P0 bleibt ein Versuchsstand ohne Tip. Ihre STL-Prüfungen
validieren diese Neukonzeption nicht. Die spätere CAD-Ausarbeitung wird hier,
entsprechend dem Folgeauftrag, für FreeCAD beschrieben.

## 1. Entscheidung und wesentliche Grenzen

**Vorzugsmechanismus D:** Der vorgerollte Tip bildet selbst den kleinen
Formabschnitt. Eine von außen öffnende Kassette hält nur seinen unverwickelten
Überstand. Ein massiver Kern schließt stumpf an der vorderen Tip-Stirnfläche an
und wird zur breiten Seite herausgezogen. Es gibt keinen Zentrierstift im Tip.

Für P1 bleiben Tip und Kern stationär; der Benutzer wickelt das Papier um beide.
Damit werden eine Drehmomentkupplung und eine noch unbewiesene automatische
Zuführung vermieden. Ein Rollantrieb wäre ein späterer, getrennt zu prüfender
Entwicklungsschritt.

Zwei Funktionen sind entscheidend und noch nicht nachgewiesen:

1. Ein übliches zylindrisches Mundstück geht in eine konische Formzone über.
   Diese zusammengesetzte Kontur hat nicht dieselbe Abwicklung wie ein reiner
   Kegelstumpf. Knickfreiheit am Übergang ist eine Prototypfrage.
2. Die Haltekraft zwischen Paper und Tip muss deutlich größer sein als die zum
   Herausziehen des Kerns erforderliche Kraft. Eine perfekt haltende Vorrichtung
   allein beweist keine stabile Verbindung des fertigen Produkts.

Ein gleichmäßig durchgehender geometrischer Kegel verlangt einen passend
konischen Tip. Für den ersten Versuch wird die Kompatibilität mit gewöhnlichen
zylindrischen, vorgerollten Tips priorisiert und die Kontur entsprechend benannt.

## 2. Kritische Überprüfung der bisherigen Konstruktion

| Frage | Befund |
|---|---|
| Stabilität während des Rollens | Der alte Vollkern stützt die Papierhülle. Nach Entfernen bleibt die schmale Öffnung ohne Tip ungestützt. |
| Platz für den Tip | Der alte Kern belegt den Innenraum. Ein Tip kann nicht zusätzlich denselben Raum belegen. Der Kern muss vor dem Tip enden oder eine passende Aufnahme erhalten. |
| Reihenfolge | Für zuverlässige Lage wird der vorgerollte Tip zuerst gehalten; anschließend wird Paper gemeinsam um Tip und Kern geformt. |
| Separate Tip-Aufnahme | Sie vermeidet den unbekannten inneren Aufbau des Papier-Tips und lässt sich außerhalb der Wickelfläche anordnen. |
| Fixierung | Formangepasste äußere Teilbacken, axialer Anschlag und begrenzte Klemmung; keine Hülse zwischen Paper und Tip. |
| Mitdrehen | Bei stationärem Kern bleibt auch der Tip stationär. Bei später rotierendem Kern muss der Tip synchron mitlaufen. Unterschiedliche Zwangsbewegungen würden Papier verspannen. |
| Entnahme | Der Kern verlässt den Cone zur breiten Griffseite. Danach wird die Tip-Aufnahme radial geöffnet und das Produkt ausgehoben. |

Eine Trichterführung allein definiert weder Tiplage noch Überdeckung. Eine
beidseitig geschlossene Außenführung kann den Cone nach dem Kleben einschließen;
jede äußere Aufnahme im Produktbereich muss deshalb vollständig öffnen können.

## 3. Zwei voneinander getrennte Stabilitätsprobleme

### Werkzeug

Ein massiver Kernanfang um 6 mm ist ein anderer Lastfall als ein 1–2 mm dünner
Zentrierstift. Eine feine FDM-Spitze ist hier nicht erforderlich. Der Kern beginnt
mit einer stumpfen, verrundeten Stirnkante und wird zum Griff hin breiter.

Das breite Werkzeugende und seine Führung tragen den Kern. Der Papier-Tip darf
nicht als mechanisches Lager für Werkzeuggewicht oder seitliche Handkräfte
dienen. Ein an den Tip gepresster, sonst ungestützter Dorn wäre ein ungünstiger
Kraftpfad.

Zur Einordnung, ausdrücklich kein Festigkeitsnachweis: Ein gleichmäßig 6 mm
dicker Vollstab mit 70 mm freier Länge hätte bei 1 N Querlast etwa 3,30 MPa
Biegespannung. Mit angenommenen E = 2.000 N/mm² ergäben sich etwa 0,90 mm
Durchbiegung. Der wirkliche konische Körper ist steifer als dieser Vergleich,
FDM-Anisotropie und die Verbindung zur Führung bleiben jedoch zu prüfen.
Eine präzise Führung ist auch dann nötig, wenn kein unmittelbarer Bruch droht.

Eine zusätzliche Abstützung auf der schmalen Formfläche würde das Papier beim
Wickeln blockieren. Sie müsste zuvor zurückziehen und ist für P1 nicht vorgesehen.
Beidseitig wird die Gesamtanordnung positioniert; die Tip-Halterung ist dabei
ausdrücklich kein zweites tragendes Kernlager.

### Fertiger Cone

Der gerollte Tip stützt die Mundzone von innen. Er darf weder oval geklemmt noch
nach dem Entformen lose werden. Entscheidend sind seine eigene Formstabilität,
eine passende Wicklung und genügend wirksame Überdeckung. Feuchtes Paper und
Rückfederung können die Verbindung verändern.

Der lange Gummistreifen verbindet zunächst Paper mit Paper. Er erzeugt nicht
automatisch eine definierte Klebung zwischen Paper und Tip. P1 setzt keine
zusätzlichen Klebstoffe oder Klebung des Tips am Werkzeug voraus.

## 4. Geometrie und Arbeitsannahmen

| Größe | Ausgangswert / Bereich | Status |
|---|---|---|
| Tip-Außendurchmesser | zuerst 6,0 mm; später zum Beispiel 5,5 / 6,0 / 6,5 mm | jeweiliges reales Los vermessen |
| Tip-Gesamtlänge | zuerst 18 mm; später etwa 15–21 mm | Annahme |
| Freier hinterer Überstand | Ziel 3 mm; Aufnahme greift nur etwa 2 mm | an jeder Umfangsposition auf Papierfreiheit prüfen |
| Nominelle Einbettung | 18 − 3 = 15 mm | rechnerische Länge |
| Kleinste wirksame Überdeckung | vorläufig mindestens 12 mm über den Umfang | Versuchsanforderung, kein Haltekraftnachweis |
| Breiter Kern-Durchmesser | zunächst 12 mm | Annahme, Papierpassung neu prüfen |
| Achshöhe über Arbeitsfläche | vorläufig 35 mm | Fingerzugang von unten prüfen |
| Bewegliche Kunststoffpassungen | zunächst 0,3–0,5 mm Durchmesserspiel bzw. äquivalentes Führungsspiel | Drucker-Probekörper erforderlich |

Papier-Endränder sind bei unbeschnittenen Rechtecken nicht automatisch eben.
Ein mittlerer Tipüberstand von 3 mm garantiert deshalb noch keinen freien
Klemmbereich. Maßgeblich sind der kleinste freie Überstand und die kleinste
Einbettung über den gesamten Umfang. Die Aufnahme endet axial vor jeder
Papierkante; als vorläufiges Ziel bleibt mindestens 0,5 mm freie Trennung.

Den Tip zusätzlich an die bisherigen 68/98 mm Formzone anzuhängen wäre falsch:
Schon der eingebettete Abschnitt von 15 mm ergibt 83/113 mm und überschreitet
damit die angenommenen Papierlängen 78/110 mm, noch ohne Endrandreserven.
Für eine neue nominelle papierbedeckte Zielzone von
68/98 mm werden zunächst 15 mm eingebetteter Tip und 53/83 mm konische Körperzone
budgetiert. Der halbe Kegelwinkel wäre bei 6→12 mm etwa 3,240°/2,070°.
Diese Werte sind ein Maßbudget, **kein erneuter Nachweis der Papierpassung**.
Die tatsächlich erforderlichen Kernverlängerungen hängen von der neuen
Papierlage ab und werden vor CAD-Festlegung neu bestimmt.

### Zylindrischer oder konischer Tip

Ein Zylinder und ein Kegel besitzen unterschiedliche ebene Abwicklungen. An ihrer
gemeinsamen Ringlinie entsteht ein Neigungswechsel; eine unverformte ebene
Papierbahn kann dort nicht überall ideal anliegen. Eine kurze Übergangszone kann
praktisch helfen, löst die geometrische Unvereinbarkeit aber nicht automatisch.
Auch eine glatte, räumlich gekrümmte Verrundung garantiert keine Faltenfreiheit.

Zum Vergleich: Für die bisherige durchgehende Kegellinie 6→12 mm über 68/98 mm
müsste ein 18 mm langer Tip selbst von 6 auf 7,588/7,102 mm wachsen. Ein solcher
konischer Tip wäre die geometrisch sauberere Alternative. Er verlangt passend
vorgeformte Verbrauchsteile und darf nicht stillschweigend als gewöhnlicher
zylindrischer Tip vorausgesetzt werden.

P1 prüft daher zuerst den zylindrischen Tip mit bündigem Kernanschluss. Bleibt
der Übergang trotz korrekter Position und geringer Spannung sichtbar unzureichend,
wird eine passende konische Tip-Variante verglichen. Der Anspruch an eine exakt
durchgehende Kegelform erfordert gegebenenfalls diese geänderte Tip-Geometrie.

### Unterschiedliche Tips

Innenliegende W-/M-Faltungen und lose Wicklungen schließen einen universellen
Zentrierstift aus. Außendurchmesser und Stirnflächen sind die relevanten
Referenzen. Wechseleinsätze sind einem universellen FDM-Spannfutter vorzuziehen:
Jedes Einsatzpaar passt zu einem kleinen Durchmesserbereich und besitzt dieselbe
Achsreferenz zur Basis. Ein Durchmesserwechsel erfordert auch einen dazu passenden
Kernanfang. Länge wird über den axialen Anschlag eingestellt.

Flache Tip-Streifen müssen für P1 zuerst separat vorgerollt und auf Maß geprüft
werden. Ihre gleichzeitige automatische Herstellung wäre ein zusätzlicher
Mechanismus und ist nicht Bestandteil dieser Vorzugsarchitektur.

## 5. Vier Mechanismen mit Kollisionsprüfung

### A — Vollkern mit integrierter innerer Tip-Aufnahme

Ein kurzer Zentrieransatz ragt vom kleinen Kernende in einen bereits offenen
Tip. Eine Stirnschulter legt dessen Position fest; geringe Passungsreibung hält
ihn. Danach wird Paper um Tip und Kern gewickelt.

**Vorteile:** wenige Teile, direkte Koaxialität, kompakt.

**Probleme:** unbekannter Tip-Innenraum, Verformung innerer Faltungen, filigraner
Zapfen und zusätzliche Auszugreibung. Bei zu starkem Sitz zieht der Zapfen den
Tip beim Entformen aus der Papierhülle. Eine äußere Aufnahmehülse unter dem Paper
wäre ebenfalls ungünstig: Sie belegt den gewünschten direkten Kontakt zwischen
Tip und Paper und hinterlässt nach Entfernen Spiel.

**Entnahme:** zur breiten Seite grundsätzlich möglich; Zapfen muss geradlinig
aus dem Tip herausziehen, ohne Widerhaken oder Presssitz. Nur für genau definierte
offene Tip-Geometrien eine überzeugende Option.

### B — Teilbarer oder radial verkleinerbarer Kern

Zwei Formsegmente werden beim Wickeln durch einen inneren Schieber gespreizt.
Nach dem Kleben wird der Schieber gezogen, die Segmente können nach innen und
anschließend breitwärts herausgenommen werden. Eine äußere Tip-Aufnahme hält
den Tip unabhängig davon.

**Vorteile:** mögliche Reduktion der ersten Abzugskraft; Formkörper könnte sich
von anhaftendem Paper lösen, bevor er axial bewegt wird.

**Probleme:** Trennfugen können sich abzeichnen oder Paper greifen. Platz für
tragfähige Wände, Schieber und Bewegung ist am schmalen Ende knapp. FDM-Spiel,
Segmentversatz, Reinigung, Verklemmen und Rückstellung erzeugen zusätzliche
Fehlerquellen. Ein an der Fuge eingeklemmtes Paper kann beim Kollabieren beschädigt
werden.

**Entnahme:** kollisionsfrei nur bei nachgewiesenem radialem Rückzug und ohne
Papier in den Spalten. Für P1 nicht gerechtfertigt, weil ein starrer Kern bereits
einen offenen breitseitigen Auszugsweg besitzt. Wiederaufnahme erst bei einem
gemessenen, anders nicht beherrschbaren Entformproblem.

### C — Äußere Rollform mit Tip-Führung, ohne vollständigen Innenkern

Eine geteilte Tip-Aufnahme hält den Tip. Eine offene konische Außenform und
nacheinander bewegte Wischsegmente legen die Papierflügel herum; eine Nahtöffnung
bleibt frei. Eine breite Endführung muss die große Öffnung gegen Ovalität stützen
und vor der Entnahme öffnen.

**Vorteile:** kein Vollkern aus dem fertigen Cone zu ziehen; Tip bleibt direkt
in Kontakt mit Paper. Perspektivisch stärker mechanisch geführter Ablauf.

**Probleme:** Die noch unverklebte Papierbahn kann ausbeulen, an den Wischkanten
knicken oder sich im Nahtbereich doppelt legen. Äußere Formflächen sind während
des Einlegens im Weg und müssen sequenziell öffnen. Tiphaltung allein definiert
die breite runde Öffnung nicht. Ein gleichförmig laufendes Band löst die über die
Länge unterschiedlichen Umfangsgeschwindigkeiten ebenfalls nicht.

**Entnahme:** Außenteile öffnen radial, gegebenenfalls breiten Former zurückziehen,
dann Tip-Aufnahme öffnen. Mechanisch plausibel, aber höchste Unsicherheit bei
Papierführung und reproduzierbarer Innenkontur.

### D — Tip als Formsegment, äußere Haltekassette und stumpfer Vollkern

Der Tip wird nur an seinem unverwickelten hinteren Bereich von außen gehalten.
Seine freie Vorderseite liegt am kleinen Kernende an. Der Kern dringt nicht in
den Tip ein und trägt keine Aufnahmehülse unter dem Paper. Das Paper liegt direkt
auf beiden Formabschnitten.

**Vorteile:** unabhängig von Tip-Innenfaltungen, glatter einteiliger Kern,
zugängliche Naht und klarer Auszugsweg. Größenanpassung durch passende Tip-Einsätze
und Kernanfänge. Tip und Werkzeugbelastung lassen sich getrennt behandeln.

**Probleme:** zylindrisch-konischer Konturübergang, tatsächliche Papierkante an
der Klemme, Klemmkraftfenster und Kraftverhältnis bei der Entnahme. Stationäres
Wickeln erfordert Fingerraum und bleibt zunächst manuell. Ein vollständig
geführter Auszug benötigt zusätzlichen Bauraum zur breiten Seite.

**Entnahme:** den massiven Kern vom Tip weg zur breiten Seite ziehen. An jeder
festen Papierposition folgen schmalere Querschnitte; der Tip muss nicht über einen
breiteren Kern geschoben werden. Anschließend Kassette radial öffnen.

## 6. Gewichtete Vorauswahl, 1 bis 10

Punkte sind technische Erwartungen unter den beschriebenen Randbedingungen,
keine Ergebnisse von Versuchen. Bewertet wird jeweils der vollständige Mechanismus.

| Kriterium | Gewicht | A | B | C | D |
|---|---:|---:|---:|---:|---:|
| Qualität und Reproduzierbarkeit | 25 % | 7 | 7 | 6 | 8 |
| Zuverlässige Tip-Integration | 25 % | 6 | 8 | 8 | 8 |
| Einfache Bedienung | 20 % | 7 | 5 | 7 | 7 |
| Beschädigungsfreie Entnahme | 15 % | 7 | 8 | 9 | 9 |
| FDM-Herstellbarkeit | 10 % | 8 | 4 | 7 | 8 |
| Kompaktheit und Design | 5 % | 9 | 5 | 7 | 8 |
| **Gewichtete Summe / 10** | **100 %** | **6,95** | **6,60** | **7,30** | **7,95** |

A verliert durch die Abhängigkeit vom unbekannten Tip-Innenraum. B gewinnt bei
Entformung, verliert durch Segmente und Bedienfolge. C entkoppelt die Entnahme
vom Vollkern, muss aber die Papierform weitgehend von außen erzeugen. D erhält
die beste Gesamtbewertung wegen direktem Paper-Tip-Kontakt und klar getrennten
Form-, Halte- und Freigabefunktionen.

Die hohen Entnahmepunkte für D beziehen sich auf den günstigen geometrischen
Weg. Sie setzen geringe reale Abzugskräfte voraus. Die Matrix ersetzt diesen
Nachweis nicht. Fällt der Übergangs- oder Haltekraftversuch durch, bleibt D eine
Vorzugsarchitektur, aber noch keine freigegebene Produktlösung.

## 7. Konkreter Aufbau und Funktionsfolge von D

### Baugruppen und Teile

1. **Basis:** trägt Tip-Kassette, Papierauflage und hintere Kernführung. Keine
   starre Papierkante bleibt während des Wickelns festgeklemmt.
2. **Einteiliger Formkern mit Griff und Führungsanbindung:** stumpfer Anfang,
   konische Formfläche, steifes breites Ende. Die Anbindung kann im Prototyp
   integriert werden; eine getrennte wechselbare Ausführung wäre ein fünftes
   Druckteil. Sie hält den Kern auch ohne Tip vollständig selbstständig.
3. **Unterer Tip-Wechseleinsatz:** definiert Achse und hinteren axialen Anschlag;
   berührt nur den freien Tip-Überstand.
4. **Obere passende Klemmbacke:** öffnet vollständig nach oben. Für P1 begrenzte
   einstellbare Klemmung mit harter Wegbegrenzung; keine ungeprüfte kräftige
   Schnappfeder.

Die Backenkörper können hinter dem Tip-Ende massiv ausgeführt sein. Nur ihre
Kontaktzone greift in den kurzen freien Überstand; es wird kein dünner,
lang auskragender FDM-Finger auf der Papierkontaktseite vorausgesetzt.
Eine nur etwa 2 mm lange Haltezone kann einen weichen Tip bei seitlichem
Wickelzug kippen lassen. Deshalb gehört die Lage seiner vorderen Stirnfläche
unter Last zur Prüfung. Reicht diese Führung nicht aus, werden längerer freier
Überstand und entsprechend längerer Tip verglichen; die Mindestüberdeckung
muss erhalten bleiben. Zusätzliche Klemmkraft ohne Verformungsnachweis wäre
keine zulässige Abkürzung.

Hinzu kommen realistisch ein Scharnierstift, eine Klemmschraube und eine Mutter.
Vier Druckteile sind das Ausgangsziel, kein Versprechen eines vollständigen
Dreiteilers. Zwei Funktionsbewegungen: Kern axial zurückziehen, Klemmbacke öffnen.

Eine durchgehend geführte Kernentnahme braucht Hub mindestens bis die gesamte
unter Paper liegende Kernfläche frei ist. Dieser Hub folgt aus der neuen
Papierhülle, nicht allein aus 53/83 mm Nenn-Körperzone. Hinter dem Gerät muss dieser
Weg verfügbar bleiben. Die Führung darf weder Paper berühren noch den Griff auf
dem Auszugsweg einsperren. Baugruppen- und Bewegungsraum werden gemeinsam geprüft.

### Bedienung

1. **Tip einlegen:** passenden Einsatz wählen, vorgerollten Tip an den hinteren
   Anschlag legen, Backe sanft bis zur eingestellten Begrenzung schließen.
2. **Kern vorfahren:** seine Stirnfläche bis zum eingestellten Anschlag an den
   Tip heranführen. Die Führung setzt die Lage; keine kräftige axiale Vorspannung
   auf den Papier-Tip ausüben.
3. **Paper anlegen und wickeln:** freie Tip-Zone an der Klemme kontrollieren,
   erste Überdeckung von Hand anlegen, dann um Tip und Kern weiterführen. Die
   Orientierungshilfe darf Schwenken nicht blockieren. Beide Formteile bleiben
   stationär; es gibt noch keinen behaupteten automatischen Einzug.
4. **Naht schließen:** Klebestreifen bleibt von oben zugänglich. Über die
   Tip-Zone hinweg Paper auf Paper schließen und ausreichend anziehen lassen.
5. **Entformen:** Kern geradlinig zur breiten Seite ausziehen, anschließend
   Tip-Klemme öffnen und den fertigen Cone am stabilisierten Bereich ausheben.

Das sind fünf Benutzerphasen, aber mehr als fünf Einzelbewegungen. Insbesondere
Kern vorfahren und Backe öffnen sind reale Bedienhandlungen. Sie zu verschweigen
würde die Einfachheit der Konstruktion überzeichnen.

### Rotation und Fixierung

P1 fixiert Kern und Tip gegen unerwünschte Relativbewegung. Eine spätere
Rotationsversion müsste beide synchron drehen oder die Tip-Aufnahme reibungsarm
mitlaufen lassen. Ein angetriebener Kern gegen einen starr festgeklemmten Tip ist
keine zulässige Mischlösung. Unabhängige Rollen lösen außerdem nicht automatisch
die komplexe Papierzuführung über Zylinder und Kegel.

## 8. Kritische Toleranzen und Kräfte

Alle Zahlen sind vorläufige Prototypziele, keine nachgewiesenen Serienwerte:

| Stelle | Ausgangsziel | Begründung |
|---|---|---|
| Tip-/Kern-Achsversatz | höchstens 0,2 mm | einseitige Stufe und schrägen Paperlauf begrenzen |
| Durchmessersprung an der Stoßstelle | höchstens 0,2 mm | direkt aufeinander abgestimmter Tip und fertig gemessener Kern |
| Axialer Spalt an der Stoßstelle | 0–0,2 mm | keine breite ungestützte Papierzone; kein Tip-Stauchen |
| Wiederholte Tip-Axialposition | ±0,5 mm | Anschlag und Papierüberdeckung reproduzierbar halten |
| Unbelastete Einsatzpassung | zunächst etwa 0,2–0,4 mm Durchmesserzugabe | Tip einlegen können; Halten erfolgt durch begrenzte Backe |
| Kernführungs-Spiel | zunächst 0,3–0,5 mm, am Druck prüfen | Druckmaß und Fluchtung gemeinsam berücksichtigen |
| Klemmen bis zur Papierkante | mindestens 0,5 mm freie axiale Trennung | kein Paper in der Backe |

Ein Wechsel des Tip-Durchmessers verändert gleichzeitig Kernanfang, Übergang,
Papierabwicklung und Aufnahme. Ein Universalclip ohne diese Anpassung wäre keine
saubere Größenverstellung.

Eine belastbare Klemmkraft lässt sich ohne Reibwert und Quetschgrenze des
konkreten Tips nicht seriös festlegen. Als grobes Reibmodell muss bei kombinierter
Axialkraft F und Drehmoment M gelten:

```text
mu * N >= sqrt(F² + (M / r_eff)²)
```

N bezeichnet die aufsummierte Normalkraft der Backenkontakte. Reibwert,
wirksamer Radius und zulässige reversible Verformung sind zu messen. Die untere
Grenze folgt aus dem benötigten Halt, die obere aus Ovalisierung beziehungsweise
dauerhafter Beschädigung. Existiert kein ausreichend breites Fenster, ist die
Kontaktgeometrie ungeeignet; stärkeres Zudrehen ist keine Lösung.

Zusätzlich gilt für das fertige Produkt als vorgeschlagenes Entwicklungsziel:

```text
kleinste gemessene Paper-Tip-Haltekraft
    >= 2 * größte gemessene Kern-Abzugskraft
```

Der Faktor zwei ist eine zu validierende Entwicklungsreserve. Beim Kernabzug
darf der festgehaltene Tip nicht aus der Paperhülle gezogen werden. Die Prüfung
findet unter passenden trockenen und frisch verklebten Bedingungen statt.

## 9. Drei Pflichtversuche vor der CAD-Detailfreigabe

1. **Übergang und echter Papierweg:** Mit einem Tip-Los und einem Papierformat
   starten. Mindestens zehn Wicklungen filmen; Falte, Brücke, schiefe Naht,
   kleinsten freien Tipüberstand und kleinste Überdeckung erfassen. Prüfen, ob
   Paper tatsächlich an allen Außenbauteilen vorbeikommt. Zylindrische und bei
   Bedarf passende konische Tips vergleichen.
2. **Klemmfenster:** Axialen Halt und Verdrehwiderstand bei zunehmender Klemmung
   prüfen, Rundheit vor und nach Entlastung per Konturfoto erfassen. Die Backe darf
   keine bleibende Falte erzeugen. Die Tip-Vorderseite auch unter seitlichem
   Wickelzug auf Kippen und Achsversatz prüfen. Daraus Kontaktlänge, Anschlag und
   Kraftbegrenzung ableiten.
3. **Entnahme und Endprodukt:** Kern-Abzugskraft und Paper-Tip-Auszugwiderstand
   getrennt messen. Beim realen Entformen Tipwanderung, Nahtöffnung und
   Beschädigung beobachten. Vorgeschlagen: Tipwanderung höchstens 0,5 mm und keine
   sichtbare Beschädigung; Kraftreserve wie oben.

Erst danach ein Bedienerversuch, beispielsweise fünf Anfänger mit je sechs
gewerteten Durchgängen nach Übung. Vorläufig mindestens 27 von 30 ohne Riss,
bleibende Übergangsfalte, offene Naht oder Tipverlust. Diese kleine Stichprobe
ist ein Entwicklungstor und keine statistische Zusage für Serienzuverlässigkeit.

## 10. Spätere parametrische Konstruktion in FreeCAD

Noch kein Code. Vorgesehen ist folgender Aufbau:

- Spreadsheet mit Tip-Durchmesser und -Länge, freiem Überstand, Mindest-
  Überdeckung, Papierformat, Gesamtlängenbudget, breitem Durchmesser, axialem
  Spalt, Klemmweg, Führungsspiel, Achshöhe und Auszugshub.
- Abgeleitete Maße für eingebetteten Tipabschnitt, Körperlänge und Winkel.
  Die bisherige reine Kegel-Abwicklungsprüfung wird für die neue Kontur ersetzt;
  sie darf nicht nur um eine Tip-Länge ergänzt werden.
- Eigene Bodies für Basis, Kern/Führungsanbindung und die zwei Einsatzhälften.
  Stabiles gemeinsames Achs- und Ursprungssystem, keine Referenz auf zufällig
  erzeugte Verrundungskanten.
- Rotationsprofil für den Kern, Skizzen und Pads/Pockets für Basis und Backen.
  Den Paper-Tip als eigenes Referenzbauteil einschließlich möglicher Innenfaltung
  und den Wrapper als Bauraumhülle modellieren; Referenzkörper nicht als Druckteile
  exportieren.
- Bewegungsprüfung in Einlege-, Wickel-, Klebe-, Auszugs- und Offenstellung.
  Über den ganzen Hub auf Kollisionen prüfen, insbesondere Paperkante/Backe,
  Kern/Tip, breite Paperkante/hintere Führung und Griff/Gehäuse.
- FDM-Orientierung getrennt vom Zusammenbau prüfen. Glatte Kernfläche ohne
  Stützen, ausreichend massive Führungsanbindung und austauschbare, reinigbare
  Einsätze; keine unbewertete dünne FDM-Dauerfeder als einzige Haltefunktion.
- Erst nach Ausführung und Prüfung im tatsächlichen CAD-System gültige
  Volumenkörper sowie FCStd/STEP und STL je Druckteil ausgeben.

## 11. Nachweisstand

Geometrische Bewegungsrichtung und Maßbudgets wurden analytisch geprüft;
Winkel, alternative konische Tip-Durchmesser und Matrixsummen wurden numerisch
nachgerechnet. Eine unabhängige mechanische und geometrische Prüfung bestätigte
die wesentlichen Kollisions- und Kraftflussbedingungen.

Zum Zeitpunkt dieser Konzeptstudie wurden keine neuen CAD-Geometrien, physischen
Prototypen oder Testergebnisse erzeugt. Der anschließende P1-Stand und seine
Geometrieprüfungen sind separat dokumentiert. Klemmfenster, Übergangsqualität und Endprodukt-Halt sind
offene Pflichtnachweise. Der vorgeschlagene Mechanismus ist technisch plausibel;
eine Produktionsfreigabe folgt daraus nicht.
