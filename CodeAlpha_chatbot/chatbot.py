def get_bot_response(user_input):
    text = user_input.lower().strip()
    
    if text in ["hello", "hi"]:
        return "Hi!"
    elif text in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"
    elif text == "what are you doing":
        return "Just chatting with you!"
    elif text in ["bye", "goodbye"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Try saying 'hello' or 'how are you'."

def start_chat():
    print("Chatbot: Hello! I am ready to chat. (Type 'bye' to exit)")
    
    while True:
        user_message = input("You: ")
        bot_reply = get_bot_response(user_message)
        
        print(f"Chatbot: {bot_reply}")
        
        if user_message.lower().strip() in ["bye", "goodbye"]:
            break

if __name__ == "__main__":
    start_chat()