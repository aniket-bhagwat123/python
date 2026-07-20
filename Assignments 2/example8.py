# 3. Write a program which accepts one number and prints sum of digits.

num = input("Enter a number")

total = 0

for i in num:
    total += int(i)


print(total)