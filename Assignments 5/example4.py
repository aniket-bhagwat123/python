# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers. 

from functools import reduce

Input_List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 

# filter listing

even_number = list(filter(lambda x : x % 2 == 0, Input_List))

print(f"Even Number: {even_number}")


# map listing

even_addition = list(map(lambda x : x ** 2, even_number))

print(f"Even Addition Number: {even_addition}")


# reduce listing

reduce_even_addition = reduce(lambda x, y: x + y, even_addition)

print(f"Reduce Even Addition Number: {reduce_even_addition}")