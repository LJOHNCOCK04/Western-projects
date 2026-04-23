# -----------------------------------------------
# Computer Science II - Term Project
#Leemon Johncock LEC TUE TR 10 - 11:15
# -----------------------------------------------   


#Library Management System this system allows users to manager books members loans, and be able to search and see reservations.

import sys
import json

# Base Class for Library
class Person:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id

    def Display(self):
        print(f"Name: {self.__name}")


# Member Class inheriting from Person
class Member(Person):
    def __init__(self, member_id, name):
        super().__init__(name, member_id)
        self.__name = name
        self.__member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.__name} borrowed {book.get_title()}")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.__name} returned {book.get_title()}")
        else:
            print(f"{self.__name} did not borrow {book.get_title()}")

# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True

    def get_title(self):
        return self.__title
    
    def is_available(self):
        return self.__is_available
    
    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False


    def return_book(self):
        self.__is_available = True

    def display(self):  
        status = "Available" if self.__is_available else "Checked Out"
        print(f"{self.__title} by {self.__author} ISBN: {self.__isbn} [{status}]")

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []
        self.reservations = []


    def add_book(self, book):
        self.books.append(book)
        

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member._Member__name}")

    def search_books(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book
        return None
    

    def sort_books(self):
        n = len(self.books)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.books[j].get_title() > self.books[j+1].get_title():
                    self.books[j], self.books[j+1] = self.books[j+1], self.books[j]


    def borrow_book(self, member, title):
        book = self.search_books(title)
        if book and book.is_available():
            if book.borrow():
                member.borrow_book(book)
                self.loans.append((member, book))
            else:
                print("Book is not available. (ADDED to reservation queue)")
                self.reservations.append((member, book))
        else:
            print("Book not found.") 


# Return book method

    def return_book(self, member, title):
        book = self.search_books(title)
        if book:
            book.return_book()
            member.return_book(book)
            print(f"{book.get_title()} has been returned.")


# checking the reservation queue

            for i, ( res_member, res_book) in enumerate(self.reservations):
                if res_book == book:
                    print(f"{res_member.name} has reserved {book.get_title()}.")
                    self.reservations.pop(i)
                    break

        else:
            print("Book not found.")   


# Recursion method to count total books in the library
    def count_books(self, index=0):
        if index == len(self.books):
            return 0
        return 1 + self.count_books(index + 1)
    

#Displaying all the books in the library

    def display_books(self):
        for book in self.books:
            book.display()






# menu function to display options to the user
def menu():
    print('\n===== Library Systems =====')
    print('1. Add Book')
    print('2. Add Member')
    print('3. Display books')
    print('4. Search book')
    print('5. Borrow book')
    print('6. Return book')
    print('7. sort book')
    print('8. count books')
    print('9. Exit')

# main function to run the library system
def main():
    library = Library()

    while True:
        menu()
        choice = input("Enter your choice: ")


#1
        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")

            # Input validation for ISBN
            isbn = input("Enter Book ISBN: ")
            while isbn.strip() == "":
                print("ISBN cannot be empty.")
                isbn = input("Enter Book ISBN: ")
            while not isbn.isdigit():
                print("ISBN must be numeric.")
                isbn = input("Enter Book ISBN: ")
            while isbn.len() != 10 and isbn.len() != 13:
                print("ISBN must be 10 or 13 digits long.")
                isbn = input("Enter Book ISBN: ")
            
            
            library.add_book(Book( title, author,isbn))


#2
        elif choice == "2":
            member_id = input("Enter Member ID: ")
            while len(member_id) != 5:
                print("Member ID must be 5 characters long.")
                member_id = input("Enter Member ID: ")


            name = input("Enter Name: ")
            while name.strip() == "":
                print("Name cannot be empty.")
                name = input("Enter Name: ")

            while name.isdigit():
                print("Name cannot be numeric.")
                name = input("Enter Name: ")

            library.add_member(Member(member_id, name))


#3
        elif choice == "3":
            print("\nBooks in the library:")
            library.display_books()


#4
        elif choice == "4":
            title = input("Enter book title: ")
            book = library.search_books(title)
            if book:
                book.display()
            else:
                print("Book not found.")


#5
        elif choice == "5":
            name = input("Enter member name: ")
            while name.strip() == "":
                print("Name cannot be empty.")
                name = input("Enter Name: ")

            while name.isdigit():
                print("Name cannot be numeric.")
                name = input("Enter Name: ")

            member = next((m for m in library.members if m._Member__name == name), None)
            if member:
                title = input("Enter book title: ")
                library.borrow_book(member, title)
            else:
                print("Member not found.")


#6
        elif choice == "6":
            name = input("Enter member name: ")
            member = next((m for m in library.members if m._Member__name == name), None)
            if member:
                title = input("Enter book title: ")
                library.return_book(member, title)
            else:
                print("Member not found.")


#7
        elif choice == "7":
            library.sort_books()
            print("Books sorted by title.")


#8
        elif choice == "8":
            print("Total books:", library.count_books())


#9
        elif choice == "9":
            print("Goodbye!")
            

        else:
            print("Invalid choice.")

    


if __name__ == "__main__":
    main()