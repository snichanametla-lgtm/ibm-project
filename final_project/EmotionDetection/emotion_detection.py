import requests  # optional, only if you use it for API calls

def emotion_detector(text):
    """
    Simple mock function to analyze emotion from text.
    Returns a dictionary of emotion scores and dominant emotion.
    """
    # Initialize all scores
    emotion_scores = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0
    }

    text_lower = text.lower()

    # Basic keyword-based scoring
    if any(word in text_lower for word in ["happy", "joy", "glad"]):
        emotion_scores["joy"] = 1.0
        dominant = "joy"
    elif any(word in text_lower for word in ["sad", "unhappy", "cry"]):
        emotion_scores["sadness"] = 1.0
        dominant = "sadness"
    elif any(word in text_lower for word in ["angry", "mad", "furious"]):
        emotion_scores["anger"] = 1.0
        dominant = "anger"
    elif any(word in text_lower for word in ["fear", "scared", "afraid"]):
        emotion_scores["fear"] = 1.0
        dominant = "fear"
    elif any(word in text_lower for word in ["disgust", "gross", "nasty"]):
        emotion_scores["disgust"] = 1.0
        dominant = "disgust"
    else:
        dominant = None  # no dominant emotion detected

    # Add dominant emotion to the dictionary
    emotion_scores["dominant_emotion"] = dominant

    return emotion_scores
