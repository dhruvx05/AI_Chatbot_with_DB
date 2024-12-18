# chatbot.py

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import database 

# Define the prompt template
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model="phi3")  # Replace "phi3" with your specific model
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    # Connect to the database and create the table
    conn = database.connect_to_db()
    database.create_table(conn)

    context = ""  # Initialize context as an empty string
    print("Welcome to the AI ChatBot!")
    print("Type 'exit' to quit, 'show history' to see past conversations, or 'delete history' to clear all conversations.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "show history":
            # Fetch and display conversation history
            conversations = database.fetch_conversations(conn)
            if not conversations:
                print("No conversation history found.")
            else:
                print("Conversation History:")
                for i, (user, bot) in enumerate(conversations, start=1):
                    print(f"{i}. User: {user} | Bot: {bot}")
            continue
        elif user_input.lower() == "delete history":
            # Delete all conversation history
            confirm = input("Are you sure you want to delete all conversation history? (yes/no): ").lower()
            if confirm == "yes":
                database.delete_all_conversations(conn)
                print("All conversation history has been deleted.")
            else:
                print("Deletion canceled.")
            continue
        # Get AI response using the model
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)

        # Update context
        context += f"\nUser: {user_input}\nAI: {result}"

        # Store the conversation in the database
        database.insert_conversation(conn, user_input, result)

    # Close the connection when done
    conn.close()
    
if __name__ == "__main__":
    handle_conversation()
