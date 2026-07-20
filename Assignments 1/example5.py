# 5. Write a program which accepts one number and prints that many numbers in reverse
# order.

num = int(input("Enter Number"))

for i in range(num, 0, -1):
  print(i)