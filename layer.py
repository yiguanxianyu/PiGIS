from abc import ABC, abstractmethod

from GISType import GISType, class_type


# Maybe we should use factory pattern?
class BaseLayer(ABC):
    def __init__(self):
        self.index = None
        self.name = None
        self.projection = None
        self.type = GISType.Point
        self.type_as_str = class_type[self.type]
        ...

    @abstractmethod
    def read_from_file(self, path):
        pass


class PointLayer(BaseLayer, ABC):
    def __init__(self):
        super(PointLayer, self).__init__(1)


def create_layer(path):
    return PointLayer()


if __name__ == "__main__":
    s = PointLayer()
    s.read_from_file(1)
