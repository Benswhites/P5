import time
import fleet
import threading

ok = "ok"
work = "work"


class Order:
    def __init__(self, name, num):
        self.name = name
        self.num = num


def thread_test(name, val):
    err = 0
    job = 1
    while 0 < val:
        for i in range(0, len(name)):
            if name[i].state == ok:
                threading.Thread(target=name[i].activation, args=[job, name[i]]).start()
                val -= 1
                job += 1
            elif name[i].state != work:
                print("%s is %s" % (name[i].name, name[i].state))
                err += 1
            if val == 0:
                break
        if err == len(name):
            print("total system error")
            print("tasks remaining: %s" % val)
            val = 0
        else:
            err = 0
        time.sleep(1)
    if val != 0:
        print("unfinished error how the shit did that happen")
    else:
        time.sleep(10)
        print("order finished")


fleet.Ship.shipyard(5)
order1 = Order("ninja", 15)
thread_test(fleet.navi, order1.num)
fleet.Ship.sad_detector(fleet.navi)
