class WordFinder:
    def set_grid(self, grid):

        grid_list = [list(row) for row in grid]

        for row in range(len(grid_list)):
            print(grid_list[row]) 

        return grid_list

        

    def count(self, word, grid_list):

        # "checks" will break the "while loop" after checking the 6 directional
        # sides of "grid_list"
        checks = 0
        count = 0
        store_letter = ""
        word_len = len(word)

        while (checks < 1):
        
            for row in range(len(grid_list)):
                #print(row)
                grid_row = str(grid_list[row])
                #print(grid_row)
                string_rep = ''.join(grid_row)
                print(string_rep)
                print(type(string_rep))
                print("---------")
                count += string_rep.count(word)
            
            checks += 1

        print(f"Checks: {checks}")
        print(f"Count: {count}")


        pass # Just put it here for now




if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    #print
    (finder.count("TIRA", grid)) # 7 
    #print(finder.count("TA")) # 13
    #print(finder.count("RITARI")) # 3
    #print(finder.count("A")) # 8
    #print(finder.count("AA")) # 6
    #print(finder.count("RAITA")) # 0  


# This is something I dropped while coding because there's a more efficient way to achieve the same result:
"""for row in range(len(grid_list)):
            #print(row)
            grid_row = str(grid_list[row])
            print(grid_row)

            for column in range(len(grid_row)):
                if word[column] == grid_row[column]:
                    store_letter += grid_row[column]
                    if len(word) == len(store_letter):
                        count += 1
                    else:
                        continue
                else:
                    store_letter = "" # Reset the string if the word is not matching"""
            # I need to check if I can turn the specific row back into a string, 
            # and from there, compare each character individually. When the word is complete, 
            # I'll increment the count by 1

# I didn't know about the method .count(), and i was trying to find a way to create it by myself
# but i've stopped in the middle and had to search if there was a way to compare a string into another string
# and return how many times that 1st string is into the 2nd one.