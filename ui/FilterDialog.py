from PySide6.QtWidgets import QDialog

from ui.raw import Ui_inputFilterDialog


class FilterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_inputFilterDialog()
        self.ui.setupUi(self)

    def get_text(self):
        self.open()
        print(self.ui.lineEdit.text())
