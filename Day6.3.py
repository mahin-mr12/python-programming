# WAP to remove duplicates element in a list

a=[1,2,3,4,5,6,4,3]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)