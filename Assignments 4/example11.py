# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of
# each number.

nums = [1, 2, 3, 4, 5, 6, 7]

squares = list(map(lambda x : x * x, nums))

print(squares)