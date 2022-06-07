# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_graph.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QFrame, QGraphicsView, QGridLayout,
                               QSizePolicy)


class Ui_Graph(object):
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
        self.gridLayout = QGridLayout(Graph)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(Graph)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setFrameShape(QFrame.NoFrame)
        self.graphicsView.setLineWidth(0)

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(Graph)

        QMetaObject.connectSlotsByName(Graph)

    # setupUi

    def retranslateUi(self, Graph):
        Graph.setWindowTitle(QCoreApplication.translate("Graph", u"Form", None))
    # retranslateUi
