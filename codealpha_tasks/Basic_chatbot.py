def get_response(user_input):
    """return a response based on user input."""
    user_input=user_input.lower()

    if"hello" in user_input or"hi" in user_input:
        return "Hello there! How can i assist you today?"
    elif "your name" is user_input:
        return"I'm CodealphaBot,  your friendly Python Chatbot!"
    elif"how are you"in user_input:
        return "I'm doing great, Thanks fop!, What about you?"
    elif"Help" in user_input:
        return "you can ask me about the weather, my name, or just say Hello!"
    elif"bye" in user_input or "exit" in user_input:
        return "Goodbye! Hope to chat with you again"
    else:
        return "I'm not sure how to respond to that yet. Try  to say 'Hello' or 'Help'."
print("Welcome to CodeAlpha Chatboat!")
print("Type 'bye' or 'exit'to end the chat.\n ")

while True:
    user_input= input("You:")
    response= get_response(user_input)
    print("Bot:", response)

    if user_input.lower() in["Bye" , "exit"]:
        break

