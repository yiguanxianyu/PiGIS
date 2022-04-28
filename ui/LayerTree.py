from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem

from ui.raw import Ui_LayerTree

from PySide6.QtWidgets import QWidget


class LayerTree(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LayerTree()
        self.ui.setupUi(self)

        sim = QStandardItemModel()

        item1 = QStandardItem()
        item1.setText('试试')
        item1.setCheckable(True)

        item2 = QStandardItem()
        item2.setText('试试')
        item2.setCheckable(True)

        title = QStandardItem()
        title.setText('Layer')

        sim.appendColumn([item1, item2])

        item1.setChild(0, 0, QStandardItem('项目信息说明'))

        sim.setHorizontalHeaderItem(0, title)

        self.ui.treeView.setModel(sim)
        self.ui.treeView.expandAll()
