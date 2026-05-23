# Closira AI Engineering Intern Assignment

A Python-based AI customer support workflow built for the Closira internship assignment.  
This project demonstrates:

- FAQ answering
- Lead qualification
- Escalation detection
- Automated conversation summarization

Built using the **Google Gemini API** with structured JSON responses for clean backend integration.

---

# Features

- AI-powered customer support workflow
- Automatic escalation detection
- Lead information extraction
- Session summarization
- Structured JSON response handling
- Gemini Developer API integration
- Lightweight and cost-efficient architecture

---

# Tech Stack

- Python
- Google Gemini API
- python-dotenv
- JSON-based response architecture

---

# Project Structure

```bash
project-folder/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <your-repository-link>
cd <repository-folder>
```

---

## 2. Create Virtual Environment

### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install google-genai python-dotenv
```

---

## 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

# How to Run

Run the main script:

```bash
python main.py
```

Start chatting as the customer.

To end the session and generate the final summary:

```text
quit
```

If an escalation rule is triggered, the system will automatically:

- Detect the escalation
- Log the escalation reason
- Generate the final conversation summary

---

# System Architecture & Design Choices

## Structured JSON Engine

The system uses Gemini's:

```python
response_mime_type="application/json"
```

This forces the model to return a structured response containing:

```json
{
  "reply": "...",
  "escalate": false,
  "escalation_reason": "",
  "lead_data": {}
}
```

This architecture cleanly separates:

- Customer-facing responses
- Backend workflow logic
- Escalation handling
- Lead qualification data

---

## Cost Efficiency

The architecture was transitioned from OpenAI APIs to:

### Google Gemini Developer Tier

Using:

```text
gemini-2.5-flash
```

Benefits:

- Lower operational cost
- Fast response generation
- Production-ready performance
- Free-tier friendly development

---

# Trade-offs & Limitations

## Memory Management

The current implementation appends structured state data into the message history for every turn.

### Advantage

- Better conversational memory
- Accurate workflow state tracking

### Limitation

- Higher context token usage during long conversations

---

## SOP Storage

Currently, the clinic SOP is hardcoded inside the system instructions.

### Recommended Production Approach

For real-world enterprise scalability, the SOP layer should be moved to:

- Vector Database (RAG Architecture)
- External CMS
- Knowledge Base API

This would allow:

- Dynamic SOP updates
- Better maintainability
- Multi-client scalability
- Easier enterprise deployment

---

# Future Improvements

- RAG-based knowledge retrieval
- Multi-agent workflow support
- Database integration
- Web dashboard
- Analytics & reporting
- Voice support
- Real-time CRM integration

---

# Example Workflow

```text
Customer Query
       ↓
Gemini AI Processing
       ↓
Structured JSON Output
       ↓
Lead Qualification / FAQ Response
       ↓
Escalation Detection
       ↓
Final Summary Generation
```

---

# Author

**Ansh**  
B.Tech CSE (AI & Edge Computing)

---

# License

This project is created for internship assignment and educational purposes.