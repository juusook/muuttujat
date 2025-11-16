import mysql.connector
from flask import Flask, jsonify

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="Juuso",
        password="salasana",
        database="flight_game"
    )

def get_airport_by_icao(icao_code):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

app = Flask(__name__)

@app.route("/kenttä/<icao>")
def airport_api(icao):
    airport = get_airport_by_icao(icao)
    if airport is None:
        return jsonify({"error": "ICAO code not found"}), 404

    response = {
        "ICAO": airport["ident"],
        "Name": airport["name"],
        "Municipality": airport["municipality"]
    }

    return jsonify(response)