# 8. Write a lambda function which accepts two numbers and returns addition.

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))

addition = lambda x, y : x + y

print(f"Addition : {addition(num1, num2)}")