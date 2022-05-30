from PiMapObj.PiGeometry import PiGeometry
from PiMapObj.PiPoint import PiPoint
from PiMapObj.PiMultiPoint import PiMultiPoint
from PiMapObj.PiMultiPolyline import PiMultiPolyline
from PiMapObj.PiMultiPolygon import PiMultiPolygon
from PiMapObj.PiAttribute import PiAttribute,PiAttributes


class PiFeature():
    def __init__(self,geometry_type,fields):
        if geometry_type == 0:
            self.geometry = PiMultiPoint()
        elif geometry_type == 1:
            self.geometry = PiMultiPolyline()
        elif geometry_type == 2:
            self.geometry = PiMultiPolygon()
        else:
            pass
        self.geometry_type = geometry_type
        self.attributes = PiAttributes(fields)
        self.symbol = None
    
    def load(self,reader,load_type):
        if load_type == 'lay':
            self.geometry.load(reader,load_type)
            self.attributes.load(reader,load_type)
        elif type == 'shp':
            pass
    
    def get_mbr(self):
        return self.geometry.get_mbr()

    def __str__(self):
        return "geo:%s,attr:%s" % (self.geometry,self.attributes)

    __repr__ = __str__
    

class PiFeatures():
    def __init__(self):
        self.features = []
        self.count = 0

    def load(self,reader,load_type,geometry_type,fields):
        self.geometry_type = geometry_type
        if load_type == 'lay':
            self.count = reader.read_int32() # 要素个数
            for i in range(self.count):
                new_feature = PiFeature(geometry_type,fields)
                new_feature.load(reader,load_type)
                self.features.append(new_feature)
        elif type == 'shp':
            pass
    
    def get_mbr(self):
        mbr = False
        if self.count > 0:
            mbr = self.features[0].get_mbr()
            for i in range(self.count):
                mbr.union(self.features[i].get_mbr())
        return mbr
    