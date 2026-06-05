import requests
import json


OLLAMA_URL = "http://localhost:11434/api/generate"


def classify_lead(message: str):
    
    try: 
        
        prompt = f"""
    You are a lead qualification assistant.

    Classify the lead into one of:

    - Hot
    - Warm
    - Cold

    Rules:

    Hot:
    - Wants a call
    - Has budget
    - Clear project requirement

    Warm:
    - Interested
    - Asking questions
    - Exploring options

    Cold:
    - Spam
    - Unclear
    - No buying intent

    Also generate a short personalized reply.

    Return ONLY valid JSON.

    Example:

    {{
        "classification": "Hot",
        "suggested_reply": "Thank you for reaching out..."
    }}

    Message:

    {message}
    """

        payload = {
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        result = response.json()

        return json.loads(result["response"])
    
    except Exception as e:
        
        return {
            "classification": "Warm",
            "suggested_reply": "Thank you for contacting us."
        }