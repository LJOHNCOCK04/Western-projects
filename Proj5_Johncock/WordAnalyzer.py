# Project No.: 5
# Author: Leemon Johncock
# Description: This project will analyze a list of user entered words to perform various learned string operations
# NOTES: Had trouble with variables not being strings when made and added functions, so make them strings in the code itself.
#------------------------------------------------------------------------------------

# Importing the file "test_mod" which contains the anagram checking function
import test_mod

# Function: userWords
# Purpose: Prompt the user to enter 'amount' words and concatenate them into a single string
def userWords(amount):
    concatenated_words =""  # Initialize empty string to store concatenated words
    i=0
    while i != (amount):
        i+=1
        word = str(input(f"enter word {i}: "))  # Convert input to string
        concatenated_words += word + " "  # Add word plus a space
    return concatenated_words

# Function: showWords
# Purpose: Display the concatenated string
def showWords(words):
    print(words)

# Function: convertWordsUpper
# Purpose: Convert the concatenated string to uppercase
def convertWordsUpper(concatenated_words):
    concatenated_words_converted = str(concatenated_words).upper()
    return concatenated_words_converted

# Function: stringToWordsList
# Purpose: Split the uppercase string into a list of words
def stringToWordsList(newconcatenated_words_converted):
    newconcatenated_words_list = str(newconcatenated_words_converted).split()  # Split by spaces
    print(newconcatenated_words_list)  # Show the list of words
    return newconcatenated_words_list

# Function: compressWordList
# Purpose: Create a list of unique words, then extract their first letters
def compressWordList(word_list):
    compressed_list = set(word_list)  # Remove duplicates
    print (str(compressed_list).upper())  # Display unique words
    compressed_list = [word[0] for word in compressed_list]  # Keep first letter only
    return str(compressed_list).upper()  # Convert to uppercase string

# Function: wordFrequencyCount
# Purpose: Count the number of times each letter appears as the first letter of a word
def wordFrequencyCount(integer_list, character_list, compressed_list):
    for letter in compressed_list:
        letter = str(letter).upper()  # Ensure uppercase
        if letter in character_list:
            index = ord(letter) - ord('A')  # Convert letter to 0-25 index
            integer_list[index]+=1  # Increment frequency count
    return integer_list

# Function: showWordFrequency
# Purpose: Display frequency of each letter using stars
def showWordFrequency(integer_list, character_list):
    print("\nLetter Frequency:\n")
    for i in range (26):
        print(f"{character_list[i]} {'*' * integer_list[i]}")  # Print letter followed by stars

# Main function: Orchestrates program execution
def main():
    # Ask user for number of words and validate input
    while True:
        try:
            amount = int(input("enter the ammount of words you want to read: "))
            if amount < 1:
                print("ERROR. The amount of words must be greater than 1.")
            else:
                break
        except ValueError:
            print("ERROR. You must enter a number.")

    # Step 1: Read words from the user
    concatenated_words=userWords(amount)
    showWords(concatenated_words)

    # Step 2: Convert to uppercase and split into a list
    words_converted = convertWordsUpper(concatenated_words)
    list_1 = stringToWordsList(words_converted)

    # Step 3: Compress list to first letters of unique words
    compressed_list = compressWordList(list_1)

    # Step 4: Prepare lists for frequency counting
    integer_list = ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    character_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    # Step 5: Count letter frequencies and display
    wordFrequencyCount(integer_list, character_list, compressed_list)
    showWordFrequency(integer_list, character_list)

    # Step 6: Check for anagrams using function from test_mod
    anagram = test_mod.checkAnagram(list_1)
    if anagram:
        print("These words are anagrams.")
    else:
        print("These words are not anagrams.")

# Start program execution
if __name__=="__main__":
    main()
