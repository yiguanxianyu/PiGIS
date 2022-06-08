import math

'''公共常量
'''

TYPENAME = ["Pi", "Point", "Polyline", "Polygon", "MultiPoint", "MultiPolyline", "MultiPolygon"]

'''公共变量
'''
layer_count = 0
id_count = 0

'''公用类型
'''


class PiMbr():
    pass


class PiMbr():
    def __init__(self, minx, miny, maxx, maxy):
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def union(self, object: PiMbr):
        self.minx = min(self.minx, object.minx)
        self.miny = min(self.miny, object.miny)
        self.maxx = max(self.maxx, object.maxx)
        self.maxy = max(self.maxy, object.maxy)

    def __str__(self):
        s = "%f,%f,%f,%f" % (self.minx, self.miny, self.maxx, self.maxy)
        return s

    __repr__ = __str__


'''公用函数
'''


def calculate_length(x: list, y: list) -> float:
    length = 0
    for i in range(len(x) - 1):
        length += math.sqrt((x[i + 1] - x[i]) ** 2 + (y[i + 1] - y[i]) ** 2)
    return length


def calculate_perimeter(x: list, y: list) -> float:
    perimeter = 0
    perimeter += calculate_length(x, y)
    perimeter += math.sqrt((x[-1] - x[0]) ** 2 + (y[-1] - y[0]) ** 2)
    return perimeter


def calculate_area(x: list, y: list) -> float:
    area = 0
    for i in range(1, len(x) - 1):
        x1, x2 = x[i] - x[0], x[i + 1] - x[0]
        y1, y2 = y[i] - y[0], y[i + 1] - y[0]
        area += x1 * y2 - x2 * y1
    area = abs(area) / 2
    return area
