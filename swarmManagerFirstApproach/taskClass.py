import ArrayLists
import random
import time


midtask = []

def WhatColor():
        colors = random.sample(ArrayLists.arrayOfBricks, len(ArrayLists.arrayOfProc))
        for i in range(len(ArrayLists.arrayOfProc)):
            color = colors[i]
            ArrayLists.arrayAvailableColor.append(color)

def AmountBricks():
    for i in range(len(ArrayLists.arrayAvailableColor)):
        amount = random.choice(range(5, 50))  # ændre til hvor meget der kan være i en robot
        ArrayLists.arrayAvailableBricks.append(amount)
        print("There are", ArrayLists.arrayAvailableBricks[i] ,ArrayLists.arrayAvailableColor[i], "on", ArrayLists.arrayOfProc[i])

def ModusOperandi():
    for i in range(len(ArrayLists.arrayOfProd)):
        for i in range(len(ArrayLists.arrayOfProc)):
            midtask.append(ArrayLists.arrayAvailableColor[i])
            midtask.append(random.choice(range(1, 5)))
        ArrayLists.ModusOperandiArray.append(midtask.copy())
        midtask.clear()
    print("The order concists of:", ArrayLists.ModusOperandiArray)


def Refill(z):
    newamount = 50  # ændre til hvor meget der kan være i the process robot
    if ArrayLists.arrayAvailableBricks[z] < 5:
        print(ArrayLists.arrayOfProc[z], "goes to refill")
        time.sleep(3) #Here it has to go refill
        ArrayLists.arrayAvailableBricks[z] += newamount
        print(ArrayLists.arrayOfProc[z], "has been refilled")


def ProdBotEat():
    for i in range(len(ArrayLists.arrayOfProd)):
        print(ArrayLists.arrayOfProd[i], "has started")
        time.sleep(1)
        bag = ""
        job = len(ArrayLists.arrayOfProc)
        order = ["Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete"]
        while job != 0:
            for j in range(len(ArrayLists.arrayOfProc)):
                if ArrayLists.ModusOperandiArray[i][1+j*2] > 0 and ArrayLists.State[j] == "Not Occupied" and order[j] == "Not Complete":
                    ArrayLists.State[j] = "Occupied"

                    ArrayLists.arrayOfInv[i] += ArrayLists.ModusOperandiArray[i][1+j*2]
                    newAmountAfterBrickGone = ArrayLists.arrayAvailableBricks[i] - ArrayLists.ModusOperandiArray[i][1+j*2]
                    ArrayLists.arrayAvailableBricks[i] = newAmountAfterBrickGone
                    job -= 1
                    ArrayLists.State[j] = "Not Occupied"
                    order[j] = "Complete"
                    Refill(j)
        if ArrayLists.arrayOfInv[i] < 3:
            bag = "small"
        else:
            bag = "large"
        print(ArrayLists.arrayOfProd[i], "going to station and dropping of a", str(bag), "bag with", ArrayLists.arrayOfInv[i])
        #Add movement to station
        time.sleep(5)
        ArrayLists.arrayOfInv[i] = 0
        print(ArrayLists.arrayOfProd[i], "Done")




