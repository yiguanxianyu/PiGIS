# File: main.py
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

import slots
from ui.mainwindow import Ui_MainWindow
from ui.about import Ui_AboutPage


class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutPage()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.about_page = AboutPage()
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
        slots.project.add_data(self.project)

    def show_about_page(self):
        self.about_page.show()

    @staticmethod
    def exit_app():
        QApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
