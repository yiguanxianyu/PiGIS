import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QWidget, QAbstractItemView

from ui.FieldTable import FieldTable
from ui.FilterDialog import FilterDialog
from ui.raw import Ui_AttributesTable


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.__row_count=data.shape[0]
        self.__column_count=data.shape[1]
        self.edited = {}
        self.deleted = []

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role: int = ...):
        match role:
            case Qt.ItemDataRole.DisplayRole | Qt.ItemDataRole.EditRole:
                if index in self.edited:
                    return self.edited[index]
                # TODO: Delete Item
                return str(self._data.iloc[index.row(), index.column()])
            case _:
                pass

    def setData(self, index, value, role: int = ...):
        self.edited[index] = value
        # TODO 检查数据类型是否符合
        return True

    def save_edited_data(self):
        for key, value in self.edited.items():
            self._data.iloc[key.row(), key.column()] = value
        self.edited.clear()

    def rowCount(self, index=...):
        return self.__row_count

    def columnCount(self, index=...):
        return self.__column_count

    def headerData(self, section, orientation, role=...):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])


class AttributesTable(QWidget):
    def __init__(self, layer):
        super().__init__()
        self.fieldTable = None
        self.editState = False
        self.ui = Ui_AttributesTable()
        self.ui.setupUi(self)

        data = pd.DataFrame([
            [1, 9, 2],
            [1, 0, -1],
            [3, 5, 2],
            [3, 3, 2],
            [5, 8, 9],
        ], columns=['A', 'B', 'C'])

        # table = TableModel(layer.get_attr_table())
        self.table = TableModel(data)
        self.ui.tableView.setModel(self.table)

    def save(self):
        self.table.save_edited_data()

    def edit_field(self):
        datatype = None
        self.fieldTable = FieldTable(datatype)
        self.fieldTable.show()

    def add_item(self):
        ...

    def delete_item(self):
        """
        这个好像有点难做啊
        """
        ...

    def filter_data(self):
        self.di = FilterDialog()
        self.di.open()

    def toggle_editing_changed(self, flag):
        if flag:
            self.editState = True
            self.ui.tableView.setEditTriggers(QAbstractItemView.DoubleClicked)
        else:
            self.editState = False
            self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
