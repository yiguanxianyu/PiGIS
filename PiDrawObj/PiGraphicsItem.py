from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QPainterPath
from PySide6.QtWidgets import QGraphicsItemGroup, QGraphicsItem, QGraphicsPathItem, QGraphicsPolygonItem, \
    QGraphicsEllipseItem, QGraphicsSceneDragDropEvent
from PiMapObj.PiFeature import PiFeature

from PiMapObj.PiPolygon import PiPolygon
from PiMapObj.PiPolyline import PiPolyline

class PiGraphicsItem(QGraphicsItemGroup):
    def __init__(self, geometry: PiPolyline, parent: QGraphicsItem, draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.last_pos = QPointF(0, 0)

class PiGraphicsItemGroup(QGraphicsItemGroup):
    def __init__(self, feature: PiFeature,parent: QGraphicsItem, draw_control):
        super().__init__()
        self.feature = feature
        self.id = self.feature.id
        self.geometry_type = self.feature.geometry_type
        self.draw = draw_control
        self.last_pos = QPointF(0,0)
        if self.geometry_type == 0:
            pass

class PiGraphicsPolylineItem(QGraphicsItemGroup):
    def __init__(self, geometry: PiPolyline, parent: QGraphicsItem, draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.last_pos = QPointF(0, 0)
        self.member = QGraphicsPathItem()
        self.loadMember(parent)
        self.addToGroup(self.member)

    def loadMember(self, parent):
        polyline = self.geometry
        x, y = polyline.get_x(), polyline.get_y()
        start = QPointF((x[0]) / self.draw.scale, (- y[0]) / self.draw.scale)
        path = QPainterPath(start)
        for i in range(1, polyline.count):
            end = QPointF((x[i]) / self.draw.scale, (- y[i]) / self.draw.scale)
            path.lineTo(end)
        self.member = QGraphicsPathItem(path, parent)
        self.member.setBrush(Qt.transparent)

    def addToGroup(self, item: QGraphicsItem) -> None:
        return super().addToGroup(item)

    def setFlags(self, flags) -> None:
        return super().setFlags(flags)

    def setPen(self, pen):
        self.member.setPen(pen)

    def polyline(self):
        pos = super().pos() - self.draw.expand_pos
        '''return [item.line().translated(pos) for item in self.member]'''
        return self.member.path().translated(pos)

    def shape(self) -> QPainterPath:
        path = QPainterPath()
        path.addPath(self.polyline())
        return path


class PiGraphicsPolygonItem(QGraphicsItemGroup):
    def __init__(self, geometry: PiPolygon, parent: QGraphicsItem, draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.member = QGraphicsPolygonItem()
        self.loadMember(parent)
        self.addToGroup(self.member)
        self.last_pos = QPointF(0, 0)

    def loadMember(self, parent):
        x, y, count = self.geometry.get_x(), self.geometry.get_y(), self.geometry.count
        qpoint_list = [QPointF((x[i]) / self.draw.scale, (- y[i]) / self.draw.scale) for i in range(count)]
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

    def shape(self):
        path = QPainterPath()
        path.addPolygon(self.polygon())
        return path

    def mouseReleaseEvent(self, event: QGraphicsSceneDragDropEvent) -> None:
        super().mouseReleaseEvent(event)
        now_pos = super().pos()
        delta_pos = now_pos - self.last_pos
        self.geometry.translate(delta_pos.x() * self.draw.scale, - delta_pos.y() * self.draw.scale)
        self.draw.mbr.union(self.geometry.get_mbr())
        self.last_pos = now_pos


class PiGraphicsEllipseItem(QGraphicsItemGroup):
    def __init__(self, geometry, parent: QGraphicsItem, draw_control):
        super().__init__()
        self.geometry = geometry
        self.id = self.geometry.id
        self.draw = draw_control
        self.member = QGraphicsEllipseItem()
        self.loadMember(parent)
        self.addToGroup(self.member)
        self.last_pos = QPointF(0, 0)

    def loadMember(self, parent):
        point = self.geometry
        xpos = (point.get_x()) / self.draw.scale
        ypos = (- point.get_y()) / self.draw.scale
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

    def ellipse(self):
        pos = super().pos() - self.draw.expand_pos
        return self.member.rect().translated(pos)
