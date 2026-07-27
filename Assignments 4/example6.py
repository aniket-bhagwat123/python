# 6. Write a lambda function which accepts one number and returns True if number is odd
# otherwise False.

num = int(input("Enter a number"))

is_Even_number = lambda x: True if x % 2 != 0 else False

print(f"Number is {"Odd" if is_Even_number(num) else "Even"}")