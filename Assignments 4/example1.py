# 1. Write a lambda function which accepts one number and returns square of that number.

num = int(input("Enter a number"))

square = lambda x : x * x

print(f"Square Number: {square(num)}")