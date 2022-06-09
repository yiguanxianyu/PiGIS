from typing import Sequence
from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QBrush, QMouseEvent, QPainterPath, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsItem, QGraphicsPathItem, QGraphicsSceneMouseEvent, QRubberBand
from PiConstant import DEFAULT_POINT_RADIUS, EDITBRUSHCOLOR, EDITPENCOLOR, PiEditModeConstant, PiGeometryTypeConstant
from PiMapObj.PiLayer import PiLayer
from PySide6.QtWidgets import QRubberBand

from PiMapObj.PiLayer import PiLayer
class PiGraphAdd():
    def __init__(self, view) -> None:
        self.view = view
        self.draw_control = self.view.draw_control
        self.add_on = None
    
    def start_add_on(self,layer_id):
        layer = self.draw_control.layers[layer_id]
        self.add_on = layer
        pass

    def end_add(self):
        if self.add_on == None:
            return
        layer_id = self.add_on.id
        self.add_on = None
    
    def mousePressEvent(self,event:QMouseEvent):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            self.view.super_mousePressEvent(event)
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            self.view.super_mousePressEvent(event)

    def mouseMoveEvent(self,event):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            self.view.super_mouseMoveEvent(event)
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            self.view.super_mouseMoveEvent(event)

    def mouseReleaseEvent(self,event):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            self.view.super_mouseReleaseEvent(event)
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            self.view.super_mouseReleaseEvent(event)