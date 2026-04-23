# Blackjack Card Counting Practice Tool
# Hi-Lo Count System

# Card values for Hi-Lo system:
# 2–6 = +1
# 7–9 = 0
# 10, J, Q, K, A = -1

hi_lo_values = {
    "2": 1, "3": 1, "4": 1, "5": 1, "6": 1,
    "7": 0, "8": 0, "9": 0,
    "10": -1, "J": -1, "Q": -1, "K": -1, "A": -1
}

def basic_strategy(player_total, dealer_card):
    # Very simplified basic strategy (can be expanded)
    dealer = dealer_card
    p = player_total

    if p >= 17:
        return "Stand"
    elif p <= 11:
        return "Hit"
    elif 12 <= p <= 16:
        if dealer in ["2","3","4","5","6"]:
            return "Stand"
        else:
            return "Hit"
    return "Hit"

def main():
    print("=== Blackjack Card Counter ===")
    decks = float(input("Enter number of decks in shoe: "))
    running_count = 0
    total_cards = decks * 52

    while True:
        card = input("\nEnter card seen (2-10, J, Q, K, A) or 'quit': ").upper()

        if card == "QUIT":
            break
        
        if card not in hi_lo_values:
            print("Invalid card. Try again.")
            continue

        # Update running count
        running_count += hi_lo_values[card]

        # Estimate cards removed
        total_cards -= 1
        decks_remaining = total_cards / 52
        true_count = running_count / decks_remaining if decks_remaining > 0 else running_count

        print(f"Running Count: {running_count}")
        print(f"True Count: {true_count:.2f}")

        # Optional: Get strategy advice
        #ask = input("Do you want play advice? (y/n): ").lower()
        #if ask == "y":
         #   player = int(input("Enter your hand total: "))
          #  dealer = input("Dealer upcard: ").upper()
           # print("Basic Strategy Suggestion:", basic_strategy(player, dealer))


if __name__ == "__main__":
    main()
