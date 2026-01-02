"""
server.py

This module implements the Flask web server for emotion detection application.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_analyzer():
    ''' Retrieve the text from user, then pass to be analyzed by the emotion detector.
    Finally, return the response displaying emotion scores and the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyze)
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    response_str = f"""For the given statement, the system response is {anger},
    {disgust}, {fear}, {joy} and {sadness}. 
    The dominant emotion is <b>{dominant_emotion}</b>."""

    return response_str

@app.route('/')
def render_index_page():
    ''' Render the index page to user. This is the display for input text
    from user, and the reponse back to user.
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
