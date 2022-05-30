# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chenhaoliang/chl/大学课程作业等/大三下/GIS设计与应用/work1/PiGIS/ui/raw/_about.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutPage(object):
    def setupUi(self, AboutPage):
        AboutPage.setObjectName("AboutPage")
        AboutPage.setWindowModality(QtCore.Qt.NonModal)
        AboutPage.resize(320, 270)
        AboutPage.setMinimumSize(QtCore.QSize(320, 270))
        AboutPage.setMaximumSize(QtCore.QSize(320, 240))
        AboutPage.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AboutPage)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(AboutPage)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(AboutPage)
        QtCore.QMetaObject.connectSlotsByName(AboutPage)

    def retranslateUi(self, AboutPage):
        _translate = QtCore.QCoreApplication.translate
        AboutPage.setWindowTitle(_translate("AboutPage", "About"))
        self.label.setText(_translate("AboutPage", "About"))
        self.label_2.setText(_translate("AboutPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">πGIS v0.1.0 </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Made By: </span><br/>Chi Zhang <br/>Kaihao Zheng <br/>Haoliang Chen <br/>❤️ </p><p align=\"center\"><span style=\" font-size:11pt;\">Powered by open-source software: </span><br/>PySide6 <br/>pyinstaller <br/>PyYAML </p></body></html>"))
