
from PySide6.QtCore import QLineF, QPointF
from PySide6.QtWidgets import QGraphicsItemGroup,QGraphicsLineItem,QGraphicsItem,QGraphicsPolygonItem,QGraphicsEllipseItem, QGraphicsSceneDragDropEvent
from PySide6.QtGui import QAccessible
from PiMapObj.PiLayer import PiLayer
from PiMapObj.PiProjection import PiProjection
from PiMapObj.PiPolygon import PiPolygon
from PiMapObj.PiPolyline import PiPolyline
from PiConstant import PiGeometryTypeConstant


class PiGraphicsPolylineItem(QGraphicsItemGroup):
    def __init__(self, geometry:PiPolyline, parent:QGraphicsItem, draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.loadMember(parent)
        for item in self.member:
            self.addToGroup(item)
        self.last_pos = QPointF(0,0)
    
    def loadMember(self,parent):
        self.member = []
        polyline = self.geometry
        x,y = polyline.get_x(),polyline.get_y()
        start = QPointF((x[0] - self.draw.leftup_x) / self.draw.scale, (self.draw.leftup_y - y[0]) / self.draw.scale)
        for i in range(1,polyline.count):
            end = QPointF((x[i] - self.draw.leftup_x) / self.draw.scale, (self.draw.leftup_y - y[i]) / self.draw.scale)
            item = QGraphicsLineItem(QLineF(start,end),parent)
            self.member.append(item)
            start = end

    def addToGroup(self, item: QGraphicsItem) -> None:
        return super().addToGroup(item)

    def setFlags(self, flags) -> None:
        return super().setFlags(flags)
    
    def polyline(self):
        pos = super().pos()-self.draw.expand_pos
        return [item.line().translated(pos) for item in self.member]

class PiGraphicsPolygonItem(QGraphicsItemGroup):
    def __init__(self,geometry:PiPolygon,parent:QGraphicsItem,draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.loadMember(parent)
        self.addToGroup(self.member)
        self.last_pos = QPointF(0,0)

    def loadMember(self,parent):
        x,y,count = self.geometry.get_x(),self.geometry.get_y(),self.geometry.count
        qpoint_list = [QPointF((x[i] - self.draw.leftup_x) / self.draw.scale, (self.draw.leftup_y - y[i]) / self.draw.scale) for i in range(count)]
        self.member = QGraphicsPolygonItem(qpoint_list,parent)
    
    def addToGroup(self, item: QGraphicsItem) -> None:
        return super().addToGroup(item)

    def setPen(self,pen):
        return self.member.setPen(pen)
    
    def setFlags(self, flags) -> None:
        return super().setFlags(flags)
    
    def polygon(self):
        pos = super().pos()-self.draw.expand_pos
        return self.member.polygon().translated(pos)
    
    def mouseReleaseEvent(self, event: QGraphicsSceneDragDropEvent) -> None:
        super().mouseReleaseEvent(event)
        now_pos = super().pos()
        delta_pos = now_pos - self.last_pos
        self.geometry.translate(delta_pos.x() * self.draw.scale,- delta_pos.y() * self.draw.scale)
        self.draw.mbr.union(self.geometry.get_mbr())
        self.last_pos = now_pos

class PiGraphicsEllipseItem(QGraphicsItemGroup):
    def __init__(self,geometry,parent:QGraphicsItem,draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.loadMember(parent)
        self.addToGroup(self.member)
        self.last_pos = QPointF(0,0)

    def loadMember(self,parent):
        point = self.geometry
        xpos = (point.get_x() - self.draw.leftup_x) / self.draw.scale
        ypos = (self.draw.leftup_y - point.get_y()) / self.draw.scale
        self.member = QGraphicsEllipseItem(xpos-1,ypos-1,2,2,parent)

    def addToGroup(self, item: QGraphicsItem) -> None:
        return super().addToGroup(item)

    def setPen(self,pen):
        return self.member.setPen(pen)
    
    def setFlags(self, flags) -> None:
        return super().setFlags(flags)

    def ellipse(self):
        pos = super().pos()-self.draw.expand_pos
        return self.member.rect().translated(pos)