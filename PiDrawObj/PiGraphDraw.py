from PySide6.QtCore import QPointF
from PySide6.QtGui import QPaintDevice
from PySide6.QtWidgets import QGraphicsItemGroup, QGraphicsScene, QGraphicsItem

from PiConstant import PiGeometryTypeConstant, PiLayerStatusConstant
from PiDrawObj.PiGraphicsItem import PiGraphicsItemGroup, PiGraphicsPolylineItem, PiGraphicsPolygonItem, PiGraphicsEllipseItem

# import pyqtgraph as pg


class PiGraphDraw(QPaintDevice):
    def __init__(self, view=None):
        super().__init__()
        self.max_y = 1000000
        self.max_x = 1000000
        self.scene = QGraphicsScene(-self.max_x, -self.max_y, 2 * self.max_x, 2 * self.max_y)
        self.view = view

        self.layers = {}
        self.mbr = None

        self.expand_pos = QPointF(0, 0)

        self.item_box = QGraphicsItemGroup(None)
        self.item_box.setPos(0, 0)
        self.item_collections = {}
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

    def add_layer(self, layer):
        id = layer.id
        self.layers[id] = layer
        self.item_collections[id] = {}
        # self.item_groups[id] = QGraphicsItemGroup()
        self.reset_draw_attr()
        self.load_layer_data(layer)
        
    def delete_layer(self, layer_id):
        if self.layers[layer_id].visibility == True:
            self.hide_layer(layer_id)
        del self.item_collections[layer_id]
        del self.layers[layer_id]
    
    def visulize_layer(self,layer_id):
        self.layers[layer_id].visibility = True
        for item in self.item_collections[layer_id].values():
            self.scene.addItem(item)
    
    def hide_layer(self,layer_id):
        self.layers[layer_id].visibility = False
        for item in self.item_collections[layer_id].values():
            self.scene.removeItem(item)
    
    def set_zvalue_layer(self,layer_id,zvalue):
        for item in self.item_collections[layer_id].values():
            item.setZValue(zvalue)

    def remove_feature(self,layer_id,ids):
        layer = self.layers[layer_id]
        layer.remove_feature(ids)
        for feature_id in ids:
            if layer.visibility == True:
                self.scene.removeItem(self.item_collections[layer_id][feature_id])
            del self.item_collections[layer_id][feature_id]




    def load_layer_data(self, layer):
        pen = layer.pen
        brush = layer.brush
        #print(layer.id,layer.geometry_type)
        # item_group = self.item_groups[layer.id]
        item_collection = self.item_collections[layer.id]
        for feature in layer.features.features:
            item = PiGraphicsItemGroup(feature,self.item_box,self)
            item.setFlags(
                        QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemClipsToShape)  # 给图元设置标志
            item_collection[feature.id] = item
            item.setPen(pen)
            item.setBrush(brush)
        self.visulize_layer(layer.id)

    def reset_draw_attr(self):
        '''当添加新图层时刷新绘图参数'''
        self.mbr = None
        for layer in self.layers.values():
            if self.mbr == None:
                self.mbr = layer.features.get_mbr()
            else:
                self.mbr.union(layer.features.get_mbr())
        ydis = self.mbr.maxy - self.mbr.miny
        xdis = self.mbr.maxx - self.mbr.minx
        # self.scale = max(xdis, ydis) / 400
        self.scale = 10000
        self.mid_x = (self.mbr.minx + self.mbr.maxx) / 2
        self.mid_y = (self.mbr.miny + self.mbr.maxy) / 2
        self.view.centerOn(QPointF(self.mid_x / self.scale, -self.mid_y / self.scale))
        self.view.scale(1 / self.view.show_scale, 1 / self.view.show_scale)

    def load_graphics(self):
        pass

    def get_feature_item(self,layer_id,feature_id) -> PiGraphicsItemGroup:
        return self.item_collections[layer_id][feature_id]

    def get_scene(self):
        return self.scene
