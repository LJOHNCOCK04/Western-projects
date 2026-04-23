# Accessing the Individual Characters in a String
# This program counts the number of times
# the letter T (uppercase or lowercase)
# appears in a string.

def main():
    # Create a variable to use to hold the count.
    # The variable must start with 0.
    count = 0

    # Get a string from the user.
    my_string = input('Enter a sentence: ')

    # Count the Ts.
    for ch in my_string:
        if ch == 'T' or ch  == 't':
            count += 1

    # Print the result.
    print('The letter T appears', count, 'times.')

# Call the main function.
main()

##########################################################
# String Concatenation
# This program concatenates strings.

def main():
    name = 'Carmen'
    print('The name is', name)
    name = name + ' Brown'
    print('Now the name is', name)

# Call the main function.
main()

##########################################################

# String Slicing and String Testing Methods
# The get_login_name function accepts a first name,
# last name, and ID number as arguments. It returns
# a system login name.

def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name.
    # If the name is less than 3 characters, the
    # slice will return the entire first name.
    set1 = first[0 : 3]

    # Get the first three letters of the last name.
    # If the name is less than 3 characters, the
    # slice will return the entire last name.
    set2 = last[0 : 3]

    # Get the last three characters of the student ID.
    # If the ID number is less than 3 characters, the
    # slice will return the entire ID number.
    set3 = idnumber[-3 :]

    # Put the sets of characters together.
    login_name = set1 + set2 + set3

    # Return the login name.
    return login_name

# The valid_password function accepts a password as
# an argument and returns either true or false to
# indicate whether the password is valid. A valid
# password must be at least 7 characters in length,
# have at least one uppercase letter, one lowercase
# letter, and one digit.

def valid_password(password):
    # Set the Boolean variables to false.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Begin the validation. Start by testing the
    # password's length.
    if len(password) >= 7:
        correct_length = True

        # Test each character and set the
        # appropriate flag when a required
        # character is found.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    # Determine whether all of the requirements
    # are met. If they are, set is_valid to true.
    # Otherwise, set is_valid to false.
    if correct_length and has_uppercase and \
       has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    # Return the is_valid variable.
    return is_valid

##########################################################
# String Slicing and String Testing Methods
# This program gets the user's first name, last name, and
# student ID number. Using this data it generates a
# system login name.

import login

def main():
    # Get the user's first name, last name, and ID number.
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')

    # Get the login name.
    print('Your system login name is:')
    print(login.get_login_name(first, last, idnumber))

# Call the main function.
main()

##########################################################
# String Testing Methods
# This program demonstrates several string testing methods.

def main():
    # Get a string from the user.
    user_string = input('Enter a string: ')

    print('This is what I found about that string:')

    # Test the string.
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits.')
    if user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only whitespace characters.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')

# Call the main function.
main()

##########################################################
# String Testing Methods
# This program gets a password from the user and
# validates it.

import login

def main():
    # Get a password from the user.
    password = input('Enter your password: ')

    # Validate the password.
    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print('That is a valid password.')

# Call the main function.
main()

##########################################################
# The Repetition Operator
# This program demonstrates the repetition operator.

def main():
    # Print nine rows increasing in length.
    for count in range(1, 10):
        print('Z' * count)

    # Print nine rows decreasing in length.
    for count in range(8, 0, -1):
        print('Z' * count)

# Call the main function.
main()

##########################################################
# Splitting a String
# This program demonstrates the split method.

def main():
   # Create a string with multiple words.
   my_string = 'Onetwothreefour'

   # Split the string.
   word_list = my_string.split()

   # Print the list of words.
   print(word_list)

# Call the main function.
main()

##########################################################
# Splitting a String
# This program calls the split method, using the
# '/' character as a separator.

def main():
    # Create a string with a date.
    date_string = '11/26/2012'

    # Split the date.
    date_list = date_string.split('/')

    # Display each piece of the date.
    print('Month:', date_list[0])
    print('Day:', date_list[1])
    print('Year:', date_list[2])

# Call the main function.
main()
