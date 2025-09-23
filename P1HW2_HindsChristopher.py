 # Christopher Hinds
 # 22 September 2025
 # P1HW2
 # Trip budget calculator

print("This program calculates and displays travel expenses")

#user input
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend one gas? "))
living = int(input("Approximately, how much do you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

#budget calculation
expenses = gas + living + food
balance = budget - expenses
print()
print("--------------Travel Expenses------------")
print("Location: ",destination)
print("Intitial Budget: ",budget)
print()
print("Fuel: ",gas)
print("Accomodation: ",living)
print("Food: ",food)
print()
if balance >= 0:
    print("Remaining Balance: ",balance)
else:
    print("You are over budget!")




#take user input of budget and destination
#receive input of fuel, accomodations, and food
#output location
#show starting budget
#show expenses 
#output remaing balance after expenses
#if balance is below zero tell user they are above budget