from PiConstant import PiGeometryTypeConstant
from PiMapObj import PiGlobal, PiGeometry


class PiPoint():
    pass


class PiPoint(PiGeometry.PiGeometry):
    def __init__(self):
        super().__init__(PiGeometryTypeConstant.point)
        self._x = 0
        self._y = 0
        self.count = 1

    def load(self, reader, load_type):
        if load_type == 'lay':
            self._x = reader.read_float64()
            self._y = reader.read_float64()
        elif load_type == 'shp':
            pass

    def clone(self) -> PiPoint:
        return PiPoint(self.x, self.y)

    def equal(self, object: PiPoint) -> bool:
        if abs(object.x - self.x) < 1e-6 \
                and abs(object.y - self.y) < 1e-6:
            return True
        else:
            return False
        
    def translate(self, dx, dy):
        self._x += dx
        self._y += dy
        self._changed = True

    def update(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_mbr(self):
        return PiGlobal.PiMbr(self._x, self._y, self._x, self._y)
