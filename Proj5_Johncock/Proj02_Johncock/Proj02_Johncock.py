#Project_2
#Leemon Johncock
loop='y'
while loop[0] =='y':
    NAME=input("Enter employee's name: ")
    print()
    while True:
        try:
            MONTHLY_BASE=float(input("Enter monthly base: "))
            break
        except ValueError:
            print("ERROR: That is not a vlaid number for monthly base please try again.")
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
    B_TIER_COMMISION_50=50    #$50 10-15 items sold
    B_TIER_COMMISION_75=75    #$75 above 15 items sold
    B_TIER_50_BOUNUS_START  = 10
    B_TIER_75_BOUNUS_START  = 15
    
    #M Tier commision
    M_TIER_COMMISION_60=60    #$60 15-20 items sold
    M_TIER_COMMISION_100=100  #$100 for above 20 items sold
    M_TIER_60_BOUNUS_START  = 15
    M_TIER_100_BOUNUS_START =1
    
    #P Tier commision
    P_TIER_COMMISION_75 =75   #$75 20-25 items sold
    P_TIER_COMMISION_125=125  #$125 for above 25 items sold
    P_TIER_75_BOUNUS_START  =1
    P_TIER_125_BOUNUS_START  =1
    

    if TIER.upper()== 'B':
        if ITEMS_SOLD > 15:
            TOTAL = ((ITEM_SOLD-10)*B_TIER_COMMISION_50)+(B_TIER_COMMISION_75*(ITEMS_SOLD-15))

        if ITEMS_SOLD<=9:
            TOTAL=0
            TOTAL= ITEMS_SOLD*B_TIER_COMMISION_50

        if ITEMS_SOLD<10:
            total=0
            print("WARNING: Sales must improve.")
       
            
                

   

    if TIER.upper()== 'M':
        if ITEMS_SOLD<=20:
            TOTAL=0
            TOTAL= ITEMS_SOLD*M_TIER_COMMISION_60
        if ITEMS_SOLD<15:
            print("WARNING: Sales must improve to stay in Tier M.")
            total=0
        if ITEMS_SOLD>20:
            TOTAL=((ITEMS_SOLD-20)*M_TIER_COMMISION_100)+(20*M_TIER_COMMISION_60)
   

    if TIER.upper()== 'P':
        if ITEMS_SOLD<=25:
            TOTAL=0
            TOTAL= ITEMS_SOLD*P_TIER_COMMISION_75
        if ITEMS_SOLD<20:
            print("WARNING: Sales must improve to stay in Tier P.")
            total=0
        if ITEMS_SOLD>25:
            TOTAL=((ITEMS_SOLD-25)*P_TIER_COMMISION_125)+(25*P_TIER_COMMISION_75)



     #calculating the final amount for the monthly payment.
    FINAL_TOTAL= TOTAL +MONTHLY_BASE

        

    print()
    print(f"{NAME}, Tier: {TIER}, sold {ITEMS_SOLD} items, monthly payment: {FINAL_TOTAL}")
    print()
    loop = input("Do you want to enter another employee? ")
    keep_going = loop[0]
    print()
    
