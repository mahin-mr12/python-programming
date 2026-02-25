# WAP to start a list without using builtin-in fnx.

a=[5,2,9,1,3]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)