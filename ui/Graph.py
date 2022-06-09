from PySide6.QtCore import QMetaObject
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QFrame, QWidget

from PiConstant import HIGHLIGHTCOLOR
from PiDrawObj.PiGraphView import PiGraphView
from PiMapObj.PiLayer import PiLayer
from ui.raw import Ui_Graph


class Graph(QWidget):
    def __init__(self, mw):
        super().__init__(mw)
        self.layerTree = None
        self.ui = Ui_Graph()
        self.ui.setupUi(self)

        self.ui.graphicsView = PiGraphView(self)
        self.ui.graphicsView.grabKeyboard()
        self.ui.graphicsView.setFrameShape(QFrame.NoFrame)
        self.ui.graphicsView.setLineWidth(0)
        self.ui.gridLayout.addWidget(self.ui.graphicsView, 0, 0, 1, 1)
        self.ui.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

        self.draw_control = self.ui.graphicsView.draw_control
        self.highlighted_feature = {}

    def load_layer(self, layer):
        """加载一个图层"""
        self.draw_control.add_layer(layer)

    def get_layer_by_id(self, layer_id) -> PiLayer:
        """根据id返回一个 PiLayer 对象"""
        return self.draw_control.layers[layer_id]

    def remove_layer(self, layer_id):
        """删除图层"""
        self.draw_control.delete_layer(layer_id)

    def cancel_highlight_feature(self, layer_id: int, ids=None):
        """取消高亮指定的要素"""
        if ids is None:
            if layer_id in self.highlighted_feature:
                ids = self.highlighted_feature[layer_id]
            else:
                return
        else:
            ids = {i for i in ids if i in self.highlighted_feature[layer_id]}

        layer = self.get_layer_by_id(layer_id)
        for feature_id in ids:
            feature_item = self.draw_control.get_feature_item(layer_id, feature_id)
            feature_item.setPen(layer.pen)
            feature_item.setBrush(layer.brush)

        self.highlighted_feature[layer_id] -= ids

    def highlight_feature(self, layer_id: int, ids: list[int]):
        """高亮指定的要素"""
        if layer_id not in self.highlighted_feature:
            self.highlighted_feature[layer_id] = set()
        current_highlight = self.highlighted_feature[layer_id]

        _input = set(ids)
        self.cancel_highlight_feature(layer_id, current_highlight - _input)

        # new_highlight 是新增的需要被高亮的要素
        new_highlight: set = _input - current_highlight
        for feature_id in new_highlight:
            feature_item = self.draw_control.get_feature_item(layer_id, feature_id)
            feature_item.setPen(QPen(HIGHLIGHTCOLOR))
            feature_item.setBrush(QBrush(HIGHLIGHTCOLOR))

        self.highlighted_feature[layer_id] = _input

    def set_visibility(self, layer_id, visibility):
        """改变某个 layer 的可见性"""
        # print('vis,', layer_id, layer_visibility)
        if visibility:
            self.draw_control.visulize_layer(layer_id)
        else:
            self.draw_control.hide_layer(layer_id)

    def set_zvalue(self, layer_id, z_level):
        """改变某个 layer 的 z level"""
        self.draw_control.set_zvalue_layer(layer_id, z_level)

    def set_symbology(self, layer_id, _type, _data):
        """设定符号化方式，还没太想明白 TODO"""
        pass

    def remove_features(self, layer_id, ids: list[int]):
        """删除指定的要素"""
        self.cancel_highlight_feature(layer_id, ids)
        self.draw_control.remove_features(layer_id, ids)

    def render_label(self, layer_id):
        """添加标注（动态） TODO"""
        layer = self.get_layer_by_id(layer_id)
        if layer.annotation_status:
            layer.remove_annotation()
        ...
        layer.label_status = True

    def render_annotation(self, layer_id):
        """添加注记（静态） TODO"""
        layer = self.get_layer_by_id(layer_id)
        if layer.label_status:
            layer.remove_annotation()
        ...
        layer.annotation_status = True

    def remove_label(self, layer_id):
        """移除标注（动态） TODO"""
        layer = self.get_layer_by_id(layer_id)
        ...
        layer.label_status = False

    def remove_annotation(self, layer_id):
        """移除注记（静态） TODO"""
        layer = self.get_layer_by_id(layer_id)
        ...
        layer.annotation_status = False
