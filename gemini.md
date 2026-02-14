# Project Constitution (Gemini)

## Data Schemas

### Input Payload
```json
{
  "user_input": "string",  // The feature or functionality description provided by the user
  "template_id": "default" // Identifier for specific test case templates
}
```

### Output Payload
```json
{
  "test_cases": [
    {
      "id": "TC_001",
      "title": "Verify login with valid credentials",
      "pre_conditions": "User is on login page",
      "steps": "1. Enter valid username\n2. Enter valid password\n3. Click Login",
      "expected_result": "User is redirected to dashboard",
      "type": "Positive",
      "priority": "High"
    }
  ],
  "raw_response": "string" // Full response from Ollama for fallback/display
}
```

## System Internal Prompts

### Default Test Case Generator Prompt
"You are an expert QA Automation Engineer. Your task is to generate detailed test cases based on the user's feature description.
You strictly follow this JSON format for the output:
{
  \"test_cases\": [
    {
      \"id\": \"TC_XXX\",
      \"title\": \"Concise title\",
      \"pre_conditions\": \"Prerequisites\",
      \"steps\": \"Step-by-step actions\",
      \"expected_result\": \"Expected outcome\",
      \"type\": \"Positive/Negative\",
      \"priority\": \"High/Medium/Low\"
    }
  ]
}
Do not include any conversational text outside the JSON object.
Feature Description: {user_input}"

## Behavioral Rules
1. **Model:** Use `llama3.2:3b` via Ollama.
2. **Template Adherence:** The system must strictly follow the defined JSON structure.
3. **UI Interaction:** Simple Chat UI. User sends text, System returns formatted Test Cases.
4. **Error Handling:** If Ollama is offline or returns malformed JSON, return a clear user-friendly error message.

## Architectural Invariants
1. **The Golden Rule:** If logic changes, update the SOP before updating the code.
2. **Data-First:** Define JSON Data Schema before building tools.
3. **Self-Annealing:** Analyze -> Patch -> Test -> Update Architecture.

## Maintenance Log
- Project Initialized.
- Discovery Phase Complete. Schema Defined.
- Default Prompt Template Established (Pending User Customization).
