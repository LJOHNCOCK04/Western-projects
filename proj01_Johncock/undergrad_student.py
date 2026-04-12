# Project No.: 1  
# Author: Leemon Johncock
# Description:

class UndergradStudent:
    def __init__(self, name, credits):
        self.__name = name
        self.__credits_completed = 0
        self.__courses = []
        self.__community_service_hours = 0

# Getters and setters for the student's name, credits, courses, and community service hours
    def get_name(self):
        return self.__name

    def take_course(self, course, credits):
        self.__courses.append((course, credits))
        self.__credits_completed += credits
        print(f"Course taken: {course} ({credits} credits)")

    def do_community_service(self, hours):
        self.__community_service_hours += hours

    def get_credits(self):
        return self.__credits_completed

    def get_service_hours(self):
        return self.__community_service_hours
# Method to print the student's data
    def print_data(self):
        print(f"Credits completed {self.__credits_completed}")
        print(f"Hours of community service: {self.__community_service_hours}")
