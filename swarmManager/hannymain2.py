import random
import tkinter as tk
import math
import ArrayLists
import swarmClass
import taskClass
import time as t
import threading

productBots = 20
processBots = 7

swarmClass.CreateProductBot(productBots)

swarmClass.CreateProcessBot(processBots)

#swarmClass.MakeBotLaunch()

taskClass.AmountBricks()

widthBase = 1920
heightBase = 1080

root = tk.Tk()

root.title('Fleet Visualizer')
root.geometry('1920x1080')

canvas = tk.Canvas(root, height=widthBase, width=heightBase)
canvas.pack()
frame = tk.Frame(root, bg='#04050f')
frame.place(relwidth=1, relheight=1)

bricks = ArrayLists.arrayAvailableColor

bags = \
    ['Small', 'Large']

pickers = ArrayLists.arrayOfProd


bagSample1 = []
for i in range(random.randint(1,processBots)):
    bagSample1.append([(random.randint(1,6),ArrayLists.arrayAvailableColor[random.randint(0,processBots-1)])])

print(bagSample1)


# Spawn Deploy-Robot positions at random locations
def spawnDeploy():
    for i in range(len(bricks)):
        bricks[i] = [str(bricks[i]), round(random.uniform(100,widthBase-100),1), round(random.uniform(100,heightBase-100),1)]
    for i in range(len(bags)):
        bags[i] = [str(bags[i]), round(random.uniform(100, widthBase-100), 1), round(random.uniform(100, heightBase-100), 1)]
    for i in range(len(pickers)):
        pickers[i] = [str(pickers[i]), round(random.uniform(100, widthBase-100), 1), round(random.uniform(100, heightBase-100), 1)]

# Create Deploy-Robots and Picker-bots in view
def positionDeploy(labels, bricks, bags, pickers):

    for i in range(len(bricks)):
        label = tk.Label(frame, bg=bricks[i][0])
        label.place(anchor='c', x=bricks[i][1], y=bricks[i][2], width=20, height=20)
        labels.append(label)

    for i in range(len(bags)):
        label = tk.Label(frame, bg='grey', text=bags[i][0])
        label.place(anchor='c', x=bags[i][1], y=bags[i][2], width=40, height=30)
        labels.append(label)

    for i in range(len(pickers)):
        label = tk.Label(frame, bg='white')
        label.place(anchor='c', x=pickers[i][1], y=pickers[i][2], width=10, height=10)
        labels.append(label)

    return labels

# Create Deploy-Station for product delivery
def crtDeployStation(labels):
    label = tk.Label(frame, bg='white', text='Deploy')
    label.place(anchor='c', x=widthBase-50, y=heightBase/2, width=100, height=400)
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
    k = 0.15
    object[i][1] += math.cos(math.radians(direction)) * k
    object[i][2] += math.sin(math.radians(direction)) * k

# Do the above
def obstacleSafety(labels, object1, object2):
    object = object1 + object2
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
    product[0].sort(reverse=True)

    procedure = []

    test = len(product)
    test = list(product[0][0])[1]

    totalBricks = 0
    for i in range(len(product)):
        procedure.append(list(product[i][0])[1])
        totalBricks += list(product[i][0])[0]
    #print(str(procedure) + " " + str(totalBricks))

    if totalBricks >= 3:
        procedure.insert(0,'Large')
    else:
        procedure.insert(0,'Small')

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

        target.append((widthBase-125-(i*50),heightBase/2))

        search = str(procedure[i])
        j = 0
        for sublists in object:
            if search in sublists:
                moveToGoal(j, object, target[i])
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
    if -1 <= xDist <= 1 and -1 <= yDist <= 1:
        #print(txt.format("X and Y", i))
        return True
    else:
        return False


def pickerManagement(procedure):

    return



spawnDeploy()
print(bricks)

## Processkrav
# 1. Deploybots kan ikke overlevere items
# 2. Items skal overleveres af Pickerbots
# 3. Items skal i bags
# 4. Small bag <= 2 < Large bag
# 5. Securitydistance på radius 20 pixels omkring robotterne
# 6. Products skal leveres til deploystation


# Waiting pos:
x1 = widthBase-100
y1 = heightBase/2 + 50

k = 0

while True:
    labels = []

    positionDeploy(labels, bricks, bags, pickers)



    crtDeployStation(labels)

    ## Obstacle / Safety Avoidance
    procedure = createProcedure(bagSample1)

    troels = obstacleSafety(labels,bricks,bags)
    #k += 1
    #print(k)

    swarmPlacement(procedure,troels)


    pickerManagement(procedure)

    for i in range(productBots):
        movePicker(x1-(i*25), y1, i)


    root.update()

    for label in labels:
        label.destroy()
