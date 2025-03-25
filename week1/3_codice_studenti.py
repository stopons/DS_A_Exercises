def check_number(number):
    list_number = list(number)
    list_digits = list("37137137")
    total_digits = 0

    if (len(list_digits)) != (len(list_number) -1):
        return False

    for i in range(len(list_number)):
        str_number = list_number[(i)]
        int_number = int(str_number)

        if i < len(list_digits):
            str_digits = list_digits[(i)]
            int_digits = int(str_digits)

            digits = int_number * int_digits
            total_digits += digits
            #count_digits += 1

        else:
            break

    #print(total_digits // 10)
    
    #print(count_digits)
    #print(int_number)


    if total_digits // 10 == int_number:
        return True
    elif total_digits % 10 == 0:
        return True
    else:
        return False
    

# GPT reply at the end (which i don't really like in case i don't know how many 
# "n" characters are requested, so tried to go for a more flexible code)
"""
def check_number(number: str) -> bool:
    # Step 1: Early validation of the number's length and format
    if len(number) != 9 or not number.isdigit() or number[0] != '0':
        return False

    # Step 2: Define the multipliers for the first 8 digits
    multipliers = (3, 7, 1, 3, 7, 1, 3, 7)

    # Step 3: Calculate the weighted sum of the first 8 digits
    total_sum = sum(int(digit) * weight for digit, weight in zip(number[:-1], multipliers))

    # Step 4: Calculate the check digit (distance to next multiple of 10)
    correct_check_digit = (10 - (total_sum % 10)) % 10

    print(correct_check_digit)
    print(int(number[-1]))

    # Step 5: Validate the last digit
    return int(number[-1]) == correct_check_digit
"""




if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False

    # 37137137