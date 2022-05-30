import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QSizePolicy, QPushButton
from collections import Counter

class MainWidow(QWidget):
    def __init__(self):
        super(MainWidow, self).__init__()
        self.gui()
        self.setLayout(self.wholelayout)
        self.setWindowTitle("画图")
        self.setGeometry(0, 0, 700, 400)
 
    def gui(self):
        self.wholelayout = QVBoxLayout()
        self.content = QPushButton("Welcome back!")
        self.figure = PlotScatter()
        self.wholelayout.addWidget(self.content)
        self.wholelayout.addWidget(self.figure)
        self.content.clicked.connect(self.save)
 
    def save(self):
        self.figure.pixmap.save("D:/123now.png", "png", 300)
 
 
class PlotScatter(QWidget):
    def __init__(self):
        super(PlotScatter, self).__init__()
        self.pixmap = QtGui.QPixmap(self.rect().width(), self.rect().height())
        self.pixmap.fill(QtCore.Qt.GlobalColor.transparent)
        self.draw_image()
 
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter_ = QtGui.QPainter()
        painter_.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        painter_.begin(self)
        painter_.drawPixmap(self.rect(), self.pixmap, self.pixmap.rect())
        painter_.end()
 
    def draw_image(self):
        painter = QtGui.QPainter(self.pixmap)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.RenderHint.TextAntialiasing, True)
        brush = QtGui.QBrush()
        brush.setColor(QtCore.Qt.GlobalColor.blue)
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        _rect = self.pixmap.rect()
        rect = QtCore.QRect(_rect.x() + 50, _rect.y() + 10, _rect.width() - 60, _rect.height() - 20)
        height = rect.height()
        width = rect.width()
        item_width = width / 5
        item_height = height / 2
        QPointF = QtCore.QPointF
 
        pen = QtGui.QPen()
        pen.setColor(QtCore.Qt.GlobalColor.lightGray)
 
        height_list = list()
        painter.setBrush(brush)
        for i in range(6):
            if i > 0:
                painter.save()
                painter.setPen(pen)
                painter.drawLine(QPointF(i * item_width + rect.x(), 0), QPointF(i * item_width + rect.x(), height - 40))
                painter.restore()
            else:
                painter.drawLine(QPointF(i * item_width + rect.x(), 0), QPointF(i * item_width + rect.x(), height - 40))
        for i in range(5):
            random.seed(i * 5)
            loc_ = item_width * i + item_width / 2 + rect.x()
            _temp_height = random.randint(20, int(height - 40))
            height_list.append(_temp_height)
            for loc_i in self.loc_sep(loc_, item_width / 10, random.randint(1, 7)):
                painter.drawEllipse(QtCore.QPointF(loc_i, _temp_height), 2, 2)
 
        for i in range(5):
            _rect = QtCore.QRectF(item_width * i + rect.x(), height - 30, item_width, 20)
            painter.drawText(_rect, QtCore.Qt.AlignmentFlag.AlignCenter, f"year{2020 + i}")
 
        unique_value = list(Counter(height_list))
        for i in unique_value:
            _rect = QtCore.QRectF(0, i - 10, 40, 20)
            painter.drawLine(QtCore.QPoint(45, i), QtCore.QPoint(50, i))
            painter.drawText(_rect, QtCore.Qt.AlignmentFlag.AlignRight, f"{rect.height() - i}")
 
    @staticmethod
    def loc_sep(loc, width, number):
        number_2 = number // 2
        number_1 = number % 2
        list_right = list()
        for i in range(1, number_2+1):
            list_right.append(i*width)
        list_left = [-i for i in list_right[::-1]]
 
        if number_1 == 1:
            list_left.append(0)
            list_left.extend(list_right)
            return [loc + j for j in list_left]
        else:
            list_left.extend(list_right)
            _temp = [loc_i + 0.5 * width if loc_i < 0 else loc_i - 0.5 * width for loc_i in list_left]
            return [loc + j for j in _temp]
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidow()
    widget.show()
    sys.exit(app.exec())
