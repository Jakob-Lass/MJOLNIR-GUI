# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 950)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 340))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 781, 822))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fixedOpen = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixedOpen.sizePolicy().hasHeightForWidth())
        self.fixedOpen.setSizePolicy(sizePolicy)
        self.fixedOpen.setMinimumSize(QtCore.QSize(0, 300))
        self.fixedOpen.setObjectName("fixedOpen")
        self.verticalLayout.addWidget(self.fixedOpen)
        self.collapsibleContainer = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collapsibleContainer.sizePolicy().hasHeightForWidth())
        self.collapsibleContainer.setSizePolicy(sizePolicy)
        self.collapsibleContainer.setStyleSheet("")
        self.collapsibleContainer.setObjectName("collapsibleContainer")
        self.verticalLayout.addWidget(self.collapsibleContainer)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 6, 10, -1)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 45))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.log_reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_reset_btn.setObjectName("log_reset_btn")
        self.horizontalLayout.addWidget(self.log_reset_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_GUI_state = QtWidgets.QAction(MainWindow)
        self.actionSave_GUI_state.setObjectName("actionSave_GUI_state")
        self.actionLoad_GUI_state = QtWidgets.QAction(MainWindow)
        self.actionLoad_GUI_state.setObjectName("actionLoad_GUI_state")
        self.actionGenerate_View3d_script = QtWidgets.QAction(MainWindow)
        self.actionGenerate_View3d_script.setObjectName("actionGenerate_View3d_script")
        self.actionGenerate_QELine_script = QtWidgets.QAction(MainWindow)
        self.actionGenerate_QELine_script.setObjectName("actionGenerate_QELine_script")
        self.actionGenerate_QPlane_script = QtWidgets.QAction(MainWindow)
        self.actionGenerate_QPlane_script.setObjectName("actionGenerate_QPlane_script")
        self.actionGenerate_1d_script = QtWidgets.QAction(MainWindow)
        self.actionGenerate_1d_script.setObjectName("actionGenerate_1d_script")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_mask_gui = QtWidgets.QAction(MainWindow)
        self.actionOpen_mask_gui.setObjectName("actionOpen_mask_gui")
        self.actionLoad_mask = QtWidgets.QAction(MainWindow)
        self.actionLoad_mask.setObjectName("actionLoad_mask")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionChange_Theme = QtWidgets.QAction(MainWindow)
        self.actionChange_Theme.setObjectName("actionChange_Theme")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionClose_Windows = QtWidgets.QAction(MainWindow)
        self.actionClose_Windows.setObjectName("actionClose_Windows")
        self.actionPrediction_Tool = QtWidgets.QAction(MainWindow)
        self.actionPrediction_Tool.setObjectName("actionPrediction_Tool")
        self.actionTime_Estimate_Tool = QtWidgets.QAction(MainWindow)
        self.actionTime_Estimate_Tool.setObjectName("actionTime_Estimate_Tool")
        self.actionCalculate_Molecular_Weight = QtWidgets.QAction(MainWindow)
        self.actionCalculate_Molecular_Weight.setObjectName("actionCalculate_Molecular_Weight")
        self.actionNeutron_Calculations = QtWidgets.QAction(MainWindow)
        self.actionNeutron_Calculations.setObjectName("actionNeutron_Calculations")
        self.actionGenerate_Normalization = QtWidgets.QAction(MainWindow)
        self.actionGenerate_Normalization.setObjectName("actionGenerate_Normalization")
        self.actionElectronic_Logbook = QtWidgets.QAction(MainWindow)
        self.actionElectronic_Logbook.setObjectName("actionElectronic_Logbook")
        self.actionSubtraction_Of_DataSets = QtWidgets.QAction(MainWindow)
        self.actionSubtraction_Of_DataSets.setObjectName("actionSubtraction_Of_DataSets")
        self.actionSubtraction = QtWidgets.QAction(MainWindow)
        self.actionSubtraction.setObjectName("actionSubtraction")
        self.actionCheck_Update = QtWidgets.QAction(MainWindow)
        self.actionCheck_Update.setObjectName("actionCheck_Update")
        self.action_masking_gui = QtWidgets.QAction(MainWindow)
        self.action_masking_gui.setObjectName("action_masking_gui")
        self.menuFile.addAction(self.actionSave_GUI_state)
        self.menuFile.addAction(self.actionLoad_GUI_state)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionGenerate_View3d_script)
        self.menuFile.addAction(self.actionGenerate_QELine_script)
        self.menuFile.addAction(self.actionGenerate_QPlane_script)
        self.menuFile.addAction(self.actionGenerate_1d_script)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Windows)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionSubtraction)
        self.menuTools.addAction(self.action_masking_gui)
        self.menuTools.addAction(self.actionPrediction_Tool)
        self.menuTools.addAction(self.actionTime_Estimate_Tool)
        self.menuTools.addAction(self.actionCalculate_Molecular_Weight)
        self.menuTools.addAction(self.actionNeutron_Calculations)
        self.menuTools.addAction(self.actionGenerate_Normalization)
        self.menuTools.addAction(self.actionElectronic_Logbook)
        self.menuTools.addAction(self.actionSubtraction_Of_DataSets)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MJOLNIRGui"))
        self.fixedOpen.setToolTip(_translate("MainWindow", "Manage datasets and their datafiles"))
        self.progressBar.setToolTip(_translate("MainWindow", "Current progress of action"))
        self.progressBar.setStatusTip(_translate("MainWindow", "Current progress of action"))
        self.textBrowser.setToolTip(_translate("MainWindow", "Log of messages from the gui"))
        self.textBrowser.setStatusTip(_translate("MainWindow", "Log of messages from the gui"))
        self.log_reset_btn.setToolTip(_translate("MainWindow", "Clear log"))
        self.log_reset_btn.setStatusTip(_translate("MainWindow", "Clear log"))
        self.log_reset_btn.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionSave_GUI_state.setText(_translate("MainWindow", "Save GUI state"))
        self.actionLoad_GUI_state.setText(_translate("MainWindow", "Load GUI state"))
        self.actionGenerate_View3d_script.setText(_translate("MainWindow", "Generate View3D script"))
        self.actionGenerate_QELine_script.setText(_translate("MainWindow", "Generate QE Cut script"))
        self.actionGenerate_QPlane_script.setText(_translate("MainWindow", "Generate QPlane script"))
        self.actionGenerate_1d_script.setText(_translate("MainWindow", "Generate 1D script"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_mask_gui.setText(_translate("MainWindow", "Open Mask GUI"))
        self.actionLoad_mask.setText(_translate("MainWindow", "Load Mask"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionChange_Theme.setText(_translate("MainWindow", "Change Theme"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionClose_Windows.setText(_translate("MainWindow", "Close Windows"))
        self.actionPrediction_Tool.setText(_translate("MainWindow", "Prediction Tool"))
        self.actionTime_Estimate_Tool.setText(_translate("MainWindow", "Time Estimate"))
        self.actionCalculate_Molecular_Weight.setText(_translate("MainWindow", "Calculate Molecular Weight"))
        self.actionNeutron_Calculations.setText(_translate("MainWindow", "Neutron Calculations"))
        self.actionGenerate_Normalization.setText(_translate("MainWindow", "Generate Normalization"))
        self.actionElectronic_Logbook.setText(_translate("MainWindow", "Electronic Logbook"))
        self.actionSubtraction_Of_DataSets.setText(_translate("MainWindow", "Subtraction of DataSets"))
        self.actionSubtraction.setText(_translate("MainWindow", "Subtraction"))
        self.actionCheck_Update.setText(_translate("MainWindow", "Check Update"))
        self.action_masking_gui.setText(_translate("MainWindow", "Masking Gui"))
