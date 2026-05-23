import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
# Initialize the Gemini client using the environment variable
client = genai.Client()

SOP_DATA = """
Business: Bloom Aesthetics Clinic
Hours: Mon-Sat, 9 am-7 pm
Services: Botox (from £200), Fillers (from £250), Consultations (free)
Booking: Via WhatsApp or website. 24hr cancellation required.
Escalate if: complaint, medical question, pricing negotiation, or >2 unanswered questions.
"""

SYSTEM_PROMPT = f"""
You are an AI customer support assistant for Bloom Aesthetics Clinic.
Your tone is professional, empathetic, and concise.

SOP DATA:
{SOP_DATA}

INSTRUCTIONS:
1. FAQ Answering: Answer questions STRICTLY using the SOP Data. Do not hallucinate or make up information.
2. Lead Qualification: Once basic questions are answered, smoothly ask 1-2 questions to qualify the lead (e.g., "Have you visited us before?" or "Are you looking to book a consultation?").
3. Escalation: You must flag an escalation if the user has a complaint, asks a medical question, tries to negotiate pricing, or asks something not covered in the SOP.

OUTPUT FORMAT:
You must ALWAYS respond with a valid JSON object containing the following keys:
- "reply": (string) Your message to the customer. If escalating, politely inform them a human will take over.
- "escalate": (boolean) true if the conversation requires human handoff, false otherwise.
- "escalation_reason": (string or null) The reason for escalation, or null.
- "lead_data": (object) Any qualification details collected so far (e.g., {{"visited_before": true}}).
"""

def summarize_conversation(chat_history):
    print("\n--- Generating Conversation Summary ---")
    summary_prompt = "Summarize the following customer service interaction. Include: customer intent, key details collected, SOP gaps identified (if any), and recommended next action."
    
    history_text = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in chat_history if m['role'] != 'system'])
    full_prompt = f"{summary_prompt}\n\nInteraction History:\n{history_text}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )
    print(response.text)

def main():
    print("Welcome to the Closira AI Workflow Demo (Type 'quit' to exit)\n")
    
    chat_history = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    gemini_messages = [
        types.Content(role="user", parts=[types.Part.from_text(text=SYSTEM_PROMPT)]),
        types.Content(role="model", parts=[types.Part.from_text(text="Understood. I will strictly act according to the SOP guidelines and output only valid JSON.")])
    ]
    
    while True:
        user_input = input("Customer: ")
        if user_input.lower() in ['quit', 'exit']:
            break
            
        chat_history.append({"role": "user", "content": user_input})
        gemini_messages.append(types.Content(role="user", parts=[types.Part.from_text(text=user_input)]))

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=gemini_messages,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                ),
            )
            
            ai_output = json.loads(response.text)
            print(f"AI: {ai_output.get('reply')}")
            
            chat_history.append({"role": "assistant", "content": response.text})
            gemini_messages.append(types.Content(role="model", parts=[types.Part.from_text(text=response.text)]))

            if ai_output.get('escalate'):
                print(f"\n[SYSTEM LOG] Escalation Triggered! Reason: {ai_output.get('escalation_reason')}")
                break

        except Exception as e:
            print(f"Error: {e}")
            break
            
    if len(chat_history) > 1:
        summarize_conversation(chat_history)

if __name__ == "__main__":
    main()