import time
import tkinter
from tkinter import ttk
import testfleet
import threading
import testymctestface

but_set = []
lab_set = []
name_set = []
check_num = 0
p = 5
Options = [
    "Pick desired order"
]

root = tkinter.Tk()
root.geometry('1000x700')
root.resizable(False, False)
root.title('Fleet handler')


def graphic_activation():
    wall1 = tkinter.Label(root, bg='black')
    wall1.place(anchor='nw', x=300, y=1, width=5, height=700)

    build_label1 = tkinter.Label(root, text='Desired ships')
    build_label1.place(x=1, y=1)
    build_entry1 = tkinter.Entry(root)
    build_entry1.place(x=113, y=3, width=20, height=20)
    build_button = ttk.Button(root, text='build', command=lambda: shipbuilder(int(build_entry1.get())))
    build_button.pack(ipadx=5, ipady=5, expand=True)
    build_button.place(x=139, y=1)
    button_button = ttk.Button(root, text='Break', command=lambda: download())
    button_button.pack(ipadx=5, ipady=5, expand=True)
    button_button.place(x=219, y=1)

    order_button = ttk.Button(root, text='Crate new set', command=lambda: new_order(order_menu, variable))
    order_button.pack(ipadx=5, ipady=5, expand=True)
    order_button.place(x=310, y=1)
    variable = tkinter.StringVar(root)
    variable.set(Options[0])
    order_menu = tkinter.OptionMenu(root, variable, *Options)
    order_menu.place(x=394, y=0)
    order_entry = tkinter.Entry(root)
    order_entry.place(x=535, y=3, width=25, height=25)
    order_button2 = ttk.Button(root, text='execute orders', command=lambda: order_manager(
        variable.get(), int(order_entry.get())))
    order_button2.pack(ipadx=5, ipady=5, expand=True)
    order_button2.place(x=565, y=1)
    root.mainloop()


def shipbuilder(num):
    global check_num
    testfleet.Ship.shipyard(num)
    for o in range(0, num):
        but_set.append(0)
    for i in range(0, len(but_set)):
        but_set[i] = tkinter.Button(root, text="v")
        but_set[i].place(anchor='nw', x=1, y=25+55*i, width=300, height=50)
        but_set[i].config(text="check")
    if check_num == 0:
        threading.Thread(target=traffic_light).start()
        check_num = 1


def traffic_light():
    global p
    while p != 0:
        for i in range(0, len(but_set)):
            if testfleet.navi[i].state == "ok":
                but_set[i].config(bg='green', text="%s is ready" % testfleet.navi[i].name)
            else:
                but_set[i].config(bg='red', text="%s is broken" % testfleet.navi[i].name)
            time.sleep(1)


def download():
    global p
    p = 0
    for i in range(0, len(but_set)):
        but_set[i].config(bg='grey')


def new_order(order_menu, variable):
    top = tkinter.Toplevel()
    top.geometry("750x250")
    name_entry = tkinter.Entry(top, width=25)
    name_entry.pack()
    build_button = ttk.Button(top, text="build", command=lambda: build_and_break(
        top, name_entry.get(), order_menu, variable))
    build_button.pack(ipadx=5, ipady=5, expand=True)
    build_button.place(x=337, y=20)


def build_and_break(top, name, order_menu, variable):
    testymctestface.Order.order_def(name)
    Options.append(testymctestface.orders[0].name)
    order_menu['menu'].delete(0, 'end')
    for choice in Options:
        order_menu['menu'].add_command(label=choice, command=tkinter._setit(variable, choice))
    top.destroy()


def order_manager(name, num):
    lab_set.append(num)
    name_set.append(name)
    lab_set[len(lab_set)-1] = tkinter.Label(root, text="order %s has %s remaining units" % (name, str(num)), anchor='w')
    lab_set[len(lab_set)-1].place(anchor='nw', x=310, y=-5+35*len(lab_set), width=300, height=30)
    if len(lab_set) == 1:
        order_des(testfleet.navi, num, name_set[0])


def order_des(navi, val, name):
    err = 0
    while 0 < val:
        for i in range(0, len(navi)):
            if navi[i].state == "ok":
                threading.Thread(target=navi[i].activation, args=[1, navi[i]]).start()
                val -= 1
                lab_set[0].config(text='order %s has %s remaining units' % (name, str(val)))
            elif navi[i].state != "work":
                err += 1
            if val == 0:
                break
            time.sleep(1)
        if err == len(navi):
            print("total system error")
            print("tasks remaining: %s" % val)
            break
        else:
            err = 0
        if val == 0:
            lab_set.pop(0)
            name_set.pop(0)
            if len(lab_set) > 0:
                order_des(testfleet.navi, lab_set[0], name_set[0])
        time.sleep(1)


graphic_activation()
