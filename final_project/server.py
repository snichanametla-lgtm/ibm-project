from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text_to_analyze = request.form["textToAnalyze"]
    response = emotion_detector(text_to_analyze)

    # Error handling for blank input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
