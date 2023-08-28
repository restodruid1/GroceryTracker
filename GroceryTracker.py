"""
GOAL: Grocery tracker to prevent food from expiring/wasting money. Send message to phone saying which food will expire soon.
require manual input of food items but the program will reference a database and use a standard expiration date for the item but the user can manually change this if it is incorrect.
the program will keep track of the days and will accumalate the amount of expired food over time if the user does not use the food.
Standard method: user inputs food items.

"""
import csv
from datetime import datetime
import pandas
from pandas import DataFrame

def currentDate():
    current_date = datetime.now().strftime("%m-%d-%Y")
    return current_date 

def menu():
    print("          Menu          ")
    print("__________________________")
    print("Option 1: Print log of food")
    print("Option 2: Add new item")
    print("Option 3: Delete item")
    print("Option 4: Show food expiring soon")
    print("Option 5: TBD")

def readData(fileName):
        # Read data from a file
        readFile = pandas.read_csv(fileName)
        return readFile


if __name__ == "__main__":
    
    file_name = "my_food_file.csv"
    storage_file = "GroceryTrackerStorage.csv"
    currentdate = currentDate()
    quit1 = False
    quitMainLoop = False
    
    while quitMainLoop == False:
        menu()
        menuInput = int(input("Enter a number(1, 2, 3, 4, 5)\n"))
        if menuInput == 1:
            #Try/catch block for when file is accessed with no data stored
            print(readData(storage_file))
        elif menuInput == 2:
            counter = 0   
            while quit1 == False:                                   #loop to allow user to input multiple items
                foodInput = input("Enter the name of the food ")
                monthInput = input("Enter the month of expiration ")
                dayInput = input("Enter day of expiration ")
                yearInput = input("Enter the year of expiration ")
                costOfFood = input("Enter the cost of the food(do not add dollar sign) ")
                
                costOfFood = f"${costOfFood}"                           #formatting cost with $ sign      
                expirationDate = f"{monthInput}-{dayInput}-{yearInput}"         #Creating expiration date for the food dictionary
                foodList = [[currentdate, foodInput, costOfFood, expirationDate,]]  #Organizing data for a panda df
                
                df = pandas.DataFrame(foodList, columns=['Log Date', 'Food Item', 'Cost', 'Exp Date'])  #storing food data in a panda df
                df.to_csv(file_name, mode='a', header=False, index=False)    #Writing the df to a csv file
                df.to_csv(storage_file, mode='a', header=False, index=False)

                quit2 = input("To quit enter 'q'. To continue press any key ")
                if quit2 == "q":
                    break
            
        elif menuInput == 3:
            print("option3")
            #Auto delete expired food from data.
            #Allow user to individually remove an item
            quitMainLoop = True
        elif menuInput == 4:
            #shows food expiring soon
            test = readData(storage_file)
            subset = test['Exp Date']
            print(subset)
            quitMainLoop = True
        elif menuInput == 5:
            #Money lost to food expiring
            print("option3")
            quitMainLoop = True
        else:
            print("Enter valid input")

"""Encorporate feature that reminds user daily of food that will expire soon
Goal is to reduce food wasted & know how much money you are wasting"""