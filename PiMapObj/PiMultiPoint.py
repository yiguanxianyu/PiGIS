from PiConstant import PiGeometryTypeConstant
from PiMapObj.PiGeometryCollection import PiGeometryCollection
from PiMapObj.PiPoint import PiPoint


class PiMultiPoint(PiGeometryCollection):
    def __init__(self):
        super().__init__(PiGeometryTypeConstant.multipoint)
        self.count = 0  # 点个数

    def load(self, reader, load_type):
        point_list = []
        if load_type == 'lay':
            self.count = reader.read_int32()
            for i in range(self.count):
                new_point = PiPoint()
                new_point.load(reader, load_type)
                point_list.append(new_point)
        elif load_type == 'shp':
            pass
        super().load(point_list)

    def get_mbr(self):
        return super().get_mbr()

    def add_object(self, object):
        self._collection.append(object)
        self.count += 1

    def update_object(self, index, object):
        self._collection[index] = object

    def insert_object(self, index, object):
        self._collection.insert(index, object)
        self._object_numm += 1

    def delete_object(self, index):
        del (self._collection[index])
        self._object_num -= 1

    def translate(self, dx, dy):
        return super().translate(dx, dy)
