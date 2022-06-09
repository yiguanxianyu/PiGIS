# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_symbology.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Symbology(object):
    def setupUi(self, Symbology):
        if not Symbology.objectName():
            Symbology.setObjectName(u"Symbology")
        Symbology.resize(473, 300)
        Symbology.setMinimumSize(QSize(400, 300))
        Symbology.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(Symbology)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Symbology)
        self.tabWidget.setObjectName(u"tabWidget")
        self.uniqueValue0 = QWidget()
        self.uniqueValue0.setObjectName(u"uniqueValue0")
        self.verticalLayout_2 = QVBoxLayout(self.uniqueValue0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_12 = QLabel(self.uniqueValue0)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)

        self.horizontalLayout.addWidget(self.label_12)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.uniqueValue0)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label)

        self.fieldsComboBox_0 = QComboBox(self.uniqueValue0)
        self.fieldsComboBox_0.setObjectName(u"fieldsComboBox_0")
        self.fieldsComboBox_0.setMinimumSize(QSize(80, 0))
        self.fieldsComboBox_0.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.fieldsComboBox_0)

        self.levelNumberLabel_0 = QLabel(self.uniqueValue0)
        self.levelNumberLabel_0.setObjectName(u"levelNumberLabel_0")
        self.levelNumberLabel_0.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.levelNumberLabel_0)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.uniqueValue0)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)

        self.borderWidth_0 = QLineEdit(self.uniqueValue0)
        self.borderWidth_0.setObjectName(u"borderWidth_0")
        self.borderWidth_0.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.borderWidth_0)

        self.label_19 = QLabel(self.uniqueValue0)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_11.addWidget(self.label_19)

        self.borderTypeCombo_0 = QComboBox(self.uniqueValue0)
        self.borderTypeCombo_0.addItem("")
        self.borderTypeCombo_0.addItem("")
        self.borderTypeCombo_0.addItem("")
        self.borderTypeCombo_0.addItem("")
        self.borderTypeCombo_0.addItem("")
        self.borderTypeCombo_0.addItem("")
        self.borderTypeCombo_0.setObjectName(u"borderTypeCombo_0")

        self.horizontalLayout_11.addWidget(self.borderTypeCombo_0)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_20 = QLabel(self.uniqueValue0)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_7.addWidget(self.label_20)

        self.borderColor_0 = QPushButton(self.uniqueValue0)
        self.borderColor_0.setObjectName(u"borderColor_0")

        self.horizontalLayout_7.addWidget(self.borderColor_0)

        self.label_21 = QLabel(self.uniqueValue0)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_7.addWidget(self.label_21)

        self.borderJoinCombo_0 = QComboBox(self.uniqueValue0)
        self.borderJoinCombo_0.addItem("")
        self.borderJoinCombo_0.addItem("")
        self.borderJoinCombo_0.addItem("")
        self.borderJoinCombo_0.setObjectName(u"borderJoinCombo_0")

        self.horizontalLayout_7.addWidget(self.borderJoinCombo_0)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_14 = QLabel(self.uniqueValue0)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setFont(font)

        self.verticalLayout_2.addWidget(self.label_14)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.uniqueValue0)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.beginColor_1 = QPushButton(self.uniqueValue0)
        self.beginColor_1.setObjectName(u"beginColor_1")

        self.horizontalLayout_2.addWidget(self.beginColor_1)

        self.endColor_2 = QPushButton(self.uniqueValue0)
        self.endColor_2.setObjectName(u"endColor_2")

        self.horizontalLayout_2.addWidget(self.endColor_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.uniqueValue0, "")
        self.byLevel1 = QWidget()
        self.byLevel1.setObjectName(u"byLevel1")
        self.verticalLayout_3 = QVBoxLayout(self.byLevel1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_25 = QLabel(self.byLevel1)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 20))
        self.label_25.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_25)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.byLevel1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.fieldsComboBox_1 = QComboBox(self.byLevel1)
        self.fieldsComboBox_1.setObjectName(u"fieldsComboBox_1")
        self.fieldsComboBox_1.setMinimumSize(QSize(80, 0))
        self.fieldsComboBox_1.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.fieldsComboBox_1)

        self.levelNumberLabel_1 = QLabel(self.byLevel1)
        self.levelNumberLabel_1.setObjectName(u"levelNumberLabel_1")
        self.levelNumberLabel_1.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.levelNumberLabel_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.byLevel1)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.borderWidth_1 = QLineEdit(self.byLevel1)
        self.borderWidth_1.setObjectName(u"borderWidth_1")
        self.borderWidth_1.setMinimumSize(QSize(100, 0))
        self.borderWidth_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.borderWidth_1)

        self.label_17 = QLabel(self.byLevel1)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)

        self.borderTypeCombo_1 = QComboBox(self.byLevel1)
        self.borderTypeCombo_1.addItem("")
        self.borderTypeCombo_1.addItem("")
        self.borderTypeCombo_1.addItem("")
        self.borderTypeCombo_1.addItem("")
        self.borderTypeCombo_1.addItem("")
        self.borderTypeCombo_1.addItem("")
        self.borderTypeCombo_1.setObjectName(u"borderTypeCombo_1")

        self.horizontalLayout_12.addWidget(self.borderTypeCombo_1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_22 = QLabel(self.byLevel1)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_5.addWidget(self.label_22)

        self.borderColor_1 = QPushButton(self.byLevel1)
        self.borderColor_1.setObjectName(u"borderColor_1")

        self.horizontalLayout_5.addWidget(self.borderColor_1)

        self.label_23 = QLabel(self.byLevel1)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_5.addWidget(self.label_23)

        self.borderJoinCombo_1 = QComboBox(self.byLevel1)
        self.borderJoinCombo_1.addItem("")
        self.borderJoinCombo_1.addItem("")
        self.borderJoinCombo_1.addItem("")
        self.borderJoinCombo_1.setObjectName(u"borderJoinCombo_1")

        self.horizontalLayout_5.addWidget(self.borderJoinCombo_1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.label_13 = QLabel(self.byLevel1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setFont(font)

        self.verticalLayout_3.addWidget(self.label_13)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_5 = QLabel(self.byLevel1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_13.addWidget(self.label_5)

        self.blLevelCombo = QComboBox(self.byLevel1)
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.addItem("")
        self.blLevelCombo.setObjectName(u"blLevelCombo")
        self.blLevelCombo.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_13.addWidget(self.blLevelCombo)

        self.label_24 = QLabel(self.byLevel1)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_13.addWidget(self.label_24)

        self.beginColor_2 = QPushButton(self.byLevel1)
        self.beginColor_2.setObjectName(u"beginColor_2")
        self.beginColor_2.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.beginColor_2)

        self.endColor_1 = QPushButton(self.byLevel1)
        self.endColor_1.setObjectName(u"endColor_1")

        self.horizontalLayout_13.addWidget(self.endColor_1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.tabWidget.addTab(self.byLevel1, "")
        self.singleValue2 = QWidget()
        self.singleValue2.setObjectName(u"singleValue2")
        self.verticalLayout_5 = QVBoxLayout(self.singleValue2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.singleValue2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font)

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.singleValue2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.borderWidth_2 = QLineEdit(self.singleValue2)
        self.borderWidth_2.setObjectName(u"borderWidth_2")
        self.borderWidth_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_9.addWidget(self.borderWidth_2)

        self.label_9 = QLabel(self.singleValue2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.borderTypeCombo_2 = QComboBox(self.singleValue2)
        self.borderTypeCombo_2.addItem("")
        self.borderTypeCombo_2.addItem("")
        self.borderTypeCombo_2.addItem("")
        self.borderTypeCombo_2.addItem("")
        self.borderTypeCombo_2.addItem("")
        self.borderTypeCombo_2.addItem("")
        self.borderTypeCombo_2.setObjectName(u"borderTypeCombo_2")

        self.horizontalLayout_9.addWidget(self.borderTypeCombo_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.singleValue2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.borderColor_2 = QPushButton(self.singleValue2)
        self.borderColor_2.setObjectName(u"borderColor_2")

        self.horizontalLayout_4.addWidget(self.borderColor_2)

        self.label_15 = QLabel(self.singleValue2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.borderJoinCombo_2 = QComboBox(self.singleValue2)
        self.borderJoinCombo_2.addItem("")
        self.borderJoinCombo_2.addItem("")
        self.borderJoinCombo_2.addItem("")
        self.borderJoinCombo_2.setObjectName(u"borderJoinCombo_2")

        self.horizontalLayout_4.addWidget(self.borderJoinCombo_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.label_10 = QLabel(self.singleValue2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setFont(font)

        self.verticalLayout_5.addWidget(self.label_10)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.singleValue2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.singleColor = QPushButton(self.singleValue2)
        self.singleColor.setObjectName(u"singleColor")

        self.horizontalLayout_10.addWidget(self.singleColor)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.tabWidget.addTab(self.singleValue2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(Symbology)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Symbology)
        self.beginColor_1.clicked.connect(Symbology.set_begin_color)
        self.beginColor_2.clicked.connect(Symbology.set_begin_color)
        self.endColor_1.clicked.connect(Symbology.set_end_color)
        self.endColor_2.clicked.connect(Symbology.set_end_color)
        self.singleColor.clicked.connect(Symbology.set_single_color)
        self.borderWidth_2.textEdited.connect(Symbology.set_border_width)
        self.borderWidth_1.textEdited.connect(Symbology.set_border_width)
        self.borderWidth_0.textEdited.connect(Symbology.set_border_width)
        self.borderTypeCombo_0.currentIndexChanged.connect(Symbology.set_border_type)
        self.borderTypeCombo_1.currentIndexChanged.connect(Symbology.set_border_type)
        self.borderTypeCombo_2.currentIndexChanged.connect(Symbology.set_border_type)
        self.borderColor_0.clicked.connect(Symbology.set_border_color)
        self.borderColor_2.clicked.connect(Symbology.set_border_color)
        self.borderColor_1.clicked.connect(Symbology.set_border_color)
        self.borderJoinCombo_2.currentIndexChanged.connect(Symbology.set_border_join)
        self.borderJoinCombo_0.currentIndexChanged.connect(Symbology.set_border_join)
        self.borderJoinCombo_1.currentIndexChanged.connect(Symbology.set_border_join)
        self.blLevelCombo.currentIndexChanged.connect(Symbology.set_bl_level_size)
        self.buttonBox.accepted.connect(Symbology.dialog_accept)
        self.buttonBox.rejected.connect(Symbology.dialog_reject)
        self.fieldsComboBox_0.currentIndexChanged.connect(Symbology.field_id_changed)
        self.fieldsComboBox_1.currentIndexChanged.connect(Symbology.field_id_changed)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Symbology)
    # setupUi

    def retranslateUi(self, Symbology):
        Symbology.setWindowTitle(QCoreApplication.translate("Symbology", u"Symbology", None))
        self.label_12.setText(QCoreApplication.translate("Symbology", u"Border Settings", None))
        self.label.setText(QCoreApplication.translate("Symbology", u"Choose Field", None))
        self.levelNumberLabel_0.setText(QCoreApplication.translate("Symbology", u"levels:", None))
        self.label_18.setText(QCoreApplication.translate("Symbology", u"Border Width", None))
        self.borderWidth_0.setText(QCoreApplication.translate("Symbology", u"1", None))
        self.label_19.setText(QCoreApplication.translate("Symbology", u"Border Type", None))
        self.borderTypeCombo_0.setItemText(0, QCoreApplication.translate("Symbology", u"No Line", None))
        self.borderTypeCombo_0.setItemText(1, QCoreApplication.translate("Symbology", u"Solid Line", None))
        self.borderTypeCombo_0.setItemText(2, QCoreApplication.translate("Symbology", u"Dash Line", None))
        self.borderTypeCombo_0.setItemText(3, QCoreApplication.translate("Symbology", u"Dot Line", None))
        self.borderTypeCombo_0.setItemText(4, QCoreApplication.translate("Symbology", u"Dash Dot Line", None))
        self.borderTypeCombo_0.setItemText(5, QCoreApplication.translate("Symbology", u"Dash Dot Dot Line", None))

        self.label_20.setText(QCoreApplication.translate("Symbology", u"Border Color", None))
        self.borderColor_0.setText(QCoreApplication.translate("Symbology", u"Choose Color", None))
        self.label_21.setText(QCoreApplication.translate("Symbology", u"Join Type", None))
        self.borderJoinCombo_0.setItemText(0, QCoreApplication.translate("Symbology", u"Bevel Join", None))
        self.borderJoinCombo_0.setItemText(1, QCoreApplication.translate("Symbology", u"Miter Join", None))
        self.borderJoinCombo_0.setItemText(2, QCoreApplication.translate("Symbology", u"Round Join", None))

        self.label_14.setText(QCoreApplication.translate("Symbology", u"Fill Settings (Ignored for Polylines)", None))
        self.label_3.setText(QCoreApplication.translate("Symbology", u"Fill Color", None))
        self.beginColor_1.setText(QCoreApplication.translate("Symbology", u"Begin Color", None))
        self.endColor_2.setText(QCoreApplication.translate("Symbology", u"End Color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uniqueValue0), QCoreApplication.translate("Symbology", u"Unique Value", None))
        self.label_25.setText(QCoreApplication.translate("Symbology", u"Border Settings", None))
        self.label_2.setText(QCoreApplication.translate("Symbology", u"Choose Field", None))
        self.levelNumberLabel_1.setText(QCoreApplication.translate("Symbology", u"levels:", None))
        self.label_16.setText(QCoreApplication.translate("Symbology", u"Border Width", None))
        self.borderWidth_1.setText(QCoreApplication.translate("Symbology", u"1", None))
        self.label_17.setText(QCoreApplication.translate("Symbology", u"Border Type", None))
        self.borderTypeCombo_1.setItemText(0, QCoreApplication.translate("Symbology", u"No Line", None))
        self.borderTypeCombo_1.setItemText(1, QCoreApplication.translate("Symbology", u"Solid Line", None))
        self.borderTypeCombo_1.setItemText(2, QCoreApplication.translate("Symbology", u"Dash Line", None))
        self.borderTypeCombo_1.setItemText(3, QCoreApplication.translate("Symbology", u"Dot Line", None))
        self.borderTypeCombo_1.setItemText(4, QCoreApplication.translate("Symbology", u"Dash Dot Line", None))
        self.borderTypeCombo_1.setItemText(5, QCoreApplication.translate("Symbology", u"Dash Dot Dot Line", None))

        self.label_22.setText(QCoreApplication.translate("Symbology", u"Border Color", None))
        self.borderColor_1.setText(QCoreApplication.translate("Symbology", u"Choose Color", None))
        self.label_23.setText(QCoreApplication.translate("Symbology", u"Join Type", None))
        self.borderJoinCombo_1.setItemText(0, QCoreApplication.translate("Symbology", u"Bevel Join", None))
        self.borderJoinCombo_1.setItemText(1, QCoreApplication.translate("Symbology", u"Miter Join", None))
        self.borderJoinCombo_1.setItemText(2, QCoreApplication.translate("Symbology", u"Round Join", None))

        self.label_13.setText(QCoreApplication.translate("Symbology", u"Fill Settings (Ignored for Polylines)", None))
        self.label_5.setText(QCoreApplication.translate("Symbology", u"Level Size", None))
        self.blLevelCombo.setItemText(0, QCoreApplication.translate("Symbology", u"2", None))
        self.blLevelCombo.setItemText(1, QCoreApplication.translate("Symbology", u"3", None))
        self.blLevelCombo.setItemText(2, QCoreApplication.translate("Symbology", u"4", None))
        self.blLevelCombo.setItemText(3, QCoreApplication.translate("Symbology", u"5", None))
        self.blLevelCombo.setItemText(4, QCoreApplication.translate("Symbology", u"6", None))
        self.blLevelCombo.setItemText(5, QCoreApplication.translate("Symbology", u"7", None))
        self.blLevelCombo.setItemText(6, QCoreApplication.translate("Symbology", u"8", None))
        self.blLevelCombo.setItemText(7, QCoreApplication.translate("Symbology", u"9", None))
        self.blLevelCombo.setItemText(8, QCoreApplication.translate("Symbology", u"10", None))
        self.blLevelCombo.setItemText(9, QCoreApplication.translate("Symbology", u"11", None))
        self.blLevelCombo.setItemText(10, QCoreApplication.translate("Symbology", u"12", None))
        self.blLevelCombo.setItemText(11, QCoreApplication.translate("Symbology", u"13", None))
        self.blLevelCombo.setItemText(12, QCoreApplication.translate("Symbology", u"14", None))
        self.blLevelCombo.setItemText(13, QCoreApplication.translate("Symbology", u"15", None))
        self.blLevelCombo.setItemText(14, QCoreApplication.translate("Symbology", u"16", None))

        self.label_24.setText(QCoreApplication.translate("Symbology", u"Fill Color", None))
        self.beginColor_2.setText(QCoreApplication.translate("Symbology", u"Begin Color", None))
        self.endColor_1.setText(QCoreApplication.translate("Symbology", u"End Color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.byLevel1), QCoreApplication.translate("Symbology", u"By Level", None))
        self.label_4.setText(QCoreApplication.translate("Symbology", u"Border Settings", None))
        self.label_6.setText(QCoreApplication.translate("Symbology", u"Border Width", None))
        self.borderWidth_2.setText(QCoreApplication.translate("Symbology", u"1", None))
        self.label_9.setText(QCoreApplication.translate("Symbology", u"Border Type", None))
        self.borderTypeCombo_2.setItemText(0, QCoreApplication.translate("Symbology", u"No Line", None))
        self.borderTypeCombo_2.setItemText(1, QCoreApplication.translate("Symbology", u"Solid Line", None))
        self.borderTypeCombo_2.setItemText(2, QCoreApplication.translate("Symbology", u"Dash Line", None))
        self.borderTypeCombo_2.setItemText(3, QCoreApplication.translate("Symbology", u"Dot Line", None))
        self.borderTypeCombo_2.setItemText(4, QCoreApplication.translate("Symbology", u"Dash Dot Line", None))
        self.borderTypeCombo_2.setItemText(5, QCoreApplication.translate("Symbology", u"Dash Dot Dot Line", None))

        self.label_7.setText(QCoreApplication.translate("Symbology", u"Border Color", None))
        self.borderColor_2.setText(QCoreApplication.translate("Symbology", u"Choose Color", None))
        self.label_15.setText(QCoreApplication.translate("Symbology", u"Join Type", None))
        self.borderJoinCombo_2.setItemText(0, QCoreApplication.translate("Symbology", u"Bevel Join", None))
        self.borderJoinCombo_2.setItemText(1, QCoreApplication.translate("Symbology", u"Miter Join", None))
        self.borderJoinCombo_2.setItemText(2, QCoreApplication.translate("Symbology", u"Round Join", None))

        self.label_10.setText(QCoreApplication.translate("Symbology", u"Fill Settings (Ignored for Polylines)", None))
        self.label_8.setText(QCoreApplication.translate("Symbology", u"Fill Color", None))
        self.singleColor.setText(QCoreApplication.translate("Symbology", u"Choose Color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.singleValue2), QCoreApplication.translate("Symbology", u"Single", None))
    # retranslateUi

