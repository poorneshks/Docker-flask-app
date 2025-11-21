from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.INFO)
app.logger.info("Application started")

@app.route("/")
def home():
    app.logger.info("Home endpoint accessed")
    return "<h3>Hello from Dockerized Flask App on Azure with CI/CD!</h3>"

@app.route("/health")
def health():
    app.logger.info("Health endpoint checked")
    return jsonify(status="UP")

@app.route("/error")
def error():
    app.logger.error("Intentional error endpoint triggered")
    raise Exception("Intentional error!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
