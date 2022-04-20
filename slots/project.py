from PySide6.QtWidgets import QFileDialog, QWidget
from project import PiGISProject


def open_project():
    all_types = ['PiGIS Project File (*.pgz | *.yaml)', 'All Files (*.*)']

    file_path, file_type = QFileDialog.getOpenFileName(
        QWidget(),
        'Select PiGIS Project File',
        filter=';;'.join(all_types)
    )

    new_prj = PiGISProject()
    new_prj.parse(file_path)
    return new_prj


def new_project():
    return PiGISProject()


def save_project(project: PiGISProject):
    project.save()


def save_project_to(project: PiGISProject):
    all_types = ['PiGIS Project File (*.pgz)', "YAML Ain't Markable Language (*.yaml)"]
    fp, ft = QFileDialog.getSaveFileName(QWidget(), "Save As...", filter=';;'.join(all_types))
    project.path = fp
    project.save()


def add_data(project: PiGISProject):
    """
    Read data from a vector file, create a layer and append it to the project
    :param project: PiGISProject
    :return: None
    """
    all_types = ['shapefile (*.shp)', 'GPS eXchange Format (*.GPX)']
    file_path, file_type = QFileDialog.getOpenFileName(
        QWidget(),
        'Select Vector File',
        filter=';;'.join(all_types)
    )

    project.add_layer(file_path)
