from PySide6.QtWidgets import QWidget

from ui._options import Ui_OptionsPage


class OptionsPage(QWidget):
    def __init__(self):
        super().__init__()
        # TODO: Options Page
        self.ui = Ui_OptionsPage()
        self.ui.setupUi(self)
