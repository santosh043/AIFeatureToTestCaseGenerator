# Backend Architect SOP

## Overview
The backend is a lightweight Python Flask application that serves as the bridge between the Frontend UI and the local Ollama instance. It is responsible for receiving user input, constructing the prompt according to the defined template, sending it to Ollama, and returning the structured JSON response.

## Core Responsibilities
1.  **Serve UI:** Host the static frontend files (HTML/CSS/JS).
2.  **API Endpoint:** Provide a `/generate` endpoint for the frontend.
3.  **Prompt Engineering:** Inject the user input into the strict JSON-enforcing system prompt.
4.  **Error Handling:** Manage Ollama connection errors and JSON parsing failures.

## Technical Stack
- **Language:** Python 3.x
- **Framework:** Flask (pip install flask)
- **LLM Integration:** `requests` library to call Ollama API directly.

## Workflow Logic
1.  **Receive Request:** POST `/generate` with `{"user_input": "..."}`.
2.  **Construct Prompt:**
    - Load System Prompt from `gemini.md` (or hardcoded constant based on it).
    - Append User Input.
3.  **Call Ollama:**
    - URL: `http://localhost:11434/api/generate`
    - Model: `llama3.2:3b`
    - Format: `json` (Ollama supports `format='json'` to enforce valid JSON).
4.  **Process Response:**
    - Parse standard Ollama response.
    - Extract `response` field.
    - Validate it is valid JSON with `test_cases` array.
5.  **Return Response:** Send JSON back to UI.

## Golden Rules
- **Formatting:** Always request `format='json'` from Ollama.
- **Fallbacks:** If Ollama returns non-JSON, wrap the raw text in a safe JSON object: `{"raw_response": "..."}`.
- **Stateless:** The backend stores no state.
