# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_symbology.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QLocale,
                            QMetaObject, QSize)
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem)


class Ui_Symbology(object):
    def setupUi(self, Symbology):
        if not Symbology.objectName():
            Symbology.setObjectName(u"Symbology")
        Symbology.resize(487, 369)
        Symbology.setMinimumSize(QSize(400, 300))
        Symbology.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout = QGridLayout(Symbology)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Symbology)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(Symbology)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(80, 20))
        self.lineEdit.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(Symbology)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(15000, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(Symbology)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton = QPushButton(Symbology)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(Symbology)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.retranslateUi(Symbology)

        QMetaObject.connectSlotsByName(Symbology)

    # setupUi

    def retranslateUi(self, Symbology):
        Symbology.setWindowTitle(QCoreApplication.translate("Symbology", u"Symbology", None))
        self.label.setText(QCoreApplication.translate("Symbology", u"Color", None))
        self.label_2.setText(QCoreApplication.translate("Symbology", u"Line Width  ", None))
        self.pushButton_3.setText(QCoreApplication.translate("Symbology", u"Save", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Symbology", u"Cancel", None))
    # retranslateUi
