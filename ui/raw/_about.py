# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_about.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QLocale,
                            QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QVBoxLayout)


class Ui_AboutPage(object):
    def setupUi(self, AboutPage):
        if not AboutPage.objectName():
            AboutPage.setObjectName(u"AboutPage")
        AboutPage.setWindowModality(Qt.NonModal)
        AboutPage.resize(320, 270)
        AboutPage.setMinimumSize(QSize(320, 270))
        AboutPage.setMaximumSize(QSize(320, 240))
        AboutPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(AboutPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AboutPage)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(AboutPage)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.RichText)

        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(AboutPage)

        QMetaObject.connectSlotsByName(AboutPage)

    # setupUi

    def retranslateUi(self, AboutPage):
        AboutPage.setWindowTitle(QCoreApplication.translate("AboutPage", u"About", None))
        self.label.setText(QCoreApplication.translate("AboutPage", u"About", None))
        self.label_2.setText(QCoreApplication.translate("AboutPage",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u03c0GIS v0.1.0 </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Made By: </span><br/>Chi Zhang <br/>Kaihao Zheng <br/>Haoliang Chen <br/>\u2764\ufe0f </p><p align=\"center\"><span style=\" font-size:11pt;\">Powered by open-source software: </span><br/>PySide6 <br/>pyinstaller <br/>PyYAML </p></body></html>",
                                                        None))
    # retranslateUi
