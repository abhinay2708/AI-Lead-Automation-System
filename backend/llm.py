import requests
import json


OLLAMA_URL = "http://localhost:11434/api/generate"


def classify_lead(message: str):
    
    try: 
        
        prompt = f"""
            You are an expert sales lead qualification assistant.

            Your job is to classify leads into:

            Hot
            Warm
            Cold

            Classification Rules:

            HOT:
            - Has a clear business requirement
            - Mentions budget
            - Mentions timeline
            - Wants a call/demo
            - Looking for implementation
            - Looking to hire or purchase services

            Examples:
            "Need automation for onboarding"
            "Budget 50k/month"
            "Can we schedule a call?"
            "Need this live by end of month"
    
            WARM:
            - Interested in learning more
            - Asking questions
            - Exploring solutions
            - No budget mentioned
            - No immediate purchase intent

            Examples:
            "Can you share pricing?"
            "How does this work?"
            "Is your service free or paid?"

            COLD:
            - Spam
            - Greetings only
            - Unrelated content
            - No business intent

            Examples:
            "hello"
            "unsubscribe"
            "win iphone click here"

            Return ONLY  a valid JSON object.
            Don ot use markdown.
            Do not add explanation.
            
            Output format:
            {{
            "classification":"Hot",
            "suggested_reply":"..."
            }}

            Lead Message:

            {message}
            """

        payload = {
            "model": "llama3.2:latest",
            "prompt": prompt,
            "stream": False,
            "format":"json"
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        result = response.json()

        return json.loads(result["response"])
    
    except Exception as e:
        print("ERROR:", e)
        
        return {
            "classification": "Warm",
            "suggested_reply": "Thank you for contacting us."
        }