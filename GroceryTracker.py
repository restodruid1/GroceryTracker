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
def currentMonth():
    current_date = datetime.now().strftime("%m")
    return current_date 
def currentDay():
    current_date = datetime.now().strftime("%d")
    return current_date 
def currentYear():
    current_date = datetime.now().strftime("%Y")
    return current_date 

def menu():
    print("          Menu          ")
    print("__________________________")
    print("Option 1: Print log of food")
    print("Option 2: Add new item")
    print("Option 3: Delete expired items")
    print("Option 4: Show food expiring soon")
    print("Option 5: Delete an item")
    print("Option 6: Show money lost to expired food")
    print("Option 7: Quit")

def readData(fileName):
        # Read data from a file
        readFile = pandas.read_csv(fileName)
        return readFile

def parseFileData():
    dataFile = readData(file_name)
    subsetDate = dataFile['Exp Date']       #Storing the Exp date column in a variable
    subsetFood = dataFile['Food']           #Storing the Food column in a variable
    expiringSoon = []
    index = 0                           #Tracking the loop iteration for later use
    for date in subsetDate:
        expMonth = date[0:2]            #Separate the expiration into months, days, year
        expDay = date[3:5]
        expYear = int(date[6:])         #Store the expiration year 
        if expMonth[0] == "0":
            expMonth = expMonth[1]      #If user data in format "09", change it to "9"
        if expDay[0] == "0":
            expDay = expDay[1]
                
        if expYear == int(currentYear()) and int(expMonth) == int(currentMonth()) and (int(expDay) >= int(currentDay()) and int(expDay) < int(currentDay()) + 5):      
            expiringSoon.append(subsetFood[index])
            #if the expiration date is within 5 days of expiring, store the associated food in a list
                    
        index += 1                           
    for item in expiringSoon:
        print(f"{item} is expiring within 5 days!")     #Print the item expiring soon 
    
    lengthExpiringSoon = len(expiringSoon)
    if lengthExpiringSoon == 0:
        print("There are no items expiring soon")


def foodToDataFrame():
    foodInput = input("Enter the name of the food ")
    monthInput = input("Enter the month of expiration(mm) ")
    dayInput = input("Enter day of expiration(dd) ")
    yearInput = input("Enter the year of expiration(yyyy) ")
    costOfFood = input("Enter the cost of the food(ex inp = 15) ")
                
    costOfFood = f"${costOfFood}"                           #formatting cost with $ sign      
    expirationDate = f"{monthInput}-{dayInput}-{yearInput}"         #Creating expiration date for the food dictionary
    foodList = [[currentdate, foodInput, costOfFood, expirationDate,]]  #Organizing data for a panda df
                
    df = pandas.DataFrame(foodList, columns=['Log Date', 'Food', 'Cost', 'Exp Date'])  #storing food data in a panda df
    
    #The code below fixes the dataframe headers if they get deleted
    #mapping = {df.columns[0]:'Log Date',df.columns[1]:'Food',df.columns[2]:'Cost',df.columns[1]:'Exp Date'}
    #df.rename(columns=mapping)
    #df.to_csv(file_name, mode='a', index=False)
    #df.to_csv(storage_file, mode='a', index=False) 
    
    df.to_csv(file_name, mode='a', header=False, index=False)    #Writing the df to a csv file
    df.to_csv(storage_file, mode='a', header=False, index=False)

