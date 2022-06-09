from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QPainterPath
from PySide6.QtWidgets import QGraphicsItemGroup, QGraphicsItem, QGraphicsPathItem, QGraphicsPolygonItem, \
    QGraphicsEllipseItem, QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent
from PiDrawObj.PiGraphEdit import PiEditCacheItem
from PiMapObj.PiFeature import PiFeature
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
        

class PiGraphicsItem(QGraphicsItemGroup):
    def __init__(self, geometry: PiPolyline, parent: QGraphicsItem, draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.last_pos = QPointF(0, 0)

class PiGraphicsItemGroup(QGraphicsItemGroup):
    def __init__(self, layer_id, feature: PiFeature, parent: QGraphicsItem, draw_control):
        super().__init__()
        self.feature = feature
        self.layer_id = layer_id
        self.id = self.feature.id
        self.geometry_type = self.feature.geometry_type
        self.draw = draw_control
        self.last_pos = QPointF(0,0)
        self.point_lists = []
        collection = feature.geometry._collection
        if self.geometry_type == PiGeometryTypeConstant.multipolyline.value:
            for polyline in collection:
                item = PiGraphicsPolylineItem(polyline, parent, draw_control)
                super().addToGroup(item)
            pass
        elif self.geometry_type == PiGeometryTypeConstant.multipolygon.value:
            for polygon in collection:
                item = PiGraphicsPolygonItem(polygon, parent, draw_control)
                super().addToGroup(item)
            pass
        elif self.geometry_type == PiGeometryTypeConstant.multipoint.value:
            for point in collection:
                item = PiGraphicsEllipseItem(point, parent, draw_control)
                super().addToGroup(item)
            pass
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

    def get_cache(self):
        pos = super().pos() - self.draw.expand_pos
        return self.shape().translated(pos)

    def get_point_lists(self):
        pos = super().pos() - self.draw.expand_pos
        return [[point+pos for point in item.get_point_list()] for item in self.childItems()]

    def setZValue(self, z: float) -> None:
        return super().setZValue(z)

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


class PiGraphicsPolylineItem(QGraphicsItemGroup):
    def __init__(self, geometry: PiPolyline, parent: QGraphicsItem, draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.last_pos = QPointF(0, 0)
        self.member = QGraphicsPathItem()
        self.point_list = []
        self.loadMember(parent)
        self.addToGroup(self.member)

    def loadMember(self, parent):
        polyline = self.geometry
        x, y = polyline.get_x(), polyline.get_y()
        start = QPointF((x[0]) / self.draw.scale, (- y[0]) / self.draw.scale)
        self.point_list.append(start)
        path = QPainterPath(start)
        for i in range(1, polyline.count):
            end = QPointF((x[i]) / self.draw.scale, (- y[i]) / self.draw.scale)
            self.point_list.append(end)
            path.lineTo(end)
        self.member = QGraphicsPathItem(path, parent)
        self.member.setBrush(Qt.transparent)

    def addToGroup(self, item: QGraphicsItem) -> None:
        return super().addToGroup(item)

    def setFlags(self, flags) -> None:
        return super().setFlags(flags)

    def setPen(self, pen):
        self.member.setPen(pen)

    def setBrush(self,brush):
        pass

    def polyline(self):
        pos = super().pos() - self.draw.expand_pos
        '''return [item.line().translated(pos) for item in self.member]'''
        return self.member.path().translated(pos)

    def shape(self) -> QPainterPath:
        path = QPainterPath()
        path.addPath(self.polyline())
        return path

    def get_point_list(self):
        pos = super().pos() - self.draw.expand_pos
        return [point+pos for point in self.point_list]
    
    def setZValue(self, z: float) -> None:
        return super().setZValue(z)


class PiGraphicsPolygonItem(QGraphicsItemGroup):
    def __init__(self, geometry: PiPolygon, parent: QGraphicsItem, draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.point_list = []
        self.member = QGraphicsPolygonItem()
        self.loadMember(parent)
        self.addToGroup(self.member)
        self.last_pos = QPointF(0, 0)

    def loadMember(self, parent):
        x, y, count = self.geometry.get_x(), self.geometry.get_y(), self.geometry.count
        qpoint_list = [QPointF((x[i]) / self.draw.scale, (- y[i]) / self.draw.scale) for i in range(count)]
        self.point_list = qpoint_list
        self.member = QGraphicsPolygonItem(qpoint_list, parent)

    def addToGroup(self, item: QGraphicsItem) -> None:
        return super().addToGroup(item)

    def setPen(self, pen):
        return self.member.setPen(pen)

    def setBrush(self, brush):
        return self.member.setBrush(brush)

    def setFlags(self, flags) -> None:
        return super().setFlags(flags)

    def polygon(self):
        pos = super().pos() - self.draw.expand_pos
        return self.member.polygon().translated(pos)
    
    def get_geometry(self):
        return self.polygon()
    
    def get_point_list(self):
        pos = super().pos() - self.draw.expand_pos
        return [point+pos for point in self.point_list]

    def shape(self):
        path = QPainterPath()
        path.addPolygon(self.polygon())
        return path

    def setZValue(self, z: float) -> None:
        return super().setZValue(z)


class PiGraphicsEllipseItem(QGraphicsItemGroup):
    def __init__(self, geometry, parent: QGraphicsItem, draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.point_list = []
        self.member = QGraphicsEllipseItem()
        self.loadMember(parent)
        self.addToGroup(self.member)
        self.last_pos = QPointF(0, 0)

    def loadMember(self, parent):
        point = self.geometry
        xpos = (point.get_x()) / self.draw.scale
        ypos = (- point.get_y()) / self.draw.scale
        self.point_list = QPointF(xpos,ypos)
        self.member = QGraphicsEllipseItem(xpos - 1, ypos - 1, 2, 2, parent)

    def addToGroup(self, item: QGraphicsItem) -> None:
        return super().addToGroup(item)

    def setPen(self, pen):
        return self.member.setPen(pen)

    def setBrush(self, brush):
        return self.member.setBrush(brush)

    def shape(self):
        path = QPainterPath()
        path.addEllipse(self.ellipse())
        return path

    def setFlags(self, flags) -> None:
        return super().setFlags(flags)
    
    def get_point_list(self):
        pos = super().pos() - self.draw.expand_pos
        return [point+pos for point in self.point_list]

    def ellipse(self):
        pos = super().pos() - self.draw.expand_pos
        return self.member.rect().translated(pos)

    def setZValue(self, z: float) -> None:
        return super().setZValue(z)

    def get_geometry(self):
        return self.ellipse()
