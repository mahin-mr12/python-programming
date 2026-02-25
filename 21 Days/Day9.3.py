# WAP to remove a specific element from tuple.

t=(1,2,3,4,5)
x=4
lst=list(t)
if x in lst:
    lst.remove(x)
t=tuple(lst)
print(t)