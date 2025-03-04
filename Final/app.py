from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
from datetime import datetime

app = Flask(__name__)

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            # Allow up to 15 seconds of silence before ending the recording
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)
            print("Processing audio...")

            # Recognize speech
            text = recognizer.recognize_google(audio)
            return {"success": True, "text": text}
        except sr.UnknownValueError:
            return {"success": False, "error": "Could not understand audio"}
        except sr.RequestError as e:
            return {"success": False, "error": f"Error: {str(e)}"}

def save_text_to_file(text):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"user_response_{timestamp}.txt"
    with open(file_name, "w") as file:
        file.write(text)
    return file_name

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/record-response", methods=["POST"])
def record_response():
    response = recognize_speech_from_microphone()
    if response["success"]:
        save_text_to_file(response["text"])
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
