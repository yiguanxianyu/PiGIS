from PySide6.QtWidgets import QMainWindow, QApplication

from ui.AboutPage import AboutPage
from ui.OptionPage import OptionPage
from ui._mainwindow import Ui_MainWindow
from project import PiGISProjectController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.aboutPage = AboutPage()
        self.optionPage = OptionPage()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.project = PiGISProjectController()

    def open_project(self):
        self.project.open_project()

    def new_project(self):
        self.project.new_project()

    def save_project(self):
        self.project.save_project()

    def save_project_as(self):
        self.project.save_project_as()

    def add_layer(self):
        self.project.add_layer()

    def copy_layer(self):
        self.project.copy_current_layer()

    def switch_tool_bar(self, mode):
        if mode:
            self.ui.toolBar.show()
        else:
            self.ui.toolBar.hide()

    def switch_editing(self, mode):
        self.project.currentLayer.editable = mode

    def show_options_page(self):
        self.aboutPage.show()

    def show_about_page(self):
        self.aboutPage.show()

    @staticmethod
    def exit_app():
        QApplication.instance().quit()
