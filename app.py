from flask import Flask, jsonify, request
from utils import is_prime, sum_digit, is_amstrong_number, get_fun_fact, get_number_properties, is_perfect

app = Flask(__name__)


@app.route("/add")
def add():
    return str (is_prime(1+1))


@app.route("/api/classify-number")
def classify_num():
    number = request.args.get('number')  
    return jsonify({
        "is_prime": is_prime(number),
        "digit_sum": sum_digit(number),
        "fun_fact": get_fun_fact(number), 
        "proprties": get_number_properties(number),
        "is_perfect": is_perfect(number)
    })





if __name__ == "__main__":
    app.run(debug=True)

