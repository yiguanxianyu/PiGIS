import numpy as np
from PySide6.QtCore import Qt
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
        self.pen = QPen(Qt.blue)  # 笔触
        self.brush = QBrush(Qt.white)  # 填充
        self.useless = 0  # 没用

        '''马子添加属性'''
        self.label_status = False
        self.annotation_status = False

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

    def get_attr_table(self):
        """
        小陈请注意：这里的的 feature 没有维护一个内建的 id，
        所以没有办法在把 AttrTable 里的数据和要素对应起来，
        因此需要维护一个字典或者列表存每个要素隐藏的 feature id
        """
        type_list = [np.int16, np.int32, np.int64, np.float32, np.float64, 'U20']
        data_type_list = [(field.name, type_list[field.value_type]) for field in self.fields.fields]
        data_type_list.insert(0,('id',np.int32))
        data_type = np.dtype(data_type_list)
        
        table = [tuple([feature.id] + [attr.value for attr in feature.attributes.attributes]) for feature in self.features.features]
        return np.array(table, dtype=data_type)

    def __del__(self):
        """移除图层本身 TODO"""
        pass

    def set_symbology(self, _type, _data):
        """设定符号化方式，还没太想明白 TODO"""
        pass

    def remove_feature(self, ids: list[int]):
        """删除指定的要素 TODO"""
        pass

    def highlight_feature(self, ids: list[int]):
        """高亮指定的要素 TODO"""
        pass

    def set_visibility(self, visibility):
        """改变某个 layer 的可见性 TODO"""
        # print('vis,', layer_id, layer_visibility)
        pass

    def set_zlevel(self, z_level):
        """改变本图层的 z level TODO"""
        pass

    def has_label_or_anno(self):
        return self.label_status or self.label_status

    def render_label(self):
        """添加标注（动态） TODO"""
        if self.annotation_status:
            self.remove_annotation()
        ...
        self.label_status = True

    def render_annotation(self):
        """添加注记（静态） TODO"""
        if self.label_status:
            self.remove_annotation()
        ...
        self.annotation_status = True

    def remove_label(self):
        """移除标注（动态） TODO"""
        ...
        self.label_status = False

    def remove_annotation(self):
        """移除注记（静态） TODO"""
        ...
        self.annotation_status = False


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
