from flask import Flask, request, jsonify
import uuid
import datetime

app = Flask(__name__)

# In-memory traceability ledger
ledger = []

@app.route('/log_shipment', methods=['POST'])
def log_shipment():
    data = request.get_json()
    shipment_id = str(uuid.uuid4())
    entry = {
        "shipment_id": shipment_id,
        "origin": data.get("origin"),
        "mineral_type": data.get("mineral_type"),
        "weight_kg": data.get("weight_kg"),
        "timestamp": datetime.datetime.now().isoformat()
    }
    ledger.append(entry)
    return jsonify({"status": "logged", "shipment_id": shipment_id, "entry": entry})

@app.route('/get_ledger', methods=['GET'])
def get_ledger():
    return jsonify(ledger)

if __name__ == '__main__':
    app.run(debug=True)
