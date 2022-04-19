from xml.dom import minidom
from layer import PiLayer
from GISType import class_type


class PiGISProject:
    def __init__(self):
        self.path = None
        self.version = '1.0'
        self.layer = []
        self.layer_bin = []

    def parse(self, path):
        try:
            self.path = path
            doc = minidom.parse(path)
            pi_map = doc.getElementsByTagName('PiMap')[0]
            layers = pi_map.getElementsByTagName('layers')[0].getElementsByTagName('layer')

            self.version = pi_map.attributes['minimal_version'].value

            for layer in layers:
                path = layer.getElementsByTagName('path')[0].firstChild.data

                # 新建一个图层
                new_layer = PiLayer(path)
                new_layer.projection = layer.attributes['prj'].value

                # 检查文件类型是否和工程文件定义相一致
                assert new_layer.type == class_type[layer.attributes['type'].value]

                self.layer.append(new_layer)
                print(path)

        except Exception as ep:
            print('Project file is not correct:')
            print(str(ep))

    def save(self, path):
        dom = minidom.Document().appendChild('PiGIS')
        dom.appendChild('dd')

        with open(path) as f:
            f.write(self.version)

    def add_layer(self, path):
        ...

    def remove_layer(self, index):
        self.layer_bin.append(self.layer.pop(index))

    def recover_layer(self, index):
        self.layer.append(self.layer_bin.pop(index))


if __name__ == '__main__':
    new_prj = PiGISProject()
    new_prj.parse('./demo.pgz')
