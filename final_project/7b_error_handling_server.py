from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector  # use your updated function

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text_to_analyze = request.form.get("textToAnalyze", "").strip()

    # Handle blank input before calling emotion_detector
    if not text_to_analyze:
        return "Invalid text! Please enter some text to analyze."

    response = emotion_detector(text_to_analyze)

    # Handle the 400 status code from emotion_detector
    if "status_code" in response and response["status_code"] == 400:
        return "Error: Bad Request. Please provide valid text."

    emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    scores = {emotion: response.get(emotion, 0) for emotion in emotions}
    dominant_emotion = response.get("dominant_emotion", "Unknown")

    return (
        f"For the given statement, the system response is: "
        f"{', '.join([f'{k}: {v}' for k, v in scores.items()])}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
