from PySide6.QtCore import QLineF, QPointF, Qt, QPoint
from PySide6.QtGui import QPaintDevice,QBrush, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsItemGroup,QGraphicsScene,QGraphicsPixmapItem,QGraphicsItem,QGraphicsPolygonItem
from PiConstant import PiGeometryTypeConstant,PiGraphModeConstant,PiLayerStatusConstant
from PiDrawObj.PiGraphicsItem import PiGraphicsPolylineItem,PiGraphicsPolygonItem,PiGraphicsEllipseItem
# import pyqtgraph as pg

cons = PiGeometryTypeConstant()


class PiGraphDraw(QPaintDevice):
    def __init__(self,view = None):
        super().__init__()
        self.scene = {
            PiGraphModeConstant.editable:QGraphicsScene(-250000,-250000,500000,500000),
            PiGraphModeConstant.moveable:QGraphicsScene(-250000,-250000,500000,500000),
        }
        self.view = view

        self.layers = []
        self.mbr = None

        self.cache_box = QGraphicsItemGroup(None)
        self.pixmap = QPixmap()
        self.painter = QPainter()
        self.cache = QGraphicsPixmapItem()
        self.expand_pos = QPointF(0,0)
        
        self.item_box = QGraphicsItemGroup(None)
        self.item_collections = {}
        self.layer_changed = {}
        self.layer_added = False
        self.width = 1000

        self.scale = None
        self.scale_before = None
        self.leftup_x = 0
        self.leftup_y = 0
        self.gra_x_offset = 0
        self.gra_y_offset = 0
        self.initial_x = 0
        self.initial_y = 0
        # 0:no change 1:changed -1:deleted

    def add_layer(self,layer):
        self.layers.append(layer)
        id = layer.id
        self.item_collections[id] = []
        #self.item_groups[id] = QGraphicsItemGroup()
        self.layer_changed[id] = PiLayerStatusConstant.added
        self.layer_added = True

        #self.load_graphics()

    def delete_layer(self,layer_id):
        self.layer_changed[layer_id] = PiLayerStatusConstant.deleted
        #self.load_graphics()

    def load_layer_data(self,layer):
        pen = QPen(Qt.blue)
        brush = QBrush(Qt.white)
        # item_group = self.item_groups[layer.id]
        item_collection = self.item_collections[layer.id]
        for feature in layer.features.features:
            geometry = feature.geometry
            collection = geometry._collection
            if layer.geometry_type == cons.multipolyline:
                for polyline in collection:
                    # 绘制图元
                    item = PiGraphicsPolylineItem(polyline,self.item_box,self)
                    item.setFlags(QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemClipsToShape)  # 给图元设置标志
                    item_collection.append(item)
            elif layer.geometry_type == cons.multipolygon:
                for polygon in collection:
                    # 绘制图元
                    item = PiGraphicsPolygonItem(polygon,self.item_box,self)
                    item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemClipsToShape)  # 给图元设置标志
                    item.setPen(pen)
                    item_collection.append(item)
            elif layer.geometry_type == cons.multipoint:
                for point in collection:
                    # 绘制图元
                    item = PiGraphicsEllipseItem(point,self.item_box,self)
                    item.setFlags(QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemClipsToShape)  # 给图元设置标志
                    item_collection.append(item)

    def draw_cache(self,layer):
        item_collection = self.item_collections[layer.id]
        match layer.geometry_type:
            case cons.multipolyline:
                for item in item_collection:
                    for line in item.polyline():
                        #line.translate(self.expand_pos)
                        self.painter.drawLine(line)
            case cons.multipolygon:
                print(self.expand_pos)
                for item in item_collection:
                    polygon = item.polygon()
                    #polygon.translate(self.expand_pos)
                    self.painter.drawPolygon(item.polygon())
            case cons.multipoint:
                for item in item_collection:
                    point = item.ellipse()
                    #point.translate(self.expand_pos)
                    self.painter.drawEllipse(item.ellipse())

    def load_graphics(self):
        '''加载图元以及缓冲图片'''
        #初始化
        if len(self.layers) == 0:
            return
        if self.scale == None: # 设置默认显示数据
            self.scale = 10000
        if self.layer_added == True: 
            # 重新调整外接矩形大小以便显示全部图像
            self.mbr = self.layers[0].features.get_mbr()
            for layer in self.layers:
                self.mbr.union(layer.features.get_mbr())
            ydis = self.mbr.maxy - self.mbr.miny
            xdis = self.mbr.maxx - self.mbr.minx
            self.scale = max(xdis,ydis) / 400
            self.initial_leftup_x = self.mbr.minx
            self.initial_leftup_y = self.mbr.maxy
            self.mid_x = (self.mbr.minx + self.mbr.maxx) / 2
            self.mid_y = (self.mbr.miny + self.mbr.maxy) / 2
            self.layer_added = False
        # 计算图片大小以及平移距离，以确保中心点在（0，0）
        self.width = (self.mbr.maxx - self.mbr.minx) / self.scale
        self.height = (self.mbr.maxy - self.mbr.miny) / self.scale
        self.leftup_x = self.mbr.minx
        self.leftup_y = self.mbr.maxy
        self.expand_pos = QPointF((self.leftup_x - self.initial_leftup_x)/self.scale,(self.initial_leftup_y - self.leftup_y) / self.scale)
        self.gra_x_offset = (self.mid_x - self.leftup_x) / self.scale
        self.gra_y_offset = (self.leftup_y - self.mid_y) / self.scale
        # self.initial_leftup_x = self.leftup_x
        # self.initial_leftup_y = self.leftup_y
        '''开始加载'''
        print(self.width,self.height)
        # 移除原先缓冲图片,重新调整定位
        try:
            self.scene[PiGraphModeConstant.moveable].removeItem(self.cache_box)
            self.cache_box.removeFromGroup(self.cache)
        except:
            pass
        self.cache_box.setPos( -self.gra_x_offset, -self.gra_y_offset)
        # 初始化缓冲画布
        self.pixmap = QPixmap(self.width,self.height)
        self.pixmap.fill(Qt.GlobalColor.transparent)
        # 初始化画笔
        pen = QPen(Qt.blue)
        brush = QBrush(Qt.white)
        self.painter = QPainter(self.pixmap)
        self.painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        self.painter.begin(self)
        self.painter.setPen(pen)
        self.painter.setBrush(brush)
        # 开始绘制
        self.item_box.setPos( -self.gra_x_offset, -self.gra_y_offset)
        for index in range(len(self.layers)):
            layer = self.layers[index]
            id = layer.id
            # self.item_groups[id].setPos(-self.gra_x_offset, -self.gra_y_offset)
            match self.layer_changed[id]:
                case PiLayerStatusConstant.added:
                    self.load_layer_data(layer)
                    for item in self.item_collections[id]:
                        self.scene[PiGraphModeConstant.editable].addItem(item)
                    self.draw_cache(layer)
                    self.layer_changed[id] = PiLayerStatusConstant.normal
                case PiLayerStatusConstant.visiable:
                    for item in self.item_collections[id]:
                        self.scene[PiGraphModeConstant.editable].addItem(item)
                    self.draw_cache(layer)
                    self.layer_changed[id] = PiLayerStatusConstant.normal
                case PiLayerStatusConstant.normal:
                    self.draw_cache(layer)
                case PiLayerStatusConstant.hidden:
                    try:
                        for item in self.item_collections[id]:
                            self.scene[PiGraphModeConstant.editable].removeItem(item)
                    except:
                        pass
                case PiLayerStatusConstant.deleted:
                    try:
                        for item in self.item_collections[id]:
                            self.scene[PiGraphModeConstant.editable].removeItem(item)
                    except:
                        pass
                    del self.item_collections[id]
                    del self.layer_changed[id]
                    del self.layers[index]
                    
        # 往场景中添加缓冲图片
        self.cache = QGraphicsPixmapItem(self.pixmap,self.cache_box)
        #self.cache.setPos(self.expand_pos)
        self.scene[PiGraphModeConstant.moveable].addItem(self.cache_box)
        self.painter.end()
    
    def get_scene(self,mode):
        return self.scene[mode]