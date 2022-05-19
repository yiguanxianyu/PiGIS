# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_fieldTable.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QHeaderView, QSizePolicy, QTableWidget,
    QTableWidgetItem, QToolButton, QWidget)

class Ui_FieldTable(object):
    def setupUi(self, FieldTable):
        if not FieldTable.objectName():
            FieldTable.setObjectName(u"FieldTable")
        FieldTable.resize(403, 300)
        self.gridLayout = QGridLayout(FieldTable)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(FieldTable)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 25))
        self.widget.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.addFieldButton = QToolButton(self.widget)
        self.addFieldButton.setObjectName(u"addFieldButton")

        self.horizontalLayout_2.addWidget(self.addFieldButton)

        self.deleteFieldButton = QToolButton(self.widget)
        self.deleteFieldButton.setObjectName(u"deleteFieldButton")

        self.horizontalLayout_2.addWidget(self.deleteFieldButton)

        self.saveButton = QToolButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.toggleEditingCheckBox = QCheckBox(self.widget)
        self.toggleEditingCheckBox.setObjectName(u"toggleEditingCheckBox")
        self.toggleEditingCheckBox.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout_2.addWidget(self.toggleEditingCheckBox)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.dataTable = QTableWidget(FieldTable)
        if (self.dataTable.columnCount() < 5):
            self.dataTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.dataTable.rowCount() < 5):
            self.dataTable.setRowCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.dataTable.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.dataTable.setItem(2, 2, __qtablewidgetitem11)
        self.dataTable.setObjectName(u"dataTable")
        self.dataTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.dataTable, 1, 0, 1, 1)


        self.retranslateUi(FieldTable)
        self.addFieldButton.clicked.connect(FieldTable.add_field)
        self.deleteFieldButton.clicked.connect(FieldTable.delete_field)
        self.toggleEditingCheckBox.stateChanged.connect(FieldTable.toggle_editing_changed)
        self.saveButton.clicked.connect(FieldTable.save)

        QMetaObject.connectSlotsByName(FieldTable)
    # setupUi

    def retranslateUi(self, FieldTable):
        FieldTable.setWindowTitle(QCoreApplication.translate("FieldTable", u"Form", None))
        self.addFieldButton.setText(QCoreApplication.translate("FieldTable", u"Add Field", None))
        self.deleteFieldButton.setText(QCoreApplication.translate("FieldTable", u"Delete Field", None))
        self.saveButton.setText(QCoreApplication.translate("FieldTable", u"Save", None))
        self.toggleEditingCheckBox.setText(QCoreApplication.translate("FieldTable", u"Togle Editing", None))
        ___qtablewidgetitem = self.dataTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FieldTable", u"\u52171", None));
        ___qtablewidgetitem1 = self.dataTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FieldTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem2 = self.dataTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FieldTable", u"\u52172", None));
        ___qtablewidgetitem3 = self.dataTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FieldTable", u"3", None));
        ___qtablewidgetitem4 = self.dataTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FieldTable", u"test5", None));
        ___qtablewidgetitem5 = self.dataTable.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FieldTable", u"1", None));
        ___qtablewidgetitem6 = self.dataTable.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FieldTable", u"2", None));
        ___qtablewidgetitem7 = self.dataTable.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("FieldTable", u"3", None));
        ___qtablewidgetitem8 = self.dataTable.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("FieldTable", u"4", None));
        ___qtablewidgetitem9 = self.dataTable.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("FieldTable", u"5", None));

        __sortingEnabled = self.dataTable.isSortingEnabled()
        self.dataTable.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.dataTable.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("FieldTable", u"test1", None));
        ___qtablewidgetitem11 = self.dataTable.item(2, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("FieldTable", u"test2", None));
        self.dataTable.setSortingEnabled(__sortingEnabled)

    # retranslateUi

