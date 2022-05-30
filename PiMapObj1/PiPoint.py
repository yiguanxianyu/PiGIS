import PiGlobal,PiGeometry
import copy
class PiPoint():
    pass

class PiPoint(PiGeometry.PiGeometry):
    def __init__(self):
        super().__init__(1)
        self._x = 0
        self._y = 0
    
    def load(self,reader):
        self._x = reader.read_float64()
        self._y = reader.read_float64()
    
    def clone(self) -> PiPoint:
        return PiPoint(self.x,self.y)

    def equal(self,object: PiPoint) -> bool:
        if abs(object.x - self.x) < 1e-6 \
        and abs(object.y - self.y) < 1e-6:
            return True
        else:
            return False
    
    def update(self,x,y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y


