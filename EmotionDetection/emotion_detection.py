import requests #Importing the request library
import json #Importing the json library

def emotion_detector(text_to_analyze):  #define the function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # The URL of the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} #The headers of the emotion API
    myjob = { "raw_document": { "text": text_to_analyze } } # The place holder for text to be analysed
    response = requests.post(url, json = myjob, headers=headers)  # Send a POST request to the API with the text and headers

    #If the response status code is 200, extract the data
    if response.status_code == 200:
        #parse the response from the server
        formatted_response = json.loads(response.text) # Parsing the JSON response from the API
    #If the status code is 500, set response to None
    elif response.status_code == 500:
        emotion_detector_dict = None
        dominant_emotion = None
    
    #If the status code is 400, set response to None
    elif response.status_code == 400:
        emotion_detector_dict = None
        dominant_emotion = None
    
    #For any other unexpected status codes, set data to None

    else:
        emotion_detector_dict = None
        dominant_emotion = None


    formatted_response = json.loads(response.text) # Parsing the JSON response from the API
    emotion_detector_dict = formatted_response['emotionPredictions'][0]['emotion'] #Extracting the emotion predictions and score
    dominant_emotion = max(emotion_detector_dict, key=emotion_detector_dict.get)
    emotion_detector_dict['dominant_emotion'] = dominant_emotion
    return json.dumps(emotion_detector_dict, indent=4) # Returning a dictionary containing sentiment analysis result