from flask import Flask, jsonify
# from Module_5.alkuluvut import primeNumber

def primeNumber(luku):
    given_number = int(luku)
    is_prime_number = True
    if given_number < 2:
        is_prime_number = False
    else:
        for number in range(2, given_number -1):
            if given_number % number == 0:
                is_prime_number = False
                break
    return is_prime_number

app = Flask(__name__)
@app.route("/alkuluku/<int:given_number>")
def prime_api(given_number: int):
    result = {
        "Number": given_number,
        "isPrime": primeNumber(given_number)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)