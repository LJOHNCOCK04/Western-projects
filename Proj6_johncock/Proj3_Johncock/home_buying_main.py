#Leemon Johncock
#project 3

# the imports of the other programs that help calculate the final decision
import budget_calculation
import home_buying_decision
import mortgage_calculation

#main program
def  home_buying_main():
    # providing a loop so the user doesnt have to keep running the program
    #[0] will make sure the program only check the first letter of the input. ANYTHING WITH Y CONTINUES 
    keep_going = 'y'
    while keep_going.lower()[0] == 'y':
    
            # collecting finacial input from the user
            annual_income = float(input("\nPlease enter your annual income: "))
            savings=float(input("\nEnter your savings: "))
            monthly_expenses =float(input("\nEnter your monthly expenses: "))
           
            # determining the max home price based on users budget
            max_home_price = budget_calculation.calculate_budget(annual_income, savings, monthly_expenses)

            #house price and downp payment
            home_price = float(input("\nEnter the price of the house you want to buy: " ))
            down_payment = float(input("\nEnter your down payment: "))

            #Validation of the downpayment to not equal the home price or more

            while down_payment >= home_price:
                print("\nInvalid input: Down payment cannot exceed or equal the home price.")
                down_payment = float(input("\nEnter your down payment: "))

            
                
            # mortgage information as inputs from user
            interest_rate = float(input("\nEnter the annual interest rate for the mortgage (%): "))
            loan_term= int(input("\nEnter the loan term in years: "))
          
            # Calculating the mortage payment from all user inputs from before.         
            monthly_mortgage_payment= mortgage_calculation.calculate_mortgage(home_price, down_payment, interest_rate, loan_term)

            #making the final decision in the home buying process if its affordable or not.
            home_buying_decision_ = home_buying_decision.make_home_buying_decision(home_price, max_home_price, monthly_mortgage_payment)
            
            # final decision output 
            print (f"\nDecision: {home_buying_decision_}")
            #asking the user if they would like to keep going with another house.
            keep_going = input("\nDo you want to buy another house? ")



# running the main function 
home_buying_main()       




