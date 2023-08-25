"""
GOAL: Grocery tracker to prevent food from expiring/wasting money.
require manual input of food items but the program will reference a database and use a standard expiration date for the item but the user can manually change this if it is incorrect.
the program will keep track of the days and will accumalate the amount of expired food over time if the user does not use the food.
Standard method: user inputs food items.

"""
import csv

foodDictionary = {'food': [], "exp date":[], "cost":[]}
foodDictionary1 = []
quit1 = False


while quit1 == False:
    foodInput = input("Enter the name of the food")
    dayInput = input("Enter day of expiration")
    monthInput = input("Enter the month of expiration")
    yearInput = input("Enter the year of expiration")
    costOfFood = input("Enter the cost of the food(do not add dollar sign)")
    
    
    expirationDate = f"{dayInput}/{monthInput}/{yearInput}"
    print(expirationDate)
    item = f"{foodInput} {dayInput}/{monthInput}/{yearInput} {costOfFood}"
    foodDictionary["food"].append(foodInput)
    """foodDictionary1[0]['item'] = foodInput
    foodDictionary1[0]['exp date'] = expirationDate
    foodDictionary1[0]['cost'] = costOfFood"""
    dict1 = {'item': foodInput, 'exp date' : expirationDate, 'cost': costOfFood}    #Bundle user input into a dictionary
    foodDictionary1.append(dict1)   #Add the new dictionary to the original food list of dictionaries
    
    quit2 = input("To quit enter 'q'. To continue press any key")
    if quit2 == "q":
        quit1 = True
    

#foodDictionary["foodInput"] = foodInput
print(foodDictionary)
print(foodDictionary1)

fieldNames = foodDictionary1[0].keys()
file_name = "my_food_file.csv"

# Open the file in write mode (this will create a new file if it doesn't exist)
with open(file_name, "a") as file:
    # Write data to the file
    writer = csv.DictWriter(file, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(foodDictionary1)