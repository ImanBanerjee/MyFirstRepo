# Function to say hello
def say_hello():
    print("Computer: Hello, World!")

# Function for basic chat
def chat():
    print("Computer: How are you today?")
    user_response = input("You: ")

    print("Computer: That's nice to hear!")
    print("Computer: What's your favorite color?")
    user_response = input("You: ")

    print(f"Computer: Ah, {user_response} is a nice color!")
    print("Computer: Well, it was nice chatting with you!")

if __name__ == "__main__":
    say_hello()
    chat()
