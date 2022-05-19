from PiGeometryCollection import PiGeometryCollection
from PiPolygon import PiPolygon
class PiMultiPolygon(PiGeometryCollection):
    def __init__(self):
        super().__init__(2)
        self.count = 0 # 折线个数

    def load(self,reader):
        polygon_list = []
        self.count = reader.read_int32()
        for i in range(self.count):
            new_polygon = PiPolygon() 
            new_polygon.load(reader)
            polygon_list.append(new_polygon)
        super().load(polygon_list)
        
    def update_object(self,index,object):
        self._collection[index] = object

    def insert_object(self,index,object):
        self._collection.insert(index,object)
        self._object_numm += 1
    
    def delete_object(self,index):
        del(self._collection[index])
        self._object_num -= 1