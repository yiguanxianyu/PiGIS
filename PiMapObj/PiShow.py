import sys
import random
from PiMapObj.PiPoint import PiPoint
from PiMapObj.PiPolyline import PiPolyline
from PiMapObj.PiPolygon import PiPolygon
from PySide6 import QtCore, QtWidgets, QtGui
from PiMapObj.PiLayer import PiLayer
from PiMapObj.PiProjection import PiProjection
from PiMapObj.PiConstant import PiGeometryTypeConstant

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
        self.figure.pixmap.save("data.png","png",300)

class PiGraphicsItem(QtWidgets.QGraphicsItem):
    def __init__(self):
        super().__init__()
        self.x_offset = 0
        self.y_offset = 0
        self.scale = 0 # 1 pixel = scale unit
        self.layers = []
        self.projs = []
        self.width = 0
        self.height = 0
        self.changed = True
        self.pixmap = None
    
    def update_draw_attr(self):
        layer = self.layers[0]
        proj = self.projs[0]
        features = layer.features
        self.mbr = features.get_mbr()
        self.scale = 8371.279050589676
        self.x_offset = self.mbr.minx
        self.y_offset = self.mbr.miny
        self.width = (self.mbr.maxx - self.mbr.minx) / self.scale
        self.height = (self.mbr.maxy - self.mbr.miny) / self.scale
    
    def add_layer(self,layer,proj):
        self.layers.append(layer)
        self.projs.append(proj)
        self.update_draw_attr()
        self.changed = True

    def draw_image(self,pixmap:QtGui.QPixmap=None,layer:PiLayer=None,proj:PiProjection=None) -> None:
        # self.painter
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.RenderHint.TextAntialiasing, True)
        # draw_attr
        x_offset,y_offset,scale = self.x_offset,self.y_offset,self.scale
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
                    self.draw_polyline(painter,polyline,x_offset,y_offset,scale)
            elif layer.geometry_type == PiGeometryTypeConstant().multipolygon:
                for polygon in collection:
                    self.draw_polygon(painter,polygon,x_offset,y_offset,scale)
            elif layer.geometry_type == PiGeometryTypeConstant().multipoint:
                for point in collection:
                    self.draw_point(painter,point,x_offset,y_offset,scale)
    
    def draw_polyline(self,painter,polyline:PiPolyline,x_offset,y_offset,scale):
        ymax = self.height
        count = polyline.count
        start_x = (polyline.get_x()[0] - x_offset) / scale
        start_y = (polyline.get_y()[0] - y_offset) / scale
        for i in range(1,count):
            end_x = (polyline.get_x()[i] - x_offset) / scale
            end_y = (polyline.get_y()[i] - y_offset) / scale
            painter.drawLine(start_x,ymax - start_y,end_x,ymax - end_y)
            start_x,start_y = end_x,end_y
    
    def draw_polygon(self,painter,polygon:PiPolygon,x_offset,y_offset,scale):
        ymax = self.height
        count = polygon.count
        point_list = [QtCore.QPoint((polygon.get_x()[i] - x_offset) / scale,ymax - (polygon.get_y()[i] - y_offset) / scale) for i in range(count)]
        painter.drawPolygon(point_list)
    
    def draw_point(self,painter,point:PiPoint,x_offset,y_offset,scale):
        ymax = self.height
        count = 1
        ptx = (point.get_x() - x_offset)  / scale
        pty = ymax - (point.get_y() - y_offset)  / scale
        painter.drawEllipse(ptx,pty,5,5)
    
    def boundingRect(self):
        return QtCore.QRectF(-self.width/2,-self.height/2,self.width/2,self.height/2)

    def paint(self, painter,option,widget):
        # painter_.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        if self.changed == True:
            pixmap = QtGui.QPixmap()
            pixmap = QtGui.QPixmap(self.width,self.height)
            pixmap.fill(QtCore.Qt.GlobalColor.transparent)
            self.update_draw_attr()
            for i in range(len(self.layers)):
                layer = self.layers[i]
                proj = self.projs[i]
                self.draw_image(pixmap,layer,proj)
            self.pixmap = pixmap
            self.changed = False
        painter.drawPixmap(self.boundingRect(), self.pixmap, self.pixmap.rect())


if __name__ == "__main__":
    layer = PiLayer()
    layer2 = PiLayer()
    layer3 = PiLayer()
    proj = PiProjection()
    #layer.load("图层文件/省会城市.lay")
    #layer.load("图层文件/国界线.lay")
    #print(layer.fields)
    layer.load("PiMapObj/图层文件/省级行政区.lay")
    layer2.load("PiMapObj/图层文件/国界线.lay")
    layer3.load("PiMapObj/图层文件/省会城市.lay")
    proj.load("PiMapObj/图层文件/图层文件坐标系统说明.txt")
    
    app = QtWidgets.QApplication(sys.argv)
    main = PiWindow()
    main.figure.add_layer(layer,proj)
    main.figure.add_layer(layer2,proj)
    main.figure.add_layer(layer3,proj)
    main.show()
    sys.exit(app.exec())
    


    #print(layer.get_geometry_type())
    #print(layer.get_fields())
    