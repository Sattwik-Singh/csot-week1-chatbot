# CSOT GenAI/Agentic Track - Week 1 Submission

## Overview

For Week 1, I built a terminal-based chatbot using Python and OpenRouter API. The chatbot supports multi-turn conversations and remembers previous messages by storing conversation history.

## Implementation

I used the `openai` SDK with OpenRouter and loaded the API key securely through a `.env` file using `python-dotenv`. I also added `.env` to `.gitignore` so the API key is not exposed.

I implemented the chatbot using a `ChatAgent` class. The chatbot stores conversation history using `system`, `user`, and `assistant` roles and sends the full history during every API call.

Features implemented:
- Multi-turn conversation
- Conversation memory
- Exit commands (`exit`, `quit`)
- `/reset` to clear history
- `/tokens` to check token usage
- Rolling memory buffer to limit conversation size

## What I Learned

This assignment helped me understand that LLM APIs are stateless and only remember things if previous messages are sent again. I also learned about API key safety, token usage, and how chatbot memory works.

One issue I faced was model availability on OpenRouter, so I switched to another free model.
