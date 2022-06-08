from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QSplitter

from project import PiGISProjectController
from ui import LayerTree, Graph, AboutPage
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

        # 分离器添加控件
        main_horizontal_splitter = QSplitter(Qt.Horizontal)
        main_horizontal_splitter.addWidget(layer_tree_widget)
        main_horizontal_splitter.addWidget(graph_widget)
        # 把这个 splitter 放在一个布局里才能显示出来
        self.ui.mainLayout.addWidget(main_horizontal_splitter)

    # For test only
    def mousePressEvent(self, event) -> None:
        self.ui.statusBar.update_mouse_loc(event.x(), event.y())

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

    '''
    def xiaochen_load_layers(self):
        self.graph_draw.set_view(self.graphWidget)
        self.graph_draw.load_graphics()
        
        figure = PiShow()
        for layer in layers:
            figure.add_layer(layer,proj)
        #figure.set_scene(scene)
        scene.addWidget(figure)
        
        
        figure = PiGraphicsItem()
        for layer in self.layers:
            figure.add_layer(layer,layer.proj)
        figure.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemClipsToShape)  # 给图元设置标志
        scene.addItem(figure)
        print(figure.shapeMode())
        '''
