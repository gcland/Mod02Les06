def password_create():
  while True:
    password = input("Please create a password with at least 8 characters, 1 uppercase letter, 1 lowercase letter, and 1 number: ")  
    for char in password:
        a = char.islower()
        if a == True:
            #print(f"There is a lowercase letter, {char}.")
            break
        
    for char in password:
        b = char.isupper()
        if b == True:
            #print(f"There is an uppercase letter, {char}. ")
            break
        
    for char in password:
        c = char.isnumeric()
        if c == True:
            #print(f"There is a number, {char}.")
            break
    if a == False:
        print("There is no lowercase letter. Please try again. ")   
    if b == False:
        print("There is no uppercase letter. Please try again. ")     
    if c == False:
        print("There is no number. Please try again. ") 
    
    if a and b and c == True:
        if len(password) < 8:
            print("The password must be 8 or more characters. Please try again. ")
        else:
            print("Successful password.")
            break
       
password_create()   