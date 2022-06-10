# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_attributesTable.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QAbstractItemView, QCheckBox, QHBoxLayout,
                               QSizePolicy, QSpacerItem, QTableView,
                               QToolButton, QVBoxLayout)


class Ui_AttributesTable(object):
    def setupUi(self, AttributesTable):
        if not AttributesTable.objectName():
            AttributesTable.setObjectName(u"AttributesTable")
        AttributesTable.resize(583, 401)
        AttributesTable.setContextMenuPolicy(Qt.NoContextMenu)
        self.verticalLayout = QVBoxLayout(AttributesTable)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filterData = QToolButton(AttributesTable)
        self.filterData.setObjectName(u"filterData")

        self.horizontalLayout.addWidget(self.filterData)

        self.addRowButton = QToolButton(AttributesTable)
        self.addRowButton.setObjectName(u"addRowButton")

        self.horizontalLayout.addWidget(self.addRowButton)

        self.removeRowButton = QToolButton(AttributesTable)
        self.removeRowButton.setObjectName(u"removeRowButton")

        self.horizontalLayout.addWidget(self.removeRowButton)

        self.removeFieldButton = QToolButton(AttributesTable)
        self.removeFieldButton.setObjectName(u"removeFieldButton")

        self.horizontalLayout.addWidget(self.removeFieldButton)

        self.addFieldButton = QToolButton(AttributesTable)
        self.addFieldButton.setObjectName(u"addFieldButton")

        self.horizontalLayout.addWidget(self.addFieldButton)

        self.saveButton = QToolButton(AttributesTable)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.toggleEditingCheckBox = QCheckBox(AttributesTable)
        self.toggleEditingCheckBox.setObjectName(u"toggleEditingCheckBox")
        self.toggleEditingCheckBox.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout.addWidget(self.toggleEditingCheckBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(AttributesTable)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setGridStyle(Qt.SolidLine)
        self.tableView.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(AttributesTable)
        self.addRowButton.clicked.connect(AttributesTable.add_row)
        self.toggleEditingCheckBox.stateChanged.connect(AttributesTable.toggle_editing_changed)
        self.filterData.clicked.connect(AttributesTable.filter_data)
        self.removeRowButton.clicked.connect(AttributesTable.remove_row)
        self.addFieldButton.clicked.connect(AttributesTable.add_field)
        self.removeFieldButton.clicked.connect(AttributesTable.remove_field)
        self.saveButton.clicked.connect(AttributesTable.save)

        QMetaObject.connectSlotsByName(AttributesTable)

    # setupUi

    def retranslateUi(self, AttributesTable):
        AttributesTable.setWindowTitle(QCoreApplication.translate("AttributesTable", u"Attributes Table", None))
        self.filterData.setText(QCoreApplication.translate("AttributesTable", u"Filter", None))
        self.addRowButton.setText(QCoreApplication.translate("AttributesTable", u"Add Row", None))
        self.removeRowButton.setText(QCoreApplication.translate("AttributesTable", u"Remove Row", None))
        self.removeFieldButton.setText(QCoreApplication.translate("AttributesTable", u"Remove Field", None))
        self.addFieldButton.setText(QCoreApplication.translate("AttributesTable", u"Add Field", None))
        self.saveButton.setText(QCoreApplication.translate("AttributesTable", u"Save", None))
        self.toggleEditingCheckBox.setText(QCoreApplication.translate("AttributesTable", u"Edit", None))
    # retranslateUi
