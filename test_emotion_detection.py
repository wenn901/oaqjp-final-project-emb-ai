from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_1(self): 
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'][0], 'joy')
    
    def test_2(self): 
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'][0], 'anger')

    def test_3(self): 
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'][0], 'disgust')
    
    def test_4(self): 
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'][0], 'sadness')

    def test_5(self): 
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'][0], 'fear')
   

if __name__ == '__main__':
    unittest.main()