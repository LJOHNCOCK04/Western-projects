from graduation_auditor import GraduationAuditor
from undergrad_student import UndergradStudent
from grad_student import GradStudent

# You will be required to complete the above classes as defined in the import statements
# The below main function will test your code with the required input
# You will be required to implement the functions that are used in this test function
# Ensure UndergradStudent and the GradStudent both inheret from the Student base class
# Not following this structure will result in a large loss in points for this projects grade
# See rubric and assignment document for more details

# DO NOT CHANGE THIS
# THIS IS THE TEST FUNCTION, YOUR PROGRAM MUST OUTPUT CORRECTLY BASED ON THIS FUNCTION
# SEE ASSIGNMENT DOCUMENT FOR DETAILS
# MODIFYING THIS MAIN FILE WITH RESULT IN A 0
def main():
    auditor = GraduationAuditor()

    print("\nUndergraduate Students:")
    print("=======================\n")

    students = dict()

    students["undergrads"] = list()

    # Student #1
    students["undergrads"].append(UndergradStudent("Mark Lutz", 111))
    print(students["undergrads"][0].get_name())
    print("==============")
    students["undergrads"][0].do_community_service(20)
    students["undergrads"][0].do_community_service(20)
    students["undergrads"][0].take_course("Intro to Python", 26)
    students["undergrads"][0].take_course("Intro to Computing", 8)
    students["undergrads"][0].print_data()
    print()

    # Student #2
    students["undergrads"].append(UndergradStudent("Zed Shaw", 222))
    print(students["undergrads"][1].get_name())
    print("==============")
    students["undergrads"][1].do_community_service(15)
    students["undergrads"][1].take_course("Intro to Python", 15)
    students["undergrads"][1].take_course("Intro to Computing", 8)
    students["undergrads"][1].print_data()

    print("\nGraduate Students:")
    print("==================\n")

    students["grads"] = list()

    # Student #3
    students["grads"].append(GradStudent("Naomi Ceder", 111))
    print(students["grads"][0].get_name())
    print("==============")
    students["grads"][0].publish_paper("Formal Semantics of Programming Languages")
    students["grads"][0].publish_paper("Cyber Security in Digital Sector")
    students["grads"][0].take_course("Intro to Python", 26)
    students["grads"][0].take_course("Intro to Computing", 8)
    students["grads"][0].print_data()
    print()

    # Student #4
    students["grads"].append(GradStudent("David Beazley", 222))
    print(students["grads"][1].get_name())
    print("==============")
    students["grads"][1].publish_paper("Formal Semantics of Programming Languages")
    students["grads"][1].take_course("Intro to Python", 15)
    students["grads"][1].take_course("Intro to Computing", 8)
    students["grads"][1].print_data()

    print("\nAudit results:")
    print("==============\n")

    auditor.audit(students["undergrads"])
    auditor.audit(students["grads"])


main()
