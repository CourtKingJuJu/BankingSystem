from datetime import datetime


dateFormat =  "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

"""
Method that recursevely prompts the user for the date untill a valid
date is provided. It also allows the user to just hit enter to get the 
current date

Parameters:
-----------

prompt : str
    the prompt that the user sees

allowDefault : boolean
    allows default time if user just hits enter
"""
def getDate(prompt, allowDefault=False):
    date_str = input(prompt)
    
    if allowDefault and not date_str:
        return datetime.today().strftime(dateFormat)
    
    else:
        try:
            valid_date = datetime.strptime(date_str, dateFormat)
            return valid_date.strftime(dateFormat)
        except ValueError:
            print("Invalid date format. Please enter the date in dd-mm-yyyy format")
            return getDate(prompt, allowDefault)


"""
Recursive method that asks for the amount of money and makes sure no negative 
input is taken in. 
"""
def getAmount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative value non-zero value")
        return amount
    except ValueError as e:
        print(e)
        return getAmount

"""
Recursive method that prompts the user for a category
either expense or income and does not allow for different 
input
"""
def getCategory():
    category = input("Enter the Category ('I' for income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
   
    print("Please enter a valid Category")
    getCategory()


def getDescription():
    return input("Enter a breif description of the Transaction (Optional): ")

