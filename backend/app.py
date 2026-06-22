from flask import Flask, jsonify,request
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    return "Arjun Flat Water Automation"

@app.route("/api/latest-data")
def latest_data():

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="arjun_flat_db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT sump_level,
               oht_level,
               motor_status
        FROM water_monitoring
        ORDER BY id DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    return jsonify({
        "sump_level": row[0],
        "oht_level": row[1],
        "motor_status": row[2]
    })

@app.route("/api/save-data", methods=["POST"])
def save_data():

    data = request.json

    sump_level = data["sump_level"]
    oht_level = data["oht_level"]
    motor_status = data["motor_status"]

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="arjun_flat_db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO water_monitoring
        (sump_level, oht_level, motor_status)
        VALUES (%s, %s, %s)
    """, (sump_level, oht_level, motor_status))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Data Saved Successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)