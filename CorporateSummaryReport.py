# Title: HAB Taxi Services - Corporate Summary Report Generator
# Description: Generates summary metrics across company revenue, expense, and employee data for business analytical processes.
# Date: 2024-07-31 - 2024-08-05

# Import libraries
import datetime
from functions import PPrint
# Define Functions

def LoadToList(file):
        
    f = open(file, "r")
    fRead = f.read()
    fList = fRead.split("\n")
    fRecords = []
    for item in fList:
        record = item.split(", ")
        fRecords.append(record)

    return fRecords

# Read all relevant tables into memory as lists to be used for calculations and output.
revenueList = LoadToList("Data_Files/Revenues.dat")

expensesList = LoadToList("Data_Files/Expenses.dat")

expenseItemsList = LoadToList("Data_Files/ExpenseItems.dat")

employeesList = LoadToList("Data_Files/Employees.dat")

driverDetailsList = LoadToList("Data_Files/DriverDetails.dat")

# Set up Counters and Accumulators

revAcc = 0 # total revenue
revCtr = 0
expAcc = 0
expCtr = 0
balAcc = 0
drvCtr = 0

dateStart = "2024-07-01" # input("Enter the first date the report should begin on (YYYY-MM-DD): ")
dateEnd = "2024-07-15" # input("Enter the date the report should end on (YYYY-MM-DD): ")
dateStart = datetime.datetime.strptime(dateStart, "%Y-%m-%d").date()
dateEnd = datetime.datetime.strptime(dateEnd, "%Y-%m-%d").date()

for item in revenueList:
    date = item[1]
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    if date >= dateStart and date <= dateEnd:
        revCtr += 1
        revAcc += float(item[-1])

for item in expensesList:
    date = item[2]
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    if date >= dateStart and date <= dateEnd:
        expCtr += 1
        expAcc += float(item[-1])

netProfit = revAcc - expAcc

for item in driverDetailsList:
    balAcc += float(item[-1])

drvCtr = len(employeesList)

avgRev = round(revAcc / drvCtr, 2)

# Store grouped data to determine best revenue item
groupRev = {}

for item in revenueList:
    revDate = item[1]
    revDate = datetime.datetime.strptime(revDate, "%Y-%m-%d").date()

    if revDate >= dateStart and revDate <= dateEnd:
        revType = item[2]
        revAmt = float(item[4])

        if revType not in groupRev:
            groupRev[revType] = 0
        groupRev[revType] += revAmt

# Determine which item generated the most revenue
maxRev = 0
maxRevType = ""

for revType in groupRev:
    if groupRev[revType] > maxRev:
        maxRevType = revType
        maxRev = groupRev[revType]

# Store grouped expense names and cost data by invoice #
groupExp = {}
filteredInvNo = []

for item in expensesList:
    expDate = item[2]
    expDate = datetime.datetime.strptime(expDate, "%Y-%m-%d").date()
    expInvNo = item[0]

    if expDate >= dateStart and expDate <= dateEnd:
        if expDate not in filteredInvNo:
            filteredInvNo.append(expInvNo)


for item in expenseItemsList:
    invoiceNo = item[1]

    if invoiceNo in filteredInvNo:
        expType = item[2]
        expAmt = float(item[-1])

        if invoiceNo not in groupExp:
            groupExp[invoiceNo] = [expType, expAmt]
        else:    
            groupExp[invoiceNo][1] += float(expAmt)

maxExp = float(0)
maxExpType = ""

for expType in groupExp:
    if groupExp[expType][1] > maxExp:
        maxExpType = groupExp[expType][0]
        maxExp = groupExp[expType][1]



# Display the Report
print()
print()
PPrint(90, ("HAB Taxi Services - Corporate Summary Report", "center"))
print()
PPrint(90, (f"{'-' * 70}", "center"))
PPrint(90, ("Report Period:", "center"))
PPrint(90, (f"{dateStart} - {dateEnd}", "center"))
PPrint(90, (f"{'-' * 70}", "center"))
print()
PPrint(90, ("Total Revenue:", 11, "left"), (f"${revAcc:,.2f}", 55))
PPrint(90, ("Total Expenses:", 11, "left"), (f"${expAcc:,.2f}", 55))
PPrint(90, ("Net Profit:", 11, "left"), (f"${netProfit:,.2f}", 55))
print()
PPrint(90, ("Average Revenue:", 11, "left"), (f"${avgRev:,.2f}", 55))
PPrint(90, ("Total Owed:", 11, "left"), (f"${balAcc:,.2f}", 55))
PPrint(90, ("Total Drivers:", 11, "left"), (f"{drvCtr}", 55))
print()
PPrint(90, ("Most Revenue by Type:", 11, "left"), ("Most Expensive by Type:", 55))
PPrint(90, (f"{maxRevType}", 11, "left"), (f"{maxExpType}", 55))
PPrint(90, (f"${maxRev:,.2f}", 11, "left"), (f"${maxExp:,.2f}", 55))
print()
PPrint(90, (f"{'-' * 70}", "center"))
print()
PPrint(90, ("Have a nice day!", "center"))
print()


