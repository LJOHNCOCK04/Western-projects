#Leemon Johncock
#project 3

# making the program to calculate the max home price they can afford
def calculate_budget(annual_income, savings, monthly_expenses):


   # using the given formula to find ther max home price from the income, savings, monthly expenses they have
    max_home_price = annual_income * 3 + savings - (monthly_expenses * 12 *2)


    

    # return the decision to the main program
    return max_home_price
    

#budget_calculation()   #used for testing not important