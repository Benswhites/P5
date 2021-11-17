import tkinter as tk
import random

widthBase = 700
heightBase = 500

root = tk.Tk()

root.title('Fleet GUI')
root.geometry(str(widthBase)+'x'+str(heightBase))

canvas = tk.Canvas(root, height=widthBase, width=heightBase)
canvas.pack()
frame = tk.Frame(root, bg='#04050f')
frame.place(relwidth=1, relheight=1)

root.attributes('-fullscreen', False)

fakeOrders = [[[1,'Yellow'], [2,'Green']],
              [[3, 'Red'], [2, 'Blue']],
              [[4, 'Orange'],[1, 'Brown']]]

orderList = []

## ["Red", "Blue", "Yellow", "Brown", "Green", "Purple", "Orange"]
brick = [[0, 'Red'], [0, 'Blue'], [0, 'Yellow'], [0, 'Brown'], [0, 'Green'], [0, 'Purple'], [0,'Orange']]
labels = []

## SETTING VARIABLES ##
autoOrder = 0       # Decides if program sends single or multiple orders
autoGenerate = 0    # Decides if program creates orders automatically
autoAmount = 0      # Amount of orders to generate randomly


green = '#20c94e'

orderWindow = tk.Text(frame, exportselection=0, insertofftime=0, font=("Samsung Sharp Sans", 8, "bold"))
orderWindow.place(anchor='nw', x=210, y=230, width=480, height=230)


def addBrick(value, i):
    brick[i][0] += value
    if brick[i][0] == -1:
        brick[i][0] = 0

    root.update_idletasks()
    createButtons()

def plusAndMinus(i):
    button = tk.Button(frame, text="+", command=lambda: addBrick(+1, i), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 14, "bold"), bd=0)
    button.place(anchor='c', x=65, y=240 + i * 30, width=50, height=20)

    button = tk.Button(frame, text="-", command=lambda: addBrick(-1, i), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 14, "bold"), bd=0)
    button.place(anchor='c', x=165, y=240 + i * 30, width=50, height=20)

def goButton(orderType):
    if orderType == 1:
        txtGoButton = 'Add'
    elif orderType == 2:
        txtGoButton = 'Order'

    button = tk.Button(frame, text=txtGoButton, command=lambda: sendOrder(orderType), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    button.place(anchor='nw', x=10, y=440, width=90, height=20)

    button = tk.Button(frame, text='Reset', command=lambda: reset(), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    button.place(anchor='nw', x=100, y=440, width=90, height=20)

def rndButton():
    button = tk.Button(frame, text='Generate Orders', command=lambda: generateOrders(autoGenerate, 10), bg='white', fg='black',
                       font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    button.place(anchor='nw', x=10, y=170, width=180, height=20)

def generateOrders(state, amount):
    for k in range(amount):
        for i in range(len(brick)):
            brick[i][0] = random.randint(0,6)



        order = []
        for i in range(len(brick)):
            if brick[i][0] != 0:
                order.append(brick[i])

        order_str = str(order)
        order_str = order_str.replace('[', '')
        order_str = order_str.replace(']', '')

        orderWindow.configure(state="normal")
        orderWindow.insert(tk.END, '  ' + order_str + '\n')
        orderList.append(order)
        orderWindow.configure(state="disabled")
    reset()


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
        orderList.append(order)
        orderWindow.configure(state="disabled")

def reset():
    for i in range(len(brick)):
        brick[i][0] = 0
    root.update_idletasks()
    createButtons()

def createButtons():
    for label in labels:
        label.destroy()

    label = tk.Label(frame, bg='white', text='Select Brick Colors', fg='black',
                     font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    label.place(anchor='c', x=100, y=210, width=180, height=20)
    labels.append(label)

    label = tk.Label(frame, bg='white', text='Order List', fg='black',
                     font=("Samsung Sharp Sans", 12, "bold"), bd=0)
    label.place(anchor='nw', x=210, y=200, width=180, height=20)
    labels.append(label)

    for i in range(7):

        label = tk.Label(frame, text=str(brick[i][0]), bg='white', fg='black',
                         font=("Samsung Sharp Sans", 14, "bold"), bd=0)
        label.place(anchor='c', x=115, y=240+i*30, width=50, height=20)
        labels.append(label)

        label = tk.Label(frame, bg=brick[i][1])
        label.place(anchor='c', x=20, y=240+i*30, width=20, height=20)
        labels.append(label)

        plusAndMinus(i)

    goButton(1)
    rndButton()

while True:
    createButtons()

    root.mainloop()

