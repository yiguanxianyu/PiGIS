from PySide6 import QtGui
from PySide6.QtCore import QPoint, QPointF, Qt
from PySide6.QtWidgets import QGraphicsView

from PiConstant import PiGraphModeConstant
from PiDrawObj.PiGraphAdd import PiGraphAdd
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
        self.setMouseTracking(True)
        self.window = None
        print(self.rect())
    
    def set_window(self,window):
        self.window = window

    def ui_init(self):
        # 绘画控制类
        self.draw_control = PiGraphDraw(view=self)
        self.setScene(self.draw_control.get_scene())
        # 视图拖动类
        self.move_control = PiGraphMove(view=self)
        # 编辑控制类
        self.drag_control = PiGraphDrag(view=self)
        self.edit_control = PiGraphEdit(view=self)
        self.add_control = PiGraphAdd(view=self)

    def display_init(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setDragMode(QGraphicsView.NoDrag)

    def set_show_scale(self, show_scale):
        ratio = show_scale / self.show_scale
        self.scale(ratio, ratio)
        self.show_scale = show_scale
        self.window.update_scale(self.draw_control.scale / self.show_scale)

    def centerOn(self, pos: QPointF | QPoint):
        super().centerOn(pos)
        self.center = pos

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        if self.mode == PiGraphModeConstant.moveable:
            wheelValue = event.angleDelta().y()
            ratio = wheelValue / 1200 + 1
            self.set_show_scale(self.show_scale*ratio)

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
            case PiGraphModeConstant.addable:
                self.add_control.mousePressEvent(event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        view_pos = QPoint(event.x(),event.y())
        scene_pos = self.mapToScene(view_pos)
        scale = self.draw_control.scale
        self.window.statusBar.update_coord(scene_pos.x()*scale, scene_pos.y()*scale)
        match self.mode:
            case PiGraphModeConstant.dragable:
                self.drag_control.mouseMoveEvent(event)
            case PiGraphModeConstant.moveable:
                self.move_control.mouseMoveEvent(event)
            case PiGraphModeConstant.editable:
                self.edit_control.mouseMoveEvent(event)
            case PiGraphModeConstant.addable:
                self.add_control.mouseMoveEvent(event)
            

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.mouse_pressed_button = event.button()
        match self.mode:
            case PiGraphModeConstant.dragable:
                self.drag_control.mouseReleaseEvent(event)
            case PiGraphModeConstant.moveable:
                self.move_control.mouseReleaseEvent(event)
            case PiGraphModeConstant.editable:
                self.edit_control.mouseReleaseEvent(event)
            case PiGraphModeConstant.addable:
                self.add_control.mouseReleaseEvent(event)

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        # 键盘暂且用来测试 0折线 1多边形 2点
        test_layer_id = 1
        if event.text() == "c":
            self.mode_turn_move()
        elif event.text() == "d":
            self.mode_turn_drag_layer(test_layer_id)
        elif event.text() == "e":
            self.mode_turn_edit_layer(test_layer_id)
        elif event.text() == "a":
            self.mode_turn_add_layer(test_layer_id)
        elif event.text() == "s":
            self.visulize_text_layer(test_layer_id)
        elif event.text() == "l":
            self.draw_control.save_fig('lalala.bmp')

        # return super().keyReleaseEvent(event)

    def get_layer_by_id(self,layer_id) -> PiLayer:
        return self.drag_control.layers[layer_id]

    def mode_turn_move(self):
        if self.mode != PiGraphModeConstant.moveable:
            self.mode = PiGraphModeConstant.moveable

    def mode_turn_drag_layer(self,layer_id):
        if self.mode != PiGraphModeConstant.dragable:
            self.add_control.end_add()
            self.edit_control.end_edit()
            self.drag_control.start_drag_on(layer_id)
            self.mode = PiGraphModeConstant.dragable

    def mode_turn_edit_layer(self,layer_id):
        if self.mode != PiGraphModeConstant.editable:
            self.add_control.end_add()
            self.edit_control.start_edit_on(layer_id)
            self.drag_control.end_drag()
            self.mode = PiGraphModeConstant.editable
    
    def mode_turn_add_layer(self,layer_id):
        if self.mode != PiGraphModeConstant.addable:
            self.add_control.start_add_on(layer_id)
            self.edit_control.end_edit()
            self.drag_control.end_drag()
            self.mode = PiGraphModeConstant.addable

    def window_to_map(self,window,window_pos:QPoint) -> QPointF:
        view_pos = self.mapFrom(window,window_pos)
        scene_pos = self.mapToScene(view_pos)
        draw_scale = self.draw_control.scale
        map_pos = QPointF(scene_pos.x()*draw_scale,scene_pos.y()*draw_scale)
        return map_pos
        pass

    def add_layer_text(self,layer_id):
        self.draw_control.add_layer_text(layer_id)
    
    def delete_layer_text(self,layer_id):
        self.draw_control.delete_layer_text(layer_id)



