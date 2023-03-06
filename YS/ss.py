class Test:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.function = self.sum(self._x, self._y)

    def sum(self, x, y):
        return x+y

    def ch(self):
        print(self.function)

    def setXY(self, x, y):
        self._x = x
        self._y = y


test = Test(3, 4)
test.ch()
test.setXY(5, 4)
test.ch()
