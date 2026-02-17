import json, requests
from flask import Flask
app = Flask(__name__)

@app.route("/call")
def call():
    registry = json.load(open("registry.json"))
    return requests.get(registry["service-b"] + "/data").text

app.run(host="0.0.0.0", port=5001)
