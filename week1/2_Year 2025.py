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
        return False""" # mia versione giusta a livello logico, ma errata a livello di efficacia
    
def check_year(year):
    first_half = year // 100      # e.g., 2025 // 100 = 20
    second_half = year % 100      # e.g., 2025 % 100 = 25
    return (first_half + second_half) ** 2 == year

# più efficente, meno righe, usa la logica + aritmetica per troncare le prime 
# due lettere / 100 e le ultime due prendendo il resto della divisione per 100 usando il modulo
# % 100
    
if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False