
from BinaryReader import BinaryReader
from PiFeature import PiFeature,PiFeatures
from PiField import PiField,PiFields
from PiConstant import PiGeometryTypeConstant
cons = PiGeometryTypeConstant()

class PiLayer():
    def __init__(self):
        self.fields = PiFields()
        self.features = PiFeatures()
        self.geometry_type = 0
        self.useless = 0
    
    def load(self,file_path):
        with open(file_path,"rb") as file:
            reader = BinaryReader(file.read())
        self.useless = reader.read_int32() # 版本号
        self.geometry_type = reader.read_int32() # 图层元素类型
        self.fields.load(reader) # 加载字段
        self.features.load(reader,self.geometry_type,self.fields) # 加载元素
    
    def get_geometry_type(self):
        return cons.get_str(self.geometry_type)

    def get_fields(self):
        return self.fields
    
    def get_features(self):
        return self.features

if __name__ == "__main__":
    #reader = LayerReader("图层文件/国界线.lay")
    #reader = LayerReader("图层文件/省级行政区.lay")
    layer = PiLayer()
    layer.load("图层文件/省会城市.lay")
    print(layer.get_geometry_type())
    print(layer.get_fields())
    fe = layer.features.features[0]
    fea = fe.attributes
    print(fea)
    
