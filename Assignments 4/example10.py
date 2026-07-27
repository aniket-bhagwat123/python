# 10. Write a lambda function which accepts three numbers and returns largest number.

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
num3 = int(input("Enter a number"))

largest_number = lambda x, y, z : x if x > y and x > z else y if y > z else z

print(largest_number(num1, num2, num3))