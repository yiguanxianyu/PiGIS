from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QGraphicsItem, QRubberBand
from PiConstant import PiEditModeConstant
from PiMapObj.PiLayer import PiLayer
from PySide6.QtWidgets import QRubberBand

from PiMapObj.PiLayer import PiLayer


# import pyqtgraph as pg

class PiGraphDrag():
    def __init__(self, view) -> None:
        self.view = view
        self.draw_control = self.view.draw_control
        self.select_rb = QRubberBand(QRubberBand.Rectangle, self.view)
        self.drag_on = None

    def start_drag_on(self,layer_id):
        #print("drag layer %d" % layer_id)
        layer = self.draw_control.layers[layer_id]
        for item in self.draw_control.item_collections[layer_id].values():
            item.setFlag(QGraphicsItem.ItemIsMovable,True)
        self.drag_on = layer
    
    def end_drag(self):
        if self.drag_on == None:
            return
        layer_id = self.drag_on.id
        for item in self.draw_control.item_collections[layer_id].values():
            item.setFlag(QGraphicsItem.ItemIsMovable,False)
        self.drag_on = None

    def mousePressEvent(self,event:QMouseEvent):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            self.view.super_mousePressEvent(event)
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            pass

    def mouseMoveEvent(self,event):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            self.view.super_mouseMoveEvent(event)
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            pass

    def mouseReleaseEvent(self,event):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            self.view.super_mouseReleaseEvent(event)
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            pass

