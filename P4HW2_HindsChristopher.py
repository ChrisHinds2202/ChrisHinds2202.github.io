# Christopher Hinds
# 11 Nov 25
# P4HW2
# Determine OT pay and gross pay for employees

'''
get name of employee
get hours worked
get employee pay rate

find OT hours

if employee hours > 40
    OTrate equals hours times 1.5
    OTpay equals Otrate times pay
else 
    product of hours and pay

display gross pay
display Name, pay rate, hours worked, OT hours, OT pay, regular pay, and gross pay
'''
hoursWorked = 0
pay = 0
payRate = 0
extraHours = 0
overtimePay = 0
regularPay = 0
numEmployees = 0
totalRegularPay = 0
totalOvertimePay = 0
totalGrossPay = 0
#getting input
while True:
    name = input("Enter employee's name: ")

    if name.lower() == "done":
        break
    while True:
        hoursWorked = float(input("Enter number of hours worked: "))
        payRate = float(input("Enter employee's pay rate: "))

        extraHours = 0
        overtimePay = 0

        if hoursWorked > 40:
            extraHours = hoursWorked - 40
            overtimeRate = extraHours * 1.5
            overtimePay = overtimeRate * payRate
            regularPay = payRate * 40
            pay = overtimePay + regularPay
        else:
            pay = payRate * 40
        break

    #total for end output
    totalRegularPay += regularPay
    totalOvertimePay += overtimePay
    totalGrossPay += pay
    numEmployees += 1
    
    print(f"Employee name: {name:>5}")
    print(f"{'Hours Worked':<{10}} {'Pay Rate':<{12}} {'OverTime':<{10}} {'OverTime Pay':<{10}} {'RegHour Pay':<{12}} {'Gross Pay':<{12}}")
    print("-----------------------------------------------------------------------------------------")
    print(f"{hoursWorked:<12} {payRate:<14} {extraHours:<8} {overtimePay:<12} ${regularPay:<12} ${pay:<12}")


print(f"Total of employees entered: {numEmployees:>10}")
print(f"Total Overtime Pay: ${totalOvertimePay:>10,.2f}")
print(f"Total Regular Pay: ${totalRegularPay:>10,.2f}")
print(f"Total amount paid in gross pay ${totalGrossPay:>10,.2f}")

