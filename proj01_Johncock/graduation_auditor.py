# Project No.:  1
# Author: Leemon Johncock
# Description:

from undergrad_student import UndergradStudent
from grad_student import GradStudent
from student import Student

class GraduationAuditor:
    def audit(self, students):
        for student in students:
            name = student.get_name()

            #RULE undergrad: A student must have completed at least 30 credits to graduate.
            if isinstance(student, UndergradStudent):
                    if student.get_service_hours() >= 20 and student.get_credits() >= 30:
                        print(f"{name} can graduate")
                    else:
                        print(f"{name} cannot graduate")

                #Grad rules: A grad student must have published at least 2 papers to graduate.
            elif isinstance(student, GradStudent):
                if student.get_publications() >= 2 and student.get_credits() >= 30:
                    print(f"{name} can graduate")
                
                else: 
                    print(f"{name} cannot graduate")