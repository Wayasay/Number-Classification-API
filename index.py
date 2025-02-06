from flask import Flask, jsonify, request
from utils import is_prime, sum_digit, get_fun_fact, get_number_properties, is_perfect

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask server is running on Vercel!"

@app.route("/api/classify-number")
def classify_num():
    number = request.args.get('number')
    try:
        if int(number) < 0:
            return jsonify({}
                )
    except ValueError:
        if not number or not number.isdigit():
            return jsonify({
                "number": "alphabet",
                "error": True}), 400
    

    return jsonify({
        "number": int(number),
        "is_prime": is_prime(number),
        "digit_sum": sum_digit(str(number)),
        "fun_fact": get_fun_fact(number),
        "properties": get_number_properties(str(number)),
        "is_perfect": is_perfect(number)
    })

if __name__ == "__main__":
    app.run(debug=True)
