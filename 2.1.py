while True:
    user_firstname = input("Enter first name: ")
    if len(user_firstname) <= 1:
        print("Error. First name must be at least 2 characters long.")
    else:
        print(f"Hello {user_firstname}!")
        break
while True:
    user_lastname = input("Enter last name: ")
    if len(user_lastname) <= 1:
        print("Error. Last name must be at least 2 characters long.")
    else:
        print(f"Hello {user_firstname} {user_lastname}!")
        break