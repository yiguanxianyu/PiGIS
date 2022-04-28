from PySide6.QtWidgets import QWidget

from ui.raw import Ui_Graph


class Graph(QWidget):
    def __init__(self):
        super().__init__()
        # TODO: Options Page
        self.ui = Ui_Graph()
        self.ui.setupUi(self)
