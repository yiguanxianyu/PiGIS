from PySide6 import QtGui
from PySide6.QtCore import QPoint, QPointF, Qt
from PySide6.QtWidgets import QGraphicsView

from PiConstant import PiGraphModeConstant
from PiDrawObj.PiGraphDrag import PiGraphDrag
from PiDrawObj.PiGraphDraw import PiGraphDraw
from PiDrawObj.PiGraphEdit import PiGraphEdit
from PiDrawObj.PiGraphMove import PiGraphMove
from PiMapObj.PiLayer import PiLayer


class PiGraphView(QGraphicsView):
    def __init__(self, widget):
        super().__init__(widget)
        self.mode = PiGraphModeConstant.moveable  # 默认处于移动模式
        self.last_mode = PiGraphModeConstant.dragable  # 默认处于拖动模式
        self.mouse_pressed_button = Qt.MouseButton.LeftButton
        self.center = QPointF(0, 0)
        self.show_scale = 1
        self.ui_init()
        self.display_init()

    def ui_init(self):
        # 绘画控制类
        self.draw_control = PiGraphDraw(view=self)
        self.setScene(self.draw_control.get_scene())
        # 视图拖动类
        self.move_control = PiGraphMove(view=self)
        # 编辑控制类
        self.drag_control = PiGraphDrag(view=self)
        self.edit_control = PiGraphEdit(view=self)

    def display_init(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setDragMode(QGraphicsView.NoDrag)

    def set_show_scale(self, show_scale):
        ratio = show_scale / self.show_scale
        self.scale(ratio, ratio)
        self.show_scale = show_scale

    def centerOn(self, pos: QPointF | QPoint):
        super().centerOn(pos)
        self.center = pos

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        if self.mode == PiGraphModeConstant.moveable:
            wheelValue = event.angleDelta().y()
            ratio = wheelValue / 1200 + 1
            self.scale(ratio, ratio)
            self.show_scale *= ratio
            self.centerOn(self.center)

    def super_mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        return super().mouseMoveEvent(event)

    def super_mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        return super().mousePressEvent(event)

    def super_mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        return super().mouseReleaseEvent(event)
    # '''
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        match self.mode:
            case PiGraphModeConstant.dragable:
                self.drag_control.mousePressEvent(event)
            case PiGraphModeConstant.moveable:
                self.move_control.mousePressEvent(event)
            case PiGraphModeConstant.editable:
                self.edit_control.mousePressEvent(event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        match self.mode:
            case PiGraphModeConstant.dragable:
                self.drag_control.mouseMoveEvent(event)
            case PiGraphModeConstant.moveable:
                self.move_control.mouseMoveEvent(event)
            case PiGraphModeConstant.editable:
                self.edit_control.mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.mouse_pressed_button = event.button()
        match self.mode:
            case PiGraphModeConstant.dragable:
                self.drag_control.mouseReleaseEvent(event)
            case PiGraphModeConstant.moveable:
                self.move_control.mouseReleaseEvent(event)
            case PiGraphModeConstant.editable:
                self.edit_control.mouseReleaseEvent(event)

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.text() == "c":
            self.mode_turn_move()
        elif event.text() == "d":
            self.mode_turn_drag_layer(1)
        elif event.text() == "e":
            self.mode_turn_edit_layer(1)

        # return super().keyReleaseEvent(event)

    def get_layer_by_id(self,layer_id) -> PiLayer:
        return self.drag_control.layers[layer_id]

    def mode_turn_move(self):
        if self.mode != PiGraphModeConstant.moveable:
            self.drag_control.end_drag()
            self.edit_control.end_edit()
            self.mode = PiGraphModeConstant.moveable

    def mode_turn_drag_layer(self,layer_id):
        if self.mode != PiGraphModeConstant.dragable:
            self.drag_control.start_drag_on(layer_id)
            self.mode = PiGraphModeConstant.dragable

    def mode_turn_edit_layer(self,layer_id):
        if self.mode != PiGraphModeConstant.editable:
            self.edit_control.start_edit_on(layer_id)
            self.mode = PiGraphModeConstant.editable

