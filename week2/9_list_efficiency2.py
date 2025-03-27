"""
Implement a test, where the numbers 1,2,...,n are added to the end of the list one at a time.
Then the first element of the list is deleted n times.
Implement the test with n=10^5. Make two time measurements:
How much time it takes to do all the additions, and how much time to do all the deletions.

"""

import time

def create_numbers(a, b):

    num = []

    for i in range(a, b):
        num.append(i)

    return num


def delete_numbers(del_numbers):

    for _ in range(len(del_numbers)):
        del_numbers.pop(0)
        

    return del_numbers



def main():

    n = 10**5
    start_create = time.time()
    numbers = create_numbers(1, n)
    end_create = time.time()
    print(f"{n} numbers created in {end_create - start_create:.6f} sec.")


    start_del = time.time()
    delete_numbers(numbers)
    end_del = time.time()
    print(f"{n} numbers deleted in {end_del - start_del:.6f} sec.")

    # 10000 numbers created in 0.003574 sec.
    # 10000 numbers deleted in 1.531258 sec. --- O(n**2) ---


if __name__ == "__main__":
    main()
