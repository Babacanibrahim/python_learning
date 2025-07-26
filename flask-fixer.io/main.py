from flask import Flask, render_template, request
import requests

url = "http://data.fixer.io/api/latest?access_key=8db463f46bfc06a9f37cf57da39fb246"

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():

    if request.method=="POST":
        firstCurrency = request.form.get("firstCurrency")  # DOLAR
        secondCurrency = request.form.get("secondCurrency") # TRY
        amount = request.form.get("amount") # 10

        response = requests.get(url)
        data  = response.json()
        
        firstValue = data["rates"][firstCurrency]  # 1.17
        secondValue = data["rates"][secondCurrency] # 45

        result = float(secondValue) / float(firstValue) * float(amount)

        return render_template("index.html", result = result, secondCurrency = secondCurrency, firstCurrency = firstCurrency, amount = amount)


    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)