#Project_2
#Leemon Johncock
loop='y'
while loop[0] =='y':
    name=input("Enter employee's name: ")
    print()
    while True:
        try:
            MONTHLY_BASE=float(input("Enter monthly base: "))
            break
        except ValueError:
            print("ERROR: That is not a valid number for monthly base please try again.")
            print()
    print()
    while True:
        print()
        TIER=input("Enter Tier('B','M', or 'P'): ")
        if TIER.upper() in ['B', 'm', 'p', 'b', 'M', 'P']:
           break
        else:
            print()
            print(f"Tier {TIER} is not a legitimate tier value.")
    print()
    while True:
        print()
        ITEMS_SOLD=int(input("Enter amount sold: "))
        if ITEMS_SOLD>=0:
            break
        else:
            print()
            print("Invalid number for items sold")
    #constants for all Commision pay and the tiers
    #B Tier Commision
    B_TIER_COMMISION_50 =50    #$50 10->15 items sold
    B_TIER_COMMISION_75 =75    #$75 above 15 items sold
    B_TIER_50_COMMISION_START  = 9
    B_TIER_75_COMMISION_START  = 15
    B_TIER_50_MAX_COMMISION = 5

    
    #M Tier commision
    M_TIER_COMMISION_60 =60    #$60 15->20 items sold
    M_TIER_COMMISION_100 =100  #$100 for above 20 items sold
    M_TIER_60_COMMISION_START  = 14
    M_TIER_100_COMMISION_START = 20
    M_TIER_60_MAX_COMMISION = 5
    
    
    #P Tier commision
    P_TIER_COMMISION_75 =75   #$75 20->25 items sold
    P_TIER_COMMISION_125 =125  #$125 for above 25 items sold
    P_TIER_75_COMMISION_START  =20
    P_TIER_125_COMMISION_START  =25
    P_TIER_75_MAX_COMMISION  = 5
   
    #Calculation the Total for the commisions with the amount of items sold for B TIER
    TOTAL=0
    if TIER.upper()== 'B':
        TOTAL=0
        if ITEMS_SOLD >= 10 and ITEMS_SOLD <=15 :
            TOTAL = ((ITEMS_SOLD - B_TIER_50_COMMISION_START) * B_TIER_COMMISION_50)
            
        if ITEMS_SOLD > 15:
            TOTAL= ((ITEMS_SOLD - B_TIER_COMMISION_50) + (ITEMS_SOLD - B_TIER_75_COMMISION_START)* B_TIER_COMMISION_75)
            
        if ITEMS_SOLD<10:
            TOTAL=0          #Setting the total to zero since no COMMISION, due to not selling enough
            print("WARNING: Sales must improve.")
  
   
#Calculation the Total for the commisions with the amount of items sold for M TIER
    if TIER.upper()== 'M':
        TOTAL=0
        if ITEMS_SOLD >= 15 and ITEMS_SOLD <= 20:
            TOTAL= ((ITEMS_SOLD - M_TIER_60_COMMISION_START) * M_TIER_COMMISION_60)
            
        if ITEMS_SOLD > 20:
            TOTAL= (M_TIER_60_MAX_COMMISION * M_TIER_COMMISION_60) + (ITEMS_SOLD - M_TIER_100_COMMISION_START) * M_TIER_COMMISION_100
            
        if ITEMS_SOLD<15:
            TOTAL=0          #Setting the total to zero since no COMMISION, due to not selling enough
            print("WARNING: Sales must improve to stay in Tier M.")
   
#Calculation the Total for the commisions with the amount of items sold for P TIER
    if TIER.upper()== 'P':
        TOTAL=0
        if ITEMS_SOLD >= 20 and ITEM_SOLD <= 25:
            TOTAL= ((ITEMS_SOLD - P_TIER_75_COMMISION_START) * P_TIER_COMMISION_75)
            
        if ITEMS_SOLD > 25:
            TOTAL= (P_TIER_75_MAX_COMMISION * P_TIER_COMMISION_75)+((ITEMS_SOLD - P_TIER_125_COMMISION_START) * P_TIER_COMMISION_125)
            
            
        if ITEMS_SOLD<20:
            TOTAL=0          #Setting the total to zero since no COMMISION, due to not selling enough
            print("WARNING: Sales must improve to stay in Tier P.")


     #calculating the final amount for the monthly payment.
    FINAL_TOTAL=TOTAL+MONTHLY_BASE

        
#Dislplaying the final amount with other givin input information
    print()
    print(f"{name}, Tier: .upper'{TIER}', sold {ITEMS_SOLD} items, monthly payment: {FINAL_TOTAL:.2f}")
    print()
    loop = input("Do you want to enter another employee? ")
    keep_going = loop[0]
    print()
    
