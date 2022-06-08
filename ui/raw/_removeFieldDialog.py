# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_removeFieldDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QGridLayout, QListWidget, QListWidgetItem,
    QSizePolicy, QWidget)

class Ui_RemoveField(object):
    def setupUi(self, RemoveField):
        if not RemoveField.objectName():
            RemoveField.setObjectName(u"RemoveField")
        RemoveField.setWindowModality(Qt.ApplicationModal)
        RemoveField.resize(174, 300)
        self.gridLayout = QGridLayout(RemoveField)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fieldList = QListWidget(RemoveField)
        self.fieldList.setObjectName(u"fieldList")
        self.fieldList.setSelectionMode(QAbstractItemView.MultiSelection)
        self.fieldList.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.fieldList, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(RemoveField)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(RemoveField)
        self.buttonBox.rejected.connect(RemoveField.reject)
        self.buttonBox.accepted.connect(RemoveField.field_chosen)

        QMetaObject.connectSlotsByName(RemoveField)
    # setupUi

    def retranslateUi(self, RemoveField):
        RemoveField.setWindowTitle(QCoreApplication.translate("RemoveField", u"Remove Field", None))
    # retranslateUi

