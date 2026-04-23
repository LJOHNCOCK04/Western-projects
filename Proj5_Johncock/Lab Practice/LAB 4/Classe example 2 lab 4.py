def print_square(number):
    square= number * number
    print(f"\nthe square of the number is: {square}")

def main():
    number_square=float(input("please enter the number you would like to square: "))
    print_square(number_square)


main()