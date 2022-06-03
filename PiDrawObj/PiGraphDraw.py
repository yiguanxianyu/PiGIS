from PySide6.QtCore import QLineF, QPointF, Qt, QPoint
from PySide6.QtGui import QPaintDevice,QBrush, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsView,QGraphicsItemGroup,QGraphicsScene,QGraphicsPixmapItem,QGraphicsItem,QGraphicsPolygonItem,QGraphicsLineItem,QGraphicsEllipseItem
from PiMapObj.PiConstant import PiGeometryTypeConstant
from PiDrawObj.PiGraphicsItem import QGraphicsPolylineItem
# import pyqtgraph as pg


class PiGraphDraw(QPaintDevice):
    def __init__(self):
        super().__init__()
        self.scene = {
            "editable":QGraphicsScene(),
            "moveable":QGraphicsScene()
        }
        self.mode = "editable"
        self.view = QGraphicsView()

        self.layers = []
        self.cache = QGraphicsPixmapItem()
        self.graphic_item_collection = []

        self.width = 1000

        self.scale = None
        self.scale_before = None
        self.geo_x_offset = 0
        self.geo_y_offset = 0
        self.gra_x_offset = 0
        self.gra_y_offset = 0
        self.changed = True

    def add_layer(self,layer):
        self.layers.append(layer)

    def set_view(self,view):
        view.draw_control = self
        self.view = view
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setScene(self.scene[self.mode])

    def moveable_show(self):
        self.mode = "moveable"
        self.view.setScene(self.scene[self.mode])
    
    def editable_show(self):
        self.mode = "editable"
        self.view.setScene(self.scene[self.mode])

    def load_graphics(self):
        self.graphic_item_collection = []
        self.scene = {
            "editable":QGraphicsScene(-250000,-250000,500000,500000),
            "moveable":QGraphicsScene(-250000,-250000,500000,500000)
        }
        if self.scale == None: # 设置默认显示数据
            mbr = self.layers[0].features.get_mbr()
            for layer in self.layers:
                mbr.union(layer.features.get_mbr())
            self.scale_before = 0
            self.scale = 10000
            self.width = (mbr.maxx - mbr.minx) / self.scale
            self.height = (mbr.maxy - mbr.miny) / self.scale
            self.geo_x_offset = mbr.minx
            self.geo_y_offset = mbr.miny
            self.gra_x_offset = self.width / 2
            self.gra_y_offset = self.height / 2
        else:
            self.width = (mbr.maxx - mbr.minx) / self.scale
            self.height = (mbr.maxy - mbr.miny) / self.scale
        '''
        if self.scale < 5 * self.scale_before5 or self.scale > 0.2 * self.scale_before > 0.2:
            return
        '''
        print(self.width,self.height)
        grh_offset_point = QPointF(self.gra_x_offset,self.gra_y_offset)
        self.scale_before = self.scale
        cons = PiGeometryTypeConstant()
        pixmap = QPixmap(self.width,self.height)
        pixmap.fill(Qt.GlobalColor.transparent)
        pen = QPen(Qt.blue)
        brush = QBrush(Qt.white)
        temp_painter = QPainter(pixmap)
        temp_painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        temp_painter.begin(self)
        temp_painter.setPen(pen)
        temp_painter.setBrush(brush)
        for layer in self.layers:
            for feature in layer.features.features:
                geometry = feature.geometry
                collection = geometry._collection
                if layer.geometry_type == cons.multipolyline:
                    for polyline in collection:
                        qpoint_list = [QPointF((polyline.get_x()[i] - self.geo_x_offset) / self.scale - self.gra_x_offset, self.height - (polyline.get_y()[i] - self.geo_y_offset) / self.scale - self.gra_y_offset) for i in range(polyline.count)]
                        item = QGraphicsPolylineItem(qpoint_list)
                        self.graphic_item_collection.append(item)
                        for i in range(polyline.count - 1):
                            temp_painter.drawLine(qpoint_list[i] + grh_offset_point,qpoint_list[i + 1] + grh_offset_point)
                        #item.setPen(pen)
                elif layer.geometry_type == cons.multipolygon:
                    for polygon in collection:
                        qpoint_list = [QPointF((polygon.get_x()[i] - self.geo_x_offset) / self.scale - self.gra_x_offset, self.height - (polygon.get_y()[i] - self.geo_y_offset) / self.scale - self.gra_y_offset) for i in range(polygon.count)]
                        item = QGraphicsPolygonItem(qpoint_list)
                        item.setPen(pen)
                        self.graphic_item_collection.append(item)
                        for qpoint in qpoint_list:
                            qpoint += grh_offset_point
                        temp_painter.drawPolygon(qpoint_list)
                elif layer.geometry_type == cons.multipoint:
                    for point in collection:
                        xpos = (point.get_x() - self.geo_x_offset) / self.scale
                        ypos = self.height - (point.get_y() - self.geo_y_offset) / self.scale
                        item = QGraphicsEllipseItem(xpos-2,ypos-2,4,4)
                        self.graphic_item_collection.append(item)
                        temp_painter.drawEllipse(QPointF(xpos,ypos) + grh_offset_point,2,2)
        for item in self.graphic_item_collection:
            self.scene["editable"].addItem(item)
            item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemClipsToShape)  # 给图元设置标志
        self.pixmap = QGraphicsPixmapItem()
        self.pixmap.setPos( -self.gra_x_offset, -self.gra_y_offset)
        self.cache = QGraphicsPixmapItem(pixmap,self.pixmap)
        self.scene["moveable"].addItem(self.pixmap)
        #pixmap.save('lalala.png','PNG')
        temp_painter.end()
        del pixmap
        del temp_painter
        self.view.setScene(self.scene[self.mode])

    def stable_load(self):
        cons = PiGeometryTypeConstant()
        pixmap = QPixmap(self.width,self.height)
        pixmap.fill(Qt.GlobalColor.transparent)
        pen = QPen(Qt.blue)
        brush = QBrush(Qt.white)
        temp_painter = QPainter(pixmap)
        temp_painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        temp_painter.begin(self)
        temp_painter.setPen(pen)
        temp_painter.setBrush(brush)
        for layer in self.layers:
            for feature in layer.features.features:
                geometry = feature.geometry
                collection = geometry._collection
                if layer.geometry_type == cons.multipolyline:
                    for polyline in collection:
                        qpoint_list = [QPointF((polyline.get_x()[i] - self.geo_x_offset) / self.scale, self.height - (polyline.get_y()[i] - self.geo_y_offset) / self.scale) for i in range(polyline.count)]
                        for i in range(polyline.count - 1):
                            temp_painter.drawLine(qpoint_list[i],qpoint_list[i + 1])
                        #item = QGraphicsPolylineItem(qpoint_list)
                        #item.setPen(pen)
                        #self.graphic_item_collection.append(item)
                elif layer.geometry_type == cons.multipolygon:
                    for polygon in collection:
                        qpoint_list = [QPointF((polygon.get_x()[i] - self.geo_x_offset) / self.scale, self.height - (polygon.get_y()[i] - self.geo_y_offset) / self.scale) for i in range(polygon.count)]
                        temp_painter.drawPolygon(qpoint_list)
                        #item = QGraphicsPolygonItem(qpoint_list)
                        #item.setPen(pen)
                        #self.graphic_item_collection.append(item)
                elif layer.geometry_type == cons.multipoint:
                    for point in collection:
                        xpos = (point.get_x() - self.geo_x_offset) / self.scale
                        ypos = self.height - (point.get_y() - self.geo_y_offset) / self.scale
                        temp_painter.drawEllipse(QPointF(xpos,ypos),2,2)
                        #item = QGraphicsEllipseItem(xpos-2,ypos-2,4,4)
                        #self.graphic_item_collection.append(item)
        #for item in self.graphic_item_collection:
        #    self.scene["editable"].addItem(item)
        #    item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemClipsToShape)  # 给图元设置标志
        self.cache = QGraphicsPixmapItem(pixmap)
        self.scene["moveable"].addItem(self.cache)
        #pixmap.save('lalala.png','PNG')
        temp_painter.end()
        del pixmap
        del temp_painter
        self.view.setScene(self.scene[self.mode])

    def active_load(self):
        cons = PiGeometryTypeConstant()
        pen = QPen(Qt.blue)
        brush = QBrush(Qt.white)
        for layer in self.layers:
            for feature in layer.features.features:
                geometry = feature.geometry
                collection = geometry._collection
                if layer.geometry_type == cons.multipolyline:
                    for polyline in collection:
                        qpoint_list = [QPointF((polyline.get_x()[i] - self.geo_x_offset) / self.scale, self.height - (polyline.get_y()[i] - self.geo_y_offset) / self.scale) for i in range(polyline.count)]
                        item = QGraphicsPolylineItem(qpoint_list)
                        self.graphic_item_collection.append(item)

                elif layer.geometry_type == cons.multipolygon:
                    for polygon in collection:
                        qpoint_list = [QPointF((polygon.get_x()[i] - self.geo_x_offset) / self.scale, self.height - (polygon.get_y()[i] - self.geo_y_offset) / self.scale) for i in range(polygon.count)]
                        item = QGraphicsPolygonItem(qpoint_list)
                        item.setPen(pen)
                        self.graphic_item_collection.append(item)
                elif layer.geometry_type == cons.multipoint:
                    for point in collection:
                        xpos = (point.get_x() - self.geo_x_offset) / self.scale
                        ypos = self.height - (point.get_y() - self.geo_y_offset) / self.scale
                        item = QGraphicsEllipseItem(xpos-2,ypos-2,4,4)
                        self.graphic_item_collection.append(item)
        for item in self.graphic_item_collection:
            self.scene["editable"].addItem(item)
            item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemClipsToShape)  # 给图元设置标志
        self.view.setScene(self.scene[self.mode])
        