# 4. Write a program which accepts one number and prints all even numbers till that
# number.

num = int(input("Enter a number"))

for i in range(1, num + 1):
    if i % 2 == 0:
        print(f"Even Numbers: {i}")