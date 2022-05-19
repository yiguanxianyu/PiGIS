from copy import deepcopy

import yaml
from PySide6.QtWidgets import QFileDialog, QWidget

import layer
from constants import *
from constants import class_type


class PiGISProject:
    def __init__(self):
        self.path = None
        self.layer = []
        self.layerBin = []

    def parse(self, path: str):
        """
        Read project from a project file
        :param path: project file path
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                y = yaml.safe_load(f.read())

            assert y['Application']['app_name'] == 'PiGIS'
            ver = y['Application']['minimal_version'].split('.')
            major, minor, patch = int(ver[0]), int(ver[1]), int(ver[2])

            # Check πGIS version
            version_error = False
            if PiGIS_MAJOR_VERSION < major:
                version_error = True
            elif PiGIS_MAJOR_VERSION == major:
                if PiGIS_MINOR_VERSION < minor:
                    version_error = True
                elif PiGIS_MINOR_VERSION == minor:
                    if PiGIS_PATCH_VERSION < patch:
                        version_error = True

            if version_error:
                raise Exception("πGIS version not satisfied")

            for curr_layer in y['layers']:
                metadata = curr_layer['metadata']
                path = metadata['path']

                # Create a new layer
                new_layer = layer.create_layer(path)
                new_layer.projection = metadata['prj']
                new_layer.name = curr_layer['name']

                # Check if the layer type is correspond to the source file
                assert curr_layer.type == class_type[metadata['type']]

                self.layer.append(new_layer)
                print(path)

            self.path = path

        except Exception as ep:
            print('An error occurred while parsing project file:')
            print(str(ep))

    def save(self):
        """
        Save current project to file
        """

        config = {
            'Application': {
                'app_name': 'PiGIS',
                'minimal_version': f'{PiGIS_MAJOR_VERSION}.{PiGIS_MINOR_VERSION}.{PiGIS_PATCH_VERSION}',
            }
        }

        layer_config = []
        for curr_layer in self.layer:
            layer_info = {
                'layer_name': curr_layer.name,
                'metadata': {
                    'path': curr_layer.path,
                    'prj': curr_layer.projection,
                    'type': curr_layer.type_as_str
                },
                'style': curr_layer.style
            }

            layer_config.append(layer_info)

        config['layer'] = layer_config
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(yaml.safe_dump(config))

    def add_layer(self, _layer):
        """
        Add a new layer to the project
        :param _layer: feature layer
        :return: None
        """
        self.layer.append(_layer)

    def remove_layer(self, index: int):
        """
        Remove a layer and append it to layer_bin
        :param index: index of layer in layers
        :return: None
        """
        self.layerBin.append(self.layer.pop(index))

    def recover_layer(self, index: int):
        """
        Recover a layer from layer_bin and append it to layer
        :param index: ddd
        :return:
        """
        self.layer.append(self.layerBin.pop(index))


class PiGISProjectController:
    def __init__(self):
        self.currentLayer = None
        self.__project = PiGISProject()

    def new_project(self):
        self.__project = PiGISProject()

    def set_save_config(self):
        all_types = ['PiGIS Project File (*.pgz)', "YAML Ain't Markable Language (*.yaml)"]
        fp, ft = QFileDialog.getSaveFileName(QWidget(), "Save As...", filter=';;'.join(all_types))
        self.__project.path = fp

    def save_project(self):
        """
        Save project to current path
        """
        if not self.__project.path:
            self.set_save_config()
        self.__project.save()

    def save_project_as(self):
        """
        Save project to given path
        """
        self.set_save_config()
        self.__project.save()

    def open_project(self):
        """
        Open a project from file
        """
        all_types = ['PiGIS Project File (*.pgz; *.yaml)', 'All Files (*.*)']

        file_path, file_type = QFileDialog.getOpenFileName(
            QWidget(),
            'Select PiGIS Project File',
            filter=';;'.join(all_types)
        )

        self.__project = PiGISProject()
        self.__project.parse(file_path)

    def add_layer(self):
        """
        Create a layer from a vector file and append it to the project
        """
        all_types = ['shapefile (*.shp)', 'GPS eXchange Format (*.GPX)']

        file_path, file_type = QFileDialog.getOpenFileName(
            QWidget(),
            'Select File',
            filter=';;'.join(all_types)
        )

        # TODO: parse selected layer file
        self.__project.add_layer(None)

    def copy_current_layer(self):
        """
        Append a deepcopy of the selected layer to the project
        Not done yet
        """
        pass
        self.__project.layer.append(
            deepcopy(self.__project.layer[self.currentLayer])
        )


if __name__ == '__main__':
    new_prj_ = PiGISProject()
    new_prj_.parse('./demo.yaml')
