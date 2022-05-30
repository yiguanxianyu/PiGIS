import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QPointF

from PiMapObj.PiConstant import PiGeometryTypeConstant
from PiMapObj.PiLayer import PiLayer
from PiMapObj.PiPoint import PiPoint
from PiMapObj.PiPolygon import PiPolygon
from PiMapObj.PiPolyline import PiPolyline
from PiMapObj.PiProjection import PiProjection


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


class PiShow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.x_offset = 0
        self.y_offset = 0
        self.scale = 0  # 1 pixel = scale unit
        self.layers = []
        self.projs = []
        self.painter = None

    def update_draw_attr(self):
        layer = self.layers[0]
        proj = self.projs[0]
        features = layer.features
        mbr = features.get_mbr()
        yscale = (mbr.maxy - mbr.miny) / self.height()
        xscale = (mbr.maxx - mbr.minx) / self.width()
        self.scale = max(yscale, xscale)
        self.x_offset = mbr.minx
        self.y_offset = mbr.miny

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter_ = QtGui.QPainter()
        # painter_.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        pixmap = QtGui.QPixmap(self.rect().width(), self.rect().height())
        pixmap.fill(QtCore.Qt.GlobalColor.transparent)
        self.update_draw_attr()
        for i in range(len(self.layers)):
            layer = self.layers[i]
            proj = self.projs[i]
            self.draw_image(pixmap, layer, proj)
        painter_.begin(self)
        painter_.drawPixmap(self.rect(), pixmap, pixmap.rect())
        painter_.end()

    def add_layer(self, layer, proj):
        self.layers.append(layer)
        self.projs.append(proj)

    def draw_image(self, pixmap: QtGui.QPixmap = None, layer: PiLayer = None, proj: PiProjection = None) -> None:
        # self.painter
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.RenderHint.TextAntialiasing, True)
        # draw_attr
        x_offset, y_offset, scale = self.x_offset, self.y_offset, self.scale
        features = layer.features
        brush = QtGui.QBrush()
        brush.setColor(QtCore.Qt.GlobalColor.blue)
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        pen = QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(brush)

        for feature in features.features:
            geometry = feature.geometry
            collection = geometry._collection
            if layer.geometry_type == PiGeometryTypeConstant().multipolyline:
                for polyline in collection:
                    self.draw_polyline(painter, polyline, x_offset, y_offset, scale)
            elif layer.geometry_type == PiGeometryTypeConstant().multipolygon:
                for polygon in collection:
                    self.draw_polygon(painter, polygon, x_offset, y_offset, scale)
            elif layer.geometry_type == PiGeometryTypeConstant().multipoint:
                for point in collection:
                    self.draw_point(painter, point, x_offset, y_offset, scale)

        # painter.drawLine(20, 40, 250, 40)
        # painter.drawLine(20, 100, 250, 100)

    def draw_polyline(self, painter, polyline: PiPolyline, x_offset, y_offset, scale):
        y_max = self.height()
        count = polyline.count

        points = []
        for i in range(count):
            end_x = (polyline.get_x()[i] - x_offset) / scale
            end_y = (polyline.get_y()[i] - y_offset) / scale
            points.append(QPointF(end_x, y_max - end_y))

        painter.drawPolyline(points)

    def draw_polygon(self, painter, polygon: PiPolygon, x_offset, y_offset, scale):
        ymax = self.height()
        count = polygon.count
        point_list = [
            QtCore.QPoint((polygon.get_x()[i] - x_offset) / scale, ymax - (polygon.get_y()[i] - y_offset) / scale) for i
            in range(count)]
        painter.drawPolygon(point_list)

    def draw_point(self, painter, point: PiPoint, x_offset, y_offset, scale):
        ymax = self.height()
        count = 1
        ptx = (point.get_x() - x_offset) / scale
        pty = ymax - (point.get_y() - y_offset) / scale
        painter.drawEllipse(ptx, pty, 5, 5)


if __name__ == "__main__":
    layer = PiLayer()
    layer2 = PiLayer()
    layer3 = PiLayer()
    proj = PiProjection()
    # layer.load("图层文件/省会城市.lay")
    # layer.load("图层文件/国界线.lay")
    # print(layer.fields)
    layer.load("PiMapObj/图层文件/省级行政区.lay")
    layer2.load("PiMapObj/图层文件/国界线.lay")
    layer3.load("PiMapObj/图层文件/省会城市.lay")
    proj.load("PiMapObj/图层文件/图层文件坐标系统说明.txt")

    app = QtWidgets.QApplication(sys.argv)
    main = PiWindow()
    main.figure.add_layer(layer, proj)
    main.figure.add_layer(layer2, proj)
    main.figure.add_layer(layer3, proj)
    main.show()
    sys.exit(app.exec())

    # print(layer.get_geometry_type())
    # print(layer.get_fields())
