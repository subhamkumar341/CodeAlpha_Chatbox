
while True:
    user = input("You: ").lower()

    if user in ["hi", "hello"]:
        print("subham pc: Hello! How can I help you?")
    elif user in ["how are you?", "how are you"]:
        print("subham pc: I'm just a ai, but I'm doing fine! How about you?")
    elif user in ["i am fine", "i'm fine", "i am good", "i'm good"]:
        print("subham pc: That's great to hear!")
    elif user in ["bye", "exit", "quit"]:
        print("subham pc: Goodbye! Have a nice day.")
        break
    else:
        print("subham pc: Sorry, I didn't understand that.")
