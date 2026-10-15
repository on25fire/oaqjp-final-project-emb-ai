"""Flask web application for emotion detection"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """Analyze submitted text and return its detected emotion."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotion

    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return result

@app.route("/")
def render_index_page():
    """Display the emotion detector web page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
