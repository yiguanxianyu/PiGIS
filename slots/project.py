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

