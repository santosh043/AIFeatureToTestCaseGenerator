
import json
import requests
import sys

def handshake(model="llama3.2:3b"):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    
    # Simple prompt to test connectivity
    payload = {
        "model": model,
        "prompt": "Say 'Connection Successful' and nothing else.",
        "stream": False
    }

    print(f"Adding handshake request to {url} with model {model}...")

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            print("Status Code: 200 OK")
            result = response.json()
            print("Response:", result.get("response", "No response field found"))
            return True
        else:
            print(f"Error: Received status code {response.status_code}")
            print("Response:", response.text)
            return False

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama. Is it running on port 11434?")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    success = handshake()
    if not success:
        sys.exit(1)
