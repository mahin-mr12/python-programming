# WAP to reverse a tuple.

t=(1,2,3,4,5)
rev=()

for i in t:
    rev=(i,) +rev
    
print(rev)