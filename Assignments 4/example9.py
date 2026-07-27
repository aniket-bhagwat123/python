# 9. Write a lambda function which accepts two numbers and returns multiplication.

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))

multiplication = lambda x, y : x * y

print(f"Multiplication : {multiplication(num1, num2)}")