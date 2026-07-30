# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers. 

from functools import reduce


Input_List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# filters listing

filters = list(filter(lambda x: x >= 70 and x <= 90, Input_List))

print(filters)



# map listing

maps = list(map(lambda x: x + 10, filters))

print(maps)



# reduce listing

reduces = reduce(lambda x, y : x * y, maps)

print(reduces)
