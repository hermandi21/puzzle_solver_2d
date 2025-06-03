# Puzzle Solver 2D

## Vorgensweise:
### Die Aufnahmen wurden in drei verschiedene Puzzles aufgeteilt. Wir haben uns dazu entschieden jedes
### Bild nach folgendem Schema zu benennen `pzl_<puzzle_nr>_<stück_nr>_<seite>.jpg`


data/pzl_1/
├── pzl_1_001_back.jpg
├── pzl_1_001_front.jpg
├── pzl_1_002_back.jpg
├── pzl_1_002_front.jpg
├── pzl_1_003_back.jpg
├── pzl_1_003_front.jpg
├── pzl_1_004_back.jpg
├── pzl_1_004_front.jpg
├── pzl_1_full_back.jpg      ← alle 4 Teile zusammen, Rückseite
└── pzl_1_full_front.jpg      ← alle 4 Teile zusammen, Vorderseite



## Erste Idee:
- Wir gehen davon aus dass wir das fertige Puzzlemuster schon kennen.

1. Referenzbild vom gesamten Puzzle erstellen
    - Das Referenzbild so zuschneiden dass es das gesamte Bild ausfuellt
2. Bild von den einzelnen Puzzlestuecken erstellen
    - Mithilfe von Regionenerkennung mit Bounding Boxen die Matrix erstellen
    - Größe des einzelnen Puzzlestuecks an das Referenzbild anpassen
    - Das Puzzlestueck als Filter nutzen. Mit dieser Filtermaske über das Referenzbild iterieren und 
    pro Pixel den Korrelationskoeffizienten berechnen.
    Dies wiederrum fuer alle moeglichen Roatationsmoeglichkeiten durchfueheren.
    

