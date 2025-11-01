# chatbot.py

print("Hello! I am your rule-based chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").strip().lower()
    
    if user_input == "hi" or user_input == "hello":
        print("Chatbot: Hello! How can I help you today?")
    elif user_input in ["how are you?", "how are you"]:
        print("Chatbot: I'm just a program, but I'm doing great! How are you?")
    elif user_input == "what is your name?":
        print("Chatbot: I am a simple rule-based chatbot.")
    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    elif "weather" in user_input:
        print("Chatbot: I can't check the weather yet, but it's always sunny in Python!")
    elif "help" in user_input:
        print("Chatbot: You can ask me about myself, greet me, or say 'bye' to exit.")
    else:
        print("Chatbot: Sorry, I don't understand that. Try something else or say 'help'.")

# End of chatbot.py
