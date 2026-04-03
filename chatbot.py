import re
import random

def chatbot_response(user_input):
    user_input = user_input.lower().strip()


    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return random.choice([
            "Hello! 😊 How can I help you?",
            "Hi there! What can I do for you?",
            "Hey! Need any help?"
        ])


    elif re.search(r'\b(your name|who are you)\b', user_input):
        return "I am a simple Rule-Based Chatbot created for AI Internship."


    elif re.search(r'\b(my name is)\b', user_input):
        name = user_input.split("is")[-1].strip()
        return f"Nice to meet you, {name}! 😊"


    elif "help" in user_input:
        return "I can chat with you! Try asking about time, date, or say hello."


    elif "tell time" in user_input:
        from datetime import datetime
        return "Current time is: " + datetime.now().strftime("%H:%M:%S")


    elif "tell date" in user_input:
        from datetime import datetime
        return "Today's date is: " + datetime.now().strftime("%d-%m-%Y")


    elif re.search(r'\b(how are you)\b', user_input):
        return "I'm just a bot, but I'm doing great! 😄"


    elif re.search(r'\b(bye|exit|quit)\b', user_input):
        return "Goodbye! Have a nice day! 👋"


    else:
        return "Sorry, I didn't understand that. Can you rephrase?"


def start_chat():
    print("🤖 Chatbot: Hello! Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() in ["exit", "quit", "bye"]:
            break


if __name__ == "__main__":
    start_chat()