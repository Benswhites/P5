import ArrayLists
import random

def AmountBricks():
    global color
    global amount
    global procBotContents
    for i in range(len(ArrayLists.arrayOfProc)):
        color = random.choice(ArrayLists.arrayOfBricks)
        amount = random.choice(range(5, 50)) #ændre til hvor meget der kan være i en robot
        ArrayLists.arrayAvailableColor.append(color)
        ArrayLists.arrayAvailableBricks.append(amount)
    print(ArrayLists.arrayAvailableColor, ArrayLists.arrayAvailableBricks)

    for i in range(len(ArrayLists.arrayOfProd)):
        newamount = 50  # ændre til hvor meget der kan være i the process robot
        for i in range(len(ArrayLists.arrayOfProc)):
            prodTaskColor = random.choice(ArrayLists.arrayAvailableColor)
            if prodTaskColor == ArrayLists.arrayAvailableColor[0]:
                totalAmountOfColor0 = ArrayLists.arrayAvailableBricks[0]
                prodTaskHowManyOfColor0 = random.choice(range(0,5))
                newAmountAfterBrickGone0 = totalAmountOfColor0- prodTaskHowManyOfColor0
                ArrayLists.arrayAvailableBricks[0] = newAmountAfterBrickGone0
                if ArrayLists.arrayAvailableBricks[0] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[0] = newamount

            elif prodTaskColor == ArrayLists.arrayAvailableColor[1]:
                totalAmountOfColor1 = ArrayLists.arrayAvailableBricks[1]
                prodTaskHowManyOfColor1 = random.choice(range(0,5))
                newAmountAfterBrickGone1 = totalAmountOfColor1 - prodTaskHowManyOfColor1
                ArrayLists.arrayAvailableBricks[1] = newAmountAfterBrickGone1
                if ArrayLists.arrayAvailableBricks[1] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[1] = newamount

            elif prodTaskColor == ArrayLists.arrayAvailableColor[2]:
                totalAmountOfColor2= ArrayLists.arrayAvailableBricks[2]
                prodTaskHowManyOfColor2 = random.choice(range(0,5))
                newAmountAfterBrickGone2 = totalAmountOfColor2 - prodTaskHowManyOfColor2
                ArrayLists.arrayAvailableBricks[2] = newAmountAfterBrickGone2
                if ArrayLists.arrayAvailableBricks[2] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[2] = newamount

            elif prodTaskColor == ArrayLists.arrayAvailableColor[3]:
                totalAmountOfColor3 = ArrayLists.arrayAvailableBricks[3]
                prodTaskHowManyOfColor3 = random.choice(range(0,5))
                newAmountAfterBrickGone3 = totalAmountOfColor3 - prodTaskHowManyOfColor3
                ArrayLists.arrayAvailableBricks[3] = newAmountAfterBrickGone3
                if ArrayLists.arrayAvailableBricks[3] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[3] = newamount

            elif prodTaskColor == ArrayLists.arrayAvailableColor[4]:
                totalAmountOfColor4 = ArrayLists.arrayAvailableBricks[4]
                prodTaskHowManyOfColor4 = random.choice(range(0,5))
                newAmountAfterBrickGone4 = totalAmountOfColor4 - prodTaskHowManyOfColor4
                ArrayLists.arrayAvailableBricks[4] = newAmountAfterBrickGone4
                if ArrayLists.arrayAvailableBricks[4] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[4] = newamount

            elif prodTaskColor == ArrayLists.arrayAvailableColor[5]:
                totalAmountOfColor5 = ArrayLists.arrayAvailableBricks[5]
                prodTaskHowManyOfColor5 = random.choice(range(0,5))
                newAmountAfterBrickGone5 = totalAmountOfColor5 - prodTaskHowManyOfColor5
                ArrayLists.arrayAvailableBricks[5] = newAmountAfterBrickGone5
                if ArrayLists.arrayAvailableBricks[5] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[5] = newamount

            elif prodTaskColor == ArrayLists.arrayAvailableColor[6]:
                totalAmountOfColor6 = ArrayLists.arrayAvailableBricks[6]
                prodTaskHowManyOfColor6 = random.choice(range(0,5))
                newAmountAfterBrickGone6 = totalAmountOfColor6 - prodTaskHowManyOfColor6
                ArrayLists.arrayAvailableBricks[6] = newAmountAfterBrickGone6
                if ArrayLists.arrayAvailableBricks[6] < 5: #ændre til det antal bricks der skal til for en ordre
                    ArrayLists.arrayAvailableBricks[6] = newamount

        print("Process agents colors: ", ArrayLists.arrayAvailableColor, "Amount of bricks in each color:", ArrayLists.arrayAvailableBricks)