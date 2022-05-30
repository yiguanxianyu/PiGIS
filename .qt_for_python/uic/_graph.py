# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chenhaoliang/chl/大学课程作业等/大三下/GIS设计与应用/work1/PiGIS/ui/raw/_graph.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Graph(object):
    def setupUi(self, Graph):
        Graph.setObjectName("Graph")
        Graph.resize(548, 504)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Graph.sizePolicy().hasHeightForWidth())
        Graph.setSizePolicy(sizePolicy)
        Graph.setMinimumSize(QtCore.QSize(100, 0))
        self.gridLayout = QtWidgets.QGridLayout(Graph)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(Graph)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setLineWidth(0)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(Graph)
        QtCore.QMetaObject.connectSlotsByName(Graph)

    def retranslateUi(self, Graph):
        _translate = QtCore.QCoreApplication.translate
        Graph.setWindowTitle(_translate("Graph", "Form"))
