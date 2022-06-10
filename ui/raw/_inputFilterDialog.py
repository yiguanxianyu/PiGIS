# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_inputFilterDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QLocale,
                            QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QLineEdit, QSizePolicy,
                               QToolButton)


class Ui_inputFilterDialog(object):

    def setupUi(self, inputFilterDialog):
        if not inputFilterDialog.objectName():
            inputFilterDialog.setObjectName(u"inputFilterDialog")
        inputFilterDialog.setWindowModality(Qt.ApplicationModal)
        inputFilterDialog.resize(300, 120)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            inputFilterDialog.sizePolicy().hasHeightForWidth())
        inputFilterDialog.setSizePolicy(sizePolicy)
        inputFilterDialog.setLocale(
            QLocale(QLocale.English, QLocale.UnitedStates))
        inputFilterDialog.setModal(True)
        self.confirmButton = QToolButton(inputFilterDialog)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(160, 80, 111, 31))
        self.CancelButton = QToolButton(inputFilterDialog)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(30, 80, 111, 31))
        self.lineEdit = QLineEdit(inputFilterDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 20, 241, 31))

        self.retranslateUi(inputFilterDialog)
        self.CancelButton.clicked.connect(inputFilterDialog.reject)
        self.confirmButton.clicked.connect(inputFilterDialog.accept)

        QMetaObject.connectSlotsByName(inputFilterDialog)

    # setupUi

    def retranslateUi(self, inputFilterDialog):
        inputFilterDialog.setWindowTitle(
            QCoreApplication.translate("inputFilterDialog", u"Input Filter",
                                       None))
        self.confirmButton.setText(
            QCoreApplication.translate("inputFilterDialog", u"Cancel", None))
        self.CancelButton.setText(
            QCoreApplication.translate("inputFilterDialog", u"Confirm", None))

    # retranslateUi
