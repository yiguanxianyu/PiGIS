import numpy as np
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem, QCursor, QAction
from PySide6.QtWidgets import QWidget, QMenu
from pandas import DataFrame

from PiMapObj.PiLayer import PiLayer
from constants import QItemType
from ui.AttributesTable import AttributesTable
from ui.LayerItem import LayerItem
from ui.Symbology import SymbologyPage
from ui.raw import Ui_LayerTree

current_index: QModelIndex = None


def copy_layer(layer):
    __type = layer.type()

    if __type is QItemType.LayerGroup:
        new_item = LayerItem(__type, [], layer.text())
        lrs = layer.layers
        new_item.insertRows(0, len(lrs))
        for i in range(len(lrs)):
            new_i = copy_layer(lrs[i])
            new_item.setChild(i, new_i)
    else:
        new_item = LayerItem(__type, layer.layer, layer.text())

    return new_item


class LayerItemModel(QStandardItemModel):
    def __init__(self, layer_tree, *args):
        super(LayerItemModel, self).__init__(*args)
        self.layerTree = layer_tree
        # 设置对象原型
        self.setItemPrototype(LayerItem(QItemType.Default, None))

    def remove_layer(self):
        item = self.itemFromIndex(current_index)
        self.layerTree.graph.remove_layer(item.layer)
        item_parent = item.parent() if current_index.parent().isValid() else self
        item_parent.removeRow(current_index.row())

    def remove_layer_group(self):
        item = self.itemFromIndex(current_index)
        curr_row = current_index.row()
        is_not_root = current_index.parent().isValid()
        item_parent = item.parent() if is_not_root else self
        layers = item_parent.takeRow(curr_row)[0].layers

        if is_not_root:
            item_parent.insertRows(curr_row, len(layers))
            for i in range(len(layers)):
                item_parent.setChild(curr_row + i, copy_layer(layers[i]))
        else:
            for i in range(len(layers)):
                self.insertRow(curr_row + i, copy_layer(layers[i]))


