# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_attributesTable.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QAbstractItemView, QCheckBox, QGridLayout,
                               QHBoxLayout, QTableView,
                               QToolButton, QWidget)


class Ui_AttributesTable(object):
    def setupUi(self, AttributesTable):
        if not AttributesTable.objectName():
            AttributesTable.setObjectName(u"AttributesTable")
        AttributesTable.setWindowModality(Qt.ApplicationModal)
        AttributesTable.resize(583, 401)
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
        self.filterData = QToolButton(self.widget)
        self.filterData.setObjectName(u"filterData")

        self.horizontalLayout.addWidget(self.filterData)

        self.addRowButton = QToolButton(self.widget)
        self.addRowButton.setObjectName(u"addRowButton")

        self.horizontalLayout.addWidget(self.addRowButton)

        self.removeRowButton = QToolButton(self.widget)
        self.removeRowButton.setObjectName(u"removeRowButton")

        self.horizontalLayout.addWidget(self.removeRowButton)

        self.addFieldButton = QToolButton(self.widget)
        self.addFieldButton.setObjectName(u"addFieldButton")

        self.horizontalLayout.addWidget(self.addFieldButton)

        self.removeFieldButton = QToolButton(self.widget)
        self.removeFieldButton.setObjectName(u"removeFieldButton")

        self.horizontalLayout.addWidget(self.removeFieldButton)

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
        self.addRowButton.clicked.connect(AttributesTable.add_row)
        self.toggleEditingCheckBox.stateChanged.connect(AttributesTable.toggle_editing_changed)
        self.filterData.clicked.connect(AttributesTable.filter_data)
        self.removeRowButton.clicked.connect(AttributesTable.remove_row)
        self.addFieldButton.clicked.connect(AttributesTable.add_field)
        self.removeFieldButton.clicked.connect(AttributesTable.remove_field)

        QMetaObject.connectSlotsByName(AttributesTable)

    # setupUi

    def retranslateUi(self, AttributesTable):
        AttributesTable.setWindowTitle(QCoreApplication.translate("AttributesTable", u"Attributes Table", None))
        self.filterData.setText(QCoreApplication.translate("AttributesTable", u"Filter", None))
        self.addRowButton.setText(QCoreApplication.translate("AttributesTable", u"Add Row", None))
        self.removeRowButton.setText(QCoreApplication.translate("AttributesTable", u"Remove Row", None))
        self.addFieldButton.setText(QCoreApplication.translate("AttributesTable", u"Add Field", None))
        self.removeFieldButton.setText(QCoreApplication.translate("AttributesTable", u"Remove Field", None))
        self.toggleEditingCheckBox.setText(QCoreApplication.translate("AttributesTable", u"Toggle Editing", None))
    # retranslateUi
