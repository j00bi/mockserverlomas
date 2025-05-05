from flask import Flask, request, jsonify

app = Flask(__name__)

mock_data = {
    "PC99999": {
        "Status": "Available",
        "Location": "Warehouse A",
        "ETA": "2025-05-07T15:00:00Z"
    },
    "PC99998": {
        "Status": "Not Available",
        "Location": "Warehouse B",
        "ETA": "2025-05-08T10:00:00Z"
    }
}

@app.route("/getPCDetails", methods=["POST"])
def get_pc_details():
    data = request.get_json()
    pc_num = data.get("PC_Num")
    response = mock_data.get(pc_num)
    
    if response:
        return jsonify({"PC_Num": pc_num, **response})
    else:
        return jsonify({"error": "PC_Num not found", "code": 404}), 404

@app.route("/", methods=["GET"])
def home():
    return "Mock API is running"
