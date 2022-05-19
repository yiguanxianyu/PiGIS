from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem, QCursor, QAction
from PySide6.QtWidgets import QWidget, QMenu

from constants import QItemType
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

        match item.type():
            case QItemType.Layer:
                item_parent.removeRow(curr_row)

            case QItemType.LayerGroup:
                item_to_del = item_parent.takeRow(curr_row)[0]
                layers = item_to_del.layers

                if is_not_root:
                    item_parent.insertRows(curr_row, len(layers))
                    [item_parent.setChild(curr_row + i, copy_layer(layers[i])) for i in range(len(layers))]
                else:
                    [self.insertRow(curr_row + i, copy_layer(layers[i])) for i in range(len(layers))]

            case _:
                print('fuck')


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

    def create_menu(self):
        delete_action = QAction(self)
        delete_action.setText(u'删除')
        delete_action.triggered.connect(self.sim.remove_layer)

        self.layerContextMenu.addAction(u'添加')
        self.layerContextMenu.addAction(delete_action)
        self.layerContextMenu.addAction(u'这是一个图层')

        self.layerGroupContextMenu.addAction(u'添加')
        self.layerGroupContextMenu.addAction(delete_action)
        self.layerGroupContextMenu.addAction(u'这是一个图层组')

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
        print(item.visible)
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
