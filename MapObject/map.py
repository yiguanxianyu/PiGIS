class PiPoint:
    def __init__(self, x=0, y=0):
        self.__X = x
        self.__Y = y

    def clone(self):
        return PiPoint(self.__X, self.__Y)

    @property
    def x(self):
        return self.__X

    @property
    def y(self):
        return self.__Y


class PiRectangle:
    def __init__(self, min_x, min_y, max_x, max_y):
        self._MinX = min_x
        self._MinY = min_y
        self._MaxX = max_x
        self._MaxY = max_y

    def clone(self):
        return PiRectangle(self._MinX, self._MinY, self._MaxX, self._MaxY)

    @property
    def bounds(self):
        return PiPoint(self._MinX, self._MinY), PiPoint(self._MaxX, self._MaxY)
