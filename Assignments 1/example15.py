# 5. Write a program which accepts marks and displays grade.

marks = int(input("Enter a marks"))

if marks >= 75:
    print("Distinction")
elif marks >= 65:
    print("First Class")
elif marks >= 50:
    print("Second Class")
else:
    print("Fail")