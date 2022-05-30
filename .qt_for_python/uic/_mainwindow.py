# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chenhaoliang/chl/大学课程作业等/大三下/GIS设计与应用/work1/PiGIS/ui/raw/_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 597)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.horizontalLayout_2.addLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 820, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuLayer = QtWidgets.QMenu(self.menuBar)
        self.menuLayer.setObjectName("menuLayer")
        self.menuCreateLayer = QtWidgets.QMenu(self.menuLayer)
        self.menuCreateLayer.setObjectName("menuCreateLayer")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuVector = QtWidgets.QMenu(self.menuBar)
        self.menuVector.setObjectName("menuVector")
        self.menuRaster = QtWidgets.QMenu(self.menuBar)
        self.menuRaster.setObjectName("menuRaster")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuProject = QtWidgets.QMenu(self.menuBar)
        self.menuProject.setObjectName("menuProject")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAllowedAreas(QtCore.Qt.BottomToolBarArea|QtCore.Qt.TopToolBarArea)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionProjectNew = QtWidgets.QAction(MainWindow)
        self.actionProjectNew.setObjectName("actionProjectNew")
        self.actionProjectOpen = QtWidgets.QAction(MainWindow)
        self.actionProjectOpen.setObjectName("actionProjectOpen")
        self.actionProjectSave = QtWidgets.QAction(MainWindow)
        self.actionProjectSave.setObjectName("actionProjectSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPasteAs = QtWidgets.QAction(MainWindow)
        self.actionPasteAs.setObjectName("actionPasteAs")
        self.actionCopyLayer = QtWidgets.QAction(MainWindow)
        self.actionCopyLayer.setObjectName("actionCopyLayer")
        self.actionEnableEditing = QtWidgets.QAction(MainWindow)
        self.actionEnableEditing.setCheckable(True)
        self.actionEnableEditing.setObjectName("actionEnableEditing")
        self.actionShowToolBar = QtWidgets.QAction(MainWindow)
        self.actionShowToolBar.setCheckable(True)
        self.actionShowToolBar.setChecked(True)
        self.actionShowToolBar.setObjectName("actionShowToolBar")
        self.actionSaveImage = QtWidgets.QAction(MainWindow)
        self.actionSaveImage.setObjectName("actionSaveImage")
        self.actionProjectSaveAs = QtWidgets.QAction(MainWindow)
        self.actionProjectSaveAs.setObjectName("actionProjectSaveAs")
        self.actionNewShapefileLayer = QtWidgets.QAction(MainWindow)
        self.actionNewShapefileLayer.setObjectName("actionNewShapefileLayer")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionAddLayer = QtWidgets.QAction(MainWindow)
        self.actionAddLayer.setObjectName("actionAddLayer")
        self.menuCreateLayer.addAction(self.actionNewShapefileLayer)
        self.menuLayer.addAction(self.menuCreateLayer.menuAction())
        self.menuLayer.addAction(self.actionAddLayer)
        self.menuLayer.addAction(self.actionCopyLayer)
        self.menuLayer.addSeparator()
        self.menuLayer.addAction(self.actionEnableEditing)
        self.menuSettings.addAction(self.actionOptions)
        self.menuHelp.addAction(self.actionAbout)
        self.menuView.addAction(self.actionShowToolBar)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionPasteAs)
        self.menuEdit.addSeparator()
        self.menuProject.addAction(self.actionProjectNew)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionProjectOpen)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionProjectSave)
        self.menuProject.addAction(self.actionProjectSaveAs)
        self.menuProject.addAction(self.actionSaveImage)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionExit)
        self.menuBar.addAction(self.menuProject.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuLayer.menuAction())
        self.menuBar.addAction(self.menuVector.menuAction())
        self.menuBar.addAction(self.menuRaster.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAddLayer)

        self.retranslateUi(MainWindow)
        self.actionProjectNew.triggered.connect(MainWindow.new_project)
        self.actionProjectOpen.triggered.connect(MainWindow.open_project)
        self.actionProjectSave.triggered.connect(MainWindow.save_project)
        self.actionProjectSaveAs.triggered.connect(MainWindow.save_project_as)
        self.actionExit.triggered.connect(MainWindow.exit_app)
        self.actionAbout.triggered.connect(MainWindow.show_about_page)
        self.actionAddLayer.triggered.connect(MainWindow.add_layer)
        self.actionOptions.triggered.connect(MainWindow.show_options_page)
        self.actionShowToolBar.toggled['bool'].connect(self.toolBar.setVisible)
        self.actionEnableEditing.toggled['bool'].connect(MainWindow.switch_editing)
        self.actionCopyLayer.triggered.connect(MainWindow.copy_layer)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "πGIS"))
        self.menuLayer.setTitle(_translate("MainWindow", "Layer"))
        self.menuCreateLayer.setTitle(_translate("MainWindow", "Create Layer"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuVector.setTitle(_translate("MainWindow", "Vector"))
        self.menuRaster.setTitle(_translate("MainWindow", "Raster"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionProjectNew.setText(_translate("MainWindow", "New"))
        self.actionProjectOpen.setText(_translate("MainWindow", "Open"))
        self.actionProjectOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionProjectSave.setText(_translate("MainWindow", "Save"))
        self.actionProjectSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit πGIS"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCut.setText(_translate("MainWindow", "Cut Features"))
        self.actionCopy.setText(_translate("MainWindow", "Copy Features"))
        self.actionPaste.setText(_translate("MainWindow", "Paste Features"))
        self.actionPasteAs.setText(_translate("MainWindow", "Paste As"))
        self.actionCopyLayer.setText(_translate("MainWindow", "Copy Layer"))
        self.actionEnableEditing.setText(_translate("MainWindow", "Enable Editing"))
        self.actionShowToolBar.setText(_translate("MainWindow", "Show Tool Bar"))
        self.actionSaveImage.setText(_translate("MainWindow", "Save Map As Image"))
        self.actionProjectSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionProjectSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionNewShapefileLayer.setText(_translate("MainWindow", "New Shapefile Layer"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionAddLayer.setText(_translate("MainWindow", "Add Layer"))