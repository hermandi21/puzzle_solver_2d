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




from pathlib import Path
import shutil

# Setup für ein Jupyter-kompatibles Skript
source_dir = Path("../data/image_data")
target_dir = Path("../data/sorted_puzzles")
target_dir.mkdir(parents=True, exist_ok=True)

# Alle JPG-Dateien im Quellordner alphabetisch sortieren (basierend auf Zeitstempel im Namen)
images = sorted([f for f in source_dir.iterdir() if f.suffix.lower() == ".jpg"])

# Anzahl Bilder pro Puzzle
images_per_puzzle = 10

# Umbenennung und Kopieren
renamed_files = []
for i, img_path in enumerate(images):
    puzzle_num = (i // images_per_puzzle) + 1
    img_index = (i % images_per_puzzle) + 1
    new_name = f"pzl_{puzzle_num}_{img_index:03d}.jpg"
    new_path = target_dir / new_name
    shutil.copy(img_path, new_path)
    renamed_files.append((img_path.name, new_name))

renamed_files[:10]  # Zeige die ersten 10 Umbenennungen als Vorschau
