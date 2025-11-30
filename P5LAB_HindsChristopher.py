#Christopher Hinds
#30 Nov 2025
#P5LAB
#This program simulates a self-checkout machine, calculating change owed and dispersing it into currency denominations using a function.

import random

def disperse_change(change_owed_float):
    """
    Calculates and prints the amount of dollars, quarters, dimes, nickels,
    and pennies required to make the change from a given float amount.
    """
    # Convert float change to integer pennies to avoid floating point errors
    amount = int(round(change_owed_float * 100, 0))

    if amount < 0:
        print("Error: Change owed cannot be negative.")
        return

    # Dictionary to hold change values (alternatively use individual variables)
    dollars, quarters, dimes, nickels, pennies = 0, 0, 0, 0, 0

    # Calculate denominations using integer division (//) and modulo (%)
    dollars = amount // 100
    amount %= 100
    
    quarters = amount // 25
    amount %= 25
    
    dimes = amount // 10
    amount %= 10
    
    nickels = amount // 5
    amount %= 5
    
    pennies = amount // 1


    print(f"\nYour change of ${change_owed_float:.2f} will consist of:")
    print(f"{dollars} dollars")
    print(f"{quarters} quarters")
    print(f"{dimes} dimes")
    print(f"{nickels} nickels")
    print(f"{pennies} pennies")


def main():

    print("Welcome to the Self-Checkout Machine Simulation\n")

    # Generate a random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"The total amount owed for your purchase is: ${total_owed:.2f}")

    payment_amount = -1.0 # Initialize with an invalid value to enter the loop

    while payment_amount < total_owed:
        user_input = input(f"Enter the amount of cash you will put into the machine (must be >= ${total_owed:.2f}): $")
        payment_amount = float(user_input)
        
        if payment_amount < total_owed:
            print(f"Error: You entered ${payment_amount:.2f}, but owe ${total_owed:.2f}. Please enter enough money.")
    
    # Calculate change owed
    change_owed = payment_amount - total_owed
    print(f"\nCash Inserted: ${payment_amount:.2f}")
    print(f"Total Owed:    ${total_owed:.2f}")
    print(f"Change Owed:   ${change_owed:.2f}")
    
    # Call change dispersal function
    disperse_change(change_owed)


#call main function
if __name__ == "__main__":
    main()