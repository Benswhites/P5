import ArrayLists
import random
import time

def AmountBricks():
    for i in range(len(ArrayLists.arrayOfProc)):
        color = random.choice(ArrayLists.arrayOfBricks)
        amount = random.choice(range(5, 50)) #ændre til hvor meget der kan være i en robot
        ArrayLists.arrayAvailableColor.append(color)
        ArrayLists.arrayAvailableBricks.append(amount)
    print(ArrayLists.arrayAvailableColor, ArrayLists.arrayAvailableBricks)


def ProdBotEat():
    job = len(ArrayLists.arrayOfProc)
    Order = ["Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete",]
    while job != 0:
        newamount = 50  # ændre til hvor meget der kan være i the process robot
        for i in range(len(ArrayLists.arrayOfProc)):
            prodTaskColor = random.choice(ArrayLists.arrayAvailableColor)
            if prodTaskColor == ArrayLists.arrayAvailableColor[0] and ArrayLists.State[0] == "Not Occupied" and Order[0] == "Not Complete":
                ArrayLists.State[0] = "Occupied"
                totalAmountOfColor0 = ArrayLists.arrayAvailableBricks[0]
                prodTaskHowManyOfColor0 = random.choice(range(0,5))
                newAmountAfterBrickGone0 = totalAmountOfColor0- prodTaskHowManyOfColor0
                ArrayLists.arrayAvailableBricks[0] = newAmountAfterBrickGone0
                if ArrayLists.arrayAvailableBricks[0] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[0] = newamount
                time.sleep(2)
                job -= 1
                ArrayLists.State[0] = "Not Occupied"
                Order[0] = "Complete"


            elif prodTaskColor == ArrayLists.arrayAvailableColor[1] and ArrayLists.State[1] == "Not Occupied" and Order[1] == "Not Complete":
                ArrayLists.State[1] = "Occupied"
                totalAmountOfColor1 = ArrayLists.arrayAvailableBricks[1]
                prodTaskHowManyOfColor1 = random.choice(range(0,5))
                newAmountAfterBrickGone1 = totalAmountOfColor1 - prodTaskHowManyOfColor1
                ArrayLists.arrayAvailableBricks[1] = newAmountAfterBrickGone1
                if ArrayLists.arrayAvailableBricks[1] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[1] = newamount
                time.sleep(2)
                job -= 1
                ArrayLists.State[1] = "Not Occupied"
                Order[1] = "Complete"

            elif prodTaskColor == ArrayLists.arrayAvailableColor[2] and ArrayLists.State[2] == "Not Occupied" and Order[2] == "Not Complete":
                ArrayLists.State[2] = "Occupied"
                totalAmountOfColor2= ArrayLists.arrayAvailableBricks[2]
                prodTaskHowManyOfColor2 = random.choice(range(0,5))
                newAmountAfterBrickGone2 = totalAmountOfColor2 - prodTaskHowManyOfColor2
                ArrayLists.arrayAvailableBricks[2] = newAmountAfterBrickGone2
                if ArrayLists.arrayAvailableBricks[2] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[2] = newamount
                time.sleep(2)
                job -= 1
                ArrayLists.State[2] = "Not Occupied"
                Order[2] = "Complete"

            elif prodTaskColor == ArrayLists.arrayAvailableColor[3]:
                if ArrayLists.State[3] == "Not Occupied":
                    if Order[3] == "Not Complete":
                        ArrayLists.State[3] = "Occupied"
                        totalAmountOfColor3 = ArrayLists.arrayAvailableBricks[3]
                        prodTaskHowManyOfColor3 = random.choice(range(0,5))
                        newAmountAfterBrickGone3 = totalAmountOfColor3 - prodTaskHowManyOfColor3
                        ArrayLists.arrayAvailableBricks[3] = newAmountAfterBrickGone3
                        if ArrayLists.arrayAvailableBricks[3] < 5: #ændre til det antal bricks der skal til for en ordre
                            ArrayLists.arrayAvailableBricks[3] = newamount
                        time.sleep(2)
                        job -= 1
                        ArrayLists.State[3] = "Not Occupied"
                        Order[3] = "Complete"

            elif prodTaskColor == ArrayLists.arrayAvailableColor[4] and ArrayLists.State[4] == "Not Occupied" and Order[4] == "Not Complete":
                ArrayLists.State[4] = "Occupied"
                totalAmountOfColor4 = ArrayLists.arrayAvailableBricks[4]
                prodTaskHowManyOfColor4 = random.choice(range(0,5))
                newAmountAfterBrickGone4 = totalAmountOfColor4 - prodTaskHowManyOfColor4
                ArrayLists.arrayAvailableBricks[4] = newAmountAfterBrickGone4
                if ArrayLists.arrayAvailableBricks[4] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[4] = newamount
                time.sleep(2)
                job -= 1
                ArrayLists.State[4] = "Not Occupied"
                Order[4] = "Complete"

            elif prodTaskColor == ArrayLists.arrayAvailableColor[5] and ArrayLists.State[5] == "Not Occupied" and Order[5] == "Not Complete":
                ArrayLists.State[5] = "Occupied"
                totalAmountOfColor5 = ArrayLists.arrayAvailableBricks[5]
                prodTaskHowManyOfColor5 = random.choice(range(0,5))
                newAmountAfterBrickGone5 = totalAmountOfColor5 - prodTaskHowManyOfColor5
                ArrayLists.arrayAvailableBricks[5] = newAmountAfterBrickGone5
                if ArrayLists.arrayAvailableBricks[5] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[5] = newamount
                time.sleep(2)
                job -= 1
                ArrayLists.State[5] = "Not Occupied"
                Order[5] = "Complete"

            elif prodTaskColor == ArrayLists.arrayAvailableColor[6] and ArrayLists.State[6] == "Not Occupied" and Order[6] == "Not Complete":
                ArrayLists.State[6] = "Occupied"
                totalAmountOfColor6 = ArrayLists.arrayAvailableBricks[6]
                prodTaskHowManyOfColor6 = random.choice(range(0,5))
                newAmountAfterBrickGone6 = totalAmountOfColor6 - prodTaskHowManyOfColor6
                ArrayLists.arrayAvailableBricks[6] = newAmountAfterBrickGone6
                if ArrayLists.arrayAvailableBricks[6] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[6] = newamount
                time.sleep(2)
                job -= 1
                ArrayLists.State[6] = "Not Occupied"
                Order[6] = "Complete"

    print("Process agents colors: ", ArrayLists.arrayAvailableColor, "Amount of bricks in each color:", ArrayLists.arrayAvailableBricks)

