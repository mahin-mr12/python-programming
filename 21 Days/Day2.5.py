# Input a char and check whether it is vowel or consonent

ch= input("Enter a Letter:").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonent")