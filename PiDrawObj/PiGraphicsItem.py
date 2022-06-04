
from PySide6.QtCore import QLineF
from PySide6.QtWidgets import QGraphicsItemGroup,QGraphicsLineItem,QGraphicsItem
from PySide6.QtGui import QAccessible
from PiMapObj.PiLayer import PiLayer
from PiMapObj.PiProjection import PiProjection
from PiMapObj.PiConstant import PiGeometryTypeConstant

class QGraphicsPolylineItem(QGraphicsItemGroup):
    def __init__(self,QPoints:list,parent:QGraphicsItem = None):
        super().__init__()
        count = len(QPoints)
        start = QPoints[0]
        for i in range(1,count):
            end = QPoints[i]
            member = QGraphicsLineItem(QLineF(start,end),parent)
            self.addToGroup(member)
            start = end
    
    def addToGroup(self, item: QGraphicsItem) -> None:
        return super().addToGroup(item)