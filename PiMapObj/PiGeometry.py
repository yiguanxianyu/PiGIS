from PiMapObj import PiGlobal

"""类别标识
0 piPoint
- piPolyline
- piPolygon
- PiMultiPoint
1 PiMultiPolyline
2 PiMultiPolygon
"""


class PiGeometry:
    def __init__(self, type: int = -1):
        self.id = PiGlobal.id_count
        PiGlobal.id_count += 1
        self.type = type  # 元素的类别
        self._changed = True

    def load(self, reader):
        pass

    def get_type_name(self) -> str:
        return PiGlobal.TYPENAME[self.type]

    def get_length(self) -> float:
        return 0

    def get_area(self) -> float:
        return 0

    def get_mbr(self):
        return None
