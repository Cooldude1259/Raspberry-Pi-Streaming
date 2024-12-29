from flask import Flask, jsonify, send_from_directory
import os
import json

app = Flask(__name__)

VIDEOS_DIR = "Videos"  # Directory for video files and thumbnails
META_DIR = "VidInfo"   # Directory for video metadata (JSON)


@app.route('/')
def home():
    # Serve the index.html file
    return send_from_directory('.', 'index.html')


@app.route('/videos')
def get_videos():
    video_list = []

    # Check if VidInfo directory exists and contains JSON files
    if os.path.exists(META_DIR):
        for file in os.listdir(META_DIR):
            if file.endswith(".json"):
                with open(os.path.join(META_DIR, file), 'r') as f:
                    try:
                        metadata = json.load(f)
                        video_list.append(metadata)
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from file: {file}")
    else:
        print(f"{META_DIR} directory does not exist.")

    return jsonify(video_list)


@app.route('/Videos/<filename>')
def serve_video(filename):
    if os.path.exists(os.path.join(VIDEOS_DIR, filename)):
        return send_from_directory(VIDEOS_DIR, filename)
    else:
        return "Video not found", 404


@app.route('/Thumbnails/<filename>')
def serve_thumbnail(filename):
    if os.path.exists(os.path.join(VIDEOS_DIR, filename)):
        return send_from_directory(VIDEOS_DIR, filename)
    else:
        return "Thumbnail not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

