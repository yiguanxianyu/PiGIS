from PiMapObj.PiGeometryCollection import PiGeometryCollection
from PiMapObj.PiPoint import PiPoint

class PiMultiPoint(PiGeometryCollection):
    def __init__(self):
        super().__init__(0)
        self.count = 0 # 点个数
    
    def load(self,reader):
        point_list = []
        self.count = reader.read_int32()
        for i in range(self.count):
            new_point = PiPoint() 
            new_point.load(reader)
            point_list.append(new_point)
        super().load(point_list)

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