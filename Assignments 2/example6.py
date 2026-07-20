# 1. Write a program which accepts one number and checks whether it is prime or not.

num = int(input("Enter a number"))

if num <= 1:
    print("not prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("is not prime number")
            break
    else:
        print("is prime number")