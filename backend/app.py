
"""
NVIDIA NetQ Network Observability Lab
Main Flask Backend Application
"""

from flask import Flask, jsonify, send_from_directory
from pathlib import Path

from network_monitor import (
    get_network_devices,
    get_network_health,
    get_network_alerts
)


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Initialize Flask
app = Flask(
    __name__,
    static_folder=str(PROJECT_ROOT),
    static_url_path=""
)


# Home route
@app.route("/")
def home():
    return send_from_directory(
        str(PROJECT_ROOT),
        "index.html"
    )


# API: Get all network devices
@app.route("/api/devices", methods=["GET"])
def devices():
    return jsonify({
        "success": True,
        "devices": get_network_devices()
    })


# API: Get network health
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "success": True,
        "health": get_network_health()
    })


# API: Get network alerts
@app.route("/api/alerts", methods=["GET"])
def alerts():
    return jsonify({
        "success": True,
        "alerts": get_network_alerts()
    })


# API: Backend status
@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({
        "success": True,
        "application": "NVIDIA NetQ Network Observability Lab",
        "backend": "Flask",
        "mode": "Educational Simulation",
        "status": "Running"
    })


# Start development server
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
