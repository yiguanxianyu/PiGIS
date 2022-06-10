from PySide6.QtCore import QPointF, QRectF
from PySide6.QtGui import QPaintDevice, QPainter, QPixmap
from PySide6.QtWidgets import QGraphicsItemGroup, QGraphicsScene, QGraphicsView

from PiDrawObj.PiGraphicsItem import PiGraphicsItemGroup, PiGraphicsTextItem


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
        self.text_collections = {}
        self.layer_added = False
        self.width = 1000

        self.scale = 1000
        self.scale_before = None
        # 0:no change 1:changed -1:deleted

    def add_layer(self, layer):
        id = layer.id
        self.layers[id] = layer
        self.item_collections[id] = {}
        self.text_collections[id] = {}
        # self.item_groups[id] = QGraphicsItemGroup()
        self.reset_draw_attr()
        self.load_layer_data(layer)
        # print(layer.id,layer.geometry_type)

    def delete_layer(self, layer_id):
        if self.layers[layer_id].visibility is True:
            self.hide_layer(layer_id)
        del self.item_collections[layer_id]
        del self.text_collections[layer_id]
        del self.layers[layer_id]

    def visulize_layer(self, layer_id):
        if self.layers[layer_id].visibility == True:
            return
        for item in self.item_collections[layer_id].values():
            self.scene.addItem(item)
        self.layers[layer_id].visibility = True

    def hide_layer(self, layer_id):
        if self.layers[layer_id].visibility == False:
            return
        for item in self.item_collections[layer_id].values():
            self.scene.removeItem(item)
        self.layers[layer_id].visibility = False

    def set_zvalue_layer(self, layer_id, zvalue):
        for item in self.item_collections[layer_id].values():
            item.setZValue(zvalue)

    def set_features_visibility(self, layer_id, ids, visibility):
        if visibility is False:
            for feature_id in ids:
                item = self.item_collections[layer_id][feature_id]
                self.scene.removeItem(item)
        elif visibility is True:
            for feature_id in ids:
                item = self.item_collections[layer_id][feature_id]
                self.scene.addItem(item)

    def remove_features(self, layer_id, ids):
        layer = self.layers[layer_id]
        layer.remove_features(ids)
        for feature_id in ids:
            if layer.visibility is True:
                self.scene.removeItem(self.item_collections[layer_id][feature_id])
            del self.item_collections[layer_id][feature_id]

    def load_layer_data(self, layer):
        pen = layer.pen
        brush = layer.brush
        # print(layer.id,layer.geometry_type)
        # item_group = self.item_groups[layer.id]
        layer_id = layer.id
        item_collection = self.item_collections[layer_id]
        for feature in layer.features.features:
            item = PiGraphicsItemGroup(layer_id, feature, self.item_box, self, pen, brush)
            item_collection[feature.id] = item
        self.visulize_layer(layer_id)

    def reset_draw_attr(self):
        """当添加新图层时刷新绘图参数"""
        self.mbr = None
        for layer in self.layers.values():
            if self.mbr is None:
                self.mbr = layer.features.get_mbr()
            else:
                self.mbr.union(layer.features.get_mbr())
        ydis = self.mbr.maxy - self.mbr.miny
        xdis = self.mbr.maxx - self.mbr.minx
        # self.scale = max(xdis, ydis) / 400
        self.scale = 1000
        self.view.set_show_scale(self.scale / 10000)
        self.mid_x = (self.mbr.minx + self.mbr.maxx) / 2
        self.mid_y = (self.mbr.miny + self.mbr.maxy) / 2
        self.view.centerOn(QPointF(self.mid_x / self.scale, -self.mid_y / self.scale))
        # self.view.scale(1 / self.view.show_scale, 1 / self.view.show_scale)

    def add_layer_text(self, layer_id):
        """显示元素注记，默认显示第一个字段"""
        layer = self.layers[layer_id]
        index = layer.text_index
        item_collection = self.item_collections[layer_id]
        text_collection = self.text_collections[layer_id]
        for feature in layer.features.features:
            feature_id = feature.id
            value = feature.attributes.attributes[index].value
            text = str(value)
            item = item_collection[feature_id]
            text_item = PiGraphicsTextItem(text, item)
            text_collection[feature_id] = text_item
            for item in text_collection.values():
                if item == text_item:
                    continue
                if text_item.collidesWithItem(item):
                    del text_collection[feature_id]
                    text_item = None
                    break
            if text_item != None:
                self.scene.addItem(text_item)

    def delete_layer_text(self, layer_id):
        """删除元素注记，默认显示第一个字段"""
        layer = self.layers[layer_id]
        index = layer.text_index
        text_collection = self.text_collections[layer_id]
        for item in text_collection.values():
            self.scene.removeItem(item)

    def save_fig(self, file_path):
        rect = QGraphicsView.viewport(self.view).rect()
        pixmap = QPixmap(rect.size())
        painter = QPainter(pixmap)
        painter.begin(pixmap)
        self.view.render(painter, QRectF(pixmap.rect()), rect)
        painter.end()
        pixmap.save(file_path)

    def load_graphics(self):
        pass

    def get_feature_item(self, layer_id, feature_id) -> PiGraphicsItemGroup:
        return self.item_collections[layer_id][feature_id]

    def get_scene(self):
        return self.scene
