# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AboutPage(object):
    def setupUi(self, AboutPage):
        if not AboutPage.objectName():
            AboutPage.setObjectName(u"AboutPage")
        AboutPage.setWindowModality(Qt.NonModal)
        AboutPage.resize(320, 240)
        AboutPage.setMinimumSize(QSize(320, 240))
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
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(AboutPage)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.retranslateUi(AboutPage)

        QMetaObject.connectSlotsByName(AboutPage)
    # setupUi

    def retranslateUi(self, AboutPage):
        AboutPage.setWindowTitle(QCoreApplication.translate("AboutPage", u"About", None))
        self.label.setText(QCoreApplication.translate("AboutPage", u"About", None))
        self.label_2.setText(QCoreApplication.translate("AboutPage", u"\u03c0GIS  v0.1.0\n"
"\n"
"Made By:\n"
"Chi Zhang\n"
"Kaihao Zheng\n"
"Haoliang Chen\n"
"\n"
"Powered by open-source software:\n"
"PiSide6\n"
"pyinstaller\n"
"PyYAML", None))
    # retranslateUi
