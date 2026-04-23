#test score values
#Leemon Johncock
SCORE = float(input("please enter the score of the student: "))
print()
if SCORE<float(60):
    print("The letter Grade is: F")
    
if SCORE>=60:
    if SCORE<=69:
        print("The letter Grade is: D")
        
if SCORE>=70:
    if SCORE<=79:
        print("The letter Grade is: C")
    

if SCORE<=89:
    if SCORE>=80: 
        print ("The letter Grade is: B")
        
if SCORE>=90:
    print("The letter Grade is: A")
print()
print("thank you for using the converter goodbye")
