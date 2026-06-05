# CSOT GenAI/Agentic Track - Week 1 Submission

## Overview

For Week 1, I built a terminal-based multi-turn chatbot using the OpenRouter API and Python. The chatbot maintains conversation history, supports coherent multi-turn conversations, and demonstrates how stateless APIs can simulate memory by resending conversation history on every request.

## Implementation Details

I used the `openai` Python SDK with OpenRouter since OpenRouter follows an OpenAI-compatible API structure. To securely manage API credentials, I stored my API key in a `.env` file and loaded it using `python-dotenv`. I also added `.env` to `.gitignore` so that secrets are not accidentally committed.

The chatbot was implemented using a `ChatAgent` Python class to keep the code modular and reusable. The model is configurable through the constructor, making the chatbot model-agnostic.

The chatbot supports:

* Multi-turn conversation memory
* Conversation history using role-based messages (`system`, `user`, `assistant`)
* Exit commands (`exit`, `quit`)
* Resetting chat history using `/reset`
* Token usage inspection using `/tokens`

## Memory Handling

Since the API is stateless, the chatbot manually stores conversation history in a `messages` list and resends the full conversation during every API call.

To prevent unlimited context growth and increasing token usage, I implemented a rolling memory buffer using a maximum turn limit. When the conversation exceeds the configured limit, the oldest user-assistant message pairs are removed while preserving the system prompt.

I also tested context loss by resetting the conversation history and observing how the chatbot no longer remembered earlier information.

## Challenges Faced

One issue I encountered was model availability on OpenRouter. Some models mentioned in the instructions were unavailable, so I switched to an available free model.

Another challenge was understanding how stateless APIs work. Initially, I assumed the model remembers previous messages, but after experimenting with resetting history, I understood that memory only exists through the conversation history passed into the API.

## Learnings

This assignment helped me understand:

* How chat completion APIs work
* API key safety and environment variables
* Statelessness in LLM APIs
* Role-based message formatting
* Managing conversation memory and token growth
* Structuring Python code using classes
