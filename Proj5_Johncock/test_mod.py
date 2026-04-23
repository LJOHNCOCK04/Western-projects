# Project No.: 5
# Author: Leemon Johncock
# Description: Checks if any two words in the compressed list are anagrams.
# Returns True if any pair are anagrams, otherwise False.
#------------------------------------------------------------------------------------

# Function: checkAnagram
# Purpose: Determines whether any two words in the input list are anagrams of each other
def checkAnagram(compressed_list):

    # Convert each word to a lowercase string to ensure uniform comparison
    words = [str(word).lower() for word in compressed_list]

    # Nested loop: Compare each word with every other word that comes after it
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            # Check if the letters of the two words are identical when sorted
            if sorted(words[i]) == sorted(words[j]):
                return True  # Found a pair of anagrams, return True immediately

    # If no anagram pairs were found, return False
    return False

# checkAnagram()  # Used for testing purposes
