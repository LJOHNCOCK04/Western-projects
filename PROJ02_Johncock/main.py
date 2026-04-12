# Project No.:  2
# Authors: Leemon Johncock & Draven Aung
# Description: 
# made by leemon Johncock
from Boggle_Board import BoggleBoard

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

#defining main function to ask user input
#1. ask user for seed
#2. create a BoggleBoard object using the seed
#3. print the board
#4. ask user for a word
#5. check if the word is valid using the is_valid_word method of the Boggle
#board object
#6. print whether the word is valid or not
def main():
    seed = int(input("Enter seed: "))
    
    board = BoggleBoard()
    board.fill_board(seed)
    board.print_board()

    word = input("Enter a word: (in UPPERCASE): ")

    valid = board.is_word_valid(word)
    if valid:
        print(f"nice job!")
    else:
        print(f"I don't see that word.")

# checking if the word is a palindrome
    if is_palindrome(word):
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome.")
        





if __name__ == "__main__":
    main()
