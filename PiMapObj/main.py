import sys

from PySide6 import QtCore, QtWidgets, QtGui

from PiConstant import PiGeometryTypeConstant
from PiLayer import PiLayer
from PiPolyline import PiPolyline
from PiProjection import PiProjection


class PiWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.whole_layout = None
        self.create_gui()
        self.setLayout(self.wholelayout)
        self.setWindowTitle("画图")
        self.setGeometry(0, 0, 1000, 500)

    def create_gui(self):
        self.wholelayout = QtWidgets.QVBoxLayout()
        self.content = QtWidgets.QPushButton("Welcome back!")
        self.figure = PiShow()
        self.wholelayout.addWidget(self.content)
        self.wholelayout.addWidget(self.figure)
        self.content.clicked.connect(self.save)

    def save(self):
        self.figure.pixmap.save("data.png", "png", 300)


class PiDrawAttr():
    def __init__(self):
        self.extent = [0, 0, 0, 0]  # minx,miny,maxx,maxy
        self.scale = 0  # 1 pixel = scale unit

    def set_attr(self, minx, miny, maxx, maxy, scale):
        self.extent = [minx, miny, maxx, maxy]  # minx,miny,maxx,maxy
        self.scale = scale  # 1 pixel = scale unit


class PiShow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.pixmap = QtGui.QPixmap(1000, 500)
        self.pixmap.fill(QtCore.Qt.GlobalColor.white)
        self.draw_attr = PiDrawAttr()
        self.painter = None

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter_ = QtGui.QPainter()
        painter_.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        painter_.begin(self)
        painter_.drawPixmap(self.rect(), self.pixmap, self.pixmap.rect())
        painter_.end()

    def draw_image(self, layer: PiLayer = None, proj: PiProjection = None) -> None:
        # self.painter
        painter = QtGui.QPainter(self.pixmap)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.RenderHint.TextAntialiasing, True)
        self.painter = painter
        # draw_attr
        features = layer.features
        mbr = features.get_mbr()
        yscale = (mbr.maxy - mbr.miny) / self.height()
        xscale = (mbr.maxx - mbr.minx) / self.width()
        print(self.rect())
        print(yscale, xscale)
        scale = max(yscale, xscale)
        x_offset = mbr.minx
        y_offset = mbr.miny
        brush = QtGui.QBrush()
        brush.setColor(QtCore.Qt.GlobalColor.blue)
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        pen = QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine)
        painter.setPen(pen)

        for feature in features.features:
            geometry = feature.geometry
            collection = geometry._collection
            if layer.geometry_type == PiGeometryTypeConstant().multipolyline:
                for polyline in collection:
                    self.draw_polyline(polyline, x_offset, y_offset, scale)

        # painter.drawLine(20, 40, 250, 40)
        # painter.drawLine(20, 100, 250, 100)

    def draw_polyline(self, polyline: PiPolyline, x_offset, y_offset, scale):
        ymax = self.height()
        count = polyline.count
        start_x = (polyline.get_x()[0] - x_offset) / scale
        start_y = (polyline.get_y()[0] - y_offset) / scale
        for i in range(1, count):
            end_x = (polyline.get_x()[i] - x_offset) / scale
            end_y = (polyline.get_y()[i] - y_offset) / scale
            self.painter.drawLine(start_x, ymax - start_y, end_x, ymax - end_y)
            start_x, start_y = end_x, end_y


if __name__ == "__main__":
    layer = PiLayer()
    proj = PiProjection()
    # layer.load("图层文件/省会城市.lay")
    layer.load("图层文件/国界线.lay")
    # print(layer.fields)
    # layer.load("图层文件/省级行政区.lay")
    proj.load("图层文件/图层文件坐标系统说明.txt")

    app = QtWidgets.QApplication(sys.argv)
    main = PiWindow()
    main.figure.draw_image(layer, proj)
    main.show()
    sys.exit(app.exec())

    # print(layer.get_geometry_type())
    # print(layer.get_fields())
