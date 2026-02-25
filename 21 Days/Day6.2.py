# WAP to find duplicate elements in a list

a=[1,2,3,4,3,5]
dup=[]
for i in a:
    if a.count(i)>1 and i not in dup:
        dup.append(i)

print("Duplicate: ",dup)