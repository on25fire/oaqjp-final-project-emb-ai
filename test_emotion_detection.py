from EmotionDetection.emotion_detection import emotion_detector
import unittest
import json

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        #Test case for joyful statement
        # Note: We use json.loads() to convert the returned JSON string back into a dictionary
        result_1 = json.loads(emotion_detector('I am glad this happened'))
        self.assertEqual(result_1['dominant_emotion'],'joy')
        
        # Test case for angry statement
        result_2 = json.loads(emotion_detector('I am really mad about this'))
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case for neutral sentiment
        result_3 = json.loads(emotion_detector('I feel disgusted just hearing about this'))
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        result_4 = json.loads(emotion_detector('I am so sad about this'))
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = json.loads(emotion_detector('I am really afraid that this will happen'))
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
