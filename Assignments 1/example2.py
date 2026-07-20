# 2. Write a program which accepts one number and prints its factors.

num = int(input("Enter a number"))

# print(num)
for i in range(1, num + 1):
    # print(i)
    if num % i == 0:
        print(i)