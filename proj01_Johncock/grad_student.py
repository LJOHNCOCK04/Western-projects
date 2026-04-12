# Project No.: 1
# Author: Leemon Johncock
# Description: This file defines the grad_student class, which represents a graduate student.


class GradStudent:
    def __init__(self, name, credits):
            self.__name = name
            self.__credits_completed = 0
            self.__courses = []
            self.__publications = []
# Getters and setters for the student's name, credits, courses, and publications
    def get_name(self):
            return self.__name

    def take_course(self, course, credits):
            self.__courses.append((course, credits))
            self.__credits_completed += credits
            print(f"Course taken: {course} ({credits} credits)")

    def publish_paper(self, title):
            self.__publications.append(title)
            print(f"Publication #{len(self.__publications)}: {title}")

    def get_credits(self):
            return self.__credits_completed

    def get_publications(self):
            return len(self.__publications)
# Method to print the student's data
    def print_data(self):
            print(f"Credits completed {self.__credits_completed}")
            print(f"Number of Publications: {len(self.__publications)}")