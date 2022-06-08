from PiMapObj import PiGeometry

'''类别标识
1 PiPoint
2 PiPolyline
3 PiPolygon
4 PiMultiPoint
5 PiMultiPolyline
6 PiMultiPolygon
'''


class PiGeometryCollection(PiGeometry.PiGeometry):
    def __init__(self, type: int):
        super().__init__(type)
        self._collection = []
        self._object_num = 0
        self._length = 0
        self._area = 0
        self._mbr = None
        self._changed = True

    def load(self, object_list: list):
        for item in object_list:
            self._collection.append(item)
        self._object_num = len(object_list)

    def get_collection(self):
        return self._collection

    def update_object(self, index, object):
        self._collection[index] = object
        self._changed = True

    def insert_object(self, index, object):
        self._collection.insert(index, object)
        self._object_numm += 1
        self._changed = True

    def delete_object(self, index):
        del (self._collection[index])
        self._object_num -= 1
        self._changed = True

    def __calculate_attr(self):
        if self._object_num == 0:
            return
        self._length = 0
        self._area = 0
        self._mbr = self._collection[0].get_mbr()
        for object in self._collection:
            self._length += object.get_length()
            self._area += object.get_area()
            self._mbr.union(object.get_mbr())

    def get_object_num(self) -> int:
        return self._object_num

    def get_length(self):
        if self._changed:
            self._changed = False
            self.__calculate_attr()
        return self._length

    def get_area(self):
        if self._changed:
            self._changed = False
            self.__calculate_attr()
        return self._area

    def get_mbr(self):
        if self._changed:
            self._changed = False
            self.__calculate_attr()
        return self._mbr
