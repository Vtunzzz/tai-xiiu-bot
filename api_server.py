from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

current_session = {
    "gameId": 1234567,
    "dice": [1, 2, 3],
    "total": 6,
    "result": "xỉu"
}

@app.route("/api/taixiu/latest", methods=["GET"])
def get_latest_taixiu():
    dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(dice)
    result = "tài" if total >= 11 else "xỉu"
    current_session["gameId"] += 1
    current_session["dice"] = dice
    current_session["total"] = total
    current_session["result"] = result
    return jsonify(current_session)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
