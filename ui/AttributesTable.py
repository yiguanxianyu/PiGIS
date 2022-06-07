import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtWidgets import QWidget, QAbstractItemView, QDialog

from ui.raw import Ui_AttributesTable, Ui_RemoveField, Ui_inputFilterDialog

test_data = pd.DataFrame([
    [1, 9, 2],
    [1, 0, -1],
    [3, 5, 2],
    [3, 3, 2],
    [5, 8, 9],
], columns=['A', 'B', 'C'])


class FilterDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_inputFilterDialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)


class RemoveFieldDialog(QDialog):
    def __init__(self, parent, items):
        super().__init__(parent)
        self.ui = Ui_RemoveField()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.ui.listWidget.addItems(items)


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.__row_count = data.shape[0]
        self.__column_count = data.shape[1]
        self.edited = {}
        self.deleted = []

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role: int = ...):
        match role:
            case Qt.ItemDataRole.DisplayRole | Qt.ItemDataRole.EditRole:
                return str(self._data.iloc[index.row(), index.column()])
            case _:
                pass

    def setData(self, index, value, role: int = ...):
        self._data.iloc[index.row(), index.column()] = value
        # TODO 检查数据类型是否符合
        return True

    def rowCount(self, index=...):
        return self.__row_count

    def columnCount(self, index=...):
        return self.__column_count

    def removeRows(self, row: int, count: int, parent=...):
        self.beginRemoveRows(QModelIndex(), row, row + count - 1)
        self._data.drop(list(range(row, row + count)))
        self.__row_count -= count
        self.endRemoveRows()
        return True

    def removeColumns(self, row: int, count: int, parent=...):
        ...

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
        self.data_filter = None
        self.layer = layer
        self.fieldTable = None
        self.editState = False
        self.ui = Ui_AttributesTable()
        self.ui.setupUi(self)

        # table = TableModel(layer.get_attr_table())
        self.table = TableModel(test_data)
        self.ui.tableView.setModel(self.table)

    def focusInEvent(self, e) -> None:
        self.grabKeyboard()

    def focusOutEvent(self, e) -> None:
        self.releaseKeyboard()

    def add_row(self):
        ...

    def remove_row(self):
        rows = sorted(list(set(i.row() for i in self.ui.tableView.selectedIndexes())), reverse=True)
        if rows:
            for row in rows:
                self.table.removeRow(row)

    def add_field(self):
        pass

    def remove_field(self):
        RemoveFieldDialog(self, ['1', '2', '3']).show()

    def filter_data(self):
        self.data_filter = FilterDialog(self)
        self.data_filter.show()

    def toggle_editing_changed(self, flag):
        if flag:
            self.editState = True
            self.ui.tableView.setEditTriggers(QAbstractItemView.DoubleClicked)
        else:
            self.editState = False
            self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def closeEvent(self, event):
        pass
        # self.layer.attributesTableDestroyed()

    def features_selected(self, fids):
        pass
