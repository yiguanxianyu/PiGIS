from PiConstant import PiValueTypeConstant
cons = PiValueTypeConstant()

class PiAttribute():
    def __init__(self,value_type):
        self.value_type = value_type
        self.value = None

    def load(self,reader):
        if self.value_type == cons.int16:
            self.value = reader.read_int16()
        elif self.value_type == cons.int32:
            self.value = reader.read_int32()
        elif self.value_type == cons.int64:
            self.value = reader.read_int64()
        elif self.value_type == cons.float:
            self.value = reader.read_float32()
        elif self.value_type == cons.double:
            self.value = reader.read_float64()
        elif self.value_type == cons.string:
            self.value = reader.read_string()
        else:
            pass
    
    def __str__(self):
        return str(self.value)
    __repr__ = __str__

class PiAttributes():
    def __init__(self,fields):
        self.attributes = []
        self.field_count = fields.get_count()
        self.value_type_list = fields.get_value_type_list()

    def load(self,reader):
        for i in range(self.field_count):
            value_type = self.value_type_list[i]
            new_attribute = PiAttribute(value_type)
            new_attribute.load(reader)
            self.attributes.append(new_attribute)

    def __str__(self):
        return str(self.attributes)
    __repr__ = __str__
