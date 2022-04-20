from GISType import GISType, class_type

# PiLayer should be a factory class
class PiLayer:
    def __init__(self, path):
        self.type = 1
        self.projection = 'espg:4326'
        self.type = GISType.Point
        self.type_as_str = class_type[self.type]
        ...
