from flask import Flask, request
import run
import csv
import json
import requests

url = 'http://e5690c0c.ngrok.io/all-data'

app = Flask(__name__)
def json_to_csv():
    url = 'https://e5690c0c.ngrok.io/all-data'
    r = requests.get(url)
    data = r.json()

    header = ["Timestamp", "Category", "Activity", "Keystrokes", "Gaze", "Emotion", "Eyes"]

    with open('data/test.csv', 'w', newline='') as csvfile:

        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(header)
        for i in data:
            spamwriter.writerow(i[h] for h in header)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/predict", methods=['GET'])
def predict():
    if request.method == "GET":
        json_to_csv()
        return run.predict("data/testedited.csv")



if __name__ == '__main__':
    app.run(debug=True)
