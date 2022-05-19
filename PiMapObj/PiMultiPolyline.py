from PiMapObj.PiGeometryCollection import PiGeometryCollection
from PiMapObj.PiPolyline import PiPolyline

class PiMultiPolyline(PiGeometryCollection):
    def __init__(self):
        super().__init__(1)
        self.count = 0 # 折线个数
    
    def load(self,reader):
        polyline_list = []
        self.count = reader.read_int32()
        for i in range(self.count):
            new_polyline = PiPolyline() 
            new_polyline.load(reader)
            polyline_list.append(new_polyline)
        super().load(polyline_list)
    
    def get_mbr(self):
        return super().get_mbr()

    def update_object(self,index,object):
        self._collection[index] = object

    def insert_object(self,index,object):
        self._collection.insert(index,object)
        self._object_numm += 1
    
    def delete_object(self,index):
        del(self._collection[index])
        self._object_num -= 1
        
