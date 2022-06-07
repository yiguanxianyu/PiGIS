# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_removeFieldDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QAbstractItemView, QDialogButtonBox, QGridLayout, QListWidget)


class Ui_RemoveField(object):
    def setupUi(self, FieldList):
        if not FieldList.objectName():
            FieldList.setObjectName(u"FieldList")
        FieldList.setWindowModality(Qt.ApplicationModal)
        FieldList.resize(174, 300)
        self.gridLayout = QGridLayout(FieldList)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(FieldList)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(FieldList)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(FieldList)

        QMetaObject.connectSlotsByName(FieldList)

    # setupUi

    def retranslateUi(self, FieldList):
        FieldList.setWindowTitle(QCoreApplication.translate("FieldList", u"Remove Field", None))
    # retranslateUi
