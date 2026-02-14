# Frontend Architect SOP

## Overview
The frontend is a clean, responsive web interface designed to mimic a modern chat application. It focuses on simplicity and readability, allowing users to enter requirements and view generated test cases clearly.

## Core Responsibilities
1.  **User Input:** Text area for Feature Description.
2.  **Display:** Render generated test cases in a readable, tabular or card-like format.
3.  **Interaction:** "Generate" button with loading state.

## Design Aesthetic
- **Theme:** Clean, modern, "Data-First" design.
- **Colors:** Neutral grays, vibrant accent color (e.g., Blue or Purple) for actions.
- **Typography:** System fonts or Inter/Roboto.

## Technical Stack
- **HTML5:** Semantic structure.
- **CSS3:** Vanilla CSS (no framework overhead requested, unless specified otherwise. We will use Vanilla as per default).
- **JavaScript:** Vanilla JS for API calls and DOM manipulation.

## Component Structure
1.  **Header:** Title "Local LLM Test Case Generator".
2.  **Chat Container:**
    - **Message List:** Scrollable area for User/AI messages.
    - **Test Case Card:** A specific component to render the JSON output prettily (not just raw JSON).
3.  **Input Area:** Textarea + Send Button.

## Golden Rules
- **No Page Reloads:** Use `fetch()` for all interactions.
- **Error Visibility:** Show errors (e.g., "Ollama offline") directly in the chat stream.
- **Responsive:** Must work on different window sizes.
