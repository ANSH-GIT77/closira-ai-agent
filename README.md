# Closira AI Engineering Intern Assignment

A Python-based AI customer support workflow built for the Closira internship assignment. It demonstrates FAQ answering, lead qualification, escalation detection, and automated summarization using the Google Gemini API.

## Setup Instructions
1. Clone this repository.
2. Create a virtual environment:
```powershell
   python -m venv venv
Activate the environment:

Windows (PowerShell): .\venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install dependencies:

PowerShell
   pip install google-genai python-dotenv
Create a .env file in the root directory and add your Google Gemini API key:

Code snippet
   GEMINI_API_KEY=AIzaSy...your_actual_key_here...
How to Run
Run the main script via your terminal:

PowerShell
python main.py
Type your messages as the customer. To end a normal session and generate the final summary, type quit. If an escalation rule is triggered by your input, the system will automatically log the reason and generate the summary for you.

System Architecture & Choices
Structured JSON Engine: The system uses Gemini's response_mime_type="application/json" capability to force the model to output a dual-layer response. It simultaneously handles the customer-facing text (reply) and backend flags (escalate, escalation_reason, lead_data). This ensures clean separation of concerns between conversational AI and backend routing logic.

Cost Efficiency: Transitioned the project architecture from OpenAI to Google Gemini's Developer Tier to build a robust, production-ready system utilizing high-performance free-tier models (gemini-2.5-flash).

Trade-offs & Limitations
Memory Management: The current implementation appends full structured state data back into the message history array. While highly accurate for maintaining structured state, it consumes context tokens faster over extended multi-turn chat sessions.

SOP Storage: The clinic's SOP is currently hardcoded within the codebase as a system instruction configuration. For real enterprise SMB scale, this should be uncoupled from the engine and served via a centralized vector database (RAG pattern) or an external CMS endpoint.