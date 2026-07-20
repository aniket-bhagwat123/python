# 5. Write a program which accepts one number and checks whether it is divisible by 3 and
# 5

num = int(input("Enter a number"))

if num % 5 == 0 and num % 3 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")