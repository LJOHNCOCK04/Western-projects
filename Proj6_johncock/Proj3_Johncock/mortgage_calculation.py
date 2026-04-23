#Leemon Johncock
#project 3


def calculate_mortgage(home_price, down_payment, interest_rate, loan_term ):
     #getting the loan amount from the price minus the down payment
     loan_amount = home_price - down_payment

     #calculating the monthyl interest rate from the annual divied by 12
     monthly_interest_rate = (interest_rate/12) 

     # multipling the loan term to get the amount of payment overall the whole mortgage
     num_payments = loan_term * 12

     #calculating the monthly payment that would need to be made form the givien formula.
     Monthly_mortgage_payment= loan_amount * (monthly_interest_rate *(1+ monthly_interest_rate)** num_payments)/((1+monthly_interest_rate)**num_payments-1)



   # return the mothly payment amount to the main program
     return Monthly_mortgage_payment


 #mortgage_calculation()   #used for testing not important
