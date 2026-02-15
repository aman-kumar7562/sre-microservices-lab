from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "SRE Microservice is running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/slow")
def slow():
    time.sleep(2)
    return jsonify({"message": "Slow response simulated"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

