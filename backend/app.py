from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Sump OHT Automation Project"

@app.route("/api/latest-data")
def latest_data():
    return jsonify({
        "sump_level": 80,
        "oht_level": 35,
        "motor_status": 1
    })

app.run(debug=True)