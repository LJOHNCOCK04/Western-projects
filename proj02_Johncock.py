#Project_2
#Leemon Johncock
loop='y' # making the loop so we can repeat for as many empolyees we want. ( This will make sure the program continues at the start)
while loop[0] =='y': # setting the loop[0] this makes the loop only equal to the first letter of the input. 
   
   
    #constants for all Commision pay for each tier
    #B Tier Commision
    B_TIER_COMMISION_50 =50    #$50 10 -> 15 items sold
    B_TIER_COMMISION_75 =75    #$75 above 15 items sold
    B_TIER_50_COMMISION_START  = 9 # This is the number right before the $50 commision starts 
    B_TIER_75_COMMISION_START  = 15 # This is when the $75 commision starts
    B_TIER_50_MAX_COMMISION = 6 # This is the same for a all TIERS. This represents the max amount of items that can be sold in the lower commision.

    
    #M Tier commision
   
    M_TIER_COMMISION_60 =60    #$60 15 -> 20 items sold
    M_TIER_COMMISION_100 =100  #$100 for above 20 items sold
    M_TIER_60_COMMISION_START  = 14 #This is the number right before the $60 commision starts 
    M_TIER_100_COMMISION_START = 20 # This is when the $100 commision starts
    M_TIER_60_MAX_COMMISION = 6 # This is the same for a all TIERS. This represents the max amount of items that can be sold in the lower commision. 
    
    
    #P Tier commision
    P_TIER_COMMISION_75 =75   #$75 20 -> 25 items sold
    P_TIER_COMMISION_125 =125  #$125 for above 25 items sold
    P_TIER_75_COMMISION_START  =20 #This is the number right before the $75 commision starts 
    P_TIER_125_COMMISION_START  =25 # This is when the $125 commision starts
    P_TIER_75_MAX_COMMISION  = 6 # This is the same for a all TIERS. This represents the max amount of items that can be sold in the lower commision.


    
    # Asking for a name to start the calculations for the monthly payment. 
    name=input('\n'"Enter employee's name: ") # getting the name for employee
   
    while True:
        try:
            monthly_base=float(input('\n'"Enter monthly base: ")) #getting the input of the monthy base payment
            if monthly_base>=0:
                break
            else:
                print('\n'"ERROR: That is not a valid input for monthly base please try again.")
        except ValueError:
                # showing them that the input is invalid, and or there is a letter and not a number.
                print('\n'"ERROR: That is not a valid input for monthly base please try again.")
            
    
    while True: # creating the loop for TIER. this amkes the user keep inputing until a valid tier is entered
        
        tier=input('\n'"Enter Tier('B','M', or 'P'): ") # getting the tier of the employee
        if tier.upper() in ['B', 'M', 'P']:
           break
        else:
            # showing them that the letter they entered is a not a valid tier in this program.
            print('\n'f"Tier {tier.upper()} is not a legitimate tier value.")
    
    while True: #Creating a loop for amount sold. this allows only positve numbers, and will keep going until we get a valid number.
        try:
        
            items_sold=int(input('\n'"Enter amount sold: ")) # getting the amount of items sold from the employee
            if items_sold>=0:
                break
            else:
                # showing them that the number is invalid, and or there is a letter and not a number.
                print('\n'"Invalid number for items sold")
        except ValueError:
            print('\n'"Invalid number for items sold")
    
   
    
# Making the calculations fot B tier
    if tier.upper()== 'B':
        total=0
        if items_sold >= 10 and items_sold <=15 :
            total = ((items_sold - B_TIER_50_COMMISION_START) * B_TIER_COMMISION_50) #When they have sold enough items for $50 commision but not $75 commision
            
        if items_sold > 15:
            total= ((B_TIER_50_MAX_COMMISION * B_TIER_COMMISION_50)) + ((items_sold - B_TIER_75_COMMISION_START)* B_TIER_COMMISION_75) # When they have reached the $75 commision rate plus the $50 commsion for 6 Items
            
        if items_sold<10:
            total=0          #Setting the total to zero since no COMMISION, due to not selling enough
            print("WARNING: Sales must improve.")
  
   
# Making the calculations for M Tier
    if tier.upper()== 'M':
        total=0
        if items_sold >= 15 and items_sold <= 20:   #When they have sold enough items for $60 commision but not $100 commision
            total= ((items_sold - M_TIER_60_COMMISION_START) * M_TIER_COMMISION_60)
            
        if items_sold > 20:
            total= (M_TIER_60_MAX_COMMISION * M_TIER_COMMISION_60) + ((items_sold- M_TIER_100_COMMISION_START)*M_TIER_COMMISION_100) # When they have reached the $100 commision rate plus the $60 commsion for 6 items
            
        if items_sold<15:
            total=0          #Setting the total to zero since no COMMISION, due to not selling enough
            print("WARNING: Sales must improve to stay in Tier M.")
   
# making the calculations for p TIER
    if tier.upper()== 'P':
        total=0
        if items_sold >= 20 and items_sold <= 25: #When they have sold enough items for $75 commision but not $125 commision
            total= ((items_sold - P_TIER_75_COMMISION_START) * P_TIER_COMMISION_75) 
            
        if items_sold > 25:
            total= (P_TIER_75_MAX_COMMISION * P_TIER_COMMISION_75)+((items_sold - P_TIER_125_COMMISION_START) * P_TIER_COMMISION_125) # When they have reached the $125 commision rate plus the $75 commsion for 6 items
            
            
        if items_sold<20:
            total=0          #Setting the total to zero since no COMMISION, due to not selling enough
            print("WARNING: Sales must improve to stay in Tier P.")


     #calculating the final amount for the monthly payment for the employee.
    Final_total=total+monthly_base

        

    # Showing all inputs and results on the terminal together.
    print('\n'f"{name}, Tier: {tier.upper()}, sold {items_sold} items, Monthly payment: ${Final_total:.2f}")
  
    loop = input('\n'"Do you want to enter another employee? ")
    
    
    
