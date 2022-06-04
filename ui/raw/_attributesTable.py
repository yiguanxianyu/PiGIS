# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_attributesTable.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QHeaderView, QSizePolicy, QTableView,
    QToolButton, QWidget)

class Ui_AttributesTable(object):
    def setupUi(self, AttributesTable):
        if not AttributesTable.objectName():
            AttributesTable.setObjectName(u"AttributesTable")
        AttributesTable.setWindowModality(Qt.ApplicationModal)
        AttributesTable.resize(747, 401)
        AttributesTable.setContextMenuPolicy(Qt.NoContextMenu)
        self.gridLayout = QGridLayout(AttributesTable)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(AttributesTable)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 25))
        self.widget.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.editFieldButton = QToolButton(self.widget)
        self.editFieldButton.setObjectName(u"editFieldButton")

        self.horizontalLayout.addWidget(self.editFieldButton)

        self.addItemButton = QToolButton(self.widget)
        self.addItemButton.setObjectName(u"addItemButton")

        self.horizontalLayout.addWidget(self.addItemButton)

        self.deleteItemButton = QToolButton(self.widget)
        self.deleteItemButton.setObjectName(u"deleteItemButton")

        self.horizontalLayout.addWidget(self.deleteItemButton)

        self.filterData = QToolButton(self.widget)
        self.filterData.setObjectName(u"filterData")

        self.horizontalLayout.addWidget(self.filterData)

        self.saveButton = QToolButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.toggleEditingCheckBox = QCheckBox(self.widget)
        self.toggleEditingCheckBox.setObjectName(u"toggleEditingCheckBox")
        self.toggleEditingCheckBox.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout.addWidget(self.toggleEditingCheckBox)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.tableView = QTableView(AttributesTable)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setGridStyle(Qt.SolidLine)
        self.tableView.setSortingEnabled(True)

        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)


        self.retranslateUi(AttributesTable)
        self.editFieldButton.clicked.connect(AttributesTable.edit_field)
        self.addItemButton.clicked.connect(AttributesTable.add_item)
        self.deleteItemButton.clicked.connect(AttributesTable.delete_item)
        self.toggleEditingCheckBox.stateChanged.connect(AttributesTable.toggle_editing_changed)
        self.filterData.clicked.connect(AttributesTable.filter_data)
        self.saveButton.clicked.connect(AttributesTable.save)

        QMetaObject.connectSlotsByName(AttributesTable)
    # setupUi

    def retranslateUi(self, AttributesTable):
        AttributesTable.setWindowTitle(QCoreApplication.translate("AttributesTable", u"Attributes Table", None))
        self.editFieldButton.setText(QCoreApplication.translate("AttributesTable", u"Edit Field", None))
        self.addItemButton.setText(QCoreApplication.translate("AttributesTable", u"Add Item", None))
        self.deleteItemButton.setText(QCoreApplication.translate("AttributesTable", u"Delete Item", None))
        self.filterData.setText(QCoreApplication.translate("AttributesTable", u"Filter", None))
        self.saveButton.setText(QCoreApplication.translate("AttributesTable", u"Save", None))
        self.toggleEditingCheckBox.setText(QCoreApplication.translate("AttributesTable", u"Togle Editing", None))
    # retranslateUi

