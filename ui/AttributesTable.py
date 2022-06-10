import numpy as np
import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtWidgets import QWidget, QAbstractItemView, QDialog, QHeaderView, QMessageBox, QInputDialog

from PiMapObj.PiLayer import PiLayer
from ui.raw import Ui_AttributesTable, Ui_RemoveField, Ui_AddFieldDialog

data_type = [np.int16, np.int32, np.int64, np.float32, np.unicode_]
data_type_str = ['int16', 'int32', 'int64', 'float32', 'float64', 'string']


class AddFieldDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_AddFieldDialog()
        self.ui.setupUi(self)
        self.ui.labelMaxLength.setVisible(False)
        self.ui.maxLengthEdit.setVisible(False)

        self.ui.comboBox.addItems(data_type_str)

    def index_changed(self, index):
        if index == 5:
            self.ui.labelMaxLength.setVisible(True)
            self.ui.maxLengthEdit.setVisible(True)
        else:
            self.ui.labelMaxLength.setVisible(False)
            self.ui.maxLengthEdit.setVisible(False)

    def result(self):
        if self.ui.comboBox.currentIndex() == 5:
            return self.ui.fieldNameEdit.text(), np.dtype(f'U{self.ui.maxLengthEdit.text()}')
        return self.ui.fieldNameEdit.text(), np.dtype(data_type_str[self.ui.comboBox.currentIndex()])


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
        self.data_ = pd.DataFrame(data)
        self.fid_dtype = (data.dtype.names[0], data.dtype[0])
        self._dtype = [(data.dtype.names[i], data.dtype[i]) for i in range(1, len(data.dtype))]
        self.__row_count = len(data)
        self.__column_count = len(data[0]) - 1
        self.edited = {}
        self.deleted = []
        # 筛选相关
        self.original_data = self.data_
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
                return str(self.data_.iloc[index.row(), index.column() + 1])
            case Qt.ItemDataRole.ToolTipRole:
                return f'({index.row()},{self._dtype[index.column()][0]})  {self._dtype[index.column()][1]}'
            case _:
                return

    def setData(self, index, value, role: int = ...):
        try:
            new_data = self._dtype[index.column()][1].type(value)
            self.data_.iloc[index.row(), index.column() + 1] = new_data
            self.changed = True
            return True
        except Exception as e:
            QMessageBox.critical(QWidget(), e.__class__.__name__, str(e))
            return False

    def rowCount(self, index=...):
        return self.__row_count

    def columnCount(self, index=...):
        return self.__column_count

    def add_field(self, field):
        self._dtype.append(field)
        self.insertColumn(self.rowCount())

    def insertRows(self, begin: int, count: int, parent=...) -> bool:
        """考虑到使用场景，这里就只考虑添加一行了"""
        self.beginInsertRows(QModelIndex(), begin, begin + count - 1)

        data_to_insert = [np.max(np.array(self.data_.iloc[:, 0]).astype(self.fid_dtype[1], copy=False)) + 2]  # new fid

        for i in range(len(self._dtype)):
            temp_dtype = self._dtype[i][1]
            if np.issubdtype(temp_dtype, np.unicode_):
                data_to_insert.append(temp_dtype.type(''))
            else:
                data_to_insert.append(temp_dtype.type(0))

        self.data_ = pd.DataFrame(np.concatenate([self.data_.values, np.array([data_to_insert])]))
        self.__row_count += count
        self.endInsertRows()
        self.changed = True
        return True

    def removeRows(self, begin: int, count: int, parent=...):
        self.beginRemoveRows(QModelIndex(), begin, begin + count - 1)
        self.data_.drop(list(range(begin, begin + count)), inplace=True)
        self.data_.reset_index(drop=True, inplace=True)
        self.__row_count -= count
        self.endRemoveRows()
        self.changed = True
        return True

    def insertColumns(self, begin: int, count: int, parent=...) -> bool:
        self.beginInsertColumns(QModelIndex(), begin, begin + count - 1)
        type_ = self._dtype[-1][1].type
        self.data_[self._dtype[-1][0]] = '' if np.issubdtype(type_, np.unicode_) else type_(0)
        self.__column_count += count
        self.endInsertColumns()
        self.changed = True
        return True

    def removeColumns(self, begin: int, count: int, parent=...):
        self.beginRemoveColumns(QModelIndex(), begin, begin + count - 1)

        self.data_.drop([self.data_.columns[i + 1] for i in range(begin, begin + count)], inplace=True, axis=1)
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
                    return str(self.data_.index[section])
            case _:
                return

    def filter(self, text):
        if text:
            try:
                self.data_ = self.original_data.query(text)
                changed = True
            except Exception as e:
                QMessageBox.critical(QWidget(), e.__class__.__name__, str(e) + '\nExpression is incorrect')
                return False
        else:
            self.data_ = self.original_data
            changed = True

        if changed:
            self.__row_count = len(self.data_)
            self.parent().tableView.setModel(None)
            self.parent().tableView.setModel(self)
            self.parent().graph.cancel_highlight_feature(self.parent().layer_id)
        return True

    def save(self):
        self.changed = False
        data_type = np.dtype([self.fid_dtype] + self._dtype)
        return np.array([tuple(row) for _, row in self.data_.iterrows()], dtype=data_type)


class AttributesTable(QWidget):
    def __init__(self, graph, layer: PiLayer):
        super().__init__()
        self.graph = graph
        self.layer = layer
        self.layer_id = layer.id
        self.editState = False
        self.filter_text = ''
        self.ui = Ui_AttributesTable()
        self.ui.setupUi(self)

        self.tableView = self.ui.tableView
        self.tableView.setVerticalHeader(PiAttrHeader(self))
        # 注意这里的 parent 填成 self 可能在埋雷
        self.tableModel = TableModel(self, layer.get_attr_table())
        self.tableView.setModel(self.tableModel)

        self.edited = []
        self.added = []
        self.removed = []

    def focusInEvent(self, e) -> None:
        self.grabKeyboard()

    def focusOutEvent(self, e) -> None:
        self.releaseKeyboard()

    def save(self):
        new_data = self.tableModel.save()
        self.graph.edit_feature_attr(self.layer_id, new_data)

    def get_selected_features(self):
        data = self.tableModel.data_
        return [data.iloc[i.row(), 0] for i in self.tableView.selectionModel().selectedRows()]

    def highlight_feature(self):
        s = self.get_selected_features()
        self.graph.highlight_feature(self.layer_id, s)

    def add_row(self):
        self.tableModel.insertRow(self.tableModel.rowCount())
        self.tableView.scrollToBottom()

    def remove_row(self):
        rows = sorted(list({i.row() for i in self.tableView.selectedIndexes()}), reverse=True)
        ids = [self.tableModel.data_.iloc[i, 0] for i in rows]
        self.removed.extend(ids)

        if rows:
            length = len(rows)
            if length == 1:
                self.tableModel.removeRow(rows[0])
            elif length == rows[0] - rows[-1] + 1:
                self.tableModel.removeRows(rows[-1], length)
            else:
                for row in rows:
                    self.tableModel.removeRow(row)

            self.graph.set_features_visibility(self.layer_id, ids, False)

    def add_field(self):
        s = AddFieldDialog(self)
        if s.exec():
            self.tableModel.add_field(s.result())

    def remove_field(self):
        s = RemoveFieldDialog(self, self.tableModel.get_columns())
        field_to_remove = sorted(s.result(), reverse=True)
        for f in field_to_remove:
            self.tableModel.removeColumn(f)

    def filter_data(self):
        text, flag = QInputDialog.getText(self, 'Input Filter', 'Example: F1 > 800',
                                          text=self.filter_text)
        if flag and self.tableModel.filter(text):
            self.filter_text = text

    def toggle_editing_changed(self, flag):
        if flag:
            self.editState = True
            self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked)
        else:
            self.editState = False
            self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def closeEvent(self, event):
        self.graph.cancel_highlight_feature(self.layer_id)
        if self.tableModel.changed:
            buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel
            title = 'Changed Unsaved'
            text = "You didn't save your changes.\nSave before exit?"
            result = QMessageBox.question(self, title, text, buttons)
            match result:
                case QMessageBox.StandardButton.Yes:
                    self.tableModel.save()
                    event.accept()
                case QMessageBox.StandardButton.No:
                    self.graph.set_features_visibility(self.layer_id, self.removed, True)
                    event.accept()
                case QMessageBox.StandardButton.Cancel:
                    event.ignore()
                case _:
                    QMessageBox.critical(str(result))


class PiAttrHeader(QHeaderView):
    def __init__(self, table_widget):
        super(PiAttrHeader, self).__init__(Qt.Orientation.Vertical, table_widget.tableView)
        self.table_widget = table_widget
        self.setSectionsClickable(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

    def mouseReleaseEvent(self, e) -> None:
        self.table_widget.highlight_feature()
        super(PiAttrHeader, self).mouseReleaseEvent(e)
