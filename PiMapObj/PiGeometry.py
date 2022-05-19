from PiMapObj import PiGlobal 
'''类别标识
0 piPoint
- piPolyline
- piPolygon
- PiMultiPoint
1 PiMultiPolyline
2 PiMultiPolygon
'''
class PiGeometry():
    def __init__(self, type: int):
        self._id = PiGlobal.id_count
        PiGlobal.id_count += 1
        self._type = type # 元素的类别
    
    def load(self,reader):
        pass
    
    def get_type_name(self) -> str:
        return PiGlobal.TYPENAME[self._type]

    def get_length(self) -> float:
        return 0
    
    def get_area(self) -> float:
        return 0

    def get_mbr(self) -> float:
        return None

    
    @property
    def id(self):
        return self._id
    @property
    def type(self):
        return self._type
