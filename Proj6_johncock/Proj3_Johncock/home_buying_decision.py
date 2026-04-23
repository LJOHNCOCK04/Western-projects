#Leemon Johncock
#project 3

# make the program to run the final decision
def make_home_buying_decision(home_price,budget,mortgage_payment):
   
   # making the logic that will decide if afforable 
   #if the payments and price of the home are less than or equal to budget then afforadble anything else is not affordable
    if mortgage_payment <= budget and home_price <= budget:
        home_buying_decision = "Affordable"
    else:
        home_buying_decision = " Not affordable"

 
     # return the decision to the main program
    return home_buying_decision



#home_buying_decision()      #used for testing not important
 

