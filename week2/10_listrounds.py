"""
You are given a list that contains the numbers 1,2,...,n  in some order.
Your task is to simulate a process that collects the numbers from the list in the order from the smallest to the largest.
Each round goes through the list from left to right and collects a number if it is the next number to be collected.
The process ends when all numbers have been collected.
For example, given the list [2,1,4,7,5,3,6,8], the rounds go as follows:

Round 1: [1]
Round 2: [2,3]
Round 3: [4,5,6]
Round 4: [7,8]

In a file listrounds.py, implement the function find_rounds that takes the list as a parameter
and returns the numbers collected in the rounds as shown in the test cases below.
In this exercise, you can directly simulate the process and go through the full list on each round.

"""


def find_rounds(numbers):

    rounds = []
    n = len(numbers)
    collected = 0 # Keep track of the collected numbers

    while collected < n:
        current_round = [] # Init current round list

        for num in numbers:

            if num == 0: # Skip 0 if it's [numbers], otherwise we'll have an infinite loop
                continue

            elif num == collected + 1:
                # Incremental collection starting from 1
                current_round.append(num)
                collected += 1

        # Add data collected in the previous round
        rounds.append(current_round)

    return rounds


if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]

    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
