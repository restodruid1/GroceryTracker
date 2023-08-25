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




if __name__ == "__main__":
    
    foodDictionary1 = []
    currentdate = currentDate()
    quit1 = False
    quitMainLoop = False
    
    while quitMainLoop == False:
        menu()
        menuInput = int(input("Enter a number(1, 2, 3, 4, 5)"))
        if menuInput == 1:
            print("print out entire food inventory")
        elif menuInput == 2:    
            while quit1 == False:
                foodInput = input("Enter the name of the food ")
                monthInput = input("Enter the month of expiration ")
                dayInput = input("Enter day of expiration ")
                yearInput = input("Enter the year of expiration ")
                costOfFood = input("Enter the cost of the food(do not add dollar sign) ")
                costOfFood = f"${costOfFood}"
                
                expirationDate = f"{dayInput}-{monthInput}-{yearInput}"
                print(expirationDate)
                dict1 = {'log date': currentdate ,'item': foodInput, 'cost': costOfFood,'exp date' : expirationDate}    #Bundle user input into a dictionary
                foodDictionary1.append(dict1)   #Add the new dictionary to the original food list of dictionaries
                
                quit2 = input("To quit enter 'q'. To continue press any key")
                if quit2 == "q":
                    quit1 = True
            quitMainLoop = True
        elif menuInput == 3:
            print("option3")
            quitMainLoop = True
        elif menuInput == 4:
            print("option4")
            quitMainLoop = True
        elif menuInput == 5:
            print("option3")
            quitMainLoop = True
        else:
            print("Enter valid input")
        


    print(foodDictionary1)

    fieldNames = foodDictionary1[0].keys()  #Creating column names for the CSV file
    file_name = "my_food_file.csv"
    storage_file = "GroceryTrackerStorage.csv"

    # Open the file in write mode (this will create a new file if it doesn't exist)
    with open(storage_file, "a") as file:
        # Write data to the file
        
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(foodDictionary1)

    # Open the file in write mode (this will create a new file if it doesn't exist)
    with open(file_name, "a") as file:
        # Write data to the file
        
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(foodDictionary1)