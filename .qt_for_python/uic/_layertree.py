# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chenhaoliang/chl/大学课程作业等/大三下/GIS设计与应用/work1/PiGIS/ui/raw/_layertree.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LayerTree(object):
    def setupUi(self, LayerTree):
        LayerTree.setObjectName("LayerTree")
        LayerTree.resize(200, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LayerTree.sizePolicy().hasHeightForWidth())
        LayerTree.setSizePolicy(sizePolicy)
        LayerTree.setMinimumSize(QtCore.QSize(100, 0))
        LayerTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        LayerTree.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtWidgets.QVBoxLayout(LayerTree)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(LayerTree)
        self.treeView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.treeView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeView.setLineWidth(0)
        self.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeView.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(True)
        self.verticalLayout.addWidget(self.treeView)
        self.action_expand_all = QtWidgets.QAction(LayerTree)
        self.action_expand_all.setObjectName("action_expand_all")
        self.action_collapse_all = QtWidgets.QAction(LayerTree)
        self.action_collapse_all.setObjectName("action_collapse_all")
        self.action_add_layer_group = QtWidgets.QAction(LayerTree)
        self.action_add_layer_group.setObjectName("action_add_layer_group")

        self.retranslateUi(LayerTree)
        LayerTree.customContextMenuRequested['QPoint'].connect(LayerTree.show_context_menu)
        self.treeView.pressed['QModelIndex'].connect(LayerTree.clicked)
        self.action_add_layer_group.triggered.connect(LayerTree.add_layer_group)
        self.action_collapse_all.triggered.connect(self.treeView.collapseAll)
        self.action_expand_all.triggered.connect(self.treeView.expandAll)
        QtCore.QMetaObject.connectSlotsByName(LayerTree)

    def retranslateUi(self, LayerTree):
        _translate = QtCore.QCoreApplication.translate
        LayerTree.setWindowTitle(_translate("LayerTree", "Form"))
        self.action_expand_all.setText(_translate("LayerTree", "Expand All"))
        self.action_expand_all.setToolTip(_translate("LayerTree", "Expand All Layers"))
        self.action_collapse_all.setText(_translate("LayerTree", "Collapse All"))
        self.action_collapse_all.setToolTip(_translate("LayerTree", "Collapse All Layers"))
        self.action_add_layer_group.setText(_translate("LayerTree", "Add Layer Group"))
