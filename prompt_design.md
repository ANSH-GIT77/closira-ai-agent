# Prompt Design & Architecture

## System Prompt
The system prompt is designed to act as the primary brain of the AI workflow. It defines the persona, injects the SOP dynamically, and enforces a strict JSON output structure. By forcing JSON, the LLM simultaneously acts as a conversational agent and a classification engine (evaluating its own responses for escalations).

## Hallucination Prevention
To prevent hallucinations, the prompt explicitly states: "Answer questions STRICTLY using the SOP Data. Do not hallucinate or make up information." Furthermore, because the AI is instructed to trigger an escalation for out-of-scope questions, it provides an "escape hatch" rather than forcing the model to guess an answer when data is missing.

## Confidence-Based Escalation
Escalation is built directly into the JSON response schema. The model evaluates user input against the strict escalation triggers (medical questions, complaints, pricing negotiations, out-of-scope topics). If triggered, the model sets `"escalate": true` and populates the `"escalation_reason"`. The Python backend detects this boolean flag, logs the reason, and terminates the automated loop to hand off to a human.

## Tone and Persona
The persona is defined as an "AI customer support assistant for Bloom Aesthetics Clinic" with a "professional, empathetic, and concise" tone. This ensures the communication style aligns with the expectations of a high-end SMB aesthetics clinic, keeping interactions polite but efficient.