#WAP to check whether a char is uppercase,lowercase or not an alphabet

ch=input("Enter a Character: ")

if ch.isupper():
    print("uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not An Alphabet")