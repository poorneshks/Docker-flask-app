from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h3>Hello from Dockerized Flask App on Azure!</h3>"

@app.route('/health')
def health():
    return jsonify(status="UP")

@app.route('/error')
def error():
    raise Exception("Intentional error!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
import logging

logging.basicConfig(level=logging.INFO)
app.logger.info("Application started")

import logging

logging.basicConfig(level=logging.INFO)
app.logger.info("Application started")

@app.route("/")
def home():
    app.logger.info("Home endpoint accessed")
    return "Hello from Docker + GitHub Actions + Azure!"

