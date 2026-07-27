# 3. Write a lambda function which accepts two numbers and returns maximum number.

first = int(input("Enter 1 Number"))
second = int(input("Enter 2 Number"))

maximum = lambda a, b : a if a > b else b

print(f"Maximum Number is {maximum(first, second)}")
