# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_options.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

class Ui_OptionsPage(object):
    def setupUi(self, OptionsPage):
        if not OptionsPage.objectName():
            OptionsPage.setObjectName(u"OptionsPage")
        OptionsPage.resize(320, 240)
        OptionsPage.setMinimumSize(QSize(320, 240))
        OptionsPage.setMaximumSize(QSize(1920, 1080))

        self.retranslateUi(OptionsPage)

        QMetaObject.connectSlotsByName(OptionsPage)
    # setupUi

    def retranslateUi(self, OptionsPage):
        OptionsPage.setWindowTitle(QCoreApplication.translate("OptionsPage", u"Options", None))
    # retranslateUi

