from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtGui import QFont, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow, QApplication, QSplitter, QWidget, QTabWidget, QListWidgetItem
# import pyqtgraph as pg
from ui import LayerTree, Graph, OptionsPage, AboutPage
from ui.raw import Ui_MainWindow
from project import PiGISProjectController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__optionsPage = None
        self.__aboutPage = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.project = PiGISProjectController()

        # self.plot = pg.PlotWidget(enableAutoRange=True)
        # self.ui.graphView.addWidget(self.plot)
        # self.curve = self.plot.plot()

        layer_tree_widget = LayerTree(self)
        self.layerTree = layer_tree_widget.ui.treeView
        graph_widget = Graph()
        self.graphWidget = graph_widget.ui.graphicsView
        layer_setting_widget = QTabWidget()

        # 分离器添加控件
        main_horizontal_splitter = QSplitter(Qt.Horizontal)
        main_horizontal_splitter.addWidget(layer_tree_widget)
        main_horizontal_splitter.addWidget(graph_widget)
        main_horizontal_splitter.addWidget(layer_setting_widget)
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

    def switch_editing(self, mode):
        self.project.currentLayer.editable = mode

    def show_options_page(self):
        if self.__optionsPage is None:
            self.__optionsPage = OptionsPage()
            self.__optionsPage.setWindowModality(Qt.ApplicationModal)

        self.__optionsPage.show()

    def show_about_page(self):
        if self.__aboutPage is None:
            self.__aboutPage = AboutPage()

        self.__aboutPage.show()

    @staticmethod
    def exit_app():
        QApplication.instance().quit()
