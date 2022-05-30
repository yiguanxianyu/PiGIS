from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem, QCursor, QAction
from PySide6.QtWidgets import QWidget, QMenu, QColorDialog

from constants import QItemType
from ui.AttributesTable import AttributesTable
from ui.LayerItem import LayerItem
from ui.raw import Ui_LayerTree


# TODO:随机生成符号化的函数

def copy_layer(layer):
    new_item = LayerItem(layer.type(), layer.text())

    if layer.type() is QItemType.LayerGroup:
        lrs = layer.layers
        new_item.insertRows(0, len(lrs))
        for i in range(len(lrs)):
            new_i = copy_layer(lrs[i])
            new_item.setChild(i, new_i)
    else:
        new_item.layer = layer.layer

    return new_item


class LayerItemModel(QStandardItemModel):
    def __init__(self, layer_tree, *args):
        super(LayerItemModel, self).__init__(*args)
        self.layerTree = layer_tree
        self.setItemPrototype(LayerItem(QItemType.Default))

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
            [item_parent.setChild(curr_row + i, copy_layer(layers[i])) for i in range(len(layers))]
        else:
            [self.insertRow(curr_row + i, copy_layer(layers[i])) for i in range(len(layers))]


selected_item: LayerItem = LayerItem(QItemType.Default)
current_index: QModelIndex = None


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

    def create_layer_menu(self):
        def show_color_dialog():
            s = QColorDialog()
            print(s.getColor())

        choose_color_act = QAction(self)
        choose_color_act.setText('Choose color')
        choose_color_act.triggered.connect(show_color_dialog)

        def show_attributes_table():
            self.ab = AttributesTable()
            self.ab.show()

        show_attributes_table_act = QAction(self)
        show_attributes_table_act.setText('Show Attribute Table')
        show_attributes_table_act.triggered.connect(show_attributes_table)

        # 删除 Action
        delete_layer_act = QAction(self)
        delete_layer_act.setText(u'Delete Layer')
        delete_layer_act.triggered.connect(self.sim.remove_layer)

        self.layerContextMenu.addAction(u'This is Layer')
        self.layerContextMenu.addAction(delete_layer_act)
        self.layerContextMenu.addAction(choose_color_act)
        self.layerContextMenu.addAction(show_attributes_table_act)

    def create_layer_group_menu(self):
        # 删除 Action
        delete_layer_group_act = QAction(self)
        delete_layer_group_act.setText(u'Delete Layer Group')
        delete_layer_group_act.triggered.connect(self.sim.remove_layer_group)

        self.layerGroupContextMenu.addAction(u'This is Layer Group')
        self.layerGroupContextMenu.addAction(delete_layer_group_act)

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

        item1 = LayerItem(QItemType.LayerGroup, '图层组1')
        item2 = LayerItem(QItemType.LayerGroup, '图层组2')

        for i in range(5):
            temp = LayerItem(QItemType.Layer, f'图层{i}')
            item1.appendRow(temp)

        self.sim.insertRow(0, item1)
        self.sim.insertRow(1, item2)

    def show_context_menu(self, qp):
        qp.setY(qp.y() - self._header_height)
        current_index_ = self.treeView.indexAt(qp)

        s: LayerItem = self.sim.itemFromIndex(current_index_)

        if s:
            match s.type():
                case QItemType.Layer:
                    # 选中图层
                    self.layerContextMenu.move(QCursor().pos())
                    self.layerContextMenu.show()
                case QItemType.LayerGroup:
                    # 选中图层组
                    self.layerGroupContextMenu.move(QCursor().pos())
                    self.layerGroupContextMenu.show()
                case _:
                    raise Exception('Some error occurred')
        else:
            # 未选中项目
            self.emptyContextMenu.move(QCursor().pos())
            self.emptyContextMenu.show()

    @staticmethod
    def item_changed(item):
        print('---begin---')
        print(f'有单位发生变化:{item.text()}, {item.type()}')
        item.update_on_item_changed()
        print('---end---')

    def clicked(self, index):
        assert index == self.treeView.currentIndex()
        item = self.sim.itemFromIndex(index)
        print('visible:', item.visible)
        global selected_item, current_index
        selected_item = item
        current_index = index

    def add_layer(self, layer):
        item = LayerItem(QItemType.Layer, 'New Layer')
        item.set_layer(layer)
        self.sim.appendRow(item)

    def add_layer_group(self):
        item = LayerItem(QItemType.LayerGroup, 'New Layer Group')
        self.sim.appendRow(item)

    # TODO: get_render_list, 获取需要被渲染的图层

# def set_type(self, _type):
#     """
#     下一步取消这个函数 集成进init里面
#     """
#     self.setData(_type, UserRole.ItemType)
#
#     match _type:
#         case ItemType.Layer:
#             self.setDropEnabled(False)
#         case ItemType.LayerGroup:
#             self.setData([], UserRole.Layer)
#
#     return self