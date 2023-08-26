"""
GOAL: Grocery tracker to prevent food from expiring/wasting money.
require manual input of food items but the program will reference a database and use a standard expiration date for the item but the user can manually change this if it is incorrect.
the program will keep track of the days and will accumalate the amount of expired food over time if the user does not use the food.
Standard method: user inputs food items.

"""
import csv
from datetime import datetime

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

def readData(readFile):
    with open(readFile, "r") as file:
        # Read data from a file
        
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)

def writeData(writeFile, itemInformation):
    with open(writeFile, "a") as file:
        # Write data to the file
        
        writer = csv.writer(file)
        writer.writerow(itemInformation)




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
            print(readData(storage_file))
        elif menuInput == 2:    
            while quit1 == False:                                   #loop to allow user to input multiple items
                foodInput = input("Enter the name of the food ")
                monthInput = input("Enter the month of expiration ")
                dayInput = input("Enter day of expiration ")
                yearInput = input("Enter the year of expiration ")
                costOfFood = input("Enter the cost of the food(do not add dollar sign) ")
                
                costOfFood = f"${costOfFood}"                           #formatting cost with $ sign      
                expirationDate = f"{monthInput}-{dayInput}-{yearInput}"         #Creating expiration date for the food dictionary
                foodList = [currentdate, foodInput, costOfFood, expirationDate]
                
                writeData(storage_file, foodList)                #Writing data to file "GroceryTrackerStorage.csv"
                writeData(file_name, foodList)                   #Writing data to file "my_food_file.csv"
                
                quit2 = input("To quit enter 'q'. To continue press any key")
                if quit2 == "q":
                    quit1 = True
            
        elif menuInput == 3:
            print("option3")
            quitMainLoop = True
        elif menuInput == 4:
            expiringFood = readData(file_name)
            quitMainLoop = True
        elif menuInput == 5:
            print("option3")
            quitMainLoop = True
        else:
            print("Enter valid input")
        


    
