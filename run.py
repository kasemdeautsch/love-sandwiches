# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)


def get_sales_data():
    """
    Get sales figures input from the user.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        x = [int(value) for value in values]

        if len(values) != 6:
            raise ValueError(
                f"--Exactly 6 values required, you provided {len(values)}--"
            )
    except ValueError as e:
        print(f"XXX.Invalid data: {e}, please try again.XXX\n")
        return False
    print('x ', x)
    print('values ', values)
    return True


def update_sales_work_sheet(data):
    print('updating sales in work sheet')
    sales_work_sheet = SHEET.worksheet('sales')
    sales_work_sheet.append_row(data)
    print('sales updated.\n')


def calculate_surplus_data(sales_row):
    print('calculate surplus starting')
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]
    pprint(stock_row)


def main():
    """Run all program functions"""
    data = get_sales_data()
    print('data ', data)
    sales_data = [int(num) for num in data]
    print(sales_data)
    update_sales_work_sheet(sales_data)
    calculate_surplus_data(sales_data)


print('Welcom to lovesand project..')
main()
