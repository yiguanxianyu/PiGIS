# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_addFieldDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QComboBox, QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
                               QSizePolicy, QSpacerItem, QVBoxLayout)


class Ui_AddFieldDialog(object):
    def setupUi(self, AddFieldDialog):
        if not AddFieldDialog.objectName():
            AddFieldDialog.setObjectName(u"AddFieldDialog")
        AddFieldDialog.resize(390, 197)
        self.verticalLayout_2 = QVBoxLayout(AddFieldDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AddFieldDialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(120, 120))

        self.verticalLayout.addWidget(self.label)

        self.fieldNameEdit = QLineEdit(AddFieldDialog)
        self.fieldNameEdit.setObjectName(u"fieldNameEdit")
        self.fieldNameEdit.setMaximumSize(QSize(120, 120))

        self.verticalLayout.addWidget(self.fieldNameEdit)

        self.labelMaxLength = QLabel(AddFieldDialog)
        self.labelMaxLength.setObjectName(u"labelMaxLength")
        self.labelMaxLength.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout.addWidget(self.labelMaxLength)

        self.maxLengthEdit = QLineEdit(AddFieldDialog)
        self.maxLengthEdit.setObjectName(u"maxLengthEdit")
        self.maxLengthEdit.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout.addWidget(self.maxLengthEdit)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(AddFieldDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(120, 120))

        self.verticalLayout_3.addWidget(self.label_2)

        self.comboBox = QComboBox(AddFieldDialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(120, 120))

        self.verticalLayout_3.addWidget(self.comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(AddFieldDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(AddFieldDialog)
        self.buttonBox.accepted.connect(AddFieldDialog.accept)
        self.buttonBox.rejected.connect(AddFieldDialog.reject)
        self.comboBox.currentIndexChanged.connect(AddFieldDialog.index_changed)

        QMetaObject.connectSlotsByName(AddFieldDialog)

    # setupUi

    def retranslateUi(self, AddFieldDialog):
        AddFieldDialog.setWindowTitle(QCoreApplication.translate("AddFieldDialog", u"Add Field", None))
        self.label.setText(QCoreApplication.translate("AddFieldDialog", u"Field Name", None))
        self.labelMaxLength.setText(QCoreApplication.translate("AddFieldDialog", u"Max Length", None))
        self.label_2.setText(QCoreApplication.translate("AddFieldDialog", u"Field Type", None))
    # retranslateUi
