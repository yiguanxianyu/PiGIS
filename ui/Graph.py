from PySide6.QtCore import QMetaObject
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QFrame, QWidget, QFileDialog

from PiConstant import HIGHLIGHTCOLOR
from PiDrawObj.PiGraphView import PiGraphView
from PiMapObj.PiLayer import PiLayer
from ui.raw import Ui_Graph


# TODO 更新比例尺和鼠标坐标

class Graph(QWidget):

    def __init__(self, mw):
        super().__init__(mw)
        self.layerTree = None
        self.ui = Ui_Graph()
        self.ui.setupUi(self)
        self.view_control = PiGraphView(self)
        self.ui.graphicsView = self.view_control
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
        if ids:
            highlighted = self.highlighted_feature[layer_id]
            ids = {i for i in ids if i in highlighted}
        elif layer_id in self.highlighted_feature:
            highlighted = self.highlighted_feature[layer_id]
            ids = highlighted
        else:
            return

        layer = self.get_layer_by_id(layer_id)
        for feature_id in ids:
            feature_item = self.draw_control.get_feature_item(layer_id, feature_id)
            feature_item.setPen(layer.pen)
            feature_item.setBrush(layer.brush)

        highlighted -= ids

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

    def set_name(self, layer_id, text):
        self.get_layer_by_id(layer_id).name = text

    def set_visibility(self, layer_id, visibility):
        """改变某个 layer 的可见性"""
        if visibility:
            self.draw_control.visulize_layer(layer_id)
        else:
            self.draw_control.hide_layer(layer_id)

    def set_zvalue(self, layer_id, z_level):
        """改变某个 layer 的 z level"""
        self.draw_control.set_zvalue_layer(layer_id, z_level)

    def set_symbology_single_value(self, layer_id, pen, brush):
        """单一值渲染，不需要feature_id了，直接渲染就可以"""
        item_collection = self.draw_control.item_collections[layer_id]
        for item in item_collection.values():
            item.setPen(pen)
            item.setBrush(brush)

    def set_symbology_unique_value(self, layer_id, pen, brush_dict):
        """唯一值渲染"""
        item_collection = self.draw_control.item_collections[layer_id]
        for feature_id, brush in brush_dict.items():
            item_collection[feature_id].setPen(pen)
            item_collection[feature_id].setBrush(brush)

    def set_symbology_by_level(self, layer_id, pen, brush_dict):
        """分级渲染"""
        item_collection = self.draw_control.item_collections[layer_id]
        for feature_id, brush in brush_dict.items():
            item_collection[feature_id].setPen(pen)
            item_collection[feature_id].setBrush(brush)

    def set_scale(self, scale):
        """设置比例尺，传入的是1:x的那个x缩放点就
        怎么方便怎么来吧，可以直接用当前中心点什么的"""
        self.view_control.set_show_scale(self.draw_control.scale / scale)

    def set_features_visibility(self, layer_id, ids: list[int], visibility: bool):
        """隐藏指定的要素 TODO"""
        self.draw_control.set_features_visibility(layer_id, ids, visibility)

    def add_empty_features(self, layer_id, ids: list[int]):
        """添加空要素，id已经被给定了,目前的 feature_id
        生成方式是最大的 feature_id + 2 TODO"""
        pass

    def remove_features(self, layer_id, ids: list[int]):
        """删除指定的要素"""
        self.cancel_highlight_feature(layer_id, ids)
        self.draw_control.remove_features(layer_id, ids)

    def edit_feature_attr(self, layer_id, added, edited, removed):
        """保存修改后的属性表，数据格式为 list[tuple]，每个tuple
        为元组组成的ndarray，第一位是隐藏的 feature_id
        注意：因为可能会在属性表内新增要素，所以不是所有的 feature_id
        都存在图里，需要判断一下。目前的feature_id生成方式是最大的
        feature_id + 2 TODO"""
        dtypes = [added.dtype[i] for i in range(1, len(added.dtype))]
        fields = [added.dtype.names[i] for i in range(1, len(added.dtype))]
        for i in added:
            # i[0]  feature_id
            pass

    def save_image(self):
        """根据文件路径和后缀名将地图保存成图片"""
        all_types = ['png (*.png)', 'jpg (*.jpg, *.jpeg)', 'bitmap (*.bmp)', '*.*']
        fp, ft = QFileDialog.getSaveFileName(QWidget(), "Save Image To", filter=';;'.join(all_types))
        # fp -> file path,ft -> file extension
        match all_types.index(ft):
            case 0:
                extension = '.png'
            case 1:
                extension = '.jpg'
            case 2 | _:
                extension = '.bmp'
        # extension就是文件后缀名
        print(fp, extension)
        # put your code here
        self.draw_control.save_fig(fp + extension)

    def render_label(self, layer_id):
        """添加标注（动态） TODO"""
        layer = self.get_layer_by_id(layer_id)
        if layer.annotation_status:
            self.remove_annotation(layer_id)
        # put your code here
        layer.label_status = True

    def render_annotation(self, layer_id):
        """添加注记（静态） TODO"""
        layer = self.get_layer_by_id(layer_id)
        if layer.label_status:
            self.remove_annotation(layer_id)

        self.view_control.add_layer_text(layer_id)

        layer.annotation_status = True

    def remove_label(self, layer_id):

        layer = self.get_layer_by_id(layer_id)

        layer.label_status = False

    def remove_annotation(self, layer_id):
        """移除注记（静态） TODO"""
        layer = self.get_layer_by_id(layer_id)
        # put your code here
        self.view_control.delete_layer_text(layer_id)
        # put your code here
        layer.annotation_status = False

    """小陈添加接口"""

    # 从编辑的三个模式切换到移动模式再切回来，编辑进度不变，
    # 但如果在编辑的三个模式间跳转，则会取消编辑

    def graph_turn_move(self):
        """切换图层可移动"""
        self.view_control.mode_turn_move()

    def graph_turn_layer_dragable(self, layer_id):
        """把对应图层切换成可以拖动的模式"""
        self.view_control.mode_turn_drag_layer(layer_id)

    def graph_turn_layer_editable(self, layer_id):
        """把对应图层切换成可以编辑的模式"""
        self.view_control.mode_turn_edit_layer(layer_id)

    def graph_turn_layer_addable(self, layer_id):
        """把图层切换成可以增加要素的模式"""
        self.view_control.mode_turn_add_layer(layer_id)
