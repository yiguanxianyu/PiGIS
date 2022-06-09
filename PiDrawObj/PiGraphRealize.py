from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QGraphicsItem, QRubberBand
from PiConstant import PiEditModeConstant
from PiMapObj.PiLayer import PiLayer
from PySide6.QtWidgets import QRubberBand

from PiMapObj.PiLayer import PiLayer


# import pyqtgraph as pg

class PiGraphRealize():
    def __init__(self, view) -> None:
        self.view = view
        self.draw_control = self.view.draw_control
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

