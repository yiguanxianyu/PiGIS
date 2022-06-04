from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem, QCursor, QAction
from PySide6.QtWidgets import QWidget, QMenu, QColorDialog

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
        curr_row = current_index.row()
        is_not_root = current_index.parent().isValid()
        item_parent = item.parent() if is_not_root else self
        item_parent.removeRow(curr_row)

    def remove_layer_group(self):
        item = self.itemFromIndex(current_index)
        curr_row = current_index.row()
        is_not_root = current_index.parent().isValid()
        item_parent = item.parent() if is_not_root else self

        item_to_del = item_parent.takeRow(curr_row)[0]
        layers = item_to_del.layers

        if is_not_root:
            item_parent.insertRows(curr_row, len(layers))
            [item_parent.setChild(curr_row + i, copy_layer(layers[i]))
             for i in range(len(layers))]
        else:
            [self.insertRow(curr_row + i, copy_layer(layers[i]))
             for i in range(len(layers))]


class LayerTree(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.layerContextMenu = QMenu(self)
        self.layerGroupContextMenu = QMenu(self)
        self.emptyContextMenu = QMenu(self)
        self.mainWindow = main_window

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
        self.add_layer_test()

    def get_current_item(self) -> LayerItem:
        return self.sim.itemFromIndex(current_index)

    def create_layer_menu(self):
        def show_color_dialog():
            s = QColorDialog.getColor()
            print(s)
            self.get_current_item().set_color(s)

        choose_color_act = QAction(self)
        choose_color_act.setText('Choose color')
        choose_color_act.triggered.connect(show_color_dialog)

        def show_attributes_table():
            self.ab = AttributesTable(self.get_current_item().layer)
            self.ab.show()

        show_attributes_table_act = QAction(self)
        show_attributes_table_act.setText('Show Attribute Table')
        show_attributes_table_act.triggered.connect(show_attributes_table)

        def show_symbology_page():
            self.sp = SymbologyPage(None)
            self.sp.show()

        show_symbology_page_act = QAction(self)
        show_symbology_page_act.setText('Symbology')
        show_symbology_page_act.triggered.connect(show_symbology_page)

        def show_label():
            pass

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
        self.layerContextMenu.addAction(choose_color_act)
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

        self.emptyContextMenu.addAction(self.ui.action_add_layer_group)
        self.emptyContextMenu.addAction(self.ui.action_expand_all)
        self.emptyContextMenu.addAction(self.ui.action_collapse_all)

    def add_layer_test(self):

        item1 = LayerItem(QItemType.LayerGroup, [], '图层组1')
        item2 = LayerItem(QItemType.LayerGroup, [], '图层组2')

        for i in range(5):
            temp = LayerItem(QItemType.Layer, i, f'图层{i}')
            item1.appendRow(temp)

        self.sim.insertRow(0, item1)
        self.sim.insertRow(1, item2)

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
                raise Exception('Some error occurred')
        else:
            # 未选中项目
            self.emptyContextMenu.move(QCursor().pos())
            self.emptyContextMenu.show()

    def clicked(self, index):
        global current_index
        current_index = index

    @staticmethod
    def item_changed(item):
        print('---begin---')
        if item.type() is QItemType.Layer:
            print(f'有单位发生变化:{item.text()}, {item.type()},{item.layer}')
        else:
            print(f'有单位发生变化:{item.text()}, {item.type()},{item.layers}')
        item.update_on_item_changed()
        print('---end---')

    def get_layers(self):
        """
        TODO: 返回树状图层
        """
        pass

    def get_render_list(self):
        """
        TODO: 获取需要被渲染的图层
        """
        pass

    def add_layer(self, layer):
        item = LayerItem(QItemType.Layer, layer, 'New Layer')
        self.sim.appendRow(item)

    def add_layer_group(self):
        item = LayerItem(QItemType.LayerGroup, [], 'New Layer Group')
        self.sim.appendRow(item)
