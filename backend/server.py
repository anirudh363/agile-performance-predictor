import json 

from flask import Flask

app = Flask(__name__)


# app.register_blueprint(, url_prefix='')



@app.route('/')
def home():
    return "Welcome to the Agile Performance Prediction API"


if __name__ == "__main__":
    app.run(debug=True)