from functools import reduce

# =============================== FILTER LOGIC =============================== #

# 1. filter with lamda

nums = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda a: a % 2 == 0, nums))

print(f"Filter With Lamda {even_numbers}")



# 2. filter without lamda

nums1 = [1, 2, 3, 4, 5, 6]

def even_num(a):
    return a % 2 == 0 

even_numbers1 = list(filter(even_num, nums1))

print(f"Filter without Lamda {even_numbers1}")





# =============================== MAP LOGIC =============================== #

# 1. map with lamda

nums_list = [1, 2, 3, 4]

data = list(map(lambda x: x + 1, nums_list))

print(f"MAP with Lamda {data}")


# 2. map without lamda

nums_list1 = [1, 2, 3, 4]

def increase(x):
   return x + 1

data1 = list(map(increase, nums_list1))

print(f"MAP without lamda {data1}")






# =============================== REDUCE LOGIC =============================== #

# 1. reduce with lamda
numbers = [1, 2, 3, 4, 5]

total_some = reduce(lambda x, y: x + y, numbers)

print(f"REDUCE with lamda {total_some}")



# 2. reduce without lamda

numbers1 = [1, 2, 3, 4, 5]

def addition(acc, curr):
    return acc + curr

total_some1 = reduce(addition, numbers)

print(f"REDUCE without lamda {total_some1}")

