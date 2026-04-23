#Project No.: 3 
# Author:  Leemon Johncock
# Descripton:  Reads files with information about cars and prints to terminal for user to see.
# The program will read two files, one with information about cars in stock and one with information about incoming cars.

import os
import sys

# defining the car class and the import_car and domestic_car subclasses.
class car:
    def __init__(self, brand, model, year, type, price):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__type = type
        self.__price = price

    def get_brand(self):
        return self.__brand
    def set_brand(self, brand):
        self.__brand = brand
    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    def get_type(self):
        return self.__type
    def set_type(self, type):
        self.__type = type
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price
    
class import_car(car):
    def __init__(self, brand, model, year, type, price, country, tax):
        super().__init__(brand, model, year, type, price)
        self.__country = country
        self.__tax = tax

    def get_country(self):
        return self.__country
    def set_country(self, country):
        self.__country = country
    def get_tax(self):
        return self.__tax
    def set_tax(self, tax):
        self.__tax = tax
    def print_info(self):
        print(f"{self.get_brand():<10}"
            f"{self.get_model():<12}"
            f"{self.get_year():<8}"
            f"{self.get_price():<12,.2f}"
            f"{self.get_type():<10}"
            f"{self.get_country():<10}"
            f"{self.get_tax():<10}")

class domestic_car(car):
    def __init__(self, brand, model, year, type, price, state):
        super().__init__(brand, model, year, type, price)
        self.__state = state
        
    def get_state(self):
        return self.__state
    def set_state(self, state):
        self.__state = state
    def print_info(self):
        print(f"{self.get_brand():<10}"
            f"{self.get_model():<12}"
            f"{self.get_year():<8}"
            f"{self.get_price():<12,.2f}"
            f"{self.get_type():<10}"
            f"{self.get_state():<10}")
    
    
    # main funcion will read the file and create the appropriate car 
    # objects and add them to the appropriate lists. 
    # It will then print out the information for each car and the total 
    # number of cars in stock. It will then do the same thing for incoming cars.
def main():
    import_cars = []
    domestic_cars = []

    filename = input("Please enter a file name (with information about Cars in Stock): ")

# Reads the file and creates the appropriate car objects and 
# adds them to the appropriate lists
    with open(filename, "r") as in_stock_file:
        for line in in_stock_file:
            data = line.split()

            if data[0] == "I":
                car = import_car(data[1], data[2], int(data[3]), data[5], float(data[4]), data[6], float(data[7]))
                import_cars.append(car)

            elif data[0] == "D":
                car = domestic_car(data[1], data[2], int(data[3]), data[5], float(data[4]), data[6])
                domestic_cars.append(car)

    #printing the info for each car (import)
    print("Cars in Stock:")
    print("Import Cars:")
    for car in import_cars:
        car.print_info()
        print()

    #prints the infor for each car (domestic)
    print("Domestic Cars:")
    for car in domestic_cars:
        car.print_info()
        print()
        
    print("\nNumber of imported cars =", len(import_cars))
    print("Number of domestic cars =", len(domestic_cars))
    print("Total =", len(import_cars) + len(domestic_cars))

    #Does the same thing as above but for incoming cars

    
                
    filename = input("Please enter a file name (with information about incoming cars): ")
    with open(filename, "r") as incoming_file:
        for line in incoming_file:
            data = line.split()

            if data[0] == "I":
                car = import_car(data[1], data[2], int(data[3]), data[5], float(data[4]), data[6], float(data[7]))
                import_cars.append(car)

            elif data[0] == "D":
                car = domestic_car(data[1], data[2], int(data[3]), data[5], float(data[4]), data[6])
                domestic_cars.append(car)
   
   #printing the info for each car (import)
    print("\nIncoming Cars (added):")
    print("Import Cars:")
    for car in import_cars:
        car.print_info()
        
    #prints the infor for each car (domestic)
    print("\nDomestic Cars:")
    for car in domestic_cars:
        car.print_info()
        
  #printing the total number of cars in stock after adding incoming cars
    print("\nNumber of imported cars =", len(import_cars))
    print("Number of domestic cars =", len(domestic_cars))
    print("Total =", len(import_cars) + len(domestic_cars))



    # for demestic cars the price will be increase by 15
    for car in domestic_cars:
        car.set_price(car.get_price() * 1.15)

    print("\nDomestic Cars (after price increase):")
    for car in domestic_cars:
        car.print_info()


    #printing all cars that are less than or equal to 15000
    #showing most to least expensive cars
    print("\nCars less than or equal to $15,000 (most to least expensive):")
    all_cars = import_cars + domestic_cars  
    affordable_cars = [car for car in all_cars if car.get_price() <= 15000]
    affordable_cars.sort(key=lambda x: x.get_price(), reverse=True)

    print("\nCars ≤ $15,000 (most to least expensive):")

    for car in affordable_cars:
        car.print_info()
    











if __name__ == "__main__":
    main()