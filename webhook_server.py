from flask import Flask, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)


# Ensure log folder exists
LOG_FOLDER = "alerts_log"
os.makedirs(LOG_FOLDER, exist_ok=True)


@app.route('/chartink-webhook', methods=['POST'])
def chartink_alert():
    data = request.json
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = {
        "timestamp": timestamp,
        "data": data
    }

    log_path = os.path.join(LOG_FOLDER, "chartink_alerts.jsonl")
    with open(log_path, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    print(f"[{timestamp}] Alert received: {data}")
    return jsonify({"status": "success", "received": data}), 200



if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)