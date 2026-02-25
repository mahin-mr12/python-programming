# WAP to find the sum of rows in given matrix 

a=[[1,2,3],[4,5,6]]
for i in a:
    s=0
    for j in i:
        s+=j
    print("Row Sum: ",s)