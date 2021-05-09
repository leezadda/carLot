"""
A program with multiple functions that take 
a dictionary of car models (keys) plus the 
amount in the car lot (values)and return the
amount of car types, car per type, sum of cars,
and the abilty to update the amount
"""

def getNModels(inventoryDict): 
    return len(inventoryDict)

def getCarsPerModel(inventoryDict, keyStr):
    return inventoryDict[keyStr]

def getTotalCars(inventoryDict):
    sum = 0
    for keyStr in inventoryDict.keys():
        sum += getCarsPerModel(inventoryDict, keyStr)
    return sum

def updateInventory(inventoryDict, modelStr, newAmount):
    inventoryDict[modelStr] = newAmount

# DO NOT MODIFY THIS PART OF THE PROGRAM

inventory = {'Sentra' : 25, 'Rogue': 30, 'Versa': 15}
option = int(input(""))
if option == 1:
    result = getNModels(inventory)
    print("The number of models in the dealership is", result)
elif option == 2: 
    model = input("")
    result = getCarsPerModel(inventory,model)
    print("The number of", model, "in the dealership is", result)
elif option == 3:
    result = getTotalCars(inventory)
    print("The total number of cars in the dealership is", result)
elif option == 4:
    model = input("")
    ncars = int(input(""))
    updateInventory(inventory,model,ncars)
    print(inventory)