def deleteDataFromFile():
    dataFile = readData(file_name)
    subsetDate = dataFile['Exp Date']       #Storing the Exp date column in a variable
    subsetFood = dataFile['Food']            #Storing the Food column in a variable
    subsetCost = dataFile['Cost']          
    expiredFood = []
    expiredDate = []
    expiredCost = []
    index = 0                           #Tracking the loop iteration for later use
    for date in subsetDate:
        expMonth = date[0:2]            #Separate the expiration into months, days, year
        expDay = date[3:5]
        expYear = int(date[6:])         #Store the expiration year 
        if expMonth[0] == "0":
            expMonth = expMonth[1]      #If user data in format "09", change it to "9"
        if expDay[0] == "0":
            expDay = expDay[1]

        #if the food is expired, store the associated food in a list        
        if expYear < int(currentYear()):
            expiredFood.append(subsetFood[index])
            expiredDate.append(subsetDate[index])
            expiredCost.append(subsetCost[index])
        if expYear == int(currentYear()) and int(expMonth) < int(currentMonth()):
            expiredFood.append(subsetFood[index])
            expiredDate.append(subsetDate[index])
            expiredCost.append(subsetCost[index])
        if expYear == int(currentYear()) and int(expMonth) == int(currentMonth()) and int(expDay) < int(currentDay()):
            expiredFood.append(subsetFood[index])
            expiredDate.append(subsetDate[index])
            expiredCost.append(subsetCost[index])
                      
        index += 1
    
    
                             
    for item in expiredFood:
        print(f"{item} is expired!")        #Print the expired items
    if len(expiredFood) == 0:               #Check if there is expired food
        print("No items are expired")
        ans = "no"
    else:
        ans = input("Would you like to delete expired items?(yes or no) ")      
    
    if ans == "yes":
        dataFile2 = pandas.read_csv(file_name)  #Creat a dataframe
        print(dataFile2)
        
        for date in expiredDate:
            dataFile2.drop(dataFile2[dataFile2['Exp Date'] == date].index,inplace=True) #Delete expired item from the data
        
        print(dataFile2)      
        dataFile2.to_csv(file_name, mode='w',header=True , index=False)   #Overwrite my_food_file.csv without the expired food
        return expiredCost
            
    else:
        print("No items were deleted")
        expiredCost = []    
        return expiredCost #Returning an empty list so the main function
    

def writeCostToFile(money):
    total = 0
    check = len(money)  
    if check == 0:      #If no expired food is found, check will be 0
        print("")
    else:
        for item in money:
            item = item.strip('$') 
            item = int(item)
            total += item
        print(f"${total} lost to expired food")
        with open(cost_File, mode="a", newline='') as file: #Write money lost to expired food into a file
            writer = csv.writer(file)
            writer.writerow([total])


def readCostFromFile(file):
    with open(cost_File, mode='r', newline='') as file:
        reader = csv.reader(file)
        total = 0
        for row in reader:
            for number in row:          #For each line and item in csv file, add the integer total
                #print(number)
                number = int(number)    #Turn string into integer
                total += number
        print(f"Total amount of money lost to expired groceries ${total}")  

def deleteIndividualItem(name, date):
    dataFile3 = pandas.read_csv(file_name)      #Create df based on my_food_file.csv
    
    dataFile3.drop(dataFile3[(dataFile3['Exp Date'] == date) & (dataFile3['Food'] == name)].index, inplace=True)    #Delete user specified food item
    dataFile3.to_csv(file_name, mode='w',header=True , index=False) #Overwrite my_food_file.csv with updated data
        
    
if __name__ == "__main__":
    
    file_name = "my_food_file.csv"
    storage_file = "GroceryTrackerStorage.csv"
    cost_File = "ExpiredCostTracker.csv"
    currentdate = currentDate()
    quit1 = False
    quitMainLoop = False
    
    
    while quitMainLoop == False:
        menu()
        menuInput = int(input("Enter a number(1, 2, 3, 4, 5, 6, 7)\n"))
        if menuInput == 1:
            #Try/catch block for when file is accessed with no data stored
            print("\nEvery Item Tracked:")
            print(readData(storage_file))
            print("\nCurrent Inventory:")
            print(readData(file_name))
        elif menuInput == 2:   
            while quit1 == False:    #loop to allow user to input multiple items
                foodToDataFrame()    #Take user input for food item and store it in a pandas dataframe in a csv file
                quit2 = input("To quit enter 'q'. To continue press any key ")
                if quit2 == "q":
                    break
            
        elif menuInput == 3:
            #Auto delete expired food from data.
            expired = deleteDataFromFile()    #Delete expired food from my_food_file.csv
            writeCostToFile(expired)          #Write money lost to expired food to ExpireCostTracker.csv
            
        elif menuInput == 4: #INCORPORATE TEXT MESSAGE FEATURE
            parseFileData() #shows food expiring soon from my_food_file.csv
        
        elif menuInput == 5: #Delete individual item
            food = input("Name of item you wish to delete ")
            date = input("Expiration Date of item you wish to delete(mm-dd-yyyy) ")
            deleteIndividualItem(food, date)    #Delete individual item from my_food_file.csv
    
        elif menuInput == 6:
            readCostFromFile(cost_File)

        elif menuInput == 7:
            #QUIT
            break

        else:
            print("Enter valid input")

"""Incorporate feature that reminds user daily of food that will expire soon
Goal is to reduce food wasted & know how much money you are wasting"""