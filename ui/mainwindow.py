from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QSplitter, QTreeWidget, QWidget, QTabWidget
# import pyqtgraph as pg
from ui.AboutPage import AboutPage
from ui.OptionsPage import OptionsPage
from ui._mainwindow import Ui_MainWindow
from project import PiGISProjectController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__optionsPage = None
        self.__aboutPage = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.plot = pg.PlotWidget(enableAutoRange=True)
        # self.ui.graphView.addWidget(self.plot)
        # self.curve = self.plot.plot()

        self.project = PiGISProjectController()

        main_horizontal_splitter = QSplitter(Qt.Horizontal)

        treeWidget = QTreeWidget()
        graphWidget = QWidget()
        tabWidget = QTabWidget()

        # 分离器添加控件
        main_horizontal_splitter.addWidget(treeWidget)
        main_horizontal_splitter.addWidget(graphWidget)
        main_horizontal_splitter.addWidget(tabWidget)

        # 把这个 splitter 放在一个布局里才能显示出来
        self.ui.mainLayout.addWidget(main_horizontal_splitter)

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
        if self.__optionsPage is None:
            self.__optionsPage = OptionsPage()

        self.__optionsPage.show()

    def show_about_page(self):
        if self.__aboutPage is None:
            self.__aboutPage = AboutPage()

        self.__aboutPage.show()

    @staticmethod
    def exit_app():
        QApplication.instance().quit()
