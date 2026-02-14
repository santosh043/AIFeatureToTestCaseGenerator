
from flask import Flask, render_template, request, jsonify
import requests
import json
import logging

app = Flask(__name__)

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# --- System Prompt Definition ---
SYSTEM_PROMPT = """You are an expert QA Automation Engineer. Your task is to generate detailed test cases based on the user's feature description.
You strictly follow this JSON format for the output:
{
  "test_cases": [
    {
      "id": "TC_XXX",
      "title": "Concise title",
      "pre_conditions": "Prerequisites",
      "steps": "Step-by-step actions",
      "expected_result": "Expected outcome",
      "type": "Positive/Negative",
      "priority": "High/Medium/Low"
    }
  ]
}
Do not include any conversational text outside the JSON object.
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_test_cases():
    data = request.json
    user_input = data.get('user_input', '')

    if not user_input:
        return jsonify({"error": "User input is required"}), 400

    # Construct the full prompt
    full_prompt = f"{SYSTEM_PROMPT}\nFeature Description: {user_input}"

    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "format": "json",  # Force JSON output from Ollama
        "stream": False
    }

    try:
        logger.info(f"Sending request to Ollama: {MODEL_NAME}")
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        
        result = response.json()
        raw_response = result.get('response', '')
        
        # Validate/Parse JSON
        try:
            parsed_json = json.loads(raw_response)
        except json.JSONDecodeError:
            logger.error("Failed to parse JSON from Ollama response.")
            # Fallback: wrap raw response
            parsed_json = {"raw_response": raw_response, "test_cases": []}

        return jsonify(parsed_json)

    except requests.exceptions.RequestException as e:
        logger.error(f"Ollama connection error: {e}")
        return jsonify({"error": f"Failed to connect to Ollama: {str(e)}"}), 502

if __name__ == '__main__':
    print(f"Starting Local Test Case Generator on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
