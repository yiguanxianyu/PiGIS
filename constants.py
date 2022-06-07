from enum import Enum
import numpy as np
from PySide6.QtGui import QStandardItem

PiGIS_MAJOR_VERSION = 0
PiGIS_MINOR_VERSION = 1
PiGIS_PATCH_VERSION = 0


class QItemType(Enum):
    Layer = 1
    LayerGroup = 2
    Default = 3


class QUserRole:
    min_value = QStandardItem.UserType
    ItemType = 1000 + min_value
    Layer = 1010 + min_value
    Visible = 1020 + min_value


class GISType(Enum):
    Point = 0
    MultiPoint = 1


AVAILABLE_DATATYPE = [
    'int16', 'int32', 'int64', 'float32', 'float64', 'string'
]


def get_real_type(dt, max_length=16):
    match dt:
        case 'string':
            return np.dtype(f'U{max_length}')
        case _:
            return np.dtype(dt)


class_type = {
    'Point': GISType.Point,
    'MultiPoint': GISType.MultiPoint,
}
