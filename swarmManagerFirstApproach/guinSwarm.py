import random
import tkinter as tk
import math
import ArrayLists
import swarmClass
import taskClass
from copy import deepcopy
import time as t
import threading

# Change this, if you want more robots.
# NOTE ONLY 7 PROCESSBOTS IS ALLOWED
productBots = 10 # These robots handle the products (eg. Bricks)
processBots = 7 # These robots contain the products (eg. Bricks)

# Variables. Dont touch
orderInfo = []
orderState = []

botID = 0
botTask = ''
botState = 0

# Pickerbots info
orderInfo.append(botID)         # The ID of the robot:    An integer defining the robot.
orderInfo.append(botTask)       # The task of the robot:  One could say the destination. 0-7 == colors. 8 == dropzone
orderInfo.append(botState)      # The state of the robot: 0 == inactive, 1 == pickup, 2 == dropoff

for i in range(productBots):
    orderState.append(orderInfo)

# FDP - Means; For Debugging Purposes
#print(orderState)

# Cooperation with ROS
swarmClass.CreateProductBot(productBots)
swarmClass.CreateProcessBot(processBots)
#swarmClass.MakeBotLaunch()
taskClass.AmountBricks()


widthBase = 600
heightBase = 300

gui = tk.Tk()

gui.title('Fleet GUI')
gui.geometry(str(widthBase)+'x'+str(heightBase))

canvas = tk.Canvas(gui, height=widthBase, width=heightBase)
canvas.pack()
guiFrame = tk.Frame(gui, bg='#04050f')
guiFrame.place(relwidth=1, relheight=1)

gui.attributes('-fullscreen', False)

orderList = []

## ["Red", "Blue", "Yellow", "Brown", "Green", "Purple", "Orange"]
inventory = ArrayLists.arrayAvailableBricks
brick = [[0, 'Red'], [0, 'Blue'], [0, 'Yellow'], [0, 'Brown'], [0, 'Green'], [0, 'Cyan'], [0,'Orange']]

#print(inventory)

labels = []

## SETTING VARIABLES ##
autoOrder = 0       # Decides if program sends single or multiple orders
autoGenerate = 0    # Decides if program creates orders automatically
autoAmount = 0      # Amount of orders to generate randomly


green = '#20c94e'

orderWindow = tk.Text(guiFrame, exportselection=0, insertofftime=0, font=("Samsung Sharp Sans", 8, "bold"))
orderWindow.place(anchor='nw', x=210, y=40, width=380, height=230)



widthBase = 1920
heightBase = 1080

root = tk.Tk()

root.title('Fleet Visualizer')
root.geometry('1920x1080')

canvas = tk.Canvas(root, height=widthBase, width=heightBase)
canvas.pack()
frame = tk.Frame(root, bg='#04050f')
frame.place(relwidth=1, relheight=1)

root.attributes('-fullscreen', False)

bricks = ArrayLists.arrayAvailableColor

pickers = ArrayLists.arrayOfProd

object = bricks + pickers

bagSample1 = []

#for i in range(random.randint(1,processBots)):
    #bagSample1.append([(random.randint(1,6),ArrayLists.arrayAvailableColor[i])])

# Spawn Deploy-Robot positions at random locations
def spawnDeploy():
    for i in range(len(bricks)):
        bricks[i] = [str(bricks[i]), round(random.uniform(100,widthBase-100),1), round(random.uniform(100,heightBase-100),1)]

    for i in range(len(pickers)):
        pickers[i] = [str(pickers[i]), round(random.uniform(100, widthBase-100), 1), round(random.uniform(100, heightBase-100), 1)]

# Create Deploy-Robots and Picker-bots in view
def positionDeploy(labels, bricks, pickers):

    for i in range(len(bricks)):
        label = tk.Label(frame, bg=bricks[i][0], text=str(inventory[i]))
        label.place(anchor='c', x=round(bricks[i][1]), y=round(bricks[i][2]), width=20, height=20)
        labels.append(label)


    for i in range(len(pickers)):
        label = tk.Label(frame, bg='white')
        label.place(anchor='c', x=round(pickers[i][1]), y=round(pickers[i][2]), width=10, height=10)
        labels.append(label)

    return labels

deploy = [0,0,0,0]
refill = [0,0,0,0]
# Create Deploy-Station for product delivery and process refill
def crtDeployStation(labels, orderstate):

    label = tk.Label(frame, bg='white', text='Deploy', font=("Samsung Sharp Sans", 13, "bold"))
    label.place(anchor='c', x=widthBase - 50, y=heightBase / 2, width=100, height=400)
    labels.append(label)

    label = tk.Label(frame, bg='white', text='Refill', font=("Samsung Sharp Sans", 13, "bold"))
    label.place(anchor='c', x=50, y=heightBase / 2, width=100, height=400)
    labels.append(label)

    # We want 4 sub-stations at each station.
    # These are for refilling and dropoffs

    for i in range(len(deploy)):

        if deploy[i] == 1:
            txt = 'OCP'
            col = '#db2e3c'
            label = tk.Label(frame, bg=col)
            label.place(anchor='c', x=widthBase - 75 - 35, y=heightBase / 2 - 325 / 2 + (325 / 3) * i - 16, width=20, height=18)
            labels.append(label)
            label = tk.Label(frame, bg=col)
            label.place(anchor='c', x=widthBase - 75 - 35, y=heightBase / 2 - 325 / 2 + (325 / 3) * i + 16, width=20, height=18)
            labels.append(label)
        else:
            txt = 'AVAIL'
            col = '#20c94e'


        label = tk.Label(frame, bg=col, fg='white', text=txt, font=("Samsung Sharp Sans", 9, "bold"))
        label.place(anchor='c', x=widthBase - 75, y=heightBase/2-325/2+(325/3)*i, width=50, height=50)
        labels.append(label)

    for i in range(len(refill)):

        if refill[i] == 1:
            txt = 'OCP'
            col = '#d19a2c'
            label = tk.Label(frame, bg=col)
            label.place(anchor='c', x=75 + 35, y=heightBase / 2 - 325 / 2 + (325 / 3) * i - 20, width=20, height=10)
            labels.append(label)
            label = tk.Label(frame, bg=col)
            label.place(anchor='c', x=75 + 35, y=heightBase / 2 - 325 / 2 + (325 / 3) * i + 20, width=20, height=10)
            labels.append(label)
        else:
            txt = 'AVAIL'
            col = '#20c94e'


        label = tk.Label(frame, bg=col, fg='white', text=txt, font=("Samsung Sharp Sans", 9, "bold"))
        label.place(anchor='c', x=75, y=heightBase/2-325/2+(325/3)*i, width=50, height=50)
        labels.append(label)

    return labels

# Calculate distance between bots
def checkDistance(p, p1):

    x1 = p[0]
    y1 = p[1]
    x2 = p1[0]
    y2 = p1[1]

    result = round((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)

    if result <= 100:
        return True
    else:
        return False

# Calculate direction to nearest bot
def checkDirection(targetCoord, robotCoord):
    xDist = targetCoord[0] - robotCoord[0]
    yDist = targetCoord[1] - robotCoord[1]

    dir = math.degrees(math.atan2(yDist, xDist))

    return dir

# Move bot away in direction
def moveBotinDir(direction, object, i):
    k = 0.5
    object[i][1] += math.cos(math.radians(direction)) * k
    object[i][2] += math.sin(math.radians(direction)) * k

# Do the above
def obstacleSafety(labels, object):
    object
    safetyDist = 25

    for i in range(len(object)):
        X = object[i][1]
        Y = object[i][2]

        for j in range(len(object)):
            if j != i:
                x = object[j][1] # X coordinate could round
                y = object[j][2] # Y coordinate

                txt = "The robot is too close? {} . Color is {}"
                result = checkDistance((x,y), (X,Y))
                if result == True:
                    #print(txt.format(result, str(object[j][0])))
                    moveBotinDir(checkDirection((X,Y),(x,y)), object, i)
    return object

def createProcedure(product):

    procedure = []

    #test = len(product)
    #test = list(product[0][0])[1]

    totalBricks = 0
    for i in range(len(product)):
        procedure.append(list(product[i][0])[1])
        totalBricks += list(product[i][0])[0]
    #print(str(procedure) + " " + str(totalBricks))

    '''if totalBricks >= 3:
        procedure.insert(0,'Large')
    else:
        procedure.insert(0,'Small')'''

    return procedure

def moveToGoal(robot, robotCoord, targetCoord):
    k = 3
    xDist = targetCoord[0] - robotCoord[robot][1]
    yDist = targetCoord[1] - robotCoord[robot][2]

    robotCoord[robot][1] += math.cos(math.radians(math.degrees(math.atan2(yDist, xDist)))) * k
    robotCoord[robot][2] += math.sin(math.radians(math.degrees(math.atan2(yDist, xDist)))) * k

def swarmPlacement(procedure, object):
    target = []
    for i in range(len(procedure)):

        target.append((widthBase/2+i*20,heightBase/2))

        search = str(procedure[i])
        j = 0
        for sublists in object:
            if search in sublists:
                moveToGoal(j, object, target[i])
                #movePicker(target[i][0], target[i][1], j)
            j += 1

    #for i in range(len(pickers)):
    return

def movePickerinDir(direction, object, i):
    k = 2
    object[i][1] += round(math.cos(math.radians(direction)) * k,1)
    object[i][2] += round(math.sin(math.radians(direction)) * k,1)

def dirPicker(targetCoord, robotCoord):
    xDist = round(targetCoord[0] - robotCoord[0], 1)
    yDist = round(targetCoord[1] - robotCoord[1], 1)

    dir = round(math.degrees(math.atan2(yDist, xDist)),2)


    return dir

def movePicker(x,y,i):
    movePickerinDir(dirPicker((x, y), ((pickers[i][1]), pickers[i][2])), pickers, i)

    xDist = x - pickers[i][1]
    yDist = y - pickers[i][2]

    #txt = "{} for Picker {} is in proximity"
    if -2 <= xDist <= 2 and -2 <= yDist <= 2:
        #print(txt.format("X and Y", i))
        return True
    else:
        return False

def pickerManagement(procedure):

    return

### ABOVE

def addBrick(value, i):
    brick[i][0] += value
    if brick[i][0] == -1:
        brick[i][0] = 0

    #createButtons()

def plusAndMinus(i):
    button = tk.Button(guiFrame, text="+", command=lambda: addBrick(+1, i), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 14, "bold"), bd=0)
    button.place(anchor='c', x=65, y=50 + i * 30, width=50, height=20)

    button = tk.Button(guiFrame, text="-", command=lambda: addBrick(-1, i), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 14, "bold"), bd=0)
    button.place(anchor='c', x=165, y=50 + i * 30, width=50, height=20)

for i in range(7):
    plusAndMinus(i)

def goButton(orderType):

    if orderType == 1:
        txtGoButton = 'Add'
    elif orderType == 2:
        txtGoButton = 'Order'

    button = tk.Button(guiFrame, text=txtGoButton, command=lambda: sendOrder(orderType), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    button.place(anchor='nw', x=10, y=250, width=90, height=20)

    button = tk.Button(guiFrame, text='Reset', command=lambda: reset(), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    button.place(anchor='nw', x=100, y=250, width=90, height=20)

def rndButton():

    button = tk.Button(guiFrame, text='Generate Orders', command=lambda: generateOrders(autoGenerate, 10), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    button.place(anchor='nw', x=410, y=10, width=180, height=20)

rndButton()
goButton(1)

def generateOrders(state, amount):
    for k in range(amount):
        for i in range(len(brick)):
            brick[i][0] = random.randint(0,10)
        sendOrder(2)

def sendOrder(orderType):
    order = []
    k = 0
    for i in range(len(brick)):
        if brick[i][0] != 0:
            order.append(brick[i])
            k += 1

    order_str = str(order)
    order_str = order_str.replace('[', '')
    order_str = order_str.replace(']', '')

    if k != 0:
        orderWindow.configure(state="normal")
        orderWindow.insert(tk.END, '  '+ order_str + '\n')

        copyList = deepcopy(order)
        orderList.append(copyList)
        orderWindow.configure(state="disabled")

    reset()
    print(orderList)

def reset():
    for i in range(len(brick)):
        brick[i][0] = 0
    createButtons()

def createButtons():


    label = tk.Label(guiFrame, bg='white', text='Select Brick Colors', fg='black',
                     font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    label.place(anchor='c', x=100, y=20, width=180, height=20)
    labels.append(label)

    label = tk.Label(guiFrame, bg='white', text='Order List', fg='black',
                     font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    label.place(anchor='nw', x=210, y=10, width=180, height=20)
    labels.append(label)


    for i in range(7):

        label = tk.Label(guiFrame, text=str(brick[i][0]), bg='white', fg='black',
                         font=("Samsung Sharp Sans", 14, "bold"), bd=0)
        label.place(anchor='c', x=115, y=50+i*30, width=40, height=20)
        labels.append(label)

        label = tk.Label(guiFrame, bg=brick[i][1], text=str(inventory[i]))
        label.place(anchor='c', x=20, y=50+i*30, width=20, height=20)
        labels.append(label)

### BELOW

def ProdBotEat():
    job = len(bagSample1)
    order = ["Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete", "Not Complete",
             "Not Complete", ]
    while job != 0:
        newamount = 50  # ændre til hvor meget der kan være i the process robot
        for i in range(productBots):
            for j in range(len(bagSample1)):
                if int(list(bagSample1[j][0])[0]) > 0 and ArrayLists.State[j] == "Not Occupied" and order[j] == "Not Complete":
                    ArrayLists.State[j] = "Occupied"
                    u = getPosfromColor(str(list(bagSample1[j][0])[1]))

                    x1 = u[0]
                    y1= u[1]
                    movePicker(x1, y1, i)

                    #totalAmountOfColor = ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])]
                    #prodTaskHowManyOfColor = bagSample1[i][0][0]
                    #ArrayLists.arrayOfInv[i] += prodTaskHowManyOfColor
                    #newAmountAfterBrickGone = totalAmountOfColor - prodTaskHowManyOfColor
                    #ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] = newAmountAfterBrickGone
                    #if ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] < 5:  # ændre til det antal bricks der skal til for en ordre
                    #    ArrayLists.arrayAvailableBricks[ArrayLists.arrayAvailableColor.index(ArrayLists.arrayOfBricks[j])] = newamount
                    job -= 1
                    ArrayLists.State[j] = "Not Occupied"
                    order[j] = "Complete"

def getPosfromColor(color):
    object = pickers + bricks
    search = str(color)
    j = 0
    pos = []
    for sublists in object:
        if search in sublists:
            pos.append(object[j][1])
            pos.append(object[j][2])
            # movePicker(target[i][0], target[i][1], j)
        j += 1
    return pos

def cannopy(state,k,exceptID):
    angle = 0
    l = 100

    x = 1920 / 2
    y = 1080 / 2
    for i in range(processBots):
        angle = i * (360/processBots)

        x = 960 + math.cos(math.radians(angle))*l
        y = 540 + math.sin(math.radians(angle))*l

        target = [x,y]

        moveToGoal(i, bricks,target)

    l = 200
    for i in range(productBots):
        if i != exceptID:
            angle = i * (360/productBots) - k

            x = 960 + math.cos(math.radians(angle))*l
            y = 540 + math.sin(math.radians(angle))*l

            target = [x,y]

            movePicker(x, y, i)

    k = k + 0.2
    if k == 360:
        k = 0
    return k


occupation = []
for i in range(productBots):
    occupation.append('Not Occupied')

pickup = []
for i in range(productBots):
    pickup.append('Not Occupied')

deployment = []
for i in range(productBots):
    deployment.append(['False', 0])

cVal = [6,6,6,6,6,6,6,6,6,6]
pick = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]



def givePickerOrder(i, k):
    # Check if Picker is occupied. If not, move on

    completion = ["Complete", "Complete", "Complete", "Complete", "Complete", "Complete", "Complete"]
    if i in completedList:
        return
    for t in range(len(orderList[i])):
        completion[t] = 'Not Complete'

    k = pick[i]

    if occupation[i] == 'Not Occupied':
        occupation[i] = 'Occupied'
        pick[i] = i



    if completion[cVal[i]] == 'Not Complete' and occupation[i] == 'Occupied' and pickup[i] == 'Not Occupied':
        x ,y = getPosfromColor(orderList[i][cVal[i]][1])
        if movePicker(x, y, k):
            completion[cVal[i]] = 'Complete'
            #print(cVal)
            #print("Order Completed")
            #list(orderList[i]).pop
            ind = brickIndex.index(orderList[i][cVal[i]][1])
            inventory[ind] -= orderList[i][cVal[i]][0]
            if inventory[ind] <= 0:
                print(str('Brick inventory for ') + str(orderList[i][cVal[i]][1]) + str(' needs refilling'))


                ## To do -> Add some sort of ignore mode

            ### Take from inventory of productbots
            #print(list(orderList[i]))

            if cVal[i] == 0:
                print(str('Picker #') + str(i) + str(" is ready for Deploying"))
                deployment[i][0] = 'True'
                kVal = 1
                for t in range(len(deployment)):
                    if deployment[t][1] == 1:
                        kVal += 1
                    elif deployment[t][1] == 2:
                        kVal += 1
                    elif deployment[t][1] == 3:
                        kVal += 1
                    elif deployment[t][1] == 4:
                        kVal += 1
                deployment[i][1] = kVal
                #print(deployment[i][1])
                pickup[i] = 'Done'
    #print(completion)

    if completion[cVal[i]] == 'Complete' and occupation[i] == 'Occupied' and pickup[i] == 'Not Occupied':
        if cVal[i] >= 1:
            cVal[i] -= 1

    if deployment[i][0] == 'True' and occupation[i] == 'Occupied' and pickup[i] == 'Done':
        ## SELECT DEPLOY STATION HERE
        xCoord = xDeploy
        yCoord = yDeploy1

        if deployment[i][1] >= 5:
            movePicker(xCoord-200, 1080/2, k)


        if deployment[i][1] == 1:
            deploy[0] = 1
            yCoord = yDeploy1
            if movePicker(xCoord, yCoord, k):
                orderList.pop(i)
                occupation[i] = 'Not Occupied'
                deployment[i][0] = 'False'
                pickup[i] = 'Not Occupied'
                deploy[0] = 0
                cVal[i] = 6
                deployment[i][1] = 0
                completedList.append(i)
                p = -1
                pick[i] = -1
                return p
        elif deployment[i][1] == 2:
            deploy[1] = 1
            yCoord = yDeploy2
            if movePicker(xCoord, yCoord, k):
                orderList.pop(i)
                occupation[i] = 'Not Occupied'
                deployment[i][0] = 'False'
                pickup[i] = 'Not Occupied'
                deploy[1] = 0
                cVal[i] = 6
                deployment[i][1] = 0
                completedList.append(i)
                p = -1
                pick[i] = -1
                return p
        elif deployment[i][1] == 3:
            deploy[2] = 1
            yCoord= yDeploy3
            if movePicker(xCoord, yCoord, k):
                orderList.pop(1)
                occupation[i] = 'Not Occupied'
                deployment[i][0] = 'False'
                pickup[i] = 'Not Occupied'
                deploy[2] = 0
                cVal[i] = 6
                deployment[i][1] = 0
                completedList.append(i)
                p = -1
                pick[i] = -1
                return p
        elif deployment[i][1] == 4:
            deploy[3] = 1
            yCoord = yDeploy4
            if movePicker(xCoord, yCoord, k):
                orderList.pop(1)
                occupation[i] = 'Not Occupied'
                deployment[i][0] = 'False'
                pickup[i] = 'Not Occupied'
                deploy[3] = 0
                cVal[i] = 6
                deployment[i][1] = 0
                p = -1
                pick[i] = -1
                return p
    else:
        return

# Waiting pos:
x1 = widthBase-200
y1 = heightBase/2 + 50

# Deploy pos:
xDeploy = widthBase - 110
yDeploy1 = heightBase / 2 - 325 / 2 + (325 / 3) * 0
yDeploy2 = heightBase / 2 - 325 / 2 + (325 / 3) * 1
yDeploy3 = heightBase / 2 - 325 / 2 + (325 / 3) * 2
yDeploy4 = heightBase / 2 - 325 / 2 + (325 / 3) * 3

def movePickerToDeploy(i):
    if deploy[0] == 0:
        deploy[0] = 1
        global yP
        yP = yDeploy1
        global xP
        xP = xDeploy
        #movePicker(xDeploy, yP, i)

    if movePicker(xDeploy, yP, i) and deploy[0] == 1:
        deployment[i][0] = 'False'
        deploy[0] = 0


spawnDeploy()
print(bricks)

## Processkrav
# 1. Deploybots kan ikke overlevere items
# 2. Items skal overleveres af Pickerbots
# 3. Items skal i bags
# 4. Small bag <= 2 < Large bag
# 5. Securitydistance på radius 20 pixels omkring robotterne
# 6. Products skal leveres til deploystation


brickIndex = ['Red', 'Blue', 'Yellow', 'Brown', 'Green', 'Cyan', 'Orange']


k = 0
state = 0
wait = 1

#orderList = [[[1, 'Green'], [1, 'Orange']]]

while True:

    labels = []

    createButtons()

    positionDeploy(labels, bricks, pickers)

    crtDeployStation(labels,2)

    ## Obstacle / Safety Avoidance
    procedure = createProcedure(orderList)

    troels = obstacleSafety(labels,bricks)
    #tonny = obstacleSafety(labels,pickers)

    #swarmPlacement(procedure,troels)
    p = 0

    ## WAITING STATE
    if len(orderList) == 0:
        k = cannopy(state, k, -1)
    elif len(orderList) <= 10:
        completedList = []
        for i in range(len(orderList)):
            print(pick)

            p = givePickerOrder(i, p)
            if p == -1:
                print("Hello")
                break
    else:
        for i in range(10):
            p = givePickerOrder(i, p)
            if p == -1:
                print("Hello")
                break

            #k = cannopy(state, k, i)

    # Add functionality for max 10 orders at a time. Wait for order 11 eg.

    #print(ArrayLists.arrayAvailableColor)

    #for i in range(len(procedure)):


    root.update()
    gui.update()

    root.bind('<Escape>', lambda e: root.destroy())
    gui.bind('<Escape>', lambda e: root.destroy())

    for label in labels:
        label.destroy()
