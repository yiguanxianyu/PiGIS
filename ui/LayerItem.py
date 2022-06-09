from random import random

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem

from constants import QItemType, QUserRole


class LayerItem(QStandardItem):
    def __init__(self, _type, _layer, *args):
        super(LayerItem, self).__init__(*args)
        self.setCheckable(True)
        self.setCheckState(Qt.Checked)
        self.__type = None
        self.__layer = None

        if _type is QItemType.Layer:
            self.setDropEnabled(False)

        self.setData(_layer, QUserRole.Layer)
        self.setData(_type, QUserRole.ItemType)
        self.setData(random(), QUserRole.UniqueID)

    def row_total(self):
        if self.parent():
            return self.parent().row() + 1
        else:
            return self.row()

    def clone(self):
        """
        请注意: clone()函数并不能对其进行赋值，只能返回一个全新的对象。
        这是因为对象本身是作为 prototype 存在的，调用 clone() 时本质上
        是在调用你传进去的那个 LayerItem, 而那个 prototype 里什么都没有。
        """
        return LayerItem(QItemType.Default, None)

    def type(self):
        """返回该单位是图层还是图层组"""
        if not self.__type:
            self.__type = self.data(QUserRole.ItemType)
        return self.__type

    def id(self):
        return self.data(QUserRole.UniqueID)

    @property
    def layer(self):
        """图层，返回图层对象"""
        assert self.type() == QItemType.Layer
        if not self.__layer:
            self.__layer = self.data(QUserRole.Layer)
        return self.__layer

    @property
    def layers(self):
        """图层组，返回列表"""
        assert self.type() == QItemType.LayerGroup
        return [self.child(i) for i in range(self.rowCount())]

    def get_recursive_layers(self):
        """图层组，返回递归列表"""
        if self.type() == QItemType.LayerGroup:
            return [self.child(i).get_recursive_layers() for i in range(self.rowCount())]
        else:
            return self.layer

    def get_all_children(self, item):
        if item.id() == self.id() and id(item) != id(self):
            return []
        elif self.type() == QItemType.LayerGroup:
            lrs = []
            for iter_item in self.layers:
                lrs += iter_item.get_all_children(item)
            return lrs
        else:
            return [self]

    def get_visible_layers(self, item):
        if (item.id() == self.id() and id(item) != id(self)) or not self.self_visible:
            # if item.parent() != self.parent() or item.row() != self.row():
            return []

        if self.type() == QItemType.LayerGroup:
            lrs = []
            for iter_item in self.layers:
                lrs += iter_item.get_visible_layers(item)
            return lrs
        else:
            return [self.layer]

    @property
    def self_visible(self):
        """返回自身复选框的状态"""
        return self.checkState() == Qt.CheckState.Checked

    @property
    def visible(self):
        """返回自身的可见性"""
        temp = self
        while temp:
            if not temp.self_visible:
                return False
            temp = temp.parent()

        return True

    # def update_on_item_changed(self):
    #     """
    #     接受 itemChanged 事件
    #     """
    #
    #     def update_layer():
    #         # self.layer.set_text(self.text())
    #         pass
    #
    #     def update_layer_group():
    #         pass
    #
    #
    #     match self.type():
    #         case QItemType.Layer:
    #             update_layer()
    #         case QItemType.LayerGroup:
    #             update_layer_group()
    #         case QItemType.Default:
    #             print('怎么是default')
    #         case _:
    #             raise Exception('Some error occurred')

    # def update_layer_group(self):
    #     """
    #     更新当前图层组内包含的元素
    #     """
    #     warnings.warn("This is deprecated", DeprecationWarning)
    #     elf.layer = [self.child(i) for i in range(self.rowCount())]

    # @property
    # def layer_type(self):
    #     """
    #     返回图层本身的类型，仅对 Layer 生效
    #     """
    #
    #     # if self.type() is ItemType.Layer:
    #     #     return self._layer.type()
    #     # else:
    #     #     raise Exception('Some error occurred')
    #     return None
    #
    # def set_layer(self, layer):
    #     """
    #     为图层项设置图层，仅对 Layer 生效
    #     """
    #     assert self.type() is QItemType.Layer
    #     self.layer = layer

    # def add_layer(self, layer):
    #     """
    #     将图层添加到图层组，仅对 LayerGroup 生效
    #     """
    #     warnings.warn("This is deprecated", DeprecationWarning)
    #     assert self.type() is ItemType.LayerGroup
    #     self.layer.append(layer)
    # @property
    # def parent_visible(self):
    #     if self.parent():
    #         return self.parent().checkState() == Qt.CheckState.Checked
    #
    #     return True

    # def update_visible(self):
    #     """
    #     递归地设置每个图层的可见性
    #     """
    #     match self.type():
    #         case QItemType.Layer:
    #             # self.layer.set_visible(self.visible)
    #             pass
    #         case QItemType.LayerGroup:
    #             for item in self.layers:
    #                 item.update_visible()
    #         case QItemType.Default:
    #             print('怎么是default')
    #         case _:
    #             raise Exception('Some error occurred')
