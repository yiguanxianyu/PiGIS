from PySide6.QtWidgets import QWidget

from ui.raw import Ui_AboutPage


class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutPage()
        self.ui.setupUi(self)