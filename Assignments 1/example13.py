# 3. Write a program which accepts one number and checks whether it is perfect number or
# not.

num = int(input("Enter a number"))
som_num = 0

for i in range(1, num):
    if num % i == 0:
        som_num += i

print(som_num)

if som_num == num:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")