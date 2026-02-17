from flask import Flask
import requests

app = Flask(__name__)

@app.route("/service-a")
def a():
    return requests.get("http://localhost:5001").text

@app.route("/service-b")
def b():
    return requests.get("http://localhost:6002/data").text

app.run(host="0.0.0.0", port=8000)
