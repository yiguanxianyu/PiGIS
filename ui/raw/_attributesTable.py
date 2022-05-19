# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_attributesTable.ui'
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

class Ui_AttributesTable(object):
    def setupUi(self, AttributesTable):
        if not AttributesTable.objectName():
            AttributesTable.setObjectName(u"AttributesTable")
        AttributesTable.resize(739, 401)
        AttributesTable.setContextMenuPolicy(Qt.NoContextMenu)
        self.gridLayout = QGridLayout(AttributesTable)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dataTable = QTableWidget(AttributesTable)
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

        self.widget = QWidget(AttributesTable)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 25))
        self.widget.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.editFieldButton = QToolButton(self.widget)
        self.editFieldButton.setObjectName(u"editFieldButton")

        self.horizontalLayout.addWidget(self.editFieldButton)

        self.addItemButton = QToolButton(self.widget)
        self.addItemButton.setObjectName(u"addItemButton")

        self.horizontalLayout.addWidget(self.addItemButton)

        self.deleteItemButton = QToolButton(self.widget)
        self.deleteItemButton.setObjectName(u"deleteItemButton")

        self.horizontalLayout.addWidget(self.deleteItemButton)

        self.filterData = QToolButton(self.widget)
        self.filterData.setObjectName(u"filterData")

        self.horizontalLayout.addWidget(self.filterData)

        self.saveButton = QToolButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.toggleEditingCheckBox = QCheckBox(self.widget)
        self.toggleEditingCheckBox.setObjectName(u"toggleEditingCheckBox")
        self.toggleEditingCheckBox.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout.addWidget(self.toggleEditingCheckBox)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(AttributesTable)
        self.editFieldButton.clicked.connect(AttributesTable.edit_field)
        self.addItemButton.clicked.connect(AttributesTable.add_item)
        self.deleteItemButton.clicked.connect(AttributesTable.delete_item)
        self.toggleEditingCheckBox.stateChanged.connect(AttributesTable.toggle_editing_changed)
        self.filterData.clicked.connect(AttributesTable.filter_data)
        self.saveButton.clicked.connect(AttributesTable.save)

        QMetaObject.connectSlotsByName(AttributesTable)
    # setupUi

    def retranslateUi(self, AttributesTable):
        AttributesTable.setWindowTitle(QCoreApplication.translate("AttributesTable", u"Attributes Table", None))
        ___qtablewidgetitem = self.dataTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AttributesTable", u"\u52171", None));
        ___qtablewidgetitem1 = self.dataTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AttributesTable", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem2 = self.dataTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AttributesTable", u"\u52172", None));
        ___qtablewidgetitem3 = self.dataTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AttributesTable", u"3", None));
        ___qtablewidgetitem4 = self.dataTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AttributesTable", u"test5", None));
        ___qtablewidgetitem5 = self.dataTable.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AttributesTable", u"1", None));
        ___qtablewidgetitem6 = self.dataTable.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AttributesTable", u"2", None));
        ___qtablewidgetitem7 = self.dataTable.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AttributesTable", u"3", None));
        ___qtablewidgetitem8 = self.dataTable.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AttributesTable", u"4", None));
        ___qtablewidgetitem9 = self.dataTable.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AttributesTable", u"5", None));

        __sortingEnabled = self.dataTable.isSortingEnabled()
        self.dataTable.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.dataTable.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AttributesTable", u"test1", None));
        ___qtablewidgetitem11 = self.dataTable.item(2, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AttributesTable", u"test2", None));
        self.dataTable.setSortingEnabled(__sortingEnabled)

        self.editFieldButton.setText(QCoreApplication.translate("AttributesTable", u"Edit Field", None))
        self.addItemButton.setText(QCoreApplication.translate("AttributesTable", u"Add Item", None))
        self.deleteItemButton.setText(QCoreApplication.translate("AttributesTable", u"Delete Item", None))
        self.filterData.setText(QCoreApplication.translate("AttributesTable", u"Filter", None))
        self.saveButton.setText(QCoreApplication.translate("AttributesTable", u"Save", None))
        self.toggleEditingCheckBox.setText(QCoreApplication.translate("AttributesTable", u"Togle Editing", None))
    # retranslateUi

