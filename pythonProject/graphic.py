sett = []


class Test:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    @staticmethod
    def howmany(who):
        print(who.num)


sett.append(Test('dog', 2))
sett.append(Test('cat', 5))
sett.append(Test('fish', 7))
Test.howmany(sett.index(Test.name == 'dog'))
