import time
from random import randrange

navi = []


class Ship:
    def __init__(self, state, name):
        self.state = state
        self.name = name

    @staticmethod
    def shipyard(val):
        for i in range(0, val):
            navi.append(Ship("ok", "ship"+str(len(navi)+1)))

    @staticmethod
    def activation(job, pos):
        pos.state = "work"
        win = 0
        while win != 1:
            check = randrange(100)
            if 0 < check < 11:
                win = 1
                pos.state = "ok"
            elif 10 < check < 12:
                pos.state = "sad"
                break
            else:
                time.sleep(1)

    @staticmethod
    def sad_detector(pos):
        for i in range(0, len(pos)):
            print("%s is %s" % (pos[i].name, pos[i].state))
