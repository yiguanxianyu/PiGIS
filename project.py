import yaml
from layer import PiLayer
from GISType import class_type


class PiGISProject:
    def __init__(self):
        self.path = None
        self.major_version = 0
        self.minor_version = 1
        self.fix_version = 0
        self.layer = []
        self.layer_bin = []

    def parse(self, path: str):
        """
        Read project from a file
        :param: path: project file path
        :return: None
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                y = yaml.safe_load(f.read())

            assert y['Application']['app_name'] == 'PiGIS'
            ver = y['Application']['minimal_version'].split('.')
            major_version, minor_version, fix_version = int(ver[0]), int(ver[1]), int(ver[2])

            if self.major_version < major_version:
                raise Exception("PiGIS version not satisfied")
            elif self.major_version == major_version:
                if self.minor_version < minor_version:
                    raise Exception("PiGIS version not satisfied")
                elif self.minor_version == minor_version:
                    if self.fix_version < fix_version:
                        raise Exception("PiGIS version not satisfied")

            layers = y['layers']

            for layer in layers:
                metadata = layer['metadata']
                path = metadata['path']

                # Create a new layer
                #
                new_layer = PiLayer(path)
                new_layer.projection = metadata['prj']

                # Check if layer type is correspond to the original file
                assert layer.type == class_type[metadata['type']]

                self.layer.append(new_layer)
                print(path)

            self.path = path

        except Exception as ep:
            print('Project file error:')
            print(str(ep))

    def save(self):
        """
        Save current project to file
        :return: None
        """

        config = {
            'Application': {
                'app_name': 'PiGIS',
                'minimal_version': f'{self.major_version}.{self.minor_version}.{self.fix_version}',
            }
        }

        layer_config = []
        for curr_layer in self.layer:
            layer = {
                'metadata': {
                    'path': curr_layer.path,
                    'prj': curr_layer.projection,
                    'type': curr_layer.type_as_str
                },
                'style': curr_layer.style
            }

            layer_config.append(layer)

        config['layer'] = layer_config
        with open(self.path, 'w') as f:
            f.write(yaml.safe_dump(config))

    def add_layer(self, path: str):
        """
        Add a new layer to the project
        :param path: path for layer source file
        :return: None
        """
        ...

    def remove_layer(self, index: int):
        """
        Remove the selected layer and append it to self.layer_bin
        :param index: index of layer in layers
        :return: None
        """
        self.layer_bin.append(self.layer.pop(index))

    def recover_layer(self, index: int):
        """
        Recover a layer from layer_bin and append to layer
        :param index: ddd
        :return:
        """
        self.layer.append(self.layer_bin.pop(index))


if __name__ == '__main__':
    new_prj = PiGISProject()
    new_prj.parse('./demo.yaml')
