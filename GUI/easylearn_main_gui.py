# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\My_Codes\easylearn-fmri\eslearn\GUI\easylearn_main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 703)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(100000, 100000))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 20))
        self.textBrowser.setMaximumSize(QtCore.QSize(10000000, 100))
        self.textBrowser.setMidLineWidth(30)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 7, 0, 1, 1)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMinimumSize(QtCore.QSize(0, 100))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)
        self.model_evaluation = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_evaluation.sizePolicy().hasHeightForWidth())
        self.model_evaluation.setSizePolicy(sizePolicy)
        self.model_evaluation.setObjectName("model_evaluation")
        self.gridLayout.addWidget(self.model_evaluation, 4, 0, 1, 1)
        self.data_loading = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_loading.sizePolicy().hasHeightForWidth())
        self.data_loading.setSizePolicy(sizePolicy)
        self.data_loading.setStyleSheet("")
        self.data_loading.setIconSize(QtCore.QSize(30, 30))
        self.data_loading.setObjectName("data_loading")
        self.gridLayout.addWidget(self.data_loading, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 9, 0, 1, 1)
        self.feature_engineering = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_engineering.sizePolicy().hasHeightForWidth())
        self.feature_engineering.setSizePolicy(sizePolicy)
        self.feature_engineering.setIconSize(QtCore.QSize(30, 30))
        self.feature_engineering.setObjectName("feature_engineering")
        self.gridLayout.addWidget(self.feature_engineering, 2, 0, 1, 1)
        self.save_load = QtWidgets.QHBoxLayout()
        self.save_load.setObjectName("save_load")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit.sizePolicy().hasHeightForWidth())
        self.quit.setSizePolicy(sizePolicy)
        self.quit.setObjectName("quit")
        self.save_load.addWidget(self.quit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.save_load.addItem(spacerItem)
        self.run = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run.sizePolicy().hasHeightForWidth())
        self.run.setSizePolicy(sizePolicy)
        self.run.setIconSize(QtCore.QSize(30, 30))
        self.run.setObjectName("run")
        self.save_load.addWidget(self.run)
        self.gridLayout.addLayout(self.save_load, 8, 0, 1, 1)
        self.machine_learning = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_learning.sizePolicy().hasHeightForWidth())
        self.machine_learning.setSizePolicy(sizePolicy)
        self.machine_learning.setIconSize(QtCore.QSize(30, 30))
        self.machine_learning.setObjectName("machine_learning")
        self.gridLayout.addWidget(self.machine_learning, 3, 0, 1, 1)
        self.statistical_analysis = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statistical_analysis.sizePolicy().hasHeightForWidth())
        self.statistical_analysis.setSizePolicy(sizePolicy)
        self.statistical_analysis.setIconSize(QtCore.QSize(30, 30))
        self.statistical_analysis.setObjectName("statistical_analysis")
        self.gridLayout.addWidget(self.statistical_analysis, 5, 0, 1, 1)
        self.Visualization = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Visualization.sizePolicy().hasHeightForWidth())
        self.Visualization.setSizePolicy(sizePolicy)
        self.Visualization.setObjectName("Visualization")
        self.gridLayout.addWidget(self.Visualization, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 26))
        self.menubar.setObjectName("menubar")
        self.menueasylearn = QtWidgets.QMenu(self.menubar)
        self.menueasylearn.setObjectName("menueasylearn")
        self.menuHelp_H = QtWidgets.QMenu(self.menubar)
        self.menuHelp_H.setObjectName("menuHelp_H")
        self.menuSkin = QtWidgets.QMenu(self.menubar)
        self.menuSkin.setObjectName("menuSkin")
        MainWindow.setMenuBar(self.menubar)
        self.current_working_directory = QtWidgets.QAction(MainWindow)
        self.current_working_directory.setObjectName("current_working_directory")
        self.select_working_directory = QtWidgets.QAction(MainWindow)
        self.select_working_directory.setObjectName("select_working_directory")
        self.create_configuration_file = QtWidgets.QAction(MainWindow)
        self.create_configuration_file.setObjectName("create_configuration_file")
        self.choose_configuration_file = QtWidgets.QAction(MainWindow)
        self.choose_configuration_file.setObjectName("choose_configuration_file")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionBlack = QtWidgets.QAction(MainWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actionDarkOrange = QtWidgets.QAction(MainWindow)
        self.actionDarkOrange.setObjectName("actionDarkOrange")
        self.actionGray = QtWidgets.QAction(MainWindow)
        self.actionGray.setObjectName("actionGray")
        self.actionBlue = QtWidgets.QAction(MainWindow)
        self.actionBlue.setObjectName("actionBlue")
        self.actionNavy = QtWidgets.QAction(MainWindow)
        self.actionNavy.setObjectName("actionNavy")
        self.actionClassic = QtWidgets.QAction(MainWindow)
        self.actionClassic.setObjectName("actionClassic")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.menueasylearn.addSeparator()
        self.menueasylearn.addAction(self.select_working_directory)
        self.menueasylearn.addAction(self.create_configuration_file)
        self.menueasylearn.addAction(self.choose_configuration_file)
        self.menuSkin.addAction(self.actionDark)
        self.menuSkin.addAction(self.actionBlack)
        self.menuSkin.addAction(self.actionDarkOrange)
        self.menuSkin.addAction(self.actionGray)
        self.menuSkin.addAction(self.actionBlue)
        self.menuSkin.addAction(self.actionNavy)
        self.menuSkin.addAction(self.actionClassic)
        self.menuSkin.addAction(self.actionLight)
        self.menubar.addAction(self.menueasylearn.menuAction())
        self.menubar.addAction(self.menuHelp_H.menuAction())
        self.menubar.addAction(self.menuSkin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.model_evaluation.setText(_translate("MainWindow", "Model Evaluation"))
        self.data_loading.setText(_translate("MainWindow", "Data Loading"))
        self.feature_engineering.setText(_translate("MainWindow", "Feature Engineering"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.machine_learning.setText(_translate("MainWindow", "Machine Learning"))
        self.statistical_analysis.setText(_translate("MainWindow", "Statistical Analysis"))
        self.Visualization.setText(_translate("MainWindow", "Visualization"))
        self.menueasylearn.setTitle(_translate("MainWindow", "Project initialization(&I)"))
        self.menuHelp_H.setTitle(_translate("MainWindow", "Help(&H)"))
        self.menuSkin.setTitle(_translate("MainWindow", "Skin"))
        self.current_working_directory.setText(_translate("MainWindow", "Current working directory"))
        self.select_working_directory.setText(_translate("MainWindow", "Select working directory"))
        self.create_configuration_file.setText(_translate("MainWindow", "Create configuration file"))
        self.choose_configuration_file.setText(_translate("MainWindow", "Load configuration file"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionDarkOrange.setText(_translate("MainWindow", "DarkOrange"))
        self.actionGray.setText(_translate("MainWindow", "Gray"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionNavy.setText(_translate("MainWindow", "Navy"))
        self.actionClassic.setText(_translate("MainWindow", "Classic"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
