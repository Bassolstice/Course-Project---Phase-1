#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('description of input:  '))
#write the GetHoursWorked function

def GetHoursWorked():
    hours = float(input("Enter hours worked: "))
    return hours

#write the GetHourlyRate function
def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

# write the GetTaxRate function
def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate


def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%f}", f"{incometax:,.2f}", f"{netpay:,.2f}")

    # write the lines of code to display hourlyrate, grosspay, taxrate, incometax and netpay with correct formatting
    # taxrate needs to be formatted as percentage





    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}", f"Total Hours Worked: {TotHours:,.2f}", f"Total Gross Pay: {TotGrossPay:,.2f}", f"Total Tax: {TotTax:,.2%f}", f"Total Net Pay: {TotNetPay:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
def hours(GetHoursWorked):
    hours = float(input("Enter hours worked: "))
    return hours
        # write the code to assign to hourlyrate the return value from GetHourlyRate
def hourlyrate(GetHourlyRate):
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate
        # write the code to assign to taxrate the return value from GetTaxRate

def taxrate(GetTaxRate):
    taxrate = float(input("Enter Tax Rate: "))
    return taxrate


grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
TotEmployees += 1
TotHours += hours
TotGrossPay += grosspay
TotTax += taxrate
TotNetPay += netpay

        # write the code to increment the other total variables with the appropriate values

PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
