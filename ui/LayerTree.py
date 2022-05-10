from enum import Enum

from PySide6.QtGui import QStandardItemModel, QStandardItem, QCursor
from PySide6.QtWidgets import QWidget, QMenu

from ui.raw import Ui_LayerTree


# TODO:随机生成符号化的函数

class ItemType(Enum):
    Layer = 1
    LayerGroup = 2
    Default = 3


class UserRole:
    min_value = QStandardItem.UserType
    ItemType = 100 + min_value
    Layer = 110 + min_value
    Visible = 120 + min_value


class LayerItem(QStandardItem):

    def __init__(self, *args):
        super(LayerItem, self).__init__(*args)
        self.setCheckable(True)
        """
        问题在于，我是一个傻逼。应该把layerlist放在这里还是setdata里面呢？很容易导致itemchanged呗触发了。
        """

    def clone(self):
        return LayerItem()

    @property
    def type(self):
        return self.data(UserRole.ItemType)

    def set_type(self, _type):
        self.setData(_type, UserRole.ItemType)

        match _type:
            case ItemType.Layer:
                self.setDropEnabled(False)
            case ItemType.LayerGroup:
                self.setData([], UserRole.Layer)

        return self

    @property
    def layer(self):
        """
        图层组返回列表，图层返回图层对象
        """
        return self.data(UserRole.Layer)

    def set_layer(self, layer):
        """
        为图层项设置图层
        """
        if self.type is ItemType.Layer:
            self.setData(layer, UserRole.Layer)
            self.emitDataChanged()
        else:
            raise Exception('Some error occurred')

    def add_layer(self, layer):
        """
        将图层添加到图层组
        """
        if self.type is ItemType.LayerGroup:
            # layers: list = self.data(UserRole.Layer)
            layers = self.layer
            layers.append(layer)
            self.setData(layers, UserRole.Layer)
            self.emitDataChanged()
        else:
            raise Exception('Some error occurred')

    # TODO: 删除图层和图层组

    @property
    def self_visible(self):
        return self.checkState()

    @property
    def parent_visible(self):
        return self.parent().checkState()

    @property
    def visible(self):
        return self.parent_visible and self.self_visible

    def update_visible(self):
        """
        递归地设置每个图层的可见性
        """
        match self.type:
            case ItemType.Layer:
                # TODO: 这个 Layer 对象还没有眉目呢
                # self.layer.set_visible(self.visible)
                pass
            case ItemType.LayerGroup:
                for item in self.layer:
                    item.update_visible()
            case _:
                raise Exception('Some error occurred')

    def update_layer_group(self):
        """
        更新当前图层组内包含的元素
        """
        self.setData([self.child(i) for i in range(self.rowCount())], UserRole.Layer)

    def update_on_item_changed(self):
        """
        接受 itemChanged 事件
        """

        def update_layer():
            # TODO: 这个 Layer 对象还没有眉目呢
            # self.layer.set_text(self.text())
            pass

        def update_layer_group():
            pass

        parent = self.parent()
        if parent:
            parent.update_layer_group()

        self.update_visible()

        match self.type:
            case ItemType.Layer:
                update_layer()
            case ItemType.LayerGroup:
                update_layer_group()
            case _:
                raise Exception('Some error occurred')

    @property
    def layer_type(self):
        if self.type is ItemType.Layer:
            return self.layer.type
        else:
            raise Exception('Some error occurred')
    # self.setData(self.checkState(), UserRole.LastCheckState)
    # self.setData(self.text(), UserRole.LastText)
    #
    # def set_last_check_state(self, state):
    #     self.setData(state, UserRole.LastCheckState)
    #
    # def set_last_text(self, text):
    #     self.setData(text, UserRole.LastText)
    #
    # def check_state_changed(self):
    #     check_state = self.checkState()
    #     if check_state == self.data(UserRole.LastCheckState):
    #         return False
    #     else:
    #         self.set_last_check_state(check_state)
    #         return True
    #
    # def text_changed(self):
    #     text = self.text()
    #     if text == self.data(UserRole.LastText):
    #         return False
    #     else:
    #         self.set_last_text(text)
    #         return True


class LayerItemModel(QStandardItemModel):
    def __init__(self, *args):
        super(LayerItemModel, self).__init__(*args)
        self.setItemPrototype(LayerItem())


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
        self.create_menu()

        # 创建一个图层树模型
        self.sim = LayerItemModel()
        self.sim.itemChanged.connect(self.item_changed)
        # 设置图层框的标题
        self.sim.setHorizontalHeaderItem(0, QStandardItem(' Layers'))
        self.treeView.setModel(self.sim)
        # 不执行全部展开会导致无法检测到标题的高度从而导致 bug
        self.treeView.expandAll()
        self._header_height = self.treeView.header().height()

        self.add_layer_test()

    def create_menu(self):
        self.layerContextMenu.addAction(u'添加')
        self.layerContextMenu.addAction(u'删除')
        self.layerContextMenu.addAction(u'这是一个图层')

        self.layerGroupContextMenu.addAction(u'添加')
        self.layerGroupContextMenu.addAction(u'删除')
        self.layerGroupContextMenu.addAction(u'这是一个图层组')

        self.emptyContextMenu.addAction(self.ui.action_add_layer_group)
        self.emptyContextMenu.addAction(self.ui.action_expand_all)
        self.emptyContextMenu.addAction(self.ui.action_collapse_all)

    def add_layer_test(self):
        sim = self.sim

        item1 = LayerItem('图层组1').set_type(ItemType.LayerGroup)
        item2 = LayerItem('图层组2').set_type(ItemType.LayerGroup)

        for i in range(5):
            temp = LayerItem(f'图层{i}').set_type(ItemType.Layer)
            item1.appendRow(temp)

        sim.appendRow(item1)
        sim.appendRow(item2)

    def show_context_menu(self, qp):
        qp.setY(qp.y() - self._header_height)
        current_index = self.treeView.indexAt(qp)

        s: LayerItem = self.sim.itemFromIndex(current_index)

        if s:
            # print('-' * 10)
            # print(current_index.data())
            # print(s.checkState())
            if s.parent():
                self.layerContextMenu.move(QCursor().pos())
                self.layerContextMenu.show()
            else:
                self.layerGroupContextMenu.move(QCursor().pos())
                self.layerGroupContextMenu.show()
        else:
            self.emptyContextMenu.move(QCursor().pos())
            self.emptyContextMenu.show()

    def item_changed(self, item):
        print('---begin---')
        print(f'有单位发生变化:{item.text()}, {item.type}')
        item.update_on_item_changed()
        print('---end---')

    def clicked(self, index):
        ...

        # index.parent().data()
        # print('-' * 10)
        # print(index.data())

    def add_layer(self, layer):
        item = LayerItem('New Layer').set_type(ItemType.Layer)
        item.set_layer(layer)
        self.sim.appendRow(item)

    def add_layer_group(self):
        item = LayerItem('New Layer Group').set_type(ItemType.LayerGroup)
        self.sim.appendRow(item)
