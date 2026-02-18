# WAP to check LCM for the GCD of two number

a=12
b=12
x,y=a,b

while y!=0:
    x,y=y,x%y

gcd=x
lcm=(a*b) // gcd
print("LCM: ",lcm)