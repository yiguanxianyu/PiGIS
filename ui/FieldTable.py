from PySide6.QtWidgets import QWidget, QAbstractItemView

from ui.raw import Ui_FieldTable


class FieldTable(QWidget):
    def __init__(self, datatype):
        super().__init__()
        self.editState = False
        self.ui = Ui_FieldTable()
        self.ui.setupUi(self)

    def save(self):
        ...

    def add_field(self):
        ...

    def delete_field(self):
        ...

    def toggle_editing_changed(self, flag):
        print(flag)
        if flag:
            self.editState = True
            self.ui.dataTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        else:
            self.editState = False
            self.ui.dataTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
