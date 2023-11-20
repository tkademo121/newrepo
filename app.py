from flask import Flask, render_template, request
from model import predict_price

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            feature_value = float(request.form['feature_value'])
            prediction = predict_price(feature_value)
        except ValueError:
            prediction = "Invalid input. Please enter a valid number."

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)

