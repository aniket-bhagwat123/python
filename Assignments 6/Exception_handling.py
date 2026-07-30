# try:
#     a = int(input("Enter value1: "))
#     b = int(input("Enter value2: "))
#     c = a/b
#     print(c)
# # except Exception as exc:
# #     print(exc)
# except ZeroDivisionError as Zs:
#     print(Zs)
# except ValueError as vls:
#     print("Value entered exception: ", vls)

# Exception Handling

try:
    x = int(input("Enter a number"))

    y = x / 0
except ZeroDivisionError as exc:
    print("Number cannot be zero.", exc)
except ValueError as exc:
    print("Invalid number.", exc)