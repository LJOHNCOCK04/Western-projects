# -----------------------------------------------
# Computer Science II - Term Project
#Leemon Johncock LEC TUE TR 10 - 11:15
# -----------------------------------------------   


#Library Management System this system allows users to manager books members loans, and be able to search and see reservations.

import os

# Base Class for Library
class Person:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id

    def Display(self):
        print(f"\nName: {self.__name} \nMember ID: {self.__member_id}")

    def get_name(self):
        return self.__name
    
    def get_member_id(self):
        
        return self.__member_id


# Member Class inheriting from Person
class Member(Person):
    def __init__(self, member_id, name):
        super().__init__(name, member_id)
        self.borrowed_books = []

   

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.get_name()} borrowed {book.get_title()}")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.get_name()} returned {book.get_title()}")
        else:
            print(f"{self.get_name()} did not borrow {book.get_title()}")


    def display_member(self):
        print(f"\nMember ID: {self.get_member_id()}, Name: {self.get_name()}")

# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
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
        print(f"\n{self.__title} by {self.__author} \nISBN: {self.__isbn} \n[{status}]")

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []
        self.reservations = []


    def add_book(self, book, from_load = False):
        if not from_load:
            for b in self.books:
                if b.get_isbn() == book.get_isbn():
                    print("Book with this ISBN already exists.")
                    return
                
                if b.get_title().lower() == book.get_title().lower():
                    print("Book with this title already exists.")
                    return
        self.books.append(book)
        if not from_load:
            print(f"\nAdded book: {book.get_title()}")

        

    def add_member(self, member, from_load = False):
        if not from_load:
            for m in self.members:
                if m.get_member_id() == member.get_member_id():
                    print("\nMember with this ID already exists.")
                    return
        self.members.append(member)
        if not from_load:
            print(f"\nAdded member: {member.get_name()}")

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
        if book:
            
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
                    print(f"{res_member.get_name()} has reserved {book.get_title()}.")
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



# Methods to save and load data from files
    def save_data(self):
        data = {
            "books": [{"title": book.get_title(), "author": book.get_author(), "isbn": book.get_isbn(), "is_available": book.is_available()} for book in self.books],
            "members": [{"name": member.get_name(), "member_id": member.get_member_id()} for member in self.members],
            "loans": [{"member_name": loan[0].get_name(), "book_title": loan[1].get_title()} for loan in self.loans],
            "reservations": [{"member_name": res[0].get_name(), "book_title": res[1].get_title()} for res in self.reservations]
        }
        with open("books.txt", "w", encoding="utf-8") as books_file:
            for b in self.books:
                books_file.write(f"{b.get_title()},{b.get_author()},{b.get_isbn()},{b.is_available()}\n")
            


        with open("members.txt", "w", encoding="utf-8") as members_file:
            for m in self.members:
                members_file.write(f"{m.get_name()},{m.get_member_id()}\n")


        with open("loans.txt", "w", encoding="utf-8") as loans_file:
            for l in self.loans:
                loans_file.write(f"{l[0].get_name()},{l[1].get_title()}\n")


        with open("reservations.txt", "w", encoding="utf-8") as reservations_file:
            for r in self.reservations:
                reservations_file.write(f"{r[0].get_name()},{r[1].get_title()}\n")




    def load_data(self):
        if os.path.exists("books.txt"):
            with open("books.txt", "r", encoding="utf-8") as books_file:
                for line in books_file:
                    title, author, isbn, is_available = line.strip().split(",")
                    book = Book(title, author, isbn)
                    if is_available == "False":
                        book.borrow()
                    self.add_book(book, from_load=True)

        if os.path.exists("members.txt"):
            with open("members.txt", "r", encoding="utf-8") as members_file:
                for line in members_file:
                    name, member_id = line.strip().split(",")
                    self.add_member(Member(member_id, name), from_load=True)

        if os.path.exists("loans.txt"):
            with open("loans.txt", "r", encoding="utf-8") as loans_file:
                for line in loans_file:
                    member_name, book_title = line.strip().split(",")
                    member = next((m for m in self.members if m.get_name() == member_name), None)
                    book = next((b for b in self.books if b.get_title() == book_title), None)
                    if member and book:
                        self.loans.append((member, book))

        if os.path.exists("reservations.txt"):
            with open("reservations.txt", "r", encoding="utf-8") as reservations_file:
                for line in reservations_file:
                    member_name, book_title = line.strip().split(",")
                    member = next((m for m in self.members if m.get_name() == member_name), None)
                    book = next((b for b in self.books if b.get_title() == book_title), None)
                    if member and book:
                        self.reservations.append((member, book))



# menu function to display options to the user
def menu():
    print('\n===== Library Systems =====')
    print('1. Add Book')
    print('2. Add Member')
    print('3. Display books')
    print('4. Display members')
    print('5. Search book')
    print('6. Borrow book')
    print('7. Return book')
    print('8. sort book')
    print('9. count books')
    print('0. Exit')
    print('===========================')

# main function to run the library system
def main():
    library = Library()
    library.load_data()

    while True:
        menu()
        choice = input("\nEnter your choice: ")

        # 1. Add Book
        if choice == "1":
            title = input("\nEnter Book Title (or 0 to cancel): ")
            if title == "0":
                continue

            author = input("Enter Book Author (or 0 to cancel): ")
            if author == "0":
                continue

            isbn = input("Enter Book ISBN (or 0 to cancel): ")
            if isbn == "0":
                continue

            while isbn.strip() == "":
                print("ISBN cannot be empty.")
                isbn = input("Enter Book ISBN (or 0 to cancel): ")
                if isbn == "0":
                    break
            if isbn == "0":
                continue

            while not isbn.isdigit():
                print("ISBN must be numeric.")
                isbn = input("Enter Book ISBN (or 0 to cancel): ")
                if isbn == "0":
                    break
            if isbn == "0":
                continue

            while len(isbn) != 10 and len(isbn) != 13:
                print("ISBN must be 10 or 13 digits long.")
                isbn = input("Enter Book ISBN (or 0 to cancel): ")
                if isbn == "0":
                    break
            if isbn == "0":
                continue

            library.add_book(Book(title, author, isbn))

        # 2. Add Member
        elif choice == "2":
            member_id = input("\nEnter Member ID (or 0 to cancel): ")
            if member_id == "0":
                continue

            while len(member_id) != 5:
                print("Member ID must be 5 characters long.")
                member_id = input("Enter Member ID (or 0 to cancel): ")
                if member_id == "0":
                    break
            if member_id == "0":
                continue

            name = input("\nEnter Name (or 0 to cancel): ")
            if name == "0":
                continue

            while name.strip() == "":
                print("Name cannot be empty.")
                name = input("Enter Name (or 0 to cancel): ")
                if name == "0":
                    break
            if name == "0":
                continue

            while name.isdigit():
                print("Name cannot be numeric.")
                name = input("Enter Name (or 0 to cancel): ")
                if name == "0":
                    break
            if name == "0":
                continue

            library.add_member(Member(member_id, name))

        # 3. Display Books
        elif choice == "3":
            print("\nBooks in the library:")
            library.display_books()

        # 4. Display Members
        elif choice == "4":
            print("\nMembers in the library:")
            for member in library.members:
                member.display_member()

        # 5. Search Book
        elif choice == "5":
            title = input("\nEnter book title (or 0 to cancel): ")
            if title == "0":
                continue

            book = library.search_books(title)
            if book:
                book.display()
            else:
                print("Book not found.")

        # 6. Borrow Book
        elif choice == "6":
            name = input("\nEnter member name (or 0 to cancel): ")
            if name == "0":
                continue

            while name.strip() == "":
                print("Name cannot be empty.")
                name = input("Enter Name (or 0 to cancel): ")
                if name == "0":
                    break
            if name == "0":
                continue

            while name.isdigit():
                print("Name cannot be numeric.")
                name = input("Enter Name (or 0 to cancel): ")
                if name == "0":
                    break
            if name == "0":
                continue

            member = next((m for m in library.members if m.get_name() == name), None)
            if member:
                title = input("Enter book title (or 0 to cancel): ")
                if title == "0":
                    continue
                library.borrow_book(member, title)
            else:
                print("Member not found.")

        # 7. Return Book
        elif choice == "7":
            name = input("\nEnter member name (or 0 to cancel): ")
            if name == "0":
                continue

            member = next((m for m in library.members if m.get_name() == name), None)
            if member:
                title = input("Enter book title (or 0 to cancel): ")
                if title == "0":
                    continue
                library.return_book(member, title)
            else:
                print("Member not found.")

        # 8. Sort Books
        elif choice == "8":
            library.sort_books()
            print("\nBooks sorted by title.")

        # 9. Count Books
        elif choice == "9":
            print("\nTotal books:", library.count_books())

        # Exit
        elif choice == "0":
            library.save_data()
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
