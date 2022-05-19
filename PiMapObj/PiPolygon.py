import math
from PiMapObj import PiGlobal,PiGeometry
class PiPolygon:
    pass

class PiPolygon(PiGeometry.PiGeometry):
    def __init__(self):
        super().__init__(-1)
        self.count = 0
        self._x = []
        self._y = []
        self._length = 0
        self._mbr = None
        self._area = 0
        self._changed = True

    def load(self,reader):
        self.count = reader.read_int32()
        for i in range(self.count):
            self._x.append(reader.read_float64())
            self._y.append(reader.read_float64())
        #self.__calculate_attr()

    def __calculate_attr(self):
        if len(self._x) > 2:
            self._length  = PiGlobal.calculate_perimeter(self._x,self._y)
            self._area = PiGlobal.calculate_area(self._x,self._y)
        if len(self._x) > 0:
            self._mbr = PiGlobal.PiMbr(min(self._x),min(self._y),max(self._x),max(self._y))

    def clone(self) -> PiPolygon:
        return PiPolygon(self._x,self._y,self._innerx,self._innery)

    def delete_boundary_point(self,index):
        del(self._x[index])
        del(self._y[index])
        self.changed = True

    def insert_boundary_point(self,index,x,y):
        self._x.insert(index,x)
        self._y.insert(index,y)
        self.changed = True
    
    def insert_inner_ring(self,x,y):
        self._innerx.append(x)
        self._innery.append(y)
        self.changed = True
    
    def delete_inner_ring(self,index):
        del(self._innerx[index])
        del(self._innery[index])
        self.changed = True

    def clone(self) -> PiPolygon:
        return PiPolygon(self._x,self._y,self._innerx,self._innery)

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

    def get_length(self):
        if self._changed:
            self.__calculate_attr()
            self._changed = False
        return self._length

    def get_area(self):
        if self._changed:
            self.__calculate_attr()
            self._changed = False
        return self._area

    def get_mbr(self):
        if self._changed:
            self.__calculate_attr()
            self._changed = False
        return self._mbr
