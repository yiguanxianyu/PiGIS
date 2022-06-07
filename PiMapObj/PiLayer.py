from PySide6.QtGui import QBrush, QPen

from PiConstant import PiGeometryTypeConstant
from PiMapObj import PiGlobal
from PiMapObj.BinaryReader import BinaryReader
from PiMapObj.PiFeature import PiFeatures
from PiMapObj.PiField import PiFields
from PiMapObj.PiProjection import PiProjection

cons = PiGeometryTypeConstant()


class PiLayer():
    def __init__(self):
        self.name = ""  # 名字
        self.id = PiGlobal.layer_count  # 唯一id
        PiGlobal.layer_count += 1
        self.fields = PiFields()  # 字段元数据
        self.geometry_type = 0  # 几何图形类型
        self.features = PiFeatures()  # 几何图形
        self.proj = PiProjection()  # 投影
        self.pen = QPen()  # 笔触
        self.brush = QBrush()  # 填充
        self.useless = 0  # 没用

    def load(self, file_path, proj_path=None):
        '''加载坐标信息'''
        print(self.id)
        self.name = file_path[:-4]
        load_type = file_path[-3:]
        if load_type == 'lay':
            with open(file_path, "rb") as file:
                reader = BinaryReader(file.read())
            self.useless = reader.read_int32()  # 版本号
            self.geometry_type = reader.read_int32()  # 图层元素类型
            self.fields.load(reader, load_type)  # 加载字段
            self.features.load(reader, load_type, self.geometry_type, self.fields)  # 加载元素
        if proj_path != None:
            self.proj.load(proj_path)

    def get_geometry_type(self):
        return cons.get_str(self.geometry_type)

    def get_fields(self):
        return self.fields

    def get_features(self):
        return self.features


if __name__ == "__main__":
    # reader = LayerReader("图层文件/国界线.lay")
    # reader = LayerReader("图层文件/省级行政区.lay")
    layer = PiLayer()
    layer.load("图层文件/省会城市.lay")
    print(layer.get_geometry_type())
    print(layer.get_fields())
    fe = layer.features.features[0]
    fea = fe.attributes
    print(fea)
