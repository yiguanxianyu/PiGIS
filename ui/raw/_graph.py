# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_graph.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QLocale,
                            QMetaObject, QSize)
from PySide6.QtWidgets import (QGridLayout, QSizePolicy)


class Ui_Graph(object):
    def __init__(self):
        self.graphicsView = None

    def setupUi(self, Graph):
        if not Graph.objectName():
            Graph.setObjectName(u"Graph")
        Graph.resize(548, 504)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Graph.sizePolicy().hasHeightForWidth())
        Graph.setSizePolicy(sizePolicy)
        Graph.setMinimumSize(QSize(100, 0))
        Graph.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout = QGridLayout(Graph)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(Graph)

        QMetaObject.connectSlotsByName(Graph)

    # setupUi

    def retranslateUi(self, Graph):
        pass
    # retranslateUi
