from enum import Enum
class PiValueTypeConstant(): # 属性值类型参数
    def __init__(self):
        self.int16 = 0
        self.int32 = 1
        self.int64 = 2
        self.float = 3
        self.double = 4
        self.string = 5
    
    def get_str(self,type):
        type_list = [
            "int16",
            "int32",
            "int64",
            "float",
            "double",
            "string",
            ]
        return type_list[type]

class PiGeometryTypeConstant(): # 几何要素类型参数
    def __init__(self):
        self.multipoint = 0
        self.multipolyline = 1
        self.multipolygon = 2
    
    def get_str(self,type):
        type_list = [
            "multipoint",
            "multipolyline",
            "multipolygon",
            ]
        return type_list[type]

class PiProjectionTypeConstant(): # 投影类型常数
    def __init__(self):
        self.none = 0
        self.mercator = 1
        self.utm = 2
        self.gauss_kruger = 3
        self.lambert_conformal_conic_2sp = 4
        self.albers_equal_area = 5
    
    def get_str(self,type):
        type_list = [
            "none",
            "mercator",
            "utm",
            "gauss_kruger",
            "lambert_conformal_conic_2sp",
            "albers_equal_area",
            ]
        return type_list[type]
    
    def get_type(self,str):
        type_dict = {
            "none":0,
            "mercator":1,
            "utm":2,
            "gauss_kruger":3,
            "lambert_conformal_conic_2sp":4,
            "albers_equal_area":5,
        }
        try:
            return type_dict[str]
        except:
            return -1

class PiLinearUnitConstant(): # 线性单位常数
    def __init__(self):
        self.millimeter = 0
        self.centimeter = 1
        self.decimeter = 2
        self.meter = 3
        self.kilometer = 4
        self.scale_dict = {
            self.millimeter:1000,
            self.centimeter:100,
            self.decimeter:10,
            self.meter:1,
            self.kilometer:0.001,
            }

    def get_str(self,type):
        type_list = [
            "millimeter",
            "centimeter",
            "decimeter",
            "meter",
            "kilometer",
            ]
        return type_list[type]
    
    def get_type(self,str):
        type_dict = {
            "millimeter":0,
            "centimeter":1,
            "decimeter":2,
            "meter":3,
            "kilometer":4,
        }
        try:
            return type_dict[str]
        except:
            return -1

class PiGraphModeConstant(Enum):
    editable = 0
    moveable = 1

class PiLayerStatusConstant(Enum):
    normal = 0
    added = 1
    hidden = 2
    visiable = 3
    deleted = 4