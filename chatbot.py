import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


class ChatAgent:
    
    def __init__(
            self,
            model="openai/gpt-oss-120b:free",
            system_prompt="You are a helpful assistant.",
            max_turns=5
    ):

       
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ["OPENROUTER_API_KEY"],
        )

       
        self.model = model

        # Conversation history
        self.messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        # Last token usage
        self.last_usage = None
        self.max_turns = max_turns

    def call_model(self):
    

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )

        self.last_usage = response.usage

        assistant_reply = response.choices[0].message.content

        return assistant_reply

    def trim_history(self):
        max_messages = self.max_turns * 2

        conversation_only = self.messages[1:]

        if len(conversation_only) > max_messages:
            self.messages = (
                    [self.messages[0]]
                    + conversation_only[-max_messages:]
            )

    def reset_history(self):
        
        system_message = self.messages[0]

        self.messages = [system_message]


    def chat(self):
       
        print("Chat started. Type 'exit' or 'quit' to stop.\n")

        while True:

            user_input = input("You: ")

            # Reset command
            if user_input.lower() == "/reset":
                self.reset_history()
                print("Chat history reset.\n")
                continue

            # Tokens command
            if user_input.lower() == "/tokens":

                if self.last_usage:
                    print(
                        f"Last total tokens: "
                        f"{self.last_usage.total_tokens}\n"
                    )
                else:
                    print("No token usage yet.\n")

                continue

            # Exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            # Add user message
            self.messages.append({
                "role": "user",
                "content": user_input
            })

            # Get assistant response
            assistant_reply = self.call_model()

            # Store assistant response
            self.messages.append({
                "role": "assistant",
                "content": assistant_reply
            })

            # Trim old history
            self.trim_history()

            # Print response
            print(f"Bot: {assistant_reply}")

            # Show token usage
            if self.last_usage:
                print(
                    f"\nTokens used: "
                    f"{self.last_usage.total_tokens}\n"
                )


if __name__ == "__main__":

    agent = ChatAgent()

    agent.chat()
