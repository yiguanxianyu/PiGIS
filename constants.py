from enum import Enum

from PySide6.QtGui import QStandardItem

PiGIS_MAJOR_VERSION = 0
PiGIS_MINOR_VERSION = 1
PiGIS_PATCH_VERSION = 0


class ItemType(Enum):
    Layer = 1
    LayerGroup = 2
    Default = 3


class UserRole:
    min_value = QStandardItem.UserType
    ItemType = 1000 + min_value
    Layer = 1010 + min_value
    Visible = 1020 + min_value


class GISType(Enum):
    Point = 0
    MultiPoint = 1


class_type = {
    'Point': GISType.Point, 'MultiPoint': GISType.MultiPoint,
}
