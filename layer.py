from GISType import GISType, class_type


# Maybe we should use factory pattern?
class PointLayer:
    def __init__(self, path):
        self.name = None
        self.projection = None
        self.type = GISType.Point
        self.type_as_str = class_type[self.type]
        ...


def create_layer(path):
    return PointLayer(path)
