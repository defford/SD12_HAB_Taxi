from functions import PPrint, SaveToFileBar, WaitingMessage
import time

while True:
    
    while True:

        PPrint(90, ("          ____________________________________________________", "center"))
        PPrint(90, ("          /  __  __ ___     ____     ______              _    /", "center"))
        PPrint(90, ("        /  / / / //   |   / __ )   /_  __/____ _ _  __ (_)  /", "center"))
        PPrint(90, ("      /  / /_/ // /| |  / __ \     / /  / __ `/| |/_// /  /", "center"))
        PPrint(90, ("    /  / __  // ___ | / /_/ /    / /  / /_/ /_>  < / /  /", "center"))
        PPrint(90, ("   /  /_/ /_//_/  |_|/_____/    /_/   \__,_//_/|_|/_/  / ", "center"))
        PPrint(90, ("/___________________________________________________/", "center"))
        print()
        PPrint(90, ("'Family Owned, Community Driven'", "center"))
        print()
        PPrint(90, ("Please choose from the following options:", "center"))
        print()
        print(" " * 20, "+", "-" * 43, "+")
        print(" " * 20, "|                                             |")
        print(" " * 20, "|      1. Enter a New Employee (driver)       |")
        print(" " * 20, "|      2. Enter Company Revenues              |")
        print(" " * 20, "|      3. Enter Company Expenses              |")
        print(" " * 20, "|      4. Track Car Rentals                   |")
        print(" " * 20, "|      5. Record Employee Payment             |")
        print(" " * 20, "|      6. Print Company Profit Listing        |")
        print(" " * 20, "|      7. Print Driver Financial Listing      |")
        print(" " * 20, "|      8. Corporate Summary Report            |")
        print(" " * 20, "|      9. Quit Program                        |")
        print(" " * 20, "|                                             |")
        print(" " * 20, "+", "-" * 43, "+")
        print()

        mainMenuChoice = input("Please choose an option: ").upper()

        if mainMenuChoice == "1":

            # Loop main program until user confirms entry
            while True:

                import csv
                from datetime import datetime
                import os

                # Description: Program to add new employees to the employee database
                # Author: Nicole Sparkes
                # Date: 2024-08-01 to 2024-08

                # Function to read defaults from the defaults.dat file
                def read_last_driver_number(file_path):
                    last_driver_number = 0  # Initialize to a default value
                    # if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
                    #     return last_driver_number  # If the file doesn't exist or is empty, return 0
                    with open(file_path, 'r') as file:
                        for line in file:
                            if line:
                                last_driver_number = int(line.split(',')[0].strip())
                    return last_driver_number

                # Function to calculate time employed
                def calculate_time_employed(hire_date):
                    hire_date = datetime.strptime(hire_date, '%Y-%m-%d')
                    today = datetime.today()

                    # Calculate difference in days
                    delta_days = (today - hire_date).days

                    # Approximate calculations
                    years = delta_days / 365
                    remaining_days = delta_days % 365
                    months = remaining_days / 30
                    days = remaining_days % 30

                    return int(years), int(months), int(days)

                # Function to calculate time until license expiry
                def calculate_time_until_license_expiry(expiry_date):
                    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')
                    today = datetime.today()
                    time_until_expiry = expiry_date - today
                    return time_until_expiry.days


                # Function to calculate time until insurance renewal
                def calculate_time_until_insurance_renewal(renewal_date):
                    renewal_date = datetime.strptime(renewal_date, '%Y-%m-%d')
                    today = datetime.today()
                    time_until_renewal = renewal_date - today
                    return time_until_renewal.days

                #Function to add a new employee
                def add_new_employee(employees_file, driver_details_file):
                    # Read the last driver number
                    last_driver_number = read_last_driver_number(driver_details_file)
                    driver_number = last_driver_number + 1

                    while True:
                        # Gather new employee details
                        first_name = input("Enter the driver's first name: ")
                        last_name = input("Enter the dirver's last name: ")
                        address = input("Enter the driver's address: ")
                        city = input("Enter the driver's city: ")
                        postal_code = input("Enter the postal code: ")
                        phone_number = input( "Enter the driver's phone number (###-###-####): ")
                        license_number = input("Enter the drivers license number: ")
                        license_expiry = input("Enter the license expiry date (YYYY-MM-DD): ")
                        driver_abstract_number = input("Enter the driver abstract number (XX-###-####): ")
                        insurance_company = input("Enter the insurance company: ")
                        policy_number = input("Enter the policy number: ")
                        insurance_renewal_date = input("Enter the insurance renewal date (YYYY-MM-DD): ")
                        own_car = input("Does the driver have their own car (Y/N): ").strip().upper() == "Y"
                        own_car_status = "Yes" if own_car else "No"
                        balance_due = 0.0
                        hire_date = input("Enter the hire date (YYYY-MM-DD): ")

                        # Calculate additional fields
                        time_until_license_expiry = calculate_time_until_license_expiry(license_expiry)
                        time_until_insurance_renewal = calculate_time_until_insurance_renewal(insurance_renewal_date)

                        # Display inputs which correspond with the Employees entries
                        WaitingMessage(f"Adding {first_name} {last_name}", 3)
                        print()
                        print()
                        PPrint(70, ("HAB Taxi Services - New Employee Information", "center"))
                        PPrint(70, (f"Driver Number: {driver_number}", "center"))
                        print()
                        print()
                        print("=" * 70)
                        PPrint(70, (f"Hire date: {hire_date}", "center"))                      
                        print( "=" * 70)
                        print()
                        print()
                        print(f"Name              Address              City              Postal Code")
                        print("=" * 70)
                        PPrint(70, (f"{first_name}", "left"), (f"{address}", 14), (f"{city}", 36), (f"{postal_code}", 59))
                        print(f"{last_name}")
                        print("=" * 70)
                        print()
                        print()
                        print(f"License            License              Insurance            Policy")
                        print(f"Number             Expiry Date          Company              Number")
                        print("=" * 70)
                        PPrint(70, (f"{license_number}", "left"), (f"{license_expiry}", 19), (f"{insurance_company}", 38), (f"{policy_number}", 61))
                        print("=" * 70)
                        print()
                        print()
                        print(f"Own                   Days until                      Days until")
                        print(f"Car                 License Expiry                 Insurance Renewal")
                        print("=" * 70)
                        print(f"{own_car_status}                      {time_until_license_expiry}                              {time_until_insurance_renewal}")
                        print("=" * 70)
                        print()

                        while True:
                            confirmNewEmployee = input("Confirm if the information above is correct (Y/N): ").upper()

                            if confirmNewEmployee in ["Y", "N"]:
                                break
                            else:
                                print()
                                print("Please enter a valid option.")
                                print()

                        if confirmNewEmployee == "N":
                            continue

                    
                        SaveToFileBar("Saving to Employees file", [driver_number, first_name, last_name, address, city, postal_code], employees_file, "emp")

                        SaveToFileBar("Saving to Driver Details file", [driver_number, license_number, license_expiry, insurance_company, policy_number, own_car_status, balance_due], driver_details_file, "dd")
                        
                        print()
                        time.sleep(1)
                        print(f"New employee {first_name} {last_name} added with driver number {driver_number}.")
                        time.sleep(1.2)
                        print()
                        break

                # Paths to the files
                employee_file_path = './Data_Files/Employees.dat'
                driver_details_file_path = './Data_Files/DriverDetails.dat'

                # Function to call to add a new employee
                add_new_employee(employee_file_path, driver_details_file_path)

                
                PPrint(70, ("What would you like to do?", "center"))
                print()
                print("1. Enter another employee")
                print("2. Return to Main Menu")
                print("3. Exit Program")
                print()
                
                while True:
                    returnToMenu = input("Please select an option: ")   

                    if returnToMenu in ["1", "2", "3"]:   
                        break
                    else:
                        print()
                        print("Please enter a valid option")
                        print()

                if returnToMenu == "1":
                    continue                 
                elif returnToMenu == "2":
                    print()
                    WaitingMessage("Returning to Main Menu", 25)
                    time.sleep(0.5)
                    print()                    
                    break
                elif returnToMenu == "3":
                    break

            if returnToMenu == "3":
                print()
                PPrint(70, ("Have a Great Day!", "center"))
                time.sleep(1)
                print()
                print()
                break

            continue

        elif mainMenuChoice == "7":
            # Description - This script reads data from a file containing revenue information for HAB Taxi Services and its drivers, then proceeds to generate financial reports for individual drivers. 
            # Author - Christian Rose (Group 6)
            # Date - August 1st 2024.  

            # Define Required Libraries:
            from datetime import datetime

            # Function to process revenue data from a file and return a dictionary containing financial information for each driver:
            def process_revenue_data(file_path: str, start_date: datetime, end_date: datetime):
                drivers_financials = {}
                
                try:
                    with open(file_path, 'r') as file:
                        for line in file:
                            parts = line.strip().split(', ')
                            # Check if the line has the correct number of fields:
                            if len(parts) != 7:
                                print(f"Skipping invalid line: {line.strip()}")
                                continue
                            
                            try:
                                transaction_id = parts[0]
                                date = datetime.strptime(parts[1], '%Y-%m-%d')
                                description = parts[2].strip('"')
                                driver_id = parts[3]
                                amount = float(parts[4])
                                hst = float(parts[5])
                                total = float(parts[6])
                            except ValueError:
                                print(f"Skipping line with invalid data: {line.strip()}")
                                continue
                            # Check if the transaction date is within the specified date range:
                            if start_date <= date <= end_date:
                                if driver_id not in drivers_financials:
                                    drivers_financials[driver_id] = {
                                        'transactions': [],
                                        'earnings': 0.0,
                                        'deductions': 0.0,
                                        'net_pay': 0.0,
                                        'hst': 0.0,
                                        'transaction_count': 0
                                    }
                                # Add the transaction to the driver's financial records:
                                drivers_financials[driver_id]['transactions'].append({
                                    'Transaction ID': transaction_id,
                                    'Date': date.strftime('%Y-%m-%d'),
                                    'Description': description,
                                    'Amount': amount,
                                    'HST': hst,
                                    'Total': total
                                })
                                
                                if "Stand Fees" in description:
                                    drivers_financials[driver_id]['deductions'] += amount
                                    drivers_financials[driver_id]['hst'] += hst
                                    drivers_financials[driver_id]['net_pay'] += total
                                else:
                                    drivers_financials[driver_id]['earnings'] += amount
                                    drivers_financials[driver_id]['hst'] += hst
                                    drivers_financials[driver_id]['net_pay'] += total
                                
                                drivers_financials[driver_id]['transaction_count'] += 1
                # Handle exceptions:
                except FileNotFoundError:
                    print(f"Error: The file '{file_path}' was not found.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                
                return drivers_financials

            # Function to print the financial summary for a specific driver:
            def print_financial_summary(driver_id: str, drivers_financials: dict, start_date: datetime, end_date: datetime):
                if driver_id in drivers_financials:
                    financials = drivers_financials[driver_id]
                    print()
                    print()
                    print(f"                       HAB Taxi Services - Driver Financials Report")
                    print(f"                                    {'Driver ID: ' + driver_id}")
                    print()
                    print(f"        -----------------------------")
                    print(f"        Report Period:")
                    print(f"        {start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}")
                    print(f"        -----------------------------")
                    print()
                    print(f"        {'Transaction':<22}") 
                    print(f"        {'ID':<12}    {'Date':<11}         {'Description':<19} {'Amt':>12}")
                    print(f"        =======================================================================")

                    for i, transaction in enumerate(financials['transactions']):
                        print(f"        {transaction['Transaction ID']:<15} {transaction['Date']:<19} {transaction['Description']:<27} "
                            f"${transaction['Amount']:>0,.2f}")

                    print(f"        =======================================================================")
                    print()
                    print(f"                                                             HST:       ${financials['hst']:>0,.2f}")
                    print(f"                                                             Total:    ${financials['net_pay']:>0,.2f}")
                    print()
                    print(f"        Total items for Driver {driver_id}: {financials['transaction_count']}")
                    print()
                else:
                    print(f"No financial data found for Driver ID: {driver_id}")

            # Function to get the driver ID from the user:
            def get_driver_id():
                driver_id = input("Enter the driver ID for which you want to generate the report: ")
                return driver_id.strip()

            # Main function to execute the script:
            def main():
                start_date = datetime.strptime('2024-07-01', '%Y-%m-%d')
                end_date = datetime.strptime('2024-07-31', '%Y-%m-%d')
                file_path = 'Data_Files/Revenues.dat'
                
                drivers_financials = process_revenue_data(file_path, start_date, end_date)
                
                while True:
                    driver_id = get_driver_id()
                    if driver_id in drivers_financials:
                        print()
                        WaitingMessage(f"Generating Driver Financial Report For Employee ID {driver_id}", 20)
                        print()
                        print_financial_summary(driver_id, drivers_financials, start_date, end_date)
                    else:
                        print(f"No financial data found for Driver ID: {driver_id}. Please try again.")
                    

                    # Ask the user if they want to generate another report or finish:
                    user_choice = input("Would you like to generate another report? (Y/N): ").strip().upper()
                    if user_choice != 'Y':
                        print()
                        print("Thank you for using the HAB Taxi Services financial report generator.")
                        print()
                        WaitingMessage("Returning to Main Menu", 3)
                        time.sleep(0.5)
                        print()
                        print()
                        break

            main()
        
        elif mainMenuChoice == "3":
            print()
            print(f"{'//COMPANY EXPENSE ENTRY SYSTEM UNDER CONSTRUCTION//':^80}")
            print(f"{'(Please choose 1, 7, or 8)':^80}")
            time.sleep(0.5)
            print()
            WaitingMessage("Returning to Main Menu", 25)
            time.sleep(0.5)
            print()
            continue

        elif mainMenuChoice == "4":
            print()
            print(f"{'//CAR RENTAL TRACKING SYSTEM UNDER CONSTRUCTION//':^80}")
            print(f"{'(Please choose 1, 7, or 8)':^80}")
            time.sleep(0.5)
            print()
            WaitingMessage("Returning to Main Menu", 25)
            time.sleep(0.5)
            print()
            continue

        elif mainMenuChoice == "5":
            print()
            print(f"{'//RECORD EMPLOYEE PAYMENT SYSTEM UNDER CONSTRUCTION//':^80}")
            print(f"{'(Please choose 1, 7, or 8)':^80}")
            time.sleep(0.5)
            print()
            WaitingMessage("Returning to Main Menu", 25)
            time.sleep(0.5)
            print()
            continue

        elif mainMenuChoice == "6":
            print()
            print(f"{'//PROFIT REPORT GENERATOR UNDER CONSTRUCTION//':^80}")
            print(f"{'(Please choose 1, 7, or 8)':^80}")
            time.sleep(0.5)
            print()
            WaitingMessage("Returning to Main Menu", 25)
            time.sleep(0.5)
            print()
            continue

        elif mainMenuChoice == "2":
            print()
            print(f"{'//COMPANY REVENUE ENTRY SYSTEM UNDER CONSTRUCTION//':^80}")
            print(f"{'(Please choose 1, 7, or 8)':^80}")
            time.sleep(0.5)
            print()
            WaitingMessage("Returning to Main Menu", 25)
            time.sleep(0.5)
            print()
            continue

        elif mainMenuChoice == "8":

            while True:
                    
                # Title: HAB Taxi Services - Corporate Summary Report Generator
                # Description: Generates summary metrics across company revenue, expense, and employee data for business analytical processes.
                # Author: Daniel Efford
                # Date: 2024-07-31 - 2024-08-08

                # Import libraries
                import datetime
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

                # Determine earliest date to help user know what range to search
                earliestRevDate = datetime.datetime.now()
                earliestExpDate = datetime.datetime.now()

                for date in revenueList:
                    earlyRevDate = datetime.datetime.strptime(date[1], "%Y-%m-%d")
                    if earlyRevDate < earliestRevDate:
                        earliestRevDate = earlyRevDate

                for date in expensesList:
                    earlyExpDate = datetime.datetime.strptime(date[2], "%Y-%m-%d")
                    if earlyExpDate < earliestExpDate:
                        earliestExpDate = earlyExpDate

                earliestDate = min(earliestExpDate, earliestRevDate)
                earliestDate = earliestDate.date()

                dateStart = input(f"Enter the first date the report should begin on. Notice: No data before {earliestDate}. (YYYY-MM-DD): ")
                dateEnd = input("Enter the date the report should end on (YYYY-MM-DD): ")
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
                    itemLength = len(driverDetailsList[0])
                    if len(item) == itemLength:
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
                WaitingMessage("Generating Corporate Summary Report", 35)
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
                PPrint(90, (f"{'-' * 70}", "center"))
                print()
                print()
                time.sleep(1)

                PPrint(70, ("What would you like to do?", "center"))
                print()
                print("1. Generate Another Report")
                print("2. Return to Main Menu")
                print("3. Exit Program")
                print()
                
                while True:
                    returnToMenu = input("Please select an option: ")   

                    if returnToMenu in ["1", "2", "3"]:   
                        break
                    else:
                        print()
                        print("Please enter a valid option")
                        print()

                if returnToMenu == "1":
                    continue                 
                elif returnToMenu == "2":
                    print()
                    WaitingMessage("Returning to Main Menu", 25)
                    time.sleep(0.5)
                    print()                    
                    break
                elif returnToMenu == "3":
                    break

            if returnToMenu == "3":
                print()
                PPrint(70, ("Have a Great Day!", "center"))
                time.sleep(1)
                print()
                print()
                break

        elif mainMenuChoice == "9":
            print()
            PPrint(90, ("Have a Great Day!", "center"))
            print()
            time.sleep(1)
            print()
            break

    
    break