from PySide6.QtWidgets import QWidget

from ui._about import Ui_AboutPage


class OptionPage(QWidget):
    def __init__(self):
        super().__init__()
        # TODO: Option Page
        self.ui = Ui_AboutPage()
        self.ui.setupUi(self)