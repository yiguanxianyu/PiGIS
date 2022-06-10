from PiConstant import PiGeometryTypeConstant
from PiMapObj.PiGeometryCollection import PiGeometryCollection
from PiMapObj.PiPolygon import PiPolygon


class PiMultiPolygon(PiGeometryCollection):
    def __init__(self):
        super().__init__(PiGeometryTypeConstant.multipolygon)
        self.count = 0  # 折线个数

    def load(self, reader, load_type):
        polygon_list = []
        if load_type == 'lay':
            self.count = reader.read_int32()
            for i in range(self.count):
                new_polygon = PiPolygon()
                new_polygon.load(reader, load_type)
                polygon_list.append(new_polygon)
        elif load_type == 'shp':
            pass
        super().load(polygon_list)

    def get_mbr(self):
        return super().get_mbr()

    def add_object(self, object):
        self.count += 1
        self._collection.append(object)

    def update_object(self, index, object):
        self._collection[index] = object

    def insert_object(self, index, object):
        self._collection.insert(index, object)
        self._object_num += 1

    def delete_object(self, index):
        del (self._collection[index])
        self._object_num -= 1

    def translate(self, dx, dy):
        return super().translate(dx, dy)
