# 2. Write a program which contains one function ChkGreater() that accepts two numbers
# and prints the greater number.

first = int(input("Enter first number"))
second = int(input("Enter second number"))

def ChkGreater(num, num2):
    if num > num2:
        print(f"{num} is greater")
    else:
        print(f"{num2} is greater")


ChkGreater(first, second)