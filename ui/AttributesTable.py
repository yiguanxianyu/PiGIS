from PySide6.QtWidgets import QWidget, QAbstractItemView

from ui.FieldTable import FieldTable
from ui.raw import Ui_AttributesTable


class AttributesTable(QWidget):
    def __init__(self, layer=None):
        super().__init__()
        self.fieldTable = None
        self.editState = False
        self.ui = Ui_AttributesTable()
        self.ui.setupUi(self)

    def save(self):
        ...

    def edit_field(self):
        datatype = None
        self.fieldTable = FieldTable(datatype)
        self.fieldTable.show()

    def add_item(self):
        ...

    def delete_item(self):
        ...

    def filter_data(self):
        ...

    def toggle_editing_changed(self, flag):
        if flag:
            self.editState = True
            self.ui.dataTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        else:
            self.editState = False
            self.ui.dataTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
