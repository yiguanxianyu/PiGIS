# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_layertree.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QLocale,
                            QMetaObject, QSize, Qt)
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QAbstractItemView, QFrame, QSizePolicy, QTreeView, QVBoxLayout)


class Ui_LayerTree(object):
    def setupUi(self, LayerTree):
        if not LayerTree.objectName():
            LayerTree.setObjectName(u"LayerTree")
        LayerTree.resize(200, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LayerTree.sizePolicy().hasHeightForWidth())
        LayerTree.setSizePolicy(sizePolicy)
        LayerTree.setMinimumSize(QSize(100, 0))
        LayerTree.setContextMenuPolicy(Qt.CustomContextMenu)
        LayerTree.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.action_expand_all = QAction(LayerTree)
        self.action_expand_all.setObjectName(u"action_expand_all")
        self.action_collapse_all = QAction(LayerTree)
        self.action_collapse_all.setObjectName(u"action_collapse_all")
        self.action_add_layer_group = QAction(LayerTree)
        self.action_add_layer_group.setObjectName(u"action_add_layer_group")
        self.verticalLayout = QVBoxLayout(LayerTree)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.treeView = QTreeView(LayerTree)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.treeView.setFrameShape(QFrame.NoFrame)
        self.treeView.setLineWidth(0)
        self.treeView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropMode(QAbstractItemView.InternalMove)
        self.treeView.setDefaultDropAction(Qt.MoveAction)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeView.header().setVisible(True)

        self.verticalLayout.addWidget(self.treeView)

        self.retranslateUi(LayerTree)
        LayerTree.customContextMenuRequested.connect(LayerTree.show_context_menu)
        self.treeView.pressed.connect(LayerTree.clicked)
        self.action_add_layer_group.triggered.connect(LayerTree.add_layer_group)
        self.action_collapse_all.triggered.connect(self.treeView.collapseAll)
        self.action_expand_all.triggered.connect(self.treeView.expandAll)

        QMetaObject.connectSlotsByName(LayerTree)

    # setupUi

    def retranslateUi(self, LayerTree):
        LayerTree.setWindowTitle(QCoreApplication.translate("LayerTree", u"Form", None))
        self.action_expand_all.setText(QCoreApplication.translate("LayerTree", u"Expand All", None))
        # if QT_CONFIG(tooltip)
        self.action_expand_all.setToolTip(QCoreApplication.translate("LayerTree", u"Expand All Layers", None))
        # endif // QT_CONFIG(tooltip)
        self.action_collapse_all.setText(QCoreApplication.translate("LayerTree", u"Collapse All", None))
        # if QT_CONFIG(tooltip)
        self.action_collapse_all.setToolTip(QCoreApplication.translate("LayerTree", u"Collapse All Layers", None))
        # endif // QT_CONFIG(tooltip)
        self.action_add_layer_group.setText(QCoreApplication.translate("LayerTree", u"Add Layer Group", None))
    # retranslateUi
