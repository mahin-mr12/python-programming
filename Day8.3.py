# WAP to find the transpose of matrix

a=[[1,2,3],[4,5,6]]

row=len(a)
col=len(a[0])

for i in range(col):
    for j in range(row):
        print(a[j][i],end=" ")
    print()