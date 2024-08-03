import pandas as pd
import csv 
from datetime import datetime


class CSV():
    CSVFile = 'Transaction_Data.csv'
    
    @classmethod
    def initalize_csv(cls):
        try: 
            pd.read_csv(cls.CSVFile)
        except FileNotFoundError:
            dataFrame = pd.DataFrame(columns=["data", "amount", "category", "description"])
            dataFrame.to_csv(cls.CSVFile, index=False)
    
    @classmethod
    def addTransaction(cls, date, amount, category, description):
        pass
     
CSV.initalize_csv()


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
            pass
            
        if request == '2':
            pass

    
if __name__ == '__main__':
    main()
