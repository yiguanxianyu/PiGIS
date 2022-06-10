import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPen

from PiMapObj import PiGlobal
from PiMapObj.BinaryReader import BinaryReader
from PiMapObj.PiAttribute import PiAttributes
from PiMapObj.PiFeature import PiFeature, PiFeatures
from PiMapObj.PiField import PiFields
from PiMapObj.PiProjection import PiProjection


class PiLayer():
    def __init__(self):
        self.name = ""  # 名字
        self.file_path = ""  # 路径
        self.id = PiGlobal.layer_count  # 唯一id
        PiGlobal.layer_count += 1
        self.fields = PiFields()  # 字段元数据
        self.geometry_type = 0  # 几何图形类型
        self.features = PiFeatures()  # 几何图形
        self.proj = PiProjection()  # 投影
        self.useless = 0  # 没用
        self.pen = QPen(Qt.blue)  # 笔触
        self.brush = QBrush(Qt.white)  # 填充
        self.visibility = False
        self.text_index = 0
        self.text_visibility = False
        self.change = False

        self.label_status = False
        self.annotation_status = False

    def load(self, file_path, proj_path=None):
        """加载坐标信息"""
        self.change = True
        self.file_path = file_path
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

    def remove_features(self, ids: list[int]):
        """删除指定的要素"""
        features = self.features.features
        length = len(features)
        for index in range(1, length + 1):
            if features[length - index].id in ids:
                del features[length - index]
        self.features.count -= len(ids)

    def add_feature(self, geometry) -> PiFeature:
        new_feature = PiFeature(self.geometry_type, self.fields)
        attributes = PiAttributes(self.fields)
        attributes.set_default()
        new_feature.set_geometry(geometry)
        new_feature.set_attributes(attributes)
        self.features.features.append(new_feature)
        self.features.count += 1
        # print(new_feature.geometry)
        return new_feature

    def get_geometry_type(self):
        return self.geometry_type

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
        data_type_list.insert(0, ('id', np.int32))
        data_type = np.dtype(data_type_list)

        table = [tuple([feature.id] + [attr.value for attr in feature.attributes.attributes]) for feature in
                 self.features.features]
        return np.array(table, dtype=data_type)

    def has_label_or_anno(self):
        return self.label_status or self.label_status
