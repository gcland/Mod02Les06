#I'm not really sure what the requirements are for this task based on the verbiage from the assignment.
#Please let me know if I am missing a requirement.

while True:
    user_firstname = input("Enter first name: ")
    if len(user_firstname) <= 1:
        print("Error. First name must be at least 2 characters long.")
    for char in user_firstname:
            a = char.isdigit()
            if a == True:
                    break
            
    for char in user_firstname:
            b = char.isalnum()
            if b == False:
                    break  
    if a == True:
           print("Error. Please remove numbers from your name.")
    if b == False:
           print("Error. Please remove special characters from your name.")
    if a == False and b == True:
        print(f"Hello {user_firstname}!")
        break
while True:
    user_lastname = input("Enter last name: ")
    if len(user_lastname) <= 1:
        print("Error. First name must be at least 2 characters long.")
    for char in user_lastname:
            c = char.isdigit()
            if c == True:
                    break
            
    for char in user_lastname:
            d = char.isalnum()
            if d == False:
                    break  
    if c == True:
           print("Error. Please remove numbers from your name.")
    if d == False:
           print("Error. Please remove special characters from your name.")
    if c == False and d == True:
        print(f"Hello {user_lastname}!")
        break

email = user_firstname.lower() + user_lastname.lower() + "." + "codingtemple.com"
print(f"Email address: {email}")