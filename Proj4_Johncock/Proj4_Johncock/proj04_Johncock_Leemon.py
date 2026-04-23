# Project No. 4
# Leemon Johncock
# This program updates a bank's customers master file based on the inputs of the user. 
# It reads from the old prefix file and will writes to the new one with updated information from the user.

import os 


# --------------------------------------------------
# FUNCTIONS
# --------------------------------------------------

def file_prefix_confirmation(file_prefix):
    
    old_file = f"{file_prefix}_old.txt"
    new_file = "customers_new.txt"

    # verifying that the file actually exists
    if not os.path.exists(old_file):
        print(f"The file name {old_file} does not exist")
        return None, None
    return old_file, new_file


def get_number(one_line):
    return int(one_line[:6])


def get_balance(one_line):
    return float(one_line[7:17])


def get_name(one_line):
    return one_line[18:].strip()


# MAIN:

def main():
    # 1. Prompt for file prefix
    file_prefix = input("Enter a file prefix: ").strip()
    old_file, new_file = file_prefix_confirmation(file_prefix)

    if old_file is None:
        return  # Exit if the file doesn't exist

    try:
        # Open both input and output files safely using 'with' statements
        with open(old_file, "r") as old_f, open(new_file, "w") as new_f:
            while True:
                line = old_f.readline()

                # Stop reading if end of file is reached
                if not line:
                    break
                line = line.rstrip("\n")

                # Sentinel record
                if line == "999999":
                    new_f.write("999999\n")
                    break

                # Finds the information for the line
                acct_num = get_number(line)
                balance = get_balance(line)
                name = get_name(line)

                print(f"Verifying input: {acct_num} {balance:.2f} {name}")
                  
                write_record = True  

                # Goes through the transactions for the customer until a (advance) is selected by the user
                while True:
                    command = input("Enter a command (a,c,d,w): ").lower().strip()
                     
                    # Validating the command from user.
                    if command not in ['a', 'c', 'd', 'w']:
                        print(f"Entered an invalid command {command}.")
                        continue

                    # Deposit --------------------------------------------------------------
                    if command == 'd':
                        while True:
                            try:
                                amount = float(input("Enter deposit amount: "))
                                if amount <= 0:
                                    print("INVALID INPUT: Please enter a numeric value greater than 0.")
                                    continue
                                balance += amount
                                balance = round(balance, 2)

                                if balance > 9999999.99:
                                    print("Balance exceeds limit of 9,999,999.99. Transaction caneled.")
                                    balance -= amount
                                    continue
                                break
                            except ValueError:
                                print("INVALID INPUT: Please enter a numeric value.")

                    # Withdrawal --------------------------------------------------------------
                    elif command == 'w':
                        while True:
                            try:
                                amount = float(input("Enter withdrawal amount: "))

                                # Checking for valid positive amount
                                if amount <= 0:
                                    print("INVALID INPUT: Please enter a numeric value greater than 0.")
                                    continue
                                # preventing overdrawing the account
                                if balance - amount < -0.005:
                                    print("Transaction declined. Insufficient funds.")
                                    continue
                                balance -= amount
                                balance = round(balance, 2)
                                           
                                # checking the maximum balance limit           
                                if balance > 9999999.99:
                                    print("Balance exceeds limit of 9,999,999.99. Transaction caneled.")
                                    balance += amount 
                                    continue
                                break
                            except ValueError:
                                print("INVALID INPUT: Please enter a numeric value.")
                    
                    # Close Account --------------------------------------------------------------
                    elif command == 'c':
                        # validating the closing of an account if balance is zero.
                        if balance < 0.005:
                            print("Account is closed")
                            write_record = False  # do not write closed account
                            break  # exit transaction loop
                        else:
                            print("Account not closed because money is still in it.")
                        
                    # Advance --------------------------------------------------------------
                    elif command == 'a':
                        break  # exit transaction loop

                # Write the updated record to the new file if account was not closed
                if write_record:
                    new_f.write(f"{acct_num:06d} {balance:10.2f} {name}\n")
                    print(f"New balance: {acct_num:06d} {balance:.2f} {name}")
            
            # Confirmation that all lines were processed
            print(f"\nAll customer data processed. New file saved as {new_file}.")

    except FileNotFoundError:
        print(f"Error: could not open {file_prefix}_old.txt")


# Running the program.
if __name__ == "__main__":
    main()
