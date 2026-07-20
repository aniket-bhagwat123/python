# 3. Write a program which accepts one number and prints factorial of that number.

num = int(input("Enter a number"))
factorial_num = 1

for i in range(1, num + 1):
    factorial_num *= i

print(factorial_num)