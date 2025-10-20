# Christopher Hinds
# 19 October 2025
# PP3LAB
# calculate most efficient amount of dollars and coins for a certain amount

#get input of users money and convert to integer
amount = float(input("How much money do you have? "))
amount = int(amount * 100)

#check amount for negative/invalid input
if amount < 0:
    print("Amount can not be negative.")

#dictionary to hold change values
change, dollars, quarters, nickels, dimes, pennies = 0, 0, 0, 0, 0, 0,

if amount >= 100:
    dollars = amount // 100
    change = amount % 100

if change >= 25:
    quarters = change // 25
    change = change % 25
if change >= 10:
    dimes = change // 10
    change = change % 10
if change >= 5:
    nickels = change // 5
    change = change % 5
if change >= 1:
    pennies = change 
    change = change - pennies


print(f"Your change will consist of {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")