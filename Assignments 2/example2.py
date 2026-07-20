# 2. Write a program which accepts one number and prints sum of first N natural numbers.

num = int(input("Enter a number"))
natural_num = 0

for i in range(1, num + 1):
    natural_num += i

print(f"natural number: {natural_num}")
    