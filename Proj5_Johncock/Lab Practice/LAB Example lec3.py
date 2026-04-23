# Example 
# Leemon Johncock
number = int(input("please enter a number(0-100): "))
flag = True
while flag:
    if number>=0 and number <=100:
        print(number)
        flag = False
    else:
        print("\nInvalid! Please enter a number between 0 and 100")
        number = int(input("please enter a number(0-100): "))

while True:
    LETTER= input("Please enter M for multiplication, or E for sum of values: ")
    if LETTER.upper() in ['M', 'm', 'e', 'E']:
        break
    else:
        print()
        print("Invalid! Please enter M or E")
        print()

print(f"Operation choosen: {LETTER}")
print()

if LETTER == 'M' or LETTER== 'm':
    for x in range(1, 11, 1):
        VALUES = x * number
        print(VALUES)
SUM=0
if LETTER =='E' or LETTER== 'e':
    for y in range(0,number +1):
        if y % 2 == 0:
            SUM += y
           
print (f"The sum of even numbers up to {number} is {SUM}")


