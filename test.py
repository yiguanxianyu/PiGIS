import sys
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt


class SnippetTreeView(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        super(SnippetTreeView, self).__init__(parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setDragEnabled(False)
        self.setDragDropOverwriteMode(False)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.header().setStretchLastSection(True)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)


def create_tag_color_items():
    item_tag = QtGui.QStandardItem('tag')
    item_tag.setDropEnabled(False)
    item_color = QtGui.QStandardItem('color')
    item_color.setDropEnabled(False)
    return item_tag, item_color


def add_items(_model):
    headers = [
        'Name',
        'Tag',
        'Color',
    ]

    _model.setHorizontalHeaderLabels(headers)
    _model.setColumnCount(len(headers))

    for num in range(4):
        parent_item = QtGui.QStandardItem('parent-' + str(num))
        parent_item.setDropEnabled(True)
        item_tag, item_color = create_tag_color_items()

        for n in range(num + 2):
            child_item = QtGui.QStandardItem(str(n))
            child_item.setDropEnabled(False)
            ch_item_tag, ch_item_color = create_tag_color_items()
            parent_item.appendRow([child_item, ch_item_tag, ch_item_color])

        _model.appendRow([parent_item, item_tag, item_color])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tree = SnippetTreeView()
    tree.setSortingEnabled(True)
    model = QtGui.QStandardItemModel()
    add_items(model)
    tree.setModel(model)
    tree.expandAll()
    tree.show()
    rec = app.exec()
    sys.exit(rec)
