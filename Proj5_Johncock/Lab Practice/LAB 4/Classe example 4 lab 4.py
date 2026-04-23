def fahrenheit_to_celsius(Fahrenheit):
    celsius= (Fahrenheit-32) *(5/9)
    return celsius

def main():
    temp=float(input("please enter the fahrenheit temp: "))
    celsius= fahrenheit_to_celsius(temp)
    print(celsius)
main()