# 1: Design a Python application that creates two threads named Prime and NonPrime.

import threading

numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
prime_numb = []
not_prime_numb = []


def PrimeGets(numers):
    for i in numers:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_numb.append(i)

    print(f"Prime Number : {prime_numb}")


def NonePrimeGets(numers):
    for i in numers:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    not_prime_numb.append(i)

    print(f"Non Prime Number : {not_prime_numb}")


def main():
    prim = threading.Thread(target=PrimeGets, args=(numb,))
    nonprim = threading.Thread(target=NonePrimeGets, args=(numb,))

    prim.start()
    nonprim.start()

    prim.join()
    nonprim.join()


if __name__ == "__main__":
    main()