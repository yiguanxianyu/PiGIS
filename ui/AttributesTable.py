import numpy as np
import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtWidgets import QWidget, QAbstractItemView, QDialog, QHeaderView, QMessageBox, QInputDialog

from PiMapObj.PiLayer import PiLayer
from ui.raw import Ui_AttributesTable, Ui_RemoveField, Ui_inputFilterDialog


class FilterDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_inputFilterDialog()
        self.ui.setupUi(self)

    def accept(self) -> None:
        super(FilterDialog, self).accept()

    def done(self, arg__1: int) -> None:
        super(FilterDialog, self).done()

    def reject(self) -> None:
        super(FilterDialog, self).reject()


class RemoveFieldDialog(QDialog):
    def __init__(self, parent, items):
        super().__init__(parent)
        self.chosen = []
        self.ui = Ui_RemoveField()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.ui.fieldList.addItems(items)
        self.exec()

    def field_chosen(self):
        self.chosen = [i.row() for i in self.ui.fieldList.selectedIndexes()]
        self.accept()

    def result(self) -> list:
        return self.chosen


class TableModel(QAbstractTableModel):
    def __init__(self, parent, data):
        super(TableModel, self).__init__(parent)
        self._data = pd.DataFrame(data)

        self._dtype = [(data.dtype.names[i], data.dtype[i]) for i in range(1, len(data.dtype))]
        self.__row_count = len(data)
        self.__column_count = len(data[0]) - 1
        self.edited = {}
        self.deleted = []
        # 筛选相关
        self.original_data = self._data
        # 保存相关
        self.changed = False

    def get_columns(self):
        return [i[0] for i in self._dtype]

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role: int = ...):
        match role:
            case Qt.ItemDataRole.DisplayRole | Qt.ItemDataRole.EditRole:
                # -1是因为第一列是 feature id
                return str(self._data.iloc[index.row(), index.column() + 1])
            case Qt.ItemDataRole.ToolTipRole:
                return f'({index.row()},{self._dtype[index.column()][0]})  {self._dtype[index.column()][1]}'
            case _:
                return

    def setData(self, index, value, role: int = ...):
        try:
            new_data = self._dtype[index.column()][1].type(value)
            self._data.iloc[index.row(), index.column() + 1] = new_data
            self.changed = True
            return True
        except Exception as e:
            QMessageBox.critical(QWidget(), e.__class__.__name__, str(e))
            return False

    def rowCount(self, index=...):
        return self.__row_count

    def columnCount(self, index=...):
        return self.__column_count

    def insertRows(self, begin: int, count: int, parent=...) -> bool:
        """考虑到使用场景，这里就只考虑添加一行了"""
        self.beginInsertRows(QModelIndex(), begin, begin + count - 1)
        data_to_insert = np.array([[10000] + [self._dtype[i][1].type(0) for i in range(len(self._dtype))]])
        self._data = pd.DataFrame(np.concatenate([self._data.values, data_to_insert]))
        self.__row_count += count
        self.endInsertRows()
        self.changed = True
        return True

    def removeRows(self, begin: int, count: int, parent=...):
        self.beginRemoveRows(QModelIndex(), begin, begin + count - 1)
        self._data.drop(list(range(begin, begin + count)), inplace=True)
        self._data.reset_index(drop=True, inplace=True)
        self.__row_count -= count
        self.endRemoveRows()
        self.changed = True
        return True

    def insertColumns(self, begin: int, count: int, parent=...) -> bool:
        self.beginInsertColumns(QModelIndex(), begin, begin + count - 1)
        # TODO
        self.__column_count += count
        self.endInsertColumns()
        self.changed = True
        return True

    def removeColumns(self, begin: int, count: int, parent=...):
        self.beginRemoveColumns(QModelIndex(), begin, begin + count - 1)

        self._data.drop([self._data.columns[i + 1] for i in range(begin, begin + count)], inplace=True, axis=1)
        for i in range(begin + count - 1, begin - 1, -1):
            self._dtype.pop(i)

        self.__column_count -= count
        self.endRemoveColumns()
        self.changed = True
        return True

    def headerData(self, section, orientation, role=...):
        # section is the index of the column/row.
        match role:
            case Qt.ItemDataRole.DisplayRole | Qt.ItemDataRole.EditRole:
                if orientation == Qt.Orientation.Horizontal:
                    return str(self._dtype[section][0])

                if orientation == Qt.Orientation.Vertical:
                    return str(self._data.index[section])
            case _:
                return

    def filter(self, text):
        if text:
            try:
                self._data = self.original_data.query(text)
                changed = True
            except Exception as e:
                QMessageBox.critical(QWidget(), e.__class__.__name__, str(e) + '\nExpression is incorrect')
                return False
        else:
            self._data = self.original_data
            self.parent().graph.cancel_highlight_feature(self.parent().layer.id)
            changed = True

        if changed:
            self.__row_count = len(self._data)
            self.parent().tableView.setModel(None)
            self.parent().tableView.setModel(self)
            self.parent().graph.highlight_feature(self.parent().layer.id, self._data.index)
        return True

    def save(self):
        print('saving...')
        self.changed = True
        ...


class AttributesTable(QWidget):
    def __init__(self, graph, layer: PiLayer):
        super().__init__()
        self.graph = graph
        self.layer = layer
        self.editState = False
        self.filter_text = ''
        self.ui = Ui_AttributesTable()
        self.ui.setupUi(self)

        self.tableView = self.ui.tableView
        self.tableView.setVerticalHeader(PiAttrHeader(self))
        # 注意这里的 parent 填成 self 可能在埋雷
        self.tableModel = TableModel(self, layer.get_attr_table())
        self.tableView.setModel(self.tableModel)

    def focusInEvent(self, e) -> None:
        self.grabKeyboard()

    def focusOutEvent(self, e) -> None:
        self.releaseKeyboard()

    def get_selected_rows(self):
        return [i.row() for i in self.tableView.selectionModel().selectedRows()]

    def highlight_feature(self):
        self.graph.highlight_feature(self.layer.id, self.get_selected_rows())

    def add_row(self):
        self.tableModel.insertRow(self.tableModel.rowCount())
        self.tableView.scrollToBottom()

    def remove_row(self):
        rows = sorted(list(set(i.row() for i in self.tableView.selectedIndexes())), reverse=True)
        length = len(rows)
        if rows:
            if length == 1:
                self.tableModel.removeRow(rows[0])
            elif length == rows[0] - rows[-1] + 1:
                self.tableModel.removeRows(rows[-1], length)
            else:
                for row in rows:
                    self.tableModel.removeRow(row)
            self.graph.remove_feature(self.layer.id, rows)

    def add_field(self):
        pass

    def remove_field(self):
        s = RemoveFieldDialog(self, self.tableModel.get_columns())
        field_to_remove = sorted(s.result(), reverse=True)
        for f in field_to_remove:
            self.tableModel.removeColumn(f)

    def filter_data(self):
        text, flag = QInputDialog.getText(self, 'Input Filter', 'Example: F1 > 800',
                                          text=self.filter_text)
        if flag:
            if self.tableModel.filter(text):
                self.filter_text = text

    def toggle_editing_changed(self, flag):
        if flag:
            self.editState = True
            self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked)
        else:
            self.editState = False
            self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def closeEvent(self, event):
        if self.tableModel.changed:
            result = QMessageBox.question(self, 'Changed Unsaved', "You didn't save your changes.\nSave before exit?")
            if result == QMessageBox.StandardButton.Yes:
                self.tableModel.save()
        super(AttributesTable, self).closeEvent(event)

    def features_selected(self, fids):
        pass


class PiAttrHeader(QHeaderView):
    def __init__(self, table_widget):
        super(PiAttrHeader, self).__init__(Qt.Orientation.Vertical, table_widget.tableView)
        self.table_widget = table_widget
        self.setSectionsClickable(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

    def mouseReleaseEvent(self, e) -> None:
        self.table_widget.highlight_feature()
        super(PiAttrHeader, self).mouseReleaseEvent(e)

#
# def gen_test_data():
#     test_dtype = np.dtype(
#         [('fid', np.int32), ('A', np.int32), ('B', np.int32), ('C', np.int32), ('D', np.dtype('U20'))])
#     data0 = [(i, i + 1, i + 2, i + 3, 'iiiii') for i in range(500)]
#     return np.array(data0, dtype=test_dtype)
