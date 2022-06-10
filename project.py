from copy import deepcopy

import yaml
from PySide6.QtWidgets import QFileDialog, QWidget

import layer
from PiMapObj.PiLayer import PiLayer
from constants import *
from constants import class_type


class PiGISProject:

    def __init__(self,mw):
        self.path = None
        self.layer = []
        self.layerBin = []
        self.mainWindow = mw

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
            print(ep)

    def save(self):
        """
        Save current project to file
        """

        # part 1 overall metadata
        config = {
            'Application': {
                'app_name':
                    'PiGIS',
                'minimal_version':
                    f'{PiGIS_MAJOR_VERSION}.{PiGIS_MINOR_VERSION}.{PiGIS_PATCH_VERSION}',
            }
        }


        # part 2 Layer Tree Info

        tree_config = self.mainWindow.layerTree.get_layer_tree()
        config['tree_config']=tree_config

        # part 3 Layer Info
        layer_config = []
        for curr_layer_id in tree_config:
            curr_layer=self.mainWindow.graphWidget.get_layer_by_id(curr_layer_id)
            layer_info = {
                'layer_name': curr_layer.name,
                'metadata': {
                    'id': curr_layer_id,
                    'path': curr_layer.file_path,
                    'prj': curr_layer.proj._PiProjection__proj_name,
                    'type': int(curr_layer.geometry_type)
                },
                'style':{
                    'pen_style':int(curr_layer.pen.style()),
                    'pen_width':curr_layer.pen.width(),
                    'pen_color':curr_layer.pen.color().getRgbF(),
                    'brush':curr_layer.brush.color().getRgbF(),
                    'visibility':curr_layer.visibility,
                    'change':curr_layer.change,
                    'label_status':curr_layer.label_status,
                    'annotation_status':curr_layer.annotation_status
                }
            }

            layer_config.append(layer_info)
            print(curr_layer_id)

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

    def __init__(self, mw):
        self.mainWindow = mw
        self.currentLayer = None
        self.__project = PiGISProject(mw)

    def new_project(self):
        self.__project = PiGISProject()

    def set_save_config(self):
        all_types = [
            'PiGIS Project File (*.pgz)',
            "YAML Ain't Markable Language (*.yaml)"
        ]
        fp, ft = QFileDialog.getSaveFileName(QWidget(),
                                             "Save As...",
                                             filter=';;'.join(all_types))
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
            filter=';;'.join(all_types))

        self.__project = PiGISProject()
        self.__project.parse(file_path)

    def add_layer(self):
        """
        Create a layer from a vector file and append it to the project
        """
        all_types = [
            'Lay File (*.lay)', 'All Files (*.*)'
        ]

        file_path, file_type = QFileDialog.getOpenFileName(
            QWidget(), 'Select File', filter=';;'.join(all_types))

        if file_type == all_types[0]:
            new_layer = PiLayer()
            new_layer.load(file_path)
            self.mainWindow.graphWidget.load_layer(new_layer)
            self.mainWindow.layerTree.add_layer(new_layer.id, new_layer.name)

        # TODO: parse selected layer file
        self.__project.add_layer(None)

    def copy_current_layer(self):
        """
        Append a copy of the selected layer to the project
        Not done yet
        """
        pass


if __name__ == '__main__':
    new_prj_ = PiGISProject()
    new_prj_.parse('./demo.yaml')
