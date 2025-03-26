"""
Your task is to count how many numbers in the range [a,b] consist of the digits 2 and 5 only. 
For example, in the range [1,100] the numbers are 2, 5, 22, 25, 52 and 55, and thus the answer is 6.
In a file twodigit.py, implement the function count_numbers that counts the desired numbers in the range. 
The function is given the parameters a and b representing the end points of the range.
Your function will be tested using many different ranges. In each test, 1 <= a <= b <= 10^9.
You must implement the function efficiently so that the solution is returned quickly even for long ranges.

"""


def count_numbers(a, b):
    """Function to count valid numbers with only 2 and 5 in them """
    def generate_number(current_number):
        """ Function to generate valid numbers using digits 2 and 5 only """
        
        if current_number > b:  # If the number exceeds "b", stop
            return
        if a <= current_number <= b:  # If "current_number" is in range, count it
            nonlocal count  # This modifies the "count" variable in the outer scope (outer function)
            count += 1
        
        # Generate the next numbers by adding only '2' or '5' to the current number
        if current_number * 10 + 2 <= b:
            generate_number(current_number * 10 + 2) # Add 2 -> (22, 52, 222, 252, etc)
        if current_number * 10 + 5 <= b:
            generate_number(current_number * 10 + 5) # Add 5 -> (25, 55, 225, 255, etc)

    count = 0 # Init count in the outer function
    
    # Generate valid numbers, starting from 2 and 5
    generate_number(2)
    generate_number(5)

    return count


if __name__ == "__main__":
    print(count_numbers(1, 100))       # 6
    print(count_numbers(60, 70))       # 0
    print(count_numbers(25, 25))       # 1
    print(count_numbers(1, 10**9))     # 1022
    print(count_numbers(123456789, 987654321))  # 512
