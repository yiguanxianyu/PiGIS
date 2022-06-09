from typing import Sequence
from PySide6.QtCore import QPoint, QPointF, Qt
from PySide6.QtGui import QBrush, QMouseEvent, QPainterPath, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsItem, QGraphicsPathItem, QGraphicsSceneMouseEvent, QRubberBand
from PiConstant import DEFAULT_POINT_RADIUS, EDITBRUSHCOLOR, EDITPENCOLOR, PiEditModeConstant, PiGeometryTypeConstant
from PiDrawObj.PiGraphicsItem import PiGraphicsItemGroup
from PiMapObj.PiLayer import PiLayer
from PySide6.QtWidgets import QRubberBand

from PiMapObj.PiLayer import PiLayer
from PiMapObj.PiMultiPoint import PiMultiPoint
from PiMapObj.PiMultiPolygon import PiMultiPolygon
from PiMapObj.PiMultiPolyline import PiMultiPolyline
from PiMapObj.PiPoint import PiPoint
from PiMapObj.PiPolygon import PiPolygon
from PiMapObj.PiPolyline import PiPolyline


class PiAddCachePointItem(QGraphicsEllipseItem):
    def __init__(self,point:QPointF,add_cache):
        self.init_x = point.x()
        self.init_y = point.y()
        self.add_cache = add_cache
        if add_cache.geometry_type == PiGeometryTypeConstant.multipoint.value:
            r = DEFAULT_POINT_RADIUS
            super().__init__(self.init_x-r,self.init_y-r ,2 * r ,2 * r)
        else:
            super().__init__(self.init_x-0.5,self.init_y-0.5 ,1 ,1)

class PiAddCacheItem():
    def __init__(self,draw_control,head,geometry_type):
        self.draw_control = draw_control
        self.geometry_type = geometry_type
        self.cachePath = QPainterPath(head)
        self.cacheItem = QGraphicsPathItem()
        self.cacheItem.setPen(EDITPENCOLOR)
        self.point_list = [head]
        if self.geometry_type != PiGeometryTypeConstant.multipolyline.value:
            self.cacheItem.setBrush(EDITBRUSHCOLOR)
        else:
            self.cacheItem.setBrush(Qt.transparent)
        self.draw_control.scene.addItem(self.cacheItem)
        self.tail = PiAddCachePointItem(head,self)
        pass

    def tail_to(self,point):
        if self.geometry_type == PiGeometryTypeConstant.multipoint.value:
            self.point_list[0] = point
        else:
            self.point_list.append(point)
            self.cachePath.lineTo(point)

class PiGraphAdd():
    def __init__(self, view) -> None:
        self.view = view
        self.draw_control = self.view.draw_control
        self.add_cache = None
        self.add_on:PiLayer = None
    
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
        if event.button() == Qt.MouseButton.LeftButton:
            if self.add_cache == None:
                head = self.view.mapToScene(QPoint(event.x(),event.y()))
                geometry_type = self.add_on.geometry_type
                self.add_cache = PiAddCacheItem(self.draw_control,head,geometry_type)
                if self.add_on.geometry_type == PiGeometryTypeConstant.multipoint.value:
                    now_path = QPainterPath()
                    r = DEFAULT_POINT_RADIUS
                    now_path.addEllipse(head,r,r)
                    self.add_cache.cacheItem.setPath(now_path)
            else:
                tail = self.view.mapToScene(QPoint(event.x(),event.y()))
                self.add_cache.tail_to(tail)
        elif event.button()  == Qt.MouseButton.RightButton:
            if self.add_cache == None:
                pass
            else:
                # 加载到显示中
                layer_id = self.add_on.id
                pen = self.add_on.pen
                brush = self.add_on.brush 
                path = self.add_cache.cachePath
                item_collection = self.draw_control.item_collections[layer_id]
                # 新增多边形
                point_list = self.add_cache.point_list
                scale = self.draw_control.scale
                match self.add_on.geometry_type:
                    case PiGeometryTypeConstant.multipolygon.value:
                        polygon = PiPolygon()
                        for point in point_list:
                            polygon.add_point(point.x()*scale,-point.y()*scale)
                        geometry = PiMultiPolygon()
                        geometry.add_object(polygon)
                    case PiGeometryTypeConstant.multipolyline.value:
                        polyline = PiPolyline()
                        for point in point_list:
                            polyline.add_point(point.x()*scale,-point.y()*scale)
                        geometry = PiMultiPolyline()
                        geometry.add_object(polyline)
                    case PiGeometryTypeConstant.multipoint.value:
                        point = PiPoint()
                        point.update(point_list[0].x()*scale,-point_list[0].y()*scale)
                        geometry = PiMultiPoint()
                        geometry.add_object(point)
                feature = self.add_on.add_feature(geometry)
                item = PiGraphicsItemGroup(layer_id,feature,self.draw_control.item_box,self.draw_control,pen,brush)
                item_collection[feature.id] = item
                self.draw_control.scene.addItem(item)
                self.draw_control.scene.removeItem(self.add_cache.cacheItem)
                self.add_cache = None
        return self.view.super_mousePressEvent(event)

    def mouseMoveEvent(self,event):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            if self.add_cache != None:
                tail = self.view.mapToScene(QPoint(event.x(),event.y()))
                if self.add_on.geometry_type != PiGeometryTypeConstant.multipoint.value:
                    now_path = QPainterPath(self.add_cache.cachePath)
                    now_path.lineTo(tail)
                else:
                    now_path = QPainterPath()
                    r = DEFAULT_POINT_RADIUS
                    now_path.addEllipse(tail,r,r)
                self.add_cache.cacheItem.setPath(now_path)
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            pass
        return self.view.super_mouseMoveEvent(event)

    def mouseReleaseEvent(self,event):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            self.view.super_mouseReleaseEvent(event)
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            self.view.super_mouseReleaseEvent(event)