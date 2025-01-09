"""
Name: Discord AI ChatBot
Description:
            Simple AI chatbot will take the input from the user.
            The bot will figure out what user intends to say.
            It will look at patterns, and then output a response.
            I am not sure, how I will integrate this code to Discord, but
            I will try my best.

Structure: Modular
License: Apache 2
Version: 0.0.1
Update-date: 9 Jan 00:07
What's new: The keys entered into dictionary are in lowercase
            i.e. there is no difference between "hello" and "HeLlO"
"""

import json # Used to access required JSON files.


def load_knowledge(file_path):
    """A Function to load knowledge stored in JSON file."""
    try:
        # Open JSON file in a read-mode and return it's content.
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {} # File is not in the directory provided.


def save_knowledge(knowledge, file_path):
    """A Function to store knowledge in JSON file."""
    with open(file_path, "w") as file:
        json.dump(knowledge, file, indent=4)


def get_response(user_input, knowledge):
    """A Function to provide a reply to the user."""
    if user_input in knowledge:
        return knowledge[user_input]
    else: # User input is not in the knowledge base.
        return None


def learn_new_response(user_input, knowledge):
    """A Function to learn from the user."""
    print(f"As an AI model, I don't know how to respond to {user_input}")
    new_response = input("What should I reply to this? ")
    knowledge[user_input] = new_response # Add new combination to the knowledge base.
    return knowledge


def chat():
    """A Function to initiate a chat between the bot and the user."""
    knowledge_file = "intents.json" # Data File.
    knowledge = load_knowledge(knowledge_file) # Retrieve data from file.
    print("Chatbot is ready! Type 'exit' to quit.") # Real-Time update to user.

    while True: # Loop to keep dialog going
        user_input = input("You: ").strip().lower()
        if user_input == "exit": # Check if user wants to stop.
            save_knowledge(knowledge, knowledge_file) # Save new/existent data.
            print("Goodbye!")
            break # Stop the loop.

        # Load response from data file:
        response = get_response(user_input, knowledge)
        if response: # Reply to the user if response exists:
            print(f"Bot: {response}")
        else: # Ask user to teach the model by providing response:
            knowledge = learn_new_response(user_input, knowledge)


def main():
    chat()

if __name__ == "__main__":
    main()