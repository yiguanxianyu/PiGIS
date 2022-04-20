# File: main.py
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PySide6.QtGui import QAction, QIcon

import slots
from ui.mainwindow import Ui_MainWindow
from project import PiGISProject


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.project = None

    def open_project(self):
        self.project = slots.project.open_project()

    def new_project(self):
        self.project = slots.project.new_project()

    def save_project(self):
        slots.project.save_project(self.project)

    def save_project_to(self):
        slots.project.save_project_to(self.project)

    def add_data(self):
        all_types = ['shapefile (*.shp)', 'GPS eXchange Format (*.GPX)']
        file_path, file_type = QFileDialog.getOpenFileName(
            QWidget(),
            'Select PiGIS Project File',
            filter=';;'.join(all_types)
        )
        print(file_path, file_type)

    def login(self):
        self.ui.label.setText('你点击了登录')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
