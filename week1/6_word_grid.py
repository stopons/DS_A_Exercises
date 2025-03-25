class WordFinder:
    def set_grid(self, grid):

        grid_list = [list(row) for row in grid]

        for row in range(len(grid_list)):
            print(grid_list[row]) 

        return grid_list

        

    def count(self, word, grid_list):

        # "checks" will break the "while loop" after checking the 3 directional (combinined)
        # sides of "grid_list"
        checks = 0
        count = 0

        while (checks < 2):
            
            # left-right and right-left direction
            for row in range(len(grid_list)):
                # left-right direction
                grid_row = grid_list[row]
                string_rep = ''.join(grid_row)

                # right-left direction
                rev_string_rep = string_rep[::-1]

                # Count how many times the string matches "word" in both directions
                count += string_rep.count(word)
                count += rev_string_rep.count(word)

                # Print put only for testing purposes
                print(string_rep)
                print("---------")
                print(rev_string_rep)
                print()
            
            checks += 1 # Flag left-right and right-left as completed


            # top-bottom and bottom-top direction
            max_columns = max(len(row) for row in grid)  # Get the longest row length

            for column in range(max_columns):  
                top_bottom_str = ""  # Reset for each column
                rev_top_bottom_str = ""

                for row in range(len(grid)): 
                    if column < len(grid[row]):  # Avoid index errors if a row has less colums (charactes)
                        # top-bottom direction
                        top_bottom_str += grid[row][column]

                        # bottom-top direction
                        rev_top_bottom_str = top_bottom_str[::-1]

                # Count how many times the string matches "word" in both directions
                count += top_bottom_str.count(word)
                count += rev_top_bottom_str.count(word)

                # Print put only for testing purposes
                print(top_bottom_str)
                print("********")
                print(rev_top_bottom_str)
                print()
            
            checks += 1

        # Print put only for testing purposes
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