while True:
    command = input("Enter a command: Help, Issue, or Contact Support. ")
    if command.lower() == "help":
        print("Let me help you by providing [information].") #[information] filled with help link or instructions]
        break
    elif command.lower() == "issue" :
        while True:
            issue = input("Are you experiencing a login, performance, or error issue? ") #types of issues to choose
            if issue.lower() == "login" or issue.lower() == "performance" or issue.lower() == "error":
                print(f"User is experiencing {issue.lower()} issue.")
                break
            else:
                print("Issue not recognized. ")
            break
        break
    elif command.lower() == "contact support" or command.lower() == "support":
        print("Please call 1-555-555-5555 for 24-hr assitance. Glad I could help!") #direction to support
        break
    else: 
        print("Command not recognized. Please try again. ")
