from enum import Enum
from PySide6.QtCore import QPoint, QPointF, QRectF,QMetaObject,Qt
from PySide6.QtWidgets import QFrame,QGraphicsView
from PySide6 import QtGui
from PiDrawObj.PiGraphDraw import PiGraphDraw

class PiGraphMode(Enum):
    editable = 0
    moveable = 1


class PiGraphView(QGraphicsView):
    def __init__(self,widget):
        super().__init__(widget)
        self.draw_control = PiGraphDraw()
        self.sc = 1
        self.mode = PiGraphMode.editable # 默认处于显示模式
        self.is_moving = False
        self.center = QPointF(0,0)
        self.last_pos = QPointF()
        self.setDragMode(QGraphicsView.NoDrag) 

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        if self.mode == PiGraphMode.moveable:
            self.centerOn(self.center)
            wheelValue = event.angleDelta().y()
            ratio = wheelValue / 1200 + 1
            self.scale(ratio, ratio)
            self.sc *= ratio
            print(self.transform())
            '''
            if self.sc > 5:
                self.draw_control.scale /= 5 
                self.scale(1/self.sc,1/self.sc)
                self.sc = 1
                self.draw_control.load_graphics()
            elif self.sc < 0.2:
                self.draw_control.scale /= 0.2
                self.scale(1/self.sc,1/self.sc)
                self.sc = 1
                self.draw_control.load_graphics()
            #'''

    #'''
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.mode == PiGraphMode.editable:
            return super().mousePressEvent(event)
        elif self.mode == PiGraphMode.moveable:
            if self.is_moving == False:
                self.is_moving = True
                self.last_pos = event.pos()
                pass
            elif self.is_moving == True:
                pass

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.mode == PiGraphMode.editable:
            return super().mouseMoveEvent(event)
        elif self.mode == PiGraphMode.moveable:
            if self.is_moving == True:
                now_pos = event.pos()
                d = self.mapToScene(now_pos) - self.mapToScene(self.last_pos)
                self.center -= d
                self.centerOn(self.center)
                print(self.center)
                self.last_pos = now_pos

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.mode == PiGraphMode.editable:
            super().mouseReleaseEvent(event)
        elif self.mode == PiGraphMode.moveable:
            self.is_moving = False
        return
    #'''

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if self.mode == PiGraphMode.moveable:
            pass
        elif self.mode == PiGraphMode.editable:
            if event.text() == "c":
                self.setDragMode(QGraphicsView.ScrollHandDrag) 
                self.mode = PiGraphMode.moveable
                self.draw_control.moveable_show()

        #return super().wheelEvent(event)

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if self.mode == PiGraphMode.moveable:
            if event.text() == "c":
                self.setDragMode(QGraphicsView.NoDrag) 
                self.mode = PiGraphMode.editable
                self.draw_control.editable_show()
                self.is_moving = False
        elif self.mode == PiGraphMode.editable:
            pass

        #return super().keyReleaseEvent(event)