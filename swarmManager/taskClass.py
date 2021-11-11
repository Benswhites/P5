import ArrayLists
import random
import time


def AmountBricks():
    colors = random.sample(ArrayLists.arrayOfBricks, len(ArrayLists.arrayOfProc))
    for i in range(len(ArrayLists.arrayOfProc)):
        color = colors[i]
        amount = random.choice(range(5, 50)) #ændre til hvor meget der kan være i en robot
        ArrayLists.arrayAvailableColor.append(color)
        ArrayLists.arrayAvailableBricks.append(amount)
    print(ArrayLists.arrayAvailableColor, ArrayLists.arrayAvailableBricks)


def ProdBotEat(Inv):
    job = len(ArrayLists.arrayOfProc)
    order = ["Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete",]
    while job != 0:
        newamount = 50  # ændre til hvor meget der kan være i the process robot
        for i in range(len(ArrayLists.arrayOfProc)):
            prodTaskColor = random.choice(ArrayLists.arrayAvailableColor)
            for j in range(len(ArrayLists.arrayOfBricks)):
                if prodTaskColor == ArrayLists.arrayOfBricks[j] and ArrayLists.State[j] == "Not Occupied" and order[j] == "Not Complete":
                    ArrayLists.State[j] = "Occupied"
                    totalAmountOfColor = ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])]
                    prodTaskHowManyOfColor = random.choice(range(0,5))
                    ArrayLists.arrayOfInv[Inv] += prodTaskHowManyOfColor
                    newAmountAfterBrickGone = totalAmountOfColor - prodTaskHowManyOfColor
                    ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] = newAmountAfterBrickGone
                    if ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] < 5: #ændre til det antal bricks der skal til for en ordre
                        ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] = newamount
                    time.sleep(2)
                    job -= 1
                    ArrayLists.State[j] = "Not Occupied"
                    order[j] = "Complete"
    if ArrayLists.PrintPeen[0] == 0:
        print("Process agents colors: ", ArrayLists.arrayAvailableColor, "Amount of bricks in each color:", ArrayLists.arrayAvailableBricks, "\n")
        ArrayLists.PrintPeen[0] = 1

    time.sleep(5)
    fin = 1
    while fin != 0:
        if ArrayLists.arrayOfInv[Inv] > 7 and ArrayLists.BagState[1] == "Not Occupied":
            ArrayLists.BagState[1] = "Occupied"
            time.sleep(2)
            print("A big bag has been produced with", ArrayLists.arrayOfInv[Inv], "bricks\n")
            ArrayLists.BagState[1] = "Not Occupied"
            fin -= 1
        if ArrayLists.arrayOfInv[Inv] < 8 and ArrayLists.BagState[0] == "Not Occupied":
            ArrayLists.BagState[0] = "Occupied"
            time.sleep(2)
            print("A small bag has been produced with", ArrayLists.arrayOfInv[Inv], "bricks\n")
            ArrayLists.BagState[0] = "Not Occupied"
            fin -= 1