from flask import Flask, jsonify
from
app = Flask(__name__)

@app.route("/alkuluku/<int:given_number>")
def prime_api(given_number: int):
    result = {
        "Number": given_number,
        "isPrime": is_prime(given_number)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)