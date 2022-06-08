from PySide6.QtCore import QMetaObject
from PySide6.QtWidgets import QFrame, QWidget

from PiDrawObj.PiGraphView import PiGraphView
from PiMapObj import PiLayer
from ui.raw import Ui_Graph


class Graph(QWidget):
    def __init__(self, mw):
        super().__init__(mw)
        self.mainWindow = mw
        self.layerTree = None
        self.ui = Ui_Graph()
        self.ui.setupUi(self)

        self.ui.graphicsView = PiGraphView(self)
        self.ui.graphicsView.grabKeyboard()
        self.ui.graphicsView.setFrameShape(QFrame.NoFrame)
        self.ui.graphicsView.setLineWidth(0)
        self.ui.gridLayout.addWidget(self.ui.graphicsView, 0, 0, 1, 1)
        self.ui.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def load_layers(self, layer):
        """加载一个图层"""
        dc = self.ui.graphicsView.draw_control
        dc.add_layer(layer)
        dc.load_graphics()

    def get_layer_by_id(self, layer_id) -> PiLayer:
        """根据id返回一个 PiLayer对象"""
        pass

    def remove_layer(self, layer_id):
        """删除图层"""
        pass