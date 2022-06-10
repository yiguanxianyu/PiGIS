from PiConstant import PiValueTypeConstant

cons = PiValueTypeConstant()


class PiAttribute():
    def __init__(self, value_type):
        self.value_type = value_type
        self.value = 0

    def load(self, reader, load_type):
        if load_type == 'lay':
            match self.value_type:
                case cons.int16:
                    self.value = reader.read_int16()
                case cons.int32:
                    self.value = reader.read_int32()
                case cons.int64:
                    self.value = reader.read_int64()
                case cons.float:
                    self.value = reader.read_float32()
                case cons.double:
                    self.value = reader.read_float64()
                case cons.string:
                    self.value = reader.read_string()
                case _:
                    pass
        elif load_type == 'shp':
            pass

    def __str__(self):
        return str(self.value)

    __repr__ = __str__

class PiAttributes():
    def __init__(self, fields):
        self.attributes = []
        self.field_count = fields.get_count()
        self.value_type_list = fields.get_value_type_list()

    def load(self, reader, load_type):
        default_attribute = PiAttribute(cons.int32)
        if load_type == 'lay':
            for i in range(self.field_count):
                value_type = self.value_type_list[i]
                new_attribute = PiAttribute(value_type)
                new_attribute.load(reader, load_type)
                self.attributes.append(new_attribute)
        elif load_type == 'shp':
            pass

    def __str__(self):
        return str(self.attributes)

    def set_default(self):
        for value_type in self.value_type_list:
            new_attribute = PiAttribute(value_type)
            self.attributes.append(new_attribute)

    __repr__ = __str__
