from PySide6.QtCore import QMetaObject
from PySide6.QtWidgets import QFrame, QWidget

from PiDrawObj.PiGraphView import PiGraphView
from ui.raw import Ui_Graph


class Graph(QWidget):

    def __init__(self, mw):
        super().__init__()
        self.mainWindow = mw
        self.layerTree = None
        self.ui = Ui_Graph()
        self.ui.setupUi(self)

        self.ui.graphicsView = PiGraphView(self)
        # self.ui.graphicsView.grabKeyboard()
        self.ui.graphicsView.setFrameShape(QFrame.NoFrame)
        self.ui.graphicsView.setLineWidth(0)
        self.ui.gridLayout.addWidget(self.ui.graphicsView, 0, 0, 1, 1)

        self.ui.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    def load_layers(self, layers):
        draw_control = self.ui.graphicsView.draw_control
        for layer in layers:
            draw_control.add_layer(layer)
        draw_control.load_graphics()

    def set_layer_visibility(self, layer_id, layer_visibility):
        """
        改变某个 layer 的可见性
        """
        # print('vis,', layer_id, layer_visibility)
        pass

    def set_layer_zlevel(self, layer_id, layer_z_level):
        """
        改变某个 layer 的 z level
        """
        # print('zlv,', layer_id, layer_z_level)
        pass

    def get_layer_by_id(self, layer_id):
        """
        根据id返回一个 PiLayer
        """
        pass
