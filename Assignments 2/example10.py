# 5. Write a program which accepts one number and checks whether it is palindrome or not.

num = input("Please enter number")

reverse = num[::-1]

if num == reverse:
    print("Number is palindrome")
else:
    print("Number is not palindrome")