# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_layertree.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QSizePolicy, QTreeView, QVBoxLayout, QWidget)

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
        self.treeView.header().setVisible(True)

        self.verticalLayout.addWidget(self.treeView)


        self.retranslateUi(LayerTree)
        LayerTree.customContextMenuRequested.connect(LayerTree.show_context_menu)
        self.treeView.pressed.connect(LayerTree.clicked)

        QMetaObject.connectSlotsByName(LayerTree)
    # setupUi

    def retranslateUi(self, LayerTree):
        LayerTree.setWindowTitle(QCoreApplication.translate("LayerTree", u"Form", None))
    # retranslateUi

