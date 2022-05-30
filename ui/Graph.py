from PySide6.QtWidgets import QWidget, QGraphicsScene

from ui.raw import Ui_Graph


class Graph(QWidget):
    def __init__(self):
        super().__init__()
        # TODO: Options Page
        self.ui = Ui_Graph()
        self.ui.setupUi(self)

        # rect = QRectF(0, 0, 200, 100)
        self.scene = QGraphicsScene()  # 创建场景
        self.ui.graphicsView.setScene(self.scene)
        '''
        item1 = QGraphicsRectItem(rect)  # 创建矩形---以场景为坐标
        item1.setFlags(
            QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable)  # 给图元设置标志
        # QGraphicsItem.ItemIsSelectable---可选择
        # QGraphicsItem.ItemIsFocusable---可设置焦点
        # QGraphicsItem.ItemIsMovable---可移动
        # QGraphicsItem.ItemIsPanel---
        self.scene.addItem(item1)  # 给场景添加图元
        self.figure = PiShow()
        self.scene.addWidget(self.figure)
        '''
