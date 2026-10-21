print("=== CodeAlpha - Basic Chatbot ===")
print("By: Kalpana Sravanthi | Viswam College")
print("Type 'bye' to exit")

def get_response(msg):
    msg = msg.lower()
    if "hello" in msg or "hi" in msg:
        return "Hello Kalpana! How can I help you?"
    elif "college" in msg:
        return "You are from Viswam Engineering College"
    elif "internship" in msg:
        return "This is CodeAlpha Python Internship"
    elif "name" in msg:
        return "I am CodeAlpha Chatbot created by Kalpana"
    elif "how are you" in msg:
        return "I am fine, thank you!"
    elif "python" in msg:
        return "Python is a great programming language"
    else:
        return "Sorry, I am still learning. Ask about college/internship"

while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Bot: Bye! Thanks for chatting")
        break
    print("Bot: " + get_response(user))
