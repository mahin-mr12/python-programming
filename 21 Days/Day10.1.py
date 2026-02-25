#WAP to find missing number from 1 to n in a list

l_s = [1,3,4,5,6]
n = 6
expected_sum = n* (n+1) // 2
actual_sum =sum(l_s)
missing = expected_sum - actual_sum
print("Missing Number is: ", missing)