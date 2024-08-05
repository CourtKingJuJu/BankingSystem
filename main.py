import pandas as pd
import csv 
from datetime import datetime
from data import getAmount, getCategory, getDate, getDescription

class CSV():
    CSVFile = 'Transaction_Data.csv'
    columns = ["date", "amount", "category", "description"]
    
    @classmethod
    def initialize_csv(cls):
        try: 
            pd.read_csv(cls.CSVFile)
        except FileNotFoundError:
            dataFrame = pd.DataFrame(columns=cls.columns)
            dataFrame.to_csv(cls.CSVFile, index=False)
    
    @classmethod
    def addTransaction(cls, date, amount, category, description):
        
        #Stored new data in python dictionary
        newData = {'date': date, 'amount': amount, 'category': category, 'description': description}

        #Opening with "a" is opening in Append mode
        #Will add the new lines to the end of the file
        with open(cls.CSVFile, "a", newline="") as csvfile:
            
            #Creating CSV writer, takes a dictonary and writes it into the csvfile
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(newData)
            
        print("Added Entry, What else can we help you with today?")
        

def add():
    CSV.initialize_csv()
    date = getDate("Enter the date of the Transaction (dd-mm-yyyy) or press enter for todays date: ", allowDefault=True)
    amount = getAmount()
    category = getCategory()
    description = getDescription()
    CSV.addTransaction(date, amount, category, description)



def main():
    while True:
        print('\n1. Add a new transaction')
        print('2. View previous transactions')
        print('3. Exit')
        request = input('Select your request by entering (1-3): ')
        
        if request == '3':
            print('Exiting... Thank you')
            break
        
        if request == '1':
            add()
        
        if request == '2':
            pass

    
if __name__ == '__main__':
    main()

"""
Learning concepts
1. With open handles all memory leaks and will close the file after the code inside the block is done

"""