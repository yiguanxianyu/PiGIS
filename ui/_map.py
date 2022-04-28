# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_map.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)


class Ui_mapGraphView(object):
    def setupUi(self, mapGraphView):
        if not mapGraphView.objectName():
            mapGraphView.setObjectName(u"mapGraphView")
        mapGraphView.resize(320, 240)
        self.layout = QGridLayout(mapGraphView)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.layout.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(mapGraphView)

        QMetaObject.connectSlotsByName(mapGraphView)

    # setupUi

    def retranslateUi(self, mapGraphView):
        mapGraphView.setWindowTitle(QCoreApplication.translate("mapGraphView", u"Form", None))
    # retranslateUi
