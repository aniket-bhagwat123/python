# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

num = int(input("Enter a number"))

divisible = lambda x : x % 5 == 0

print(divisible(num))