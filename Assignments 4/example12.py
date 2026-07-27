# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even
# numbers.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x : x % 2 == 0, nums))

print(even_numbers)