from PySide6.QtGui import QStandardItemModel, QStandardItem, QCursor
from PySide6.QtWidgets import QWidget, QMenu

from ui.raw import Ui_LayerTree


class LayerTree(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.contextMenu = None
        self.mainWindow = main_window

        self.ui = Ui_LayerTree()
        self.ui.setupUi(self)
        self.treeView = self.ui.treeView
        self.create_menu()

        # 创建一个标准项单位模型
        self.sim = QStandardItemModel()
        # 设置图层框的标题
        title = QStandardItem()
        title.setText(' Layers')
        self.sim.setHorizontalHeaderItem(0, title)

        self.treeView.setModel(self.sim)
        # 不执行全部展开会导致无法检测到标题的高度
        self.treeView.expandAll()
        self._header_height = self.treeView.header().height()

        self.add_layer_test()

    def create_menu(self):
        self.contextMenu = QMenu(self)
        self.contextMenu.addAction(u'添加')
        self.contextMenu.addAction(u'删除')

    def add_layer_test(self):
        sim = self.sim

        item1 = QStandardItem()
        item1.setText('图层组1')
        item1.setCheckable(True)

        item2 = QStandardItem()
        item2.setText('图层组2')
        item2.setCheckable(True)

        for i in range(5):
            temp = QStandardItem(f'图层{i}')
            temp.setCheckable(True)
            temp.setDropEnabled(False)
            item1.appendRow(temp)

        sim.appendRow([item1])
        sim.appendRow([item2])

    def show_context_menu(self, qp):
        qp.setY(qp.y() - self._header_height)
        current_index = self.treeView.indexAt(qp)

        s: QStandardItem = self.sim.itemFromIndex(current_index)

        if s:
            print('-' * 10)
            print(current_index.data())
            print(s.checkState())

            self.contextMenu.move(QCursor().pos())
            self.contextMenu.show()

    def clicked(self, index):
        ...
        # index.parent().data()
        # print('-' * 10)
        # print(index.data())
