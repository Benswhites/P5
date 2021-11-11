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


def ProdBotEat():
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
                    newAmountAfterBrickGone = totalAmountOfColor - prodTaskHowManyOfColor
                    ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] = newAmountAfterBrickGone
                    if ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] < 5: #ændre til det antal bricks der skal til for en ordre
                        ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] = newamount
                    time.sleep(2)
                    job -= 1
                    ArrayLists.State[j] = "Not Occupied"
                    order[j] = "Complete"

    print("Process agents colors: ", ArrayLists.arrayAvailableColor, "Amount of bricks in each color:", ArrayLists.arrayAvailableBricks)

