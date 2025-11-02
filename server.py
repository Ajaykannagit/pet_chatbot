from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from io import BytesIO
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
from config import ELEVENLABS_API_KEY
from pet_bot_main import PetCareChatbot


app = Flask(__name__, static_folder="static", static_url_path="/")
CORS(app)

chatbot = PetCareChatbot()


@app.route("/")
def serve_index():
    return app.send_static_file("index.html")


@app.post("/api/chat")
def api_chat():
    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify({"error": "Missing 'text'"}), 400

    response_text, emotion = chatbot.get_response(text)
    return jsonify({"response": response_text, "emotion": emotion})


@app.post("/api/tts")
def api_tts():
    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()
    emotion = (data.get("emotion") or "calm").strip()
    if not text:
        return jsonify({"error": "Missing 'text'"}), 400

    if not ELEVENLABS_API_KEY or ELEVENLABS_API_KEY == "your-elevenlabs-key-here":
        return jsonify({"error": "TTS not configured (missing ELEVENLABS_API_KEY)"}), 501

    # Emotion settings aligned with PetCareChatbot
    emotions = {
        "happy": {"stability": 0.3, "similarity_boost": 0.7},
        "concerned": {"stability": 0.5, "similarity_boost": 0.8},
        "emergency": {"stability": 0.2, "similarity_boost": 0.9},
        "calm": {"stability": 0.7, "similarity_boost": 0.5},
    }
    settings = emotions.get(emotion, emotions["calm"])

    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    try:
        audio_stream = client.text_to_speech.convert(
            text=text,
            voice_id="EXAVITQu4vr4xnSDxMaL",
            model_id="eleven_monolingual_v1",
            voice_settings=VoiceSettings(
                stability=settings["stability"],
                similarity_boost=settings["similarity_boost"],
            ),
        )
        buf = BytesIO()
        for chunk in audio_stream:
            if isinstance(chunk, bytes):
                buf.write(chunk)
            else:
                # Some SDK versions yield dicts with 'audio'
                audio_bytes = chunk.get("audio") if isinstance(chunk, dict) else None
                if audio_bytes:
                    buf.write(audio_bytes)
        buf.seek(0)
        return send_file(buf, mimetype="audio/mpeg", as_attachment=False, download_name="speech.mp3")
    except Exception:
        # Silently return 501 so frontend can fallback to browser TTS
        return jsonify({"error": "TTS not available"}), 501


if __name__ == "__main__":
    # Run dev server
    app.run(host="0.0.0.0", port=5000, debug=True)


