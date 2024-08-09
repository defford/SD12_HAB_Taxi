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
    print(f"Next driver number: {driver_number}")


    # Gather new employee details
    first_name = input("Enter the driver's first name: ")
    last_name = input("Enter the dirver's last name: ")
    address = input("Enter the driver's address: ")
    city = input("Enter the driver's city: ")
    postal_code = input("Enter the postal code: ")
    phone_number = input( "Enter the driver's phone number: ")
    license_number = input("Enter the drivers license number: ")
    license_expiry = input("Enter the license expiry date (YYYY-MM-DD): ")
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
    print("               HAB Taxi Services - New Employee Information")
    print(f"                     Driver Number: {driver_number}")
    print(f"")
    print(f"")
    print("=" * 70)
    print(f"                      Hire date: {hire_date}")                      
    print( "=" * 70)
    print(f"")
    print(f"")
    print(f"Name              Address              City              Postal Code")
    print("=" * 70)
    print(f"{first_name}       {address}            {city}             {postal_code}")
    print(f"{last_name}")
    print("=" * 70)
    print(f"")
    print(f"")
    print(f"License            License              Insurance            Policy")
    print(f"Number             Expiry Date          Company              Number")
    print("=" * 70)
    print(f"{license_number}            {license_expiry}          {insurance_company}          {policy_number}")
    print("=" * 70)
    print(f"")
    print(f"")
    print(f"Own                   Days until                      Days until")
    print(f"Car                 License Expiry                 Insurance Renewal")
    print("=" * 70)
    print(f"{own_car_status}                      {time_until_license_expiry}                              {time_until_insurance_renewal}")
    print("=" * 70)
    print(f"")
    print(f"                Thanks for choosing HAB Taxi Services!")
    
    
    # Append new employee to employees file
    with open(employees_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([driver_number, first_name, last_name, address, city, postal_code])
    
    # Append new employee to driver details file
    with open(driver_details_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([driver_number, first_name, last_name, address, city, postal_code])
    
    print(f"\nNew employee {first_name} {last_name} added with driver number {driver_number}.")

# Paths to the files
employee_file_path = './Data_Files/Employees.dat'
driver_details_file_path = './Data_Files/DriverDetails.dat'

# Function to call to add a new employee
add_new_employee(employee_file_path, driver_details_file_path)