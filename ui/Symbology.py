from PySide6.QtWidgets import QWidget

from ui.raw import Ui_Symbology


class SymbologyPage(QWidget):
    def __init__(self, layer):
        super().__init__()
        self.ui = Ui_Symbology()
        self.ui.setupUi(self)
