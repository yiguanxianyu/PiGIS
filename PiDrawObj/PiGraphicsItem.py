from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QBrush, QPainterPath, QPen, QPolygonF
from PySide6.QtWidgets import QGraphicsItemGroup, QGraphicsItem, QGraphicsPathItem, QGraphicsPolygonItem, \
    QGraphicsEllipseItem, QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent
from PiDrawObj.PiGraphEdit import PiEditCacheItem
from PiMapObj.PiFeature import PiFeature
from PiMapObj.PiGeometry import PiGeometry
from PiMapObj.PiPoint import PiPoint
from PiMapObj.PiPolygon import PiPolygon
from PiMapObj.PiPolyline import PiPolyline
from PiConstant import PiGeometryTypeConstant, PiGraphModeConstant

class PiPainterPath(QPainterPath):
    def __init__(self):
        super().__init__()
    
    def addPath(self, path) -> None:
        return super().addPath(path)
    def addPolygon(self, polygon) -> None:
        return super().addPolygon(polygon)
    def addEllipse(self,ellipse) -> None:
        return super().addEllipse(ellipse)
        

class PiGraphicsItem(QGraphicsPathItem):
    def __init__(self, geometry: PiPolyline|PiPolygon|PiPoint, parent: QGraphicsItem, draw_control,pen:QPen,brush:QBrush):
        super().__init__(parent = parent)
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.last_pos = QPointF(0, 0)
        self.load(pen,brush)
    
    def load(self,pen,brush):
        x = self.geometry.get_x()
        y = self.geometry.get_y()
        count = self.geometry.count
        match self.geometry.type:
            case PiGeometryTypeConstant.point:
                self.point_list = [QPointF(x / self.draw.scale,y / self.draw.scale)]
                path = QPainterPath()
                path.addEllipse(self.point_list[0],0.5,0.5)
                self.setPath(path)
                self.setPen(pen)
                self.setBrush(brush)
            case PiGeometryTypeConstant.polyline:
                self.point_list = []
                start = QPointF((x[0]) / self.draw.scale, (- y[0]) / self.draw.scale)
                self.point_list.append(start)
                path = QPainterPath(start)
                for i in range(1, count):
                    end = QPointF((x[i]) / self.draw.scale, (- y[i]) / self.draw.scale)
                    self.point_list.append(end)
                    path.lineTo(end)
                self.setPath(path)
                self.setPen(pen)
                self.setBrush(Qt.transparent)
            case PiGeometryTypeConstant.polygon:
                self.point_list = [QPointF((x[i]) / self.draw.scale, (- y[i]) / self.draw.scale) for i in range(count)]
                path = QPainterPath()
                path.addPolygon(self.point_list)
                self.setPath(path)
                self.setPen(pen)
                self.setBrush(brush)

    def shape(self) -> QPainterPath:
        return self.path().translated(self.pos())
    
    def get_point_list(self):
        return [point for point in self.point_list]

class PiGraphicsItemGroup(QGraphicsItemGroup):
    def __init__(self, layer_id, feature: PiFeature, parent: QGraphicsItem, draw_control, pen, brush):
        super().__init__()
        self.feature = feature
        self.layer_id = layer_id
        self.id = self.feature.id
        self.geometry_type = self.feature.geometry_type
        self.draw = draw_control
        self.last_pos = QPointF(0,0)
        self.point_lists = []
        collection = feature.geometry._collection
        for geometry in collection:
            item = PiGraphicsItem(geometry,parent,draw_control,pen,brush)
            self.addToGroup(item)
        self.path = QPainterPath()
        self.accept_edit = False
        self.edit_cache = None
    
    def setPen(self,pen):
        for item in self.childItems():
            item.setPen(pen)
    
    def setBrush(self,brush):
        for item in self.childItems():
            item.setBrush(brush)
    
    def setFlag(self, flag: QGraphicsItem.GraphicsItemFlag, enabled: bool = ...) -> None:
        return super().setFlag(flag, enabled)
    
    def setFlags(self, flags: QGraphicsItem.GraphicsItemFlags) -> None:
        return super().setFlags(flags)
    
    def shape(self):
        path = QPainterPath()
        for item in self.childItems():
            path.addPath(item.shape())
        return path

    def get_cache(self) -> QPainterPath:
        return self.shape().translated(self.pos())

    def get_point_lists(self):
        return [[point+item.pos() for point in item.get_point_list()] for item in self.childItems()]

    def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.accept_edit == True:
            if event.button() == Qt.MouseButton.LeftButton and self.edit_cache == None:
                print("start edit feature %d" % self.id)
                self.edit_cache = PiEditCacheItem(self.draw,self)
            elif event.button() == Qt.MouseButton.RightButton and self.edit_cache != None:
                self.edit_cache.end_edit()
                self.edit_cache = None
                print("end edit feature %d" % self.id)
        else:
            super().mouseDoubleClickEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        if self.draw.view.mode == PiGraphModeConstant.dragable:
            now_pos = super().pos()
            delta_pos = now_pos - self.last_pos
            self.feature.translate(delta_pos.x() * self.draw.scale, - delta_pos.y() * self.draw.scale)
            self.last_pos = now_pos
