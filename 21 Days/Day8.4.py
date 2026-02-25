# WAP to check whether given no is present in the matrix or not

a=[[1,2,3],[4,5,6]]

x=6
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==x:
            print("Found At: ",i,j)