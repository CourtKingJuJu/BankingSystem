import pandas as pd
import csv 
from datetime import datetime
from data import getAmount, getCategory, getDate, getDescription
import matplotlib.pyplot as plt 


class CSV():
    CSVFile = 'Transaction_Data.csv'
    columns = ["date", "amount", "category", "description"]
    dateFormat =  "%d-%m-%Y"

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
    
    @classmethod
    def getTransactions(cls, startDate, endDate):
        df = pd.read_csv(cls.CSVFile)
        
        #Convert all dates into date time object to filter transactions
        df["date"] = pd.to_datetime(df["date"], format=CSV.dateFormat)
        startDate = datetime.strptime(startDate, CSV.dateFormat)
        endDate = datetime.strptime(endDate, CSV.dateFormat)
        
        #Create a Mask to see if we should select rows from transaction data 
        mask = (df["date"] >= startDate ) & (df["date"] <= endDate)
        
        #Creates a df where only items between the start and end date are in it
        filteredDf = df.loc[mask]
        
        if filteredDf.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transactions from {startDate.strftime(CSV.dateFormat)} to {endDate.strftime(CSV.dateFormat)}")
            print(filteredDf.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.dateFormat)}))
            
            totalIncome = filteredDf[filteredDf["category"] == "Income"]["amount"].sum()
            totalExpense = filteredDf[filteredDf["category"] == "Expense"]["amount"].sum()
            print("\nSummary: ")
            print(f"Total Income: ${totalIncome:.2f}")
            print(f"Total Expense: ${totalExpense:.2f}")
            print(f"Total Savings: ${(totalIncome - totalExpense):.2f}")
        
        return filteredDf
            
def add():
    CSV.initialize_csv()
    date = getDate("Enter the date of the Transaction (dd-mm-yyyy) or press enter for todays date: ", allowDefault=True)
    amount = getAmount()
    category = getCategory()
    description = getDescription()
    CSV.addTransaction(date, amount, category, description)

def plotTransactions(df):
    df.set_index('date', inplace=True)
    
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0) #Daily freuency

    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0) #Daily freuency

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    while True:
        print('\n1. Add a new transaction')
        print('2. get previous transactions')
        print('3. Exit')
        request = input('Select your request by entering (1-3): ')
        
        if request == '3':
            print('Exiting... Thank you')
            break
        
        elif request == '1':
            add()
        
        elif request == '2':
            
            startDate = input("Enter the start date (dd-mm-yyyy): ")
            endDate = input("Enter the end date (dd-mm-yyyy): ")
            df = CSV.getTransactions(startDate, endDate)
            
            if input("Do you want to see a plot graph (y/n) ").lower() == "y":
                plotTransactions(df)

    
if __name__ == '__main__':
    main()

"""
Learning concepts
1. With open handles all memory leaks and will close the file after the code inside the block is done

"""