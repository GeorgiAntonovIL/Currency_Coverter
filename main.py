import json

from flask import Flask, jsonify, render_template, request
import json
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('converter_form.html')


@app.route("/result", methods=['POST'])
def result():

    currency_1 = request.form['currency1_input']
    amount = float(request.form['amount'])
    currency_2 = request.form['currency_to_convert_into']

    req = requests.get(f'https://open.er-api.com/v6/latest/{currency_1}')
    dictionary = json.loads(req.content)
    currency_dict = dictionary['rates']
    currency_rate = currency_dict.get(currency_2)

    result_of_transfer = amount / currency_rate

    return str(result_of_transfer)


if __name__ == '__main__':
    app.run(debug=True)
