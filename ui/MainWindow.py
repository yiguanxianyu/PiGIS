from PySide6.QtCore import QPoint, QPointF, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QMainWindow, QApplication, QSplitter, QSizePolicy

from project import PiGISProjectController
from ui import LayerTree, Graph, AboutPage
from ui.StatusBar import PiStatusBar
from ui.raw import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__aboutPage = None
        self.project = PiGISProjectController(self)

        layer_tree_widget = LayerTree(self)
        self.layerTree = layer_tree_widget

        graph_widget = Graph(self)
        self.graphWidget = graph_widget
        graph_widget.layerTree = layer_tree_widget
        layer_tree_widget.graph = graph_widget
        self.add_status_bar()

        # 分离器添加控件
        main_horizontal_splitter = QSplitter(Qt.Horizontal)
        main_horizontal_splitter.addWidget(layer_tree_widget)
        main_horizontal_splitter.addWidget(graph_widget)
        # 把这个 splitter 放在一个布局里才能显示出来
        self.ui.mainLayout.addWidget(main_horizontal_splitter)
        
        self.graphWidget.view_control.set_window(self)
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_Hover,True)

    def update_scale(self, scale):
        self.statusBar.update_scale(scale)

    def update_coord(self, x, y):
        self.update_coord(x, y)

    # For test only
    def mouseMoveEvent(self, event) -> None:
        print(event)
        window_pos = QPoint(event.x(), event.y())
        map_pos = self.graphWidget.view_control.window_to_map(self,window_pos)
        self.statusBar.update_coord(map_pos.x(), map_pos.y())
        return super().mouseMoveEvent(event)

    def draw_layers(self):
        pass

    def open_project(self):
        self.project.open_project()

    def new_project(self):
        self.project.new_project()

    def save_project(self):
        self.project.save_project()

    def save_project_as(self):
        self.project.save_project_as()

    def save_image(self):
        self.graphWidget.save_image()

    def add_layer(self):
        self.project.add_layer()

    def copy_layer(self):
        self.project.copy_current_layer()

    def switch_editing(self, mode):
        self.project.currentLayer.editable = mode

    def show_options_page(self):
        pass
        # if self.__optionsPage is None:
        #     self.__optionsPage = OptionPage()
        #     self.__optionsPage.setWindowModality(Qt.ApplicationModal)
        #
        # self.__optionsPage.show()

    def show_about_page(self):
        if self.__aboutPage is None:
            self.__aboutPage = AboutPage()

        self.__aboutPage.show()

    @staticmethod
    def exit_app():
        QApplication.instance().quit()

    def add_status_bar(self):
        self.statusBar = PiStatusBar(self)
        self.statusBar.setObjectName(u"statusBar")
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(size_policy)
        self.setStatusBar(self.statusBar)
