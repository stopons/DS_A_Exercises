"""You are given a grid of letters and your task is to find words in the grid. 
A word can be read horizontally, vertically or diagonally in either direction.
In a file wordgrid.py, implement the class WordFinder with the following methods:

set_grid: sets the contents of the grid as a list, where each element is a string 
representing a row of the grid count: counts the number of occurrences of the given word

If a word can be read both forwards and backwards using the same letters, 
that should count as one occurrence only.
Your class will be tested using many different grids. 
The height and width of each test grid is at most 20 letters. Each letter is in the range A - Z."""

# I will use the DFS approach

class WordFinder:
    """Class to set the grid words in each row"""

    def __init__(self):
        self.grid_list = []
        self.rows = 0
        self.cols = 0

    def set_grid(self, grid_list):
        """Function to set the grid words in each row"""
        self.grid_list = grid_list
        self.rows = len(grid_list)
        self.cols = len(grid_list[0])

    def count(self, word):
        """Function to count how many times "word" is into the grid"""

        grid_list = self.grid_list
        max_row = self.rows
        max_col = self.cols
        word_len = len(word)

        # Counts single char ("A") in all rows without iterating them info the for loops
        if word_len == 1:
            return sum(row.count(word) for row in grid_list)

        # Set directions for word matching using a DFS approach
        directions = [
            (0, 1),   # Right
            (1, 0),   # Down
            (1, 1),   # Down-Right
            (1, -1),  # Down-Left
            (0, -1),  # Left
            (-1, 0),  # Up
            (-1, -1), # Up-Left
            (-1, 1)   # Up-Right
        ]

        # Forward direction
        count = 0
        for row in range(max_row):
            for col in range(max_col):
                if grid_list[row][col] == word[0]:
                    for drow, dcol in directions:
                        nrow, ncol = row, col
                        matched = True
                        for word_i in range(1, word_len):
                            nrow += drow
                            ncol += dcol
                            if nrow < 0 or nrow >= max_row or ncol < 0 or ncol >= max_col:
                                matched = False
                                break
                            if grid_list[nrow][ncol] != word[word_i]:
                                matched = False
                                break
                        if matched:
                            count += 1

        # Backward direction
        if word == word[::-1]:
            return count // 2
        else:
            reverse_count = 0
            reversed_word = word[::-1]
            for row in range(max_row):
                for col in range(max_col):
                    if grid_list[row][col] == reversed_word[0]:
                        for drow, dcol in directions:
                            nrow, ncol = row, col
                            matched = True
                            for word_i in range(1, len(reversed_word)):
                                nrow += drow
                                ncol += dcol
                                if nrow < 0 or nrow >= max_row or ncol < 0 or ncol >= max_col:
                                    matched = False
                                    break
                                if grid_list[nrow][ncol] != word[word_i]:
                                    matched = False
                                    break
                            if matched:
                                reverse_count += 1
            total = count + reverse_count
            return total // 2 if reverse_count > 0 else count


if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print("----------")
    print(finder.count("TIRA")) # 7
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0
