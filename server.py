from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import 
motion_detector
app = Flask("Emotion Detector")

@app.route("/EmotionDetection")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    dominant_emotion = emotion_detector_dict['dominant_emotion']
    # Return a formatted string with the emotion
    return "The given text has been identified as {}.".format(dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)