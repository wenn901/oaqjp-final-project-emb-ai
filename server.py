from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector 

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyze)
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion'][0]

    return f"For the given statement, the system response is {anger}, {disgust}, {fear}, {joy} and {sadness}. The dominant emotion is <b>{dominant_emotion}</b>."

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)