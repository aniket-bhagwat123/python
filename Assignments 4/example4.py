# 4. Write a lambda function which accepts two numbers and returns minimum number.

first = int(input("Enter 1 Number"))
second = int(input("Enter 2 Number"))

manimum = lambda a, b : a if a < b else b

print(f"Manimum Number is {manimum(first, second)}")