# Project No.:  2
# Author: Leemon Johncock & Draven Aung
# Description: Boggle board class for Project 2


from operator import index
import random
import string

class BoggleBoard:
    
        # TODO: create __init__ that: 
        # - initializes a 4x4 2D list for letters 
        # - initializes a 4x4 2D list for visited flags (all False)

    def __init__(self):
        self.board = [["" for _ in range(4)] for _ in range(4)]
        self.visited = [[False for _ in range(4)] for _ in range(4)]
        self.path = []
    # TODO: create a method fill_board(seed) that:
    #       - sets the random seed
    #       - fills the 4x4 board with random uppercase letters

    def fill_board(self, seed):
        random.seed(seed)
        letters = random.choices(string.ascii_uppercase, k=16)
        self.board = [letters[i*4:(i+1)*4] for i in range(4)]


    def reset_visited(self):
        for i in range(4):
            for j in range(4):
                self.visited[i][j] = False

    # TODO: create a method print_board() that:
    #       - prints the board in the EXACT format shown in the sample output
    #       - no hardcoding of letters

    def print_board(self):
        for i in range(4):

            print("+---+ +---+ +---+ +---+")
            row = ""
            for j in range(4):
                row += f"| {self.board[i][j]} | "
            print(row.strip())
        print("+---+ +---+ +---+ +---+")


    # TODO: create a method is_word_valid(word) that:
    #       - resets visited array to all False
    #       - scans the board for the first letter of the word
    #       - for each match, calls the recursive search method
    #       - returns True if any recursive search succeeds

    def is_word_valid(self, word):
        self.reset_visited()
        self.path = []  # Clear the path for the new word
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == word[0]:
                    if self.search(word, i, j, 0):
                        return True
        return False




    # TODO: create a recursive method search(word, row, col, index) that:
    #       - checks if index == len(word) → base case success
    #       - checks bounds and visited status
    #       - checks if board[row][col] matches word[index]
    #       - marks visited[row][col] = True
    #       - recursively checks UP, DOWN, LEFT, RIGHT neighbors
    #       - unmarks visited[row][col] before returning
    #       - returns True if any recursive call succeeds
    
    def search(self, word, row, col, index):
        if index == len(word):
            return True
        if not (0 <= row < 4 and 0 <= col < 4):
            return False
        if self.visited[row][col]:
            return False
        if self.board[row][col] != word[index]:
            return False

        self.visited[row][col] = True
        self.path.append((row, col))  # Track this cell

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  #2D up down left right
    
        for dr, dc in directions:
            if self.search(word, row + dr, col + dc, index + 1):
                return True

    # Backtrack
        self.visited[row][col] = False
        self.path.pop()
        return False
    

    # TODO: create a method print_marked_path(word) that:
    #       - prints the board again
    #       - but marks the letters used in the found word using < > around them
    #       - matches EXACT formatting from sample output


    def print_marked_path(self, word):
        
        marked = set(self.path)

        for i in range(4):

            print("+---+ +---+ +---+ +---+")

            row = ""
            for j in range(4):

                letter = self.board[i][j]

                if (i, j) in marked:
                    row += f"|<{letter}>| "
                else:
                    row += f"| {letter} | "

            print(row.strip())

        print("+---+ +---+ +---+ +---+")
