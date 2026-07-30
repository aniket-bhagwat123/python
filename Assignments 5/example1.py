# 1.Write a program which contains one lambda function which accepts one parameter and return
# power of two. 

num = int(input("Enter a number"))

power = lambda x : 2 ** x

print(power(num))