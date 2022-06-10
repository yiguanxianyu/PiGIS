from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QMouseEvent


class PiGraphMove():
    def __init__(self, view) -> None:
        self.view = view
        self.draw_control = self.view.draw_control
        self.mouse_pos_before = QPointF()
        self.is_moving = False

    def mousePressEvent(self, event: QMouseEvent):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            if self.is_moving == False:
                self.is_moving = True
                self.mouse_pos_before = event.pos()
            elif self.is_moving == True:
                self.view.setCursor(Qt.ClosedHandCursor)
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            pass
        return self.view.super_mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.is_moving == True:
            self.view.setCursor(Qt.ClosedHandCursor)
            mouse_pos_now = event.pos()
            d = self.view.mapToScene(mouse_pos_now) - self.view.mapToScene(self.mouse_pos_before)
            self.view.center -= d
            self.view.centerOn(self.view.center)
            self.mouse_pos_before = mouse_pos_now
        return self.view.super_mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.view.mouse_pressed_button == Qt.MouseButton.LeftButton:
            self.view.setCursor(Qt.ArrowCursor)
            self.is_moving = False
        elif self.view.mouse_pressed_button == Qt.MouseButton.RightButton:
            pass
        return self.view.super_mouseReleaseEvent(event)
