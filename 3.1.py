while True:
    command = input("Enter a command: Help, Issue, or Contact Support. ")
    if command.lower() == "help":
        print("Let me help you by providing [information].") #[information] filled with help link or instructions]
        break
    elif command.lower() == "issue":
        issue = input("What kind of issue are you expericing?")
        print("Okay great glad I could help!! :)") #issue response 
        break
    elif command.lower() == "contact support" or command.lower() == "support":
        print("Please call 1-555-555-5555 for 24-hr assitance. Glad I could help!") #direction to support
        break
    else: 
        print("Command not recognized. Please try again. ")
