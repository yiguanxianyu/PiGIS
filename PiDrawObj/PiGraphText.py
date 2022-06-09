from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QRubberBand
from PiConstant import PiEditModeConstant
from PiMapObj.PiLayer import PiLayer
from PySide6.QtWidgets import QRubberBand

from PiMapObj.PiLayer import PiLayer


# import pyqtgraph as pg

class PiGraphText():
    def __init__(self, view) -> None:
        self.view = view
        self.draw_control = self.view.draw_control
        self.mouse_pos_before = QPointF()
        self.is_moving = False

    def mousePressEvent(self,event:QMouseEvent):
        return self.view.super_mousePressEvent(event)

    def mouseMoveEvent(self,event):
        return self.view.super_mouseMoveEvent(event)

    def mouseReleaseEvent(self,event):
        return self.view.super_mouseReleaseEvent(event)