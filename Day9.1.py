# WAP to find max and min value in a tuple without builtin fxns.

t=(6,3,7,9)
mx=t[0]
mn=t[0]

for i in t:
    if i > mx:
        mx=i
    if i< mn:
        mn=i
print("Max: ",mx)
print("Min: ",mn)