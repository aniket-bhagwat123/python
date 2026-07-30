# 2: Design a Python application that creates two threads.
import threading

def add(a, b):
    print(f"Addition is {a + b}")

def subtraction(a,b):
    print(f"Subtraction is {a - b}")


def main():
    num = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    
    adds = threading.Thread(target=add, args=(num, num2))

    subbs = threading.Thread(target=subtraction, args=(num, num2))

    adds.start()
    subbs.start()

    adds.join()
    subbs.join()


if __name__ == "__main__":
    main()