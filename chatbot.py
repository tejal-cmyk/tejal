def chatbot(message):
    if "hello" in message.lower():
        return "Hi there!"
    elif "how are you" in message.lower():
        return "I'm just a bot, but thanks for asking!"
    elif "bye" in message.lower():
        return "Goodbye! Have a great day!"
    elif "country" in message.lower():
        return "india"
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Welcome! Ask me anything or say 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
