# intent
greetIntent = ["hi", "hey", "hello", "hi there", "hello there", "hey there"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    # if msg == "hi" or msg == "hello" or msg == "hey" or msg == "hi there" or msg == "hello there":
    #     print("Hello User")

    if msg in greetIntent:
        print("Hello User")
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand...")
