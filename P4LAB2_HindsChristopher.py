# Christopher Hinds
# 11 Nov 25
# P4LAB2
# multiplication table for a given integers


value = "yes"

while value.lower() == "yes":
    #get the userinput.
    number = int(input("Please enter an integer: "))

    if number >= 0:
        for i in range(1, 13):
            result = number * i
            print(f"{number} x {i} = {result}")
    else:
        print("This program does not handle negative numbers.")

    #ask if want to run again
    value = input("Would you like to run the program again? ")

#if answer was 'no' exit message 
print("Exiting program...")