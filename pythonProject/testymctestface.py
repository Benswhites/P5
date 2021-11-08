import time
import threading

ok = "ok"
work = "work"
orders = []


class Order:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    @staticmethod
    def order_def(name):
        orders.append(Order(name, 0))


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
                err += 1
            if val == 0:
                break
            time.sleep(1)
        if err == len(name):
            print("total system error")
            print("tasks remaining: %s" % val)
            val = 0
            break
        else:
            err = 0
        time.sleep(1)
    if val != 0:
        print("unfinished error how the shit did that happen")
    else:
        time.sleep(10)
        print("order finished")
