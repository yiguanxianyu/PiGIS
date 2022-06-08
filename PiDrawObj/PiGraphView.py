from enum import Enum
from PySide6.QtCore import QPoint, QPointF, QRectF,QMetaObject,Qt
from PySide6.QtWidgets import QFrame,QGraphicsView, QRubberBand
from PySide6 import QtGui
from PiDrawObj.PiGraphDraw import PiGraphDraw
from PiConstant import PiGraphModeConstant
from PiDrawObj.PiGraphEdit import PiGraphEdit


class PiGraphView(QGraphicsView):
    def __init__(self,widget):
        super().__init__(widget)
        self.mode = PiGraphModeConstant.moveable # 默认处于移动模式
        self.last_mode = PiGraphModeConstant.editable # 默认处于显示模式
        self.ui_init()
        self.display_init()
        self.center = QPointF(0,0)
        self.show_scale = 1

    def ui_init(self):
        # 绘画控制类
        self.draw_control = PiGraphDraw(view = self)
        self.setScene(self.draw_control.get_scene())
        # 视图拖动类
        self.mouse_pos_before = QPointF()
        c = Qt.MouseButton
        self.is_moving = False
        # 编辑控制类
        self.edit_control = PiGraphEdit(view = self)


    def display_init(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setDragMode(QGraphicsView.NoDrag) 

    def set_show_scale(self,show_scale):
        ratio = show_scale / self.show_scale
        self.scale(ratio,ratio)
        self.show_scale = show_scale
        
    def centerOn(self,pos:QPointF | QPoint):
        super().centerOn(pos)
        self.center = pos
    
    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        if self.mode == PiGraphModeConstant.moveable:
            wheelValue = event.angleDelta().y()
            ratio = wheelValue / 1200 + 1
            self.scale(ratio, ratio)
            self.show_scale *= ratio
            self.centerOn(self.center)
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
        self.mouse_pressed_button = event.button() 
        if self.mode == PiGraphModeConstant.editable:
            return super().mousePressEvent(event)
        elif self.mode == PiGraphModeConstant.moveable:
            if self.is_moving == False:
                self.is_moving = True
                self.mouse_pos_before = event.pos()
                print(self.mapToScene(self.mouse_pos_before))
            elif self.is_moving == True:
                self.setCursor(Qt.ClosedHandCursor)
                pass

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.mode == PiGraphModeConstant.editable:
            return super().mouseMoveEvent(event)
        elif self.mode == PiGraphModeConstant.moveable:
            if self.is_moving == True:
                self.setCursor(Qt.ClosedHandCursor)
                mouse_pos_now = event.pos()
                d = self.mapToScene(mouse_pos_now) - self.mapToScene(self.mouse_pos_before)
                self.center -= d
                self.centerOn(self.center)
                self.mouse_pos_before = mouse_pos_now

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.mode == PiGraphModeConstant.editable:
            super().mouseReleaseEvent(event)
        elif self.mode == PiGraphModeConstant.moveable:
            self.setCursor(Qt.ArrowCursor)
            self.is_moving = False
        return
    #'''
    '''
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if self.mode == PiGraphModeConstant.moveable:
            pass
        elif self.mode == PiGraphModeConstant.editable:
            if event.text() == "c":
                #self.setDragMode(QGraphicsView.ScrollHandDrag) 
                self.draw_control.load_graphics()
                self.mode = PiGraphModeConstant.moveable
                self.setScene(self.draw_control.get_scene(self.mode))

        #return super().wheelEvent(event)
    '''

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.text() == "c":
            if self.mode != PiGraphModeConstant.moveable:
                #self.setDragMode(QGraphicsView.ScrollHandDrag) 
                #self.draw_control.load_graphics()
                self.last_mode = self.mode
                self.mode = PiGraphModeConstant.moveable
            elif self.mode == PiGraphModeConstant.moveable:
                #self.setDragMode(QGraphicsView.NoDrag) 
                self.mode = self.last_mode
                self.is_moving = False
        elif self.mode == PiGraphModeConstant.editable:
            pass

        #return super().keyReleaseEvent(event)