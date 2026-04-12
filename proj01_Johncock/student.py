# Project No.: 1  
# Author: Leemon Johncock
# Description:


class Student():
    def __init__(self, name, credits):
        self.__name = name
        self.__credits = credits
# Getters and setters for the student's name, credits, courses, and community service hours
    def get_name(self):
        return self.__name
    
    def take_course(self, course_name, credits):
        pass
# Method to print the student's data
    def print_data(self):
        print("Name:", self.__name)
        print("Credits Earned:", self.__credits)
    