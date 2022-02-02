class Counter():
    def __init__(self) -> None:
        self._count = 0
    def addCount(self):
        self._count += 1
    def getCount(self):
        return self._count