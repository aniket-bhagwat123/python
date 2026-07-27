# 2. Write a program which contains one function ChkGreater() that accepts two numbers
# and prints the greater number.

num = int(input("enter a number"))
num2 = int(input("enter a number"))

def ChkGreater(n1, n2):
    if n1 > n2:
        print(f"{num} Num 1 is Greater")
    else:
        print(f"{num2} Num 2 is Greater")


ChkGreater(num, num2)