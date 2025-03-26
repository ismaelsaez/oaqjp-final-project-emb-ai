"""
Flask server app for emotion detection
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    """Returns emotion detection result in text"""
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        message = "<strong>Invalid text! Please try again!</strong>"
        return message
    message = "For the given statement, the system response is 'anger': " \
    f"{result['anger']}, 'disgust': {result['disgust']}, 'joy': {result['joy']}" \
    f" and 'sadness': {result['sadness']}." \
    f" The dominant emotion is <strong>{result['dominant_emotion']}</strong>."
    return message

@app.route("/")
def index():
    """Returns html for default index page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
    