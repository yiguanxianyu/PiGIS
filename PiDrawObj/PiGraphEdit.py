from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QBrush, QMouseEvent, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsItem, QGraphicsPathItem, QRubberBand
from PiConstant import PiEditModeConstant
from PiMapObj.PiLayer import PiLayer
from PySide6.QtWidgets import QRubberBand

from PiMapObj.PiLayer import PiLayer


# import pyqtgraph as pg

class PiEditCachePointItem(QGraphicsEllipseItem):
    def __init__(self,point:QPointF):
        super().__init__(point.x()-2,point.y()-2,4,4)
        super().setPen(QPen(Qt.red))
        super().setBrush(QBrush(Qt.gray))

class PiEditCacheItem():
    def __init__(self,draw_control,feature_item):
        self.draw_control = draw_control
        self.view = draw_control.view
        self.feature_item = feature_item
        self.feature = self.feature_item.feature

        cache =  self.feature_item.get_cache()
        self.cacheItem = QGraphicsPathItem(cache)
        self.cacheItem.setPen(QPen(Qt.red))
        self.cacheItem.setBrush(QBrush(Qt.gray))
        self.draw_control.scene.addItem(self.cacheItem)

        self.point_lists = feature_item.get_point_lists()
        self.points = [[PiEditCachePointItem(point) for point in point_list] for point_list in self.point_lists]
        for point_list in self.points:
            for point in point_list:
                self.draw_control.scene.addItem(point)
        #print(self.point_lists)
    
    def draw(self):
        self.cacheItem.setPen(Qt.red)
        self.cacheItem.setBrush(Qt.gray)

    def end_edit(self):
        self.draw_control.scene.removeItem(self.cacheItem)
        for point_list in self.points:
            for point in point_list:
                self.draw_control.scene.removeItem(point)
        

class PiGraphEdit():
    def __init__(self, view) -> None:
        self.view = view
        self.draw_control = self.view.draw_control
        self.edit_rb = QRubberBand(QRubberBand.Line, self.view)
        self.edit_on = None
        self.mode = PiEditModeConstant.newable
    
    def start_edit_on(self,layer_id):
        layer = self.draw_control.layers[layer_id]
        self.edit_on = layer
        for item in self.draw_control.item_collections[layer_id].values():
            item.accept_edit = True
        pass

    def end_edit(self):
        if self.edit_on == None:
            return
        layer_id = self.edit_on.id
        for item in self.draw_control.item_collections[layer_id].values():
            item.accept_edit = False
            if item.edit_cache != None:
                item.edit_cache.end_edit()
                item.edit_cache = None
        self.edit_on = None
    
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
