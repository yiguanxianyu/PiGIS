
import PiGlobal,PiGeometry
class PiPolyline:
    pass

class PiPolyline(PiGeometry.PiGeometry):
    def __init__(self):
        super().__init__(-1)
        self.count = 0
        self._x = []
        self._y = []
        self._length = 0
        self._mbr = None
        self._changed = True
    
    def load(self,reader):
        self.count = reader.read_int32()
        for i in range(self.count):
            self._x.append(reader.read_float64())
            self._y.append(reader.read_float64())
        #self.__calculate_attr()
    
    def __calculate_attr(self):
        if len(self._x) > 1:
            self._length = PiGlobal.calculate_length(self._x,self._y)
        if len(self._x) > 0:
            self._mbr = PiGlobal.PiMbr(min(self._x),min(self._y),max(self._x),max(self._y))
    
    def clone(self) -> PiPolyline:
        return PiPolyline(self._x,self._y)
    
    def delete_point(self,index):
        del(self._x[index])
        del(self._y[index])
        self.changed = True

    def insert_point(self,index,x,y):
        self._x.insert(index,x)
        self._y.insert(index,y)
        self.changed = True

    def update_point(self,index,x,y):
        self._x[index] = x
        self._y[index] = y

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

    def get_length(self):
        if self._changed:
            self.__calculate_attr()
            self._changed = False
        return self._length
    
    def get_mbr(self):
        if self._changed:
            self.__calculate_attr()
            self._changed = False
        return self._mbr
    