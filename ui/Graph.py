from PySide6.QtCore import QRectF, QMetaObject
from PySide6.QtWidgets import QFrame, QWidget

from PiDrawObj.PiGraphView import PiGraphView
from ui.raw import Ui_Graph

class Graph(QWidget):
    def __init__(self):
        super().__init__()
        # TODO: Options Page
        self.ui = Ui_Graph()
        self.ui.setupUi(self)

        self.ui.graphicsView = PiGraphView(self)
        self.ui.graphicsView.grabKeyboard()
        self.ui.graphicsView.setFrameShape(QFrame.NoFrame)
        self.ui.graphicsView.setLineWidth(0)
        self.ui.gridLayout.addWidget(self.ui.graphicsView, 0, 0, 1, 1)

        self.ui.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

        rect = QRectF(100, 100, 400, 200)
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
