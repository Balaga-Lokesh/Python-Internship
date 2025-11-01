Rule-Based Chatbot – Task 8
Overview
This project implements a simple rule-based chatbot using Python. The chatbot interacts with users in the terminal, replying to basic questions and statements using if-elif-else logic. It demonstrates fundamental concepts of control flow, input handling, and basic Natural Language Processing (NLP).

Features
Greets the user and holds a conversation until 'bye' is entered.

Handles basic greetings, queries about itself, and common phrases.

Provides default and help responses for unknown inputs.

Responds using simple keyword and phrase matching.

How to Run
Make sure you have Python 3 installed.

Download or clone this repository.

Open a terminal in the project directory.

Run the chatbot script:

bash
python chatbot.py
Interact with the chatbot. Type 'bye' to exit.

Example Interaction
text
Hello! I am your rule-based chatbot. Type 'bye' to exit.
You: hi
Chatbot: Hello! How can I help you today?
You: what is your name?
Chatbot: I am a simple rule-based chatbot.
You: how are you?
Chatbot: I'm just a program, but I'm doing great! How are you?
You: bye
Chatbot: Goodbye! Have a nice day.
Key Concepts
Control Flow: Uses if-elif-else statements to determine chatbot responses.

Input Handling: Processes user input with .strip().lower() for reliable matching.

Loops: Uses a while loop to continue the conversation until the exit command.

Practiced Interview Skills
Collecting user input in Python

Difference between if, elif, and else

Limitations of rule-based chatbots

Exiting loops on command

Organizing code for readability

Extending this Project
Add more rules for additional responses.

Handle multiple intents or complex phrases with nested logic or dictionaries.

Convert to an ML-based chatbot using libraries like NLTK, spaCy, or transformers.

Author
Lokesh Balaga