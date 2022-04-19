from enum import Enum


class GISType(Enum):
    Point = 0
    MultiPoint = 1


class_type = {
    'Point': GISType.Point, 'MultiPoint': GISType.MultiPoint,
}