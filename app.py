from flask import Flask, request, jsonify
from game_logic import process_shift
from player_state import default_player
from storage import load_user, save_user

app = Flask(__name__)

@app.get("/")
def home():
    return "OZON LEGENDS API is running"

@app.get("/api/state")
def api_state():
    user_id = request.args.get("user_id", type=int)
    if not user_id:
        return jsonify({"error": "user_id обязателен"}), 400

    player = load_user(user_id) or default_player()
    return jsonify(player)

@app.post("/api/shift")
def api_shift():
    data = request.get_json(force=True)
    user_id = int(data.get("user_id", 0))
    income = int(data.get("income", 0))

    if user_id <= 0:
        return jsonify({"error": "user_id обязателен"}), 400
    if income <= 0:
        return jsonify({"error": "income должен быть > 0"}), 400

    player = load_user(user_id) or default_player()

    result = process_shift(
        income=income,
        level=player["level"],
        xp=player["xp"],
        streak=player["streak"]
    )

    player.update(result)
    player["streak"] += 1

    save_user(user_id, player)

    return jsonify(player)
