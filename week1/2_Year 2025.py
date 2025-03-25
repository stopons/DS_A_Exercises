"""def check_year(year):
    split_year = str(year)
    list_year = list(split_year)
    first_half = int(list_year[0] + list_year[1])
    second_half = int(list_year[2] + list_year[3])
    #print(first_half)
    #print(second_half)
    
    x = pow((first_half + second_half), 2)
    
    if x / year == 1:
        return True
    else:
        return False""" # My version is correct logically, but wrong in terms of effectiveness (Big-O)

def check_year(year):
    first_half = year // 100
    second_half = year % 100
    return (first_half + second_half) ** 2 == year

# More efficient, fewer lines, use logic + arithmetic to truncate the first
# two letters / 100 and the last two by taking the remainder of the
# division by 100 using the modulo % 100

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False