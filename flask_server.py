from flask import Flask, request
import run

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/predict", methods=['GET'])
def predict():
    if request.method == "GET":
        import pandas as pd
        return run.predict("test.csv")
        #TODO:
        # call the mongoDB and download as csv, save the file name as test.csv
        # pass the entire csv file to predict() in run.py
        #do request to frontend to return predictions



if __name__ == '__main__':
    app.run(debug=True)
