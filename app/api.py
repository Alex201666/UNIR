import http.client
from flask import Flask, redirect, url_for
from app import util
from app.calc import Calculator
import http.client

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}

@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"

@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return (str(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/subtract/<op_1>/<op_2>", methods=["GET"])
def subtract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return (str(CALCULATOR.subtract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return (str(CALCULATOR.multiply(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = float(op_1), float(op_2)
        if num_2 == 0:
            return redirect(url_for('error_406'))
        return str(num_1 / num_2), http.client.OK
    except ValueError:
        return "Invalid input", http.client.BAD_REQUEST

@api_application.route("/error-406")
def error_406():
    return "Error: Division by zero", http.client.NOT_ACCEPTABLE

if __name__ == "__main__":
    api_application.run(debug=True)
