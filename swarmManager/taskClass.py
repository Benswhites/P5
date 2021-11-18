import ArrayLists
import random
import time


midtask = []

def AmountBricks():
    colors = random.sample(ArrayLists.arrayOfBricks, len(ArrayLists.arrayOfProc))
    for i in range(len(ArrayLists.arrayOfProc)):
        color = colors[i]
        amount = random.choice(range(5, 50))  # ændre til hvor meget der kan være i en robot
        ArrayLists.arrayAvailableColor.append(color)
        ArrayLists.arrayAvailableBricks.append(amount)
    print(ArrayLists.arrayAvailableColor, ArrayLists.arrayAvailableBricks)

def ModusOperandi():
    for i in range(len(ArrayLists.arrayOfProd)):
        for i in range(len(ArrayLists.arrayOfProc)):
            midtask.append(ArrayLists.arrayAvailableColor[i])
            midtask.append(random.choice(range(1, 5)))
        ArrayLists.ModusOperandiArray.append(midtask.copy())
        midtask.clear()
    print(ArrayLists.ModusOperandiArray)


def Refill():
    newamount = 50  # ændre til hvor meget der kan være i the process robot
    for i in range(len(ArrayLists.arrayOfProc)):
        if ArrayLists.arrayAvailableBricks[i] < 5:
            print(ArrayLists.arrayOfProc[i], "Goes to refill")
            time.sleep(3) #Here it has to go refill
            ArrayLists.arrayAvailableBricks[i] = newamount
            print(ArrayLists.arrayOfProc[i], "has been refilled")


def ProdBotEat():
    for i in range(len(ArrayLists.arrayOfProd)):
        job = len(ArrayLists.arrayOfProc)
        order = ["Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete"]
        while job != 0:
            for j in range(len(ArrayLists.arrayOfBricks)):
                if ArrayLists.ModusOperandiArray[i][1+j*2] > 0:# and ArrayLists.State[j] == "Not Occupied" and order[j] == "Not Complete":
                    ArrayLists.State[j] = "Occupied"
                    ArrayLists.arrayOfInv[i] += ArrayLists.ModusOperandiArray[i][1+j*2]
                    newAmountAfterBrickGone = ArrayLists.arrayAvailableBricks[i] - ArrayLists.ModusOperandiArray[i][1+j*2]
                    ArrayLists.arrayAvailableBricks[i] = newAmountAfterBrickGone
                    #if ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] < 5:  # ændre til det antal bricks der skal til for en ordre
                     #   ArrayLists.arrayAvailableBricks[
                      #      ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] = newamount
                    #time.sleep(2) # This sleep illustrates the robots getting bricks from the individual Process Bots
                    job -= 1
                    ArrayLists.State[j] = "Not Occupied"
                    order[j] = "Complete"
        print(ArrayLists.arrayOfProd[i], "Going to station and dropping of bag with", ArrayLists.arrayOfInv[i])
        #Add movement to station
        time.sleep(5)
        print(ArrayLists.arrayOfProd[i], "Done")



