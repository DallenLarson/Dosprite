import os
from flask import Flask, request, send_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    """Handles receiving a sprite file from a user"""
    file = request.files["sprite"]
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, "latest.png"))
        return "File received", 200
    return "No file uploaded", 400

@app.route("/download", methods=["GET"])
def download_file():
    """Serves the latest sprite file to users"""
    filepath = os.path.join(UPLOAD_FOLDER, "latest.png")
    if os.path.exists(filepath):
        return send_file(filepath, mimetype="image/png")
    return "No file available", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
