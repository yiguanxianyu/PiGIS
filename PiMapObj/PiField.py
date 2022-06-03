from PiMapObj.PiConstant import PiValueTypeConstant
cons = PiValueTypeConstant()
class PiField():
    def __init__(self):
        self.name = ""
        self.value_type = 0 # 数据类型
        self.useless = None
    
    def load(self,reader,load_type = 'lay'):
        if load_type == 'lay':
            self.name = reader.read_string()
            self.value_type = reader.read_int32()
            self.useless = reader.read_int32()
        elif load_type == 'shp':
            pass
    
    def get_value_type(self):
        return self.value_type

    def __str__(self):
        return "(%s,%s)" % (self.name,cons.get_str(self.value_type))

    __repr__ = __str__

class PiFields():
    def __init__(self):
        self.fields = []
        self.count = 0
    
    def load(self,reader,load_type = 'lay'):
        if load_type == 'lay':
            self.count = reader.read_int32() # 字段个数
            for i in range(self.count):
                new_field = PiField()
                new_field.load(reader,load_type)
                self.fields.append(new_field)
        elif load_type == 'shp':
            pass

    def get_count(self):
        return self.count

    def get_value_type_list(self):
        return [field.get_value_type() for field in self.fields]
        
    def __str__(self):
        return str(self.fields)

    __repr__ = __str__