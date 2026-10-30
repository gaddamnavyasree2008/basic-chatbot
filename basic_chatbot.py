
def chatbot():
    print("===== PYTHON CHATBOT =====")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "hi":
            print("Bot: Hello! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
