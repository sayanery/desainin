import json
import os

FAV_FILE = "assets/favorite.json"

def load_favorites():
    if not os.path.exists(FAV_FILE):
        with open(FAV_FILE, "w") as f:
            json.dump([], f)
    with open(FAV_FILE, "r") as f:
        return json.load(f)

def save_favorite(design):
    favorites = load_favorites()
    if design not in favorites:
        favorites.append(design)
        with open(FAV_FILE, "w") as f:
            json.dump(favorites, f, indent=2)
        return True
    return False
