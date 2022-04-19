# File: main.py
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PySide6.QtGui import QAction, QIcon
from ui.mainwindow import Ui_MainWindow
from project import PiGISProject


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.project = None

    @QtCore.Slot()
    def on_actionProjectOpen_triggered(self):
        file_type = ['PiGIS Project File (*.pgz)', 'All Files (*.*)']

        file_path, file_type = QFileDialog.getOpenFileName(
            QWidget(),
            'Select PiGIS Project File',
            filter=';;'.join(file_type)
        )

        self.project = PiGISProject(file_path)

    @QtCore.Slot()
    def on_actionProjectNew_triggered(self):
        ...

    @QtCore.Slot()
    def on_actionProjectSave_triggered(self):
        ...

    def add_data(self):
        file_type = ['shapefile (*.shp)', 'GPS eXchange Format (*.GPX)']
        print(file_type)

    def login(self):
        self.ui.label.setText('你点击了登录')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
