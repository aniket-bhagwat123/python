# 2. Write a lambda function which accepts one number and returns cube of that number.

num = int(input("Enter a number"))

square = lambda x : x * x * x

print(f"Cube Number: {square(num)}")