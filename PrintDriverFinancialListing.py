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
        print(f"----------------------------------------------------------------------------------------")
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
            print_financial_summary(driver_id, drivers_financials, start_date, end_date)
        else:
            print(f"No financial data found for Driver ID: {driver_id}. Please try again.")
        
        # Ask the user if they want to generate another report or finish:
        user_choice = input("Would you like to generate another report? (yes/no): ").strip().lower()
        if user_choice != 'yes':
            print("Thank you for using the HAB Taxi Services financial report generator.")
            break

# Execute the main function:
if __name__ == "__main__":
    main()

# End of Script.
