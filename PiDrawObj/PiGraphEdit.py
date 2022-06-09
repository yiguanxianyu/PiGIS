from typing import Sequence
from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QBrush, QMouseEvent, QPainterPath, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsItem, QGraphicsPathItem, QGraphicsSceneMouseEvent, QRubberBand
from PiConstant import DEFAULT_POINT_RADIUS, EDITBRUSHCOLOR, EDITPENCOLOR, PiEditModeConstant, PiGeometryTypeConstant
from PiMapObj.PiLayer import PiLayer
from PySide6.QtWidgets import QRubberBand

from PiMapObj.PiLayer import PiLayer


# import pyqtgraph as pg

class PiEditCachePointItem(QGraphicsEllipseItem):
    def __init__(self,point:QPointF,edit_cache):
        self.init_x = point.x()
        self.init_y = point.y()
        self.edit_cache = edit_cache
        if edit_cache.feature.geometry_type == PiGeometryTypeConstant.multipoint.value:
            r = DEFAULT_POINT_RADIUS
            super().__init__(self.init_x-r,self.init_y-r ,2 * r ,2 * r)
        else:
            super().__init__(self.init_x-0.5,self.init_y-0.5 ,1 ,1)
        super().setPen(QPen(Qt.red))
        super().setBrush(QBrush(Qt.gray))
        self.setFlags(QGraphicsItem.ItemIsMovable)
        self.index = self.edit_cache.count
        self.start_pos = None
        self.edit_cache.count += 1
    
    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.start_pos == None:
            self.start_pos = QPointF(self.get_x(),self.get_y())
        else:
            pass
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        pos = super().pos()
        if self.edit_cache.feature.geometry_type == PiGeometryTypeConstant.multipoint.value:
            path = QPainterPath(QPointF(self.init_x,self.init_y))
            path.lineTo(QPointF(self.get_x(),self.get_y()))
            self.edit_cache.cacheItem.setPath(path)
            pass
        else:
            self.edit_cache.set_cache_element_at(self.index,self.init_x+pos.x(),self.init_y+pos.y())
        self.edit_cache.add_changed_point(self)
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.start_pos = None
        return super().mouseReleaseEvent(event)
    
    def get_x(self):
        return self.init_x + self.pos().x()

    def get_y(self):
        return self.init_y + self.pos().y()

class PiEditCacheItem():
    def __init__(self,draw_control,feature_item):
        self.draw_control = draw_control
        self.view = draw_control.view
        self.feature_item = feature_item
        self.feature = self.feature_item.feature
        self.cacheItem = QGraphicsPathItem()
        self.cacheItem.setPen(QPen(EDITPENCOLOR))
        if self.feature.geometry_type == PiGeometryTypeConstant.multipolygon.value:
            self.cacheItem.setBrush(QBrush(EDITBRUSHCOLOR))
        else:
            self.cacheItem.setBrush(QBrush(Qt.transparent))
        self.cacheItem.setZValue(9999)
        self.draw_control.scene.addItem(self.cacheItem)
        self.changed_point_list:Sequence[PiEditCachePointItem] = []
        self.load()
    
    def load(self):
        self.count = 0
        self.cache:QPainterPath = self.feature_item.get_cache()
        self.cacheItem.setPath(self.cache)
        pos = self.feature_item.pos()
        self.point_lists = self.feature_item.get_point_lists()
        self.points = [[PiEditCachePointItem(point+pos,self) for point in point_list] for point_list in self.point_lists]
        for point_list in self.points:
            for point in point_list:
                point.setZValue(9999)
                self.draw_control.scene.addItem(point)
        #print(self.point_lists)

    def set_cache_element_at(self,index,x,y):
        self.cache.setElementPositionAt(index,x,y)
        self.cacheItem.setPath(self.cache)

    def add_changed_point(self,point):
        self.changed_point_list.append(point)

    def end_edit(self):
        pos = self.feature_item.pos()
        item_list = self.feature_item.childItems()
        path_list = [item.path() for item in item_list]
        for point in self.changed_point_list:
            order = 0
            index,x,y = point.index,point.get_x()-pos.x(),point.get_y()-pos.y()
            while index >= len(self.point_lists[order]):
                index -= len(self.point_lists[order])
                order += 1
            # 应用编辑(内存上)
            item_list[order].set_geometry_at(index,x,y)
            # 应用编辑(显示上)
            if item_list[order].geometry.type == PiGeometryTypeConstant.point:
                path_list[order] = QPainterPath()
                path_list[order].addEllipse(QPointF(x,y),DEFAULT_POINT_RADIUS,DEFAULT_POINT_RADIUS)
            else:
                path_list[order].setElementPositionAt(index,x,y)
            self.point_lists[order][index] = QPointF(x,y)
        for i in range(len(item_list)):
            item = item_list[i] 
            item.setPath(path_list[i]) # 更新图像
            item.point_list = self.point_lists[i] # 更新点集合
        # 应用编辑（内存上）TODO
        

        # 删除编辑缓冲图元
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
