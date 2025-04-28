import requests
import json

def review_code(prompt):
    url = "http://127.0.0.1:11434/api/chat"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemma3:4b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
        "temperature": 0.2
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=20)
        print("Raw response text:", response.text)
        response.raise_for_status()
        result = response.json()
        return result["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except KeyError:
        return f"Invalid response structure:\n{response.text}"