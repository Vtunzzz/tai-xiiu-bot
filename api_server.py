from flask import Flask, jsonify
import random
import os
from datetime import datetime
import threading
import time

app = Flask(__name__)

current_session = {
    "gameId": 2718911,
    "dice": [3, 4, 2],
    "total": 9,
    "result": "xỉu",
    "timestamp": datetime.now().isoformat()
}

def generate_taixiu_result():
    while True:
        time.sleep(50)  # Mỗi 60 giây tạo phiên mới
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        result = "tài" if total >= 11 else "xỉu"
        current_session["gameId"] += 1
        current_session["dice"] = dice
        current_session["total"] = total
        current_session["result"] = result
        current_session["timestamp"] = datetime.now().isoformat()
        print(f"[+] New game: {current_session}")

@app.route("/api/taixiu/latest", methods=["GET"])
def get_latest():
    return jsonify(current_session)

@app.route("/")
def home():
    return "✅ API Sun.Win giả lập v2 đang chạy – /api/taixiu/latest"

if __name__ == "__main__":
    threading.Thread(target=generate_taixiu_result, daemon=True).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
