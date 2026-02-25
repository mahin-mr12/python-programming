# Input a number and count how many digits it has

n=int(input("Enter a Number: "))

count = 0
while n > 0:
    count += 1
    n = n // 10

    print("Total digits=", count)