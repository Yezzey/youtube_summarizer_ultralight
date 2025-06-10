from flask import Flask, request, jsonify
from utils.summary import summarize_text

app = Flask(__name__)

@app.route("/api/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    if not data or "video_url" not in data:
        return jsonify({"error": "Missing video_url"}), 400

    video_url = data["video_url"]
    try:
        summary = summarize_text(video_url)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return "YouTube Summarizer is running. Use /api/summarize with POST."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
