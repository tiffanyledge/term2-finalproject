from flask import Flask, render_template
import requests

app = Flask(__name__)
api_key = '8e6bcea38d244f3a9d0c276030645072'

@app.route('/')
def index():
    response = requests.get(f'https://api.twelvedata.com/stocks?source=docs&apikey={api_key}')
    data = response.json()
    stocks = []

    entries = data["data"]

    for entry in entries:
        print(entry)
        stock = {
            "symbol": entry["symbol"],
            "name": entry["name"],
            "currency": entry["currency"],
            "exchange": entry["exchange"],
            "mic_code": entry["mic_code"],
            "country": entry["country"],
            "type": entry["type"]
        }

        stocks.append(stock)
    

    return render_template('index.html' , data = stocks)


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')