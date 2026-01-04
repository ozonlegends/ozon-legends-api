import json, os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def _path(user_id):
    return os.path.join(DATA_DIR, f"user_{user_id}.json")

def load_user(user_id):
    path = _path(user_id)
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

def save_user(user_id, data):
    with open(_path(user_id), "w") as f:
        json.dump(data, f, indent=2)
