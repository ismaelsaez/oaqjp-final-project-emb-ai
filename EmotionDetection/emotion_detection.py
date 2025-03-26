import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP Emotion Predict function.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        str: The text attribute of the response object from the Emotion Detection function.
    """
    # Define the URL and headers for the Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Define the input JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make the POST request to the Watson NLP API
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 400:
        emotion = {"anger": None, "disgust": None, "fear": None, 
                    "joy": None, "sadness": None, "dominant_emotion":None}
        return emotion
    formatted_response = json.loads(response.text)
    emotion = formatted_response["emotionPredictions"][0]["emotion"]
    emotion["dominant_emotion"] = max(emotion, key=emotion.get)

    return emotion