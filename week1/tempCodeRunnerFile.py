def check_number(number):
    list_number = list(number)
    list_digits = list("37137137")
    count_digits = 0
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

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False

    # 37137137