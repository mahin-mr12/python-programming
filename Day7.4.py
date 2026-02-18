# WAP to Check Password Strength

password=input("Enter the Password: ")
 
if len(password) < 6:
    print("Weak Password")
elif password.isdigit() or password.isalpha():
    print("Medium Password")
else:
    print("Strong Password")
    