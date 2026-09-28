from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def home():
    """Root endpoint — returns service metadata."""
    return jsonify({
        "service": "aws-production-engine",
        "version": os.environ.get("APP_VERSION", "1.0.0"),
        "status": "running",
        "message": "Deployed via GitOps pipeline"
    }), 200


@app.route('/health')
def health():
    """Health check endpoint for Kubernetes probes and monitoring."""
    return jsonify({
        "status": "healthy",
        "service": "aws-production-engine"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)