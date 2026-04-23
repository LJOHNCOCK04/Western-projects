#TEST FOR PROJ 2
# Project_2
# Leemon Johncock

loop = 'y'
while loop[0].lower() == 'y':
    NAME = input("Enter employee's name: ")
    print()

    # Validate monthly base input
    while True:
        try:
            MONTHLY_BASE = float(input("Enter monthly base: "))
            break
        except ValueError:
            print("ERROR: That is not a valid number for monthly base, please try again.")
            print()

    print()

    # Validate tier input
    while True:
        print()
        TIER = input("Enter Tier('B','M', or 'P'): ")
        if TIER.upper() in ['B', 'M', 'P']:
            break
        else:
            print()
            print(f"Tier {TIER} is not a legitimate tier value.")

    print()

    # Validate items sold input
    while True:
        try:
            ITEMS_SOLD = int(input("Enter amount sold: "))
            if ITEMS_SOLD >= 0:
                break
            else:
                print()
                print("Invalid number for items sold")
        except ValueError:
            print()
            print("Invalid input. Please enter a valid number.")

    # Constants for commission pay
    # B Tier Commission
    B_TIER_COMMISION_50 = 50     # $50 for items 10–15
    B_TIER_COMMISION_75 = 75     # $75 for items above 15
    # M Tier Commission
    M_TIER_COMMISION_100 = 100   # Flat $100 per item if > 14 items
    # P Tier Commission
    P_TIER_COMMISION_75 = 75     # $75 for items 20–25
    P_TIER_COMMISION_125 = 125   # $125 for items above 25

    TOTAL = 0  # Reset total each loop

    # Tier B logic
    if TIER.upper() == 'B':
        if ITEMS_SOLD <= 15:
            TOTAL = ITEMS_SOLD * B_TIER_COMMISION_50
        if ITEMS_SOLD < 10:
            print("WARNING: Sales must improve.")
        elif ITEMS_SOLD > 15:
            TOTAL = ((ITEMS_SOLD - 15) * B_TIER_COMMISION_75) + (15 * B_TIER_COMMISION_50)

    # Tier M logic (updated as per professor’s example)
    elif TIER.upper() == 'M':
        if ITEMS_SOLD > 14:
            TOTAL = ITEMS_SOLD * M_TIER_COMMISION_100
        else:
            print("WARNING: Sales must improve to stay in Tier M.")
            TOTAL = 0

    # Tier P logic
    elif TIER.upper() == 'P':
        if ITEMS_SOLD <= 25:
            TOTAL = ITEMS_SOLD * P_TIER_COMMISION_75
        if ITEMS_SOLD < 20:
            print("WARNING: Sales must improve to stay in Tier P.")
        elif ITEMS_SOLD > 25:
            TOTAL = ((ITEMS_SOLD - 25) * P_TIER_COMMISION_125) + (25 * P_TIER_COMMISION_75)

    # Final total calculation
    FINAL_TOTAL = TOTAL + MONTHLY_BASE

    # Output
    print()
    print(f"{NAME}, Tier: {TIER.upper()}, Sold {ITEMS_SOLD} items, Monthly Payment: {FINAL_TOTAL:.2f}")
    print()

    loop = input("Do you want to enter another employee? ")
    print()
