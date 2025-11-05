import json
import os

FAV_FILE = "assets/favorite.json"

def load_favorites():
    """Baca daftar favorit; buat file jika belum ada."""
    if not os.path.exists(FAV_FILE):
        with open(FAV_FILE, "w") as f:
            json.dump([], f)
    with open(FAV_FILE, "r") as f:
        return json.load(f)

def save_favorite(design):
    """Tambah desain ke favorit (kalau belum ada)."""
    favorites = load_favorites()
    if design not in favorites:
        favorites.append(design)
        with open(FAV_FILE, "w") as f:
            json.dump(favorites, f, indent=2)
        return True
    return False

def delete_favorite(design):
    """Hapus desain dari favorit."""
    favorites = load_favorites()
    if design in favorites:
        favorites.remove(design)
        with open(FAV_FILE, "w") as f:
            json.dump(favorites, f, indent=2)
        return True
    return False