class LayerTree(QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.graph = None
        self.layerContextMenu = QMenu(self)
        self.layerGroupContextMenu = QMenu(self)
        self.emptyContextMenu = QMenu(self)

        self.ui = Ui_LayerTree()
        self.ui.setupUi(self)
        self.treeView = self.ui.treeView
        # 创建一个图层树模型
        self.sim = LayerItemModel(self)
        self.sim.itemChanged.connect(self.item_changed)
        # 设置图层框的标题
        self.sim.setHorizontalHeaderItem(0, QStandardItem(' Layers'))
        self.treeView.setModel(self.sim)
        # 不执行全部展开会导致无法检测到标题的高度从而导致 bug
        self.treeView.expandAll()
        self._header_height = self.treeView.header().height()

        self.create_menu()

    def focusInEvent(self, e) -> None:
        self.grabKeyboard()

    def focusOutEvent(self, e) -> None:
        self.releaseKeyboard()

    def get_current_item(self) -> LayerItem:
        return self.sim.itemFromIndex(current_index)

    def create_layer_menu(self):
        """创建图层的右键菜单"""

        def show_attributes_table():
            layer = self.graph.get_layer_by_id(self.get_current_item().layer)
            self.ab = AttributesTable(self.graph, layer)
            self.ab.show()

        show_attributes_table_act = QAction(self)
        show_attributes_table_act.setText('Show Attribute Table')
        show_attributes_table_act.triggered.connect(show_attributes_table)

        def show_symbology_page():
            layer: PiLayer = self.graph.get_layer_by_id(self.get_current_item().layer)
            attr_table = layer.get_attr_table()
            df = DataFrame(attr_table)
            fields = layer.get_attr_table().dtype.names[1:]
            nums = [len(set(df.iloc[:, i + 1])) for i in range(len(fields))]
            sp = SymbologyPage(self, nums, fields)
            if sp.exec():
                type_, pen, brush, *args = sp.result()
                if type_ == 0:  # 唯一值
                    data = np.array(df.iloc[:, [0, args[0] + 1]])
                    sorted_data = data[np.argsort(data[:, 1])]
                    brush_dict, i = {}, 0
                    for item in sorted_data:
                        fid, value = item
                        brush_dict[fid] = brush[i]
                        if value not in brush_dict:
                            i += 1
                    self.graph.set_symbology_unique_value(layer.id, pen, brush_dict)

                elif type_ == 1:  # 分级
                    data = np.array(df.iloc[:, [0, args[0] + 1]])
                    sorted_data = data[np.argsort(data[:, 1])]
                    sorted_fids = sorted_data[:, 0]
                    levels = np.linspace(0, len(sorted_fids), len(brush) + 1)
                    levels = np.round(levels).astype(int)
                    brush_dict = {}
                    for i in range(len(levels) - 1):
                        for fid in sorted_fids[levels[i]:levels[i + 1]]:
                            brush_dict[fid] = brush[i]
                    self.graph.set_symbology_by_level(layer.id, pen, brush_dict)

                else:  # 单值
                    self.graph.set_symbology_single_value(layer.id, pen, brush)

        show_symbology_page_act = QAction(self)
        show_symbology_page_act.setText('Symbology')
        show_symbology_page_act.triggered.connect(show_symbology_page)

        def show_label():
            self.graph.render_label(self.get_current_item().layer)

        show_label_act = QAction(self)
        show_label_act.setText('Show Label')
        show_label_act.triggered.connect(show_label)

        # 删除 Action
        remove_layer_act = QAction(self)
        remove_layer_act.setText(u'Remove Layer')
        remove_layer_act.triggered.connect(self.sim.remove_layer)

        self.layerContextMenu.addAction(u'This is Layer')
        self.layerContextMenu.addAction(show_label_act)
        self.layerContextMenu.addAction(remove_layer_act)
        self.layerContextMenu.addAction(show_attributes_table_act)
        self.layerContextMenu.addAction(show_symbology_page_act)

    def create_layer_group_menu(self):
        # 删除 Action
        remove_layer_group_act = QAction(self)
        remove_layer_group_act.setText(u'Remove Layer Group')
        remove_layer_group_act.triggered.connect(self.sim.remove_layer_group)

        self.layerGroupContextMenu.addAction(u'This is Layer Group')
        self.layerGroupContextMenu.addAction(remove_layer_group_act)

    def create_menu(self):
        """
        这里还同时生成了空白区域的菜单
        """
        self.create_layer_menu()
        self.create_layer_group_menu()

        # For test only
        def load_test_layers():
            def _load(arg0, arg1):
                layer1 = PiLayer()
                layer1.load(arg0, "PiMapObj/图层文件/图层文件坐标系统说明.txt")
                self.add_layer(layer1.id, f'{layer1.name}{arg1}')
                self.graph.load_layer(layer1)

            _load("PiMapObj/图层文件/国界线.lay", '1')
            _load("PiMapObj/图层文件/省级行政区.lay", '2')
            _load("PiMapObj/图层文件/省会城市.lay", '3')

        # test loading layers
        load_layer_act = QAction(self)
        load_layer_act.setText(u'Load test layer')
        load_layer_act.triggered.connect(load_test_layers)

        self.emptyContextMenu.addAction(self.ui.action_add_layer_group)
        self.emptyContextMenu.addAction(load_layer_act)
        self.emptyContextMenu.addAction(self.ui.action_expand_all)
        self.emptyContextMenu.addAction(self.ui.action_collapse_all)

    def show_context_menu(self, qp):
        qp.setY(qp.y() - self._header_height)
        current_index_ = self.treeView.indexAt(qp)

        s: LayerItem = self.sim.itemFromIndex(current_index_)

        if s:
            s_type = s.type()
            if s_type == QItemType.Layer:
                # 选中图层
                self.layerContextMenu.move(QCursor().pos())
                self.layerContextMenu.show()
            elif s_type == QItemType.LayerGroup:
                # 选中图层组
                self.layerGroupContextMenu.move(QCursor().pos())
                self.layerGroupContextMenu.show()
            else:
                raise TypeError('Some error occurred')
        else:
            # 未选中项目
            self.emptyContextMenu.move(QCursor().pos())
            self.emptyContextMenu.show()

    @staticmethod
    def clicked(index):
        global current_index
        current_index = index

    def item_changed(self, item: LayerItem):
        if item.type() is QItemType.Layer:
            layer_id = item.layer
            self.graph.set_visibility(layer_id, item.visible)
        elif all_children := item.get_all_children(item):
            for _item in all_children:
                self.graph.set_visibility(_item.layer, _item.visible)

        new_v = self.get_visible_layers(item)
        for i in range(len(new_v) - 1, -1, -1):
            self.graph.set_zvalue(new_v[i], 10000 - i)

    def get_layer_tree(self):
        """获取递归图层树，为嵌套列表"""
        return [self.sim.item(i).get_recursive_layers() for i in range(self.sim.rowCount())]

    def set_layer_tree(self, layer_tree):
        """这个 layer 应该是 PiLayer对象"""
        for layer in layer_tree:
            if type(layer) == list:
                self.set_layer_tree(layer)
            else:
                self.add_layer(layer.id, layer.name)

    def get_visible_layers(self, item):
        """获取需要被渲染的图层"""
        lrs = []
        for i in range(self.sim.rowCount()):
            lrs += self.sim.item(i).get_visible_layers(item)

        return lrs

    def add_layer(self, layer_id, layer_name):
        item = LayerItem(QItemType.Layer, layer_id, layer_name)
        self.sim.appendRow(item)

    def add_layer_group(self):
        item = LayerItem(QItemType.LayerGroup, [], 'New Layer Group')
        self.sim.appendRow(item)
