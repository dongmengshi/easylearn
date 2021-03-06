# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/My_Codes/easylearn-fmri/eslearn/GUI/easylearn_machine_learning_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.classification = QtWidgets.QWidget()
        self.classification.setObjectName("classification")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.classification)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_method = QtWidgets.QGroupBox(self.classification)
        self.groupBox_method.setObjectName("groupBox_method")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_method)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton_classification_gaussianprocess = QtWidgets.QRadioButton(self.groupBox_method)
        self.radioButton_classification_gaussianprocess.setObjectName("radioButton_classification_gaussianprocess")
        self.gridLayout_5.addWidget(self.radioButton_classification_gaussianprocess, 3, 0, 1, 1)
        self.radioButton_classification_randomforest = QtWidgets.QRadioButton(self.groupBox_method)
        self.radioButton_classification_randomforest.setObjectName("radioButton_classification_randomforest")
        self.gridLayout_5.addWidget(self.radioButton_classification_randomforest, 5, 0, 1, 1)
        self.radioButton_classification_svm = QtWidgets.QRadioButton(self.groupBox_method)
        self.radioButton_classification_svm.setObjectName("radioButton_classification_svm")
        self.gridLayout_5.addWidget(self.radioButton_classification_svm, 1, 0, 1, 1)
        self.radioButton_classificaton_lr = QtWidgets.QRadioButton(self.groupBox_method)
        self.radioButton_classificaton_lr.setObjectName("radioButton_classificaton_lr")
        self.gridLayout_5.addWidget(self.radioButton_classificaton_lr, 0, 0, 1, 1)
        self.radioButton_classification_adaboost = QtWidgets.QRadioButton(self.groupBox_method)
        self.radioButton_classification_adaboost.setObjectName("radioButton_classification_adaboost")
        self.gridLayout_5.addWidget(self.radioButton_classification_adaboost, 8, 0, 1, 1)
        self.radioButton_classification_ridge = QtWidgets.QRadioButton(self.groupBox_method)
        self.radioButton_classification_ridge.setObjectName("radioButton_classification_ridge")
        self.gridLayout_5.addWidget(self.radioButton_classification_ridge, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_method, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox_setting = QtWidgets.QGroupBox(self.classification)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_setting.sizePolicy().hasHeightForWidth())
        self.groupBox_setting.setSizePolicy(sizePolicy)
        self.groupBox_setting.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox_setting.setObjectName("groupBox_setting")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_setting)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget_setting = QtWidgets.QStackedWidget(self.groupBox_setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_setting.sizePolicy().hasHeightForWidth())
        self.stackedWidget_setting.setSizePolicy(sizePolicy)
        self.stackedWidget_setting.setMinimumSize(QtCore.QSize(200, 0))
        self.stackedWidget_setting.setObjectName("stackedWidget_setting")
        self.to_lr = QtWidgets.QWidget()
        self.to_lr.setObjectName("to_lr")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.to_lr)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_7 = QtWidgets.QLabel(self.to_lr)
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 2, 0, 1, 1)
        self.spinBox__clf_lr_numl1ratio = QtWidgets.QSpinBox(self.to_lr)
        self.spinBox__clf_lr_numl1ratio.setObjectName("spinBox__clf_lr_numl1ratio")
        self.gridLayout_11.addWidget(self.spinBox__clf_lr_numl1ratio, 2, 1, 1, 1)
        self.doubleSpinBox_clf_lr_maxl1ratio = QtWidgets.QDoubleSpinBox(self.to_lr)
        self.doubleSpinBox_clf_lr_maxl1ratio.setMaximum(1.0)
        self.doubleSpinBox_clf_lr_maxl1ratio.setSingleStep(0.1)
        self.doubleSpinBox_clf_lr_maxl1ratio.setProperty("value", 1.0)
        self.doubleSpinBox_clf_lr_maxl1ratio.setObjectName("doubleSpinBox_clf_lr_maxl1ratio")
        self.gridLayout_11.addWidget(self.doubleSpinBox_clf_lr_maxl1ratio, 0, 1, 1, 1)
        self.doubleSpinBox_clf_lr_minl1ratio = QtWidgets.QDoubleSpinBox(self.to_lr)
        self.doubleSpinBox_clf_lr_minl1ratio.setMaximum(1.0)
        self.doubleSpinBox_clf_lr_minl1ratio.setSingleStep(0.1)
        self.doubleSpinBox_clf_lr_minl1ratio.setObjectName("doubleSpinBox_clf_lr_minl1ratio")
        self.gridLayout_11.addWidget(self.doubleSpinBox_clf_lr_minl1ratio, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.to_lr)
        self.label_5.setObjectName("label_5")
        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.to_lr)
        self.label_2.setObjectName("label_2")
        self.gridLayout_11.addWidget(self.label_2, 1, 0, 1, 1)
        self.stackedWidget_setting.addWidget(self.to_lr)
        self.to_svm = QtWidgets.QWidget()
        self.to_svm.setObjectName("to_svm")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.to_svm)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.comboBox_clf_svm_kernel = QtWidgets.QComboBox(self.to_svm)
        self.comboBox_clf_svm_kernel.setObjectName("comboBox_clf_svm_kernel")
        self.comboBox_clf_svm_kernel.addItem("")
        self.comboBox_clf_svm_kernel.addItem("")
        self.comboBox_clf_svm_kernel.addItem("")
        self.comboBox_clf_svm_kernel.addItem("")
        self.gridLayout_10.addWidget(self.comboBox_clf_svm_kernel, 0, 1, 1, 2)
        self.doubleSpinBox_clf_svm_maxc = QtWidgets.QDoubleSpinBox(self.to_svm)
        self.doubleSpinBox_clf_svm_maxc.setMaximum(1000000.0)
        self.doubleSpinBox_clf_svm_maxc.setSingleStep(0.1)
        self.doubleSpinBox_clf_svm_maxc.setProperty("value", 1.0)
        self.doubleSpinBox_clf_svm_maxc.setObjectName("doubleSpinBox_clf_svm_maxc")
        self.gridLayout_10.addWidget(self.doubleSpinBox_clf_svm_maxc, 1, 2, 1, 1)
        self.label_clf_svm_kernel = QtWidgets.QLabel(self.to_svm)
        self.label_clf_svm_kernel.setObjectName("label_clf_svm_kernel")
        self.gridLayout_10.addWidget(self.label_clf_svm_kernel, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.to_svm)
        self.label_6.setObjectName("label_6")
        self.gridLayout_10.addWidget(self.label_6, 1, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.to_svm)
        self.label_4.setObjectName("label_4")
        self.gridLayout_10.addWidget(self.label_4, 2, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.to_svm)
        self.label_10.setObjectName("label_10")
        self.gridLayout_10.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.to_svm)
        self.label_9.setObjectName("label_9")
        self.gridLayout_10.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.to_svm)
        self.label_8.setObjectName("label_8")
        self.gridLayout_10.addWidget(self.label_8, 6, 0, 1, 1)
        self.doubleSpinBox_clf_svm_minc = QtWidgets.QDoubleSpinBox(self.to_svm)
        self.doubleSpinBox_clf_svm_minc.setMinimum(0.0)
        self.doubleSpinBox_clf_svm_minc.setMaximum(100000.0)
        self.doubleSpinBox_clf_svm_minc.setSingleStep(0.1)
        self.doubleSpinBox_clf_svm_minc.setProperty("value", 1.0)
        self.doubleSpinBox_clf_svm_minc.setObjectName("doubleSpinBox_clf_svm_minc")
        self.gridLayout_10.addWidget(self.doubleSpinBox_clf_svm_minc, 2, 2, 1, 1)
        self.spinBox_clf_svm_numgamma = QtWidgets.QSpinBox(self.to_svm)
        self.spinBox_clf_svm_numgamma.setObjectName("spinBox_clf_svm_numgamma")
        self.gridLayout_10.addWidget(self.spinBox_clf_svm_numgamma, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.to_svm)
        self.label.setObjectName("label")
        self.gridLayout_10.addWidget(self.label, 3, 0, 1, 1)
        self.spinBox_clf_svm_numc = QtWidgets.QSpinBox(self.to_svm)
        self.spinBox_clf_svm_numc.setObjectName("spinBox_clf_svm_numc")
        self.gridLayout_10.addWidget(self.spinBox_clf_svm_numc, 3, 2, 1, 1)
        self.lineEdit_clf_svm_maxgamma = QtWidgets.QLineEdit(self.to_svm)
        self.lineEdit_clf_svm_maxgamma.setObjectName("lineEdit_clf_svm_maxgamma")
        self.gridLayout_10.addWidget(self.lineEdit_clf_svm_maxgamma, 4, 2, 1, 1)
        self.lineEdit_clf_svm_mingamma = QtWidgets.QLineEdit(self.to_svm)
        self.lineEdit_clf_svm_mingamma.setObjectName("lineEdit_clf_svm_mingamma")
        self.gridLayout_10.addWidget(self.lineEdit_clf_svm_mingamma, 5, 2, 1, 1)
        self.stackedWidget_setting.addWidget(self.to_svm)
        self.to_ridgeclf = QtWidgets.QWidget()
        self.to_ridgeclf.setObjectName("to_ridgeclf")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.to_ridgeclf)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_21 = QtWidgets.QLabel(self.to_ridgeclf)
        self.label_21.setObjectName("label_21")
        self.gridLayout_14.addWidget(self.label_21, 0, 0, 1, 1)
        self.doubleSpinBox_clf_ridgeclf_maxalpha = QtWidgets.QDoubleSpinBox(self.to_ridgeclf)
        self.doubleSpinBox_clf_ridgeclf_maxalpha.setMaximum(1000000.0)
        self.doubleSpinBox_clf_ridgeclf_maxalpha.setSingleStep(0.1)
        self.doubleSpinBox_clf_ridgeclf_maxalpha.setProperty("value", 1.0)
        self.doubleSpinBox_clf_ridgeclf_maxalpha.setObjectName("doubleSpinBox_clf_ridgeclf_maxalpha")
        self.gridLayout_14.addWidget(self.doubleSpinBox_clf_ridgeclf_maxalpha, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.to_ridgeclf)
        self.label_20.setObjectName("label_20")
        self.gridLayout_14.addWidget(self.label_20, 1, 0, 1, 1)
        self.doubleSpinBox_clf_ridgeclf_minalpha = QtWidgets.QDoubleSpinBox(self.to_ridgeclf)
        self.doubleSpinBox_clf_ridgeclf_minalpha.setMinimum(0.0)
        self.doubleSpinBox_clf_ridgeclf_minalpha.setMaximum(100000.0)
        self.doubleSpinBox_clf_ridgeclf_minalpha.setSingleStep(0.1)
        self.doubleSpinBox_clf_ridgeclf_minalpha.setProperty("value", 1.0)
        self.doubleSpinBox_clf_ridgeclf_minalpha.setObjectName("doubleSpinBox_clf_ridgeclf_minalpha")
        self.gridLayout_14.addWidget(self.doubleSpinBox_clf_ridgeclf_minalpha, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.to_ridgeclf)
        self.label_19.setObjectName("label_19")
        self.gridLayout_14.addWidget(self.label_19, 2, 0, 1, 1)
        self.spinBox_clf_ridgeclf_numalpha = QtWidgets.QSpinBox(self.to_ridgeclf)
        self.spinBox_clf_ridgeclf_numalpha.setObjectName("spinBox_clf_ridgeclf_numalpha")
        self.gridLayout_14.addWidget(self.spinBox_clf_ridgeclf_numalpha, 2, 1, 1, 1)
        self.stackedWidget_setting.addWidget(self.to_ridgeclf)
        self.to_guassianprocess = QtWidgets.QWidget()
        self.to_guassianprocess.setObjectName("to_guassianprocess")
        self.stackedWidget_setting.addWidget(self.to_guassianprocess)
        self.to_randomforest = QtWidgets.QWidget()
        self.to_randomforest.setObjectName("to_randomforest")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.to_randomforest)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_22 = QtWidgets.QLabel(self.to_randomforest)
        self.label_22.setObjectName("label_22")
        self.gridLayout_15.addWidget(self.label_22, 2, 0, 1, 1)
        self.spinBox_clf_randomforest_maxdepth = QtWidgets.QSpinBox(self.to_randomforest)
        self.spinBox_clf_randomforest_maxdepth.setMaximum(10000)
        self.spinBox_clf_randomforest_maxdepth.setProperty("value", 10)
        self.spinBox_clf_randomforest_maxdepth.setObjectName("spinBox_clf_randomforest_maxdepth")
        self.gridLayout_15.addWidget(self.spinBox_clf_randomforest_maxdepth, 5, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.to_randomforest)
        self.label_23.setObjectName("label_23")
        self.gridLayout_15.addWidget(self.label_23, 1, 0, 1, 1)
        self.spinBox_clf_randomforest_minestimators = QtWidgets.QSpinBox(self.to_randomforest)
        self.spinBox_clf_randomforest_minestimators.setProperty("value", 10)
        self.spinBox_clf_randomforest_minestimators.setObjectName("spinBox_clf_randomforest_minestimators")
        self.gridLayout_15.addWidget(self.spinBox_clf_randomforest_minestimators, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.to_randomforest)
        self.label_24.setObjectName("label_24")
        self.gridLayout_15.addWidget(self.label_24, 3, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.to_randomforest)
        self.label_26.setObjectName("label_26")
        self.gridLayout_15.addWidget(self.label_26, 5, 0, 1, 1)
        self.comboBox_clf_randomforest_criterion = QtWidgets.QComboBox(self.to_randomforest)
        self.comboBox_clf_randomforest_criterion.setObjectName("comboBox_clf_randomforest_criterion")
        self.comboBox_clf_randomforest_criterion.addItem("")
        self.comboBox_clf_randomforest_criterion.addItem("")
        self.gridLayout_15.addWidget(self.comboBox_clf_randomforest_criterion, 1, 1, 1, 1)
        self.spinBox_clf_randomforest_maxestimators = QtWidgets.QSpinBox(self.to_randomforest)
        self.spinBox_clf_randomforest_maxestimators.setProperty("value", 10)
        self.spinBox_clf_randomforest_maxestimators.setObjectName("spinBox_clf_randomforest_maxestimators")
        self.gridLayout_15.addWidget(self.spinBox_clf_randomforest_maxestimators, 2, 1, 1, 1)
        self.stackedWidget_setting.addWidget(self.to_randomforest)
        self.to_adaboost = QtWidgets.QWidget()
        self.to_adaboost.setObjectName("to_adaboost")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.to_adaboost)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.comboBox_clf_adaboost_baseesitmator = QtWidgets.QComboBox(self.to_adaboost)
        self.comboBox_clf_adaboost_baseesitmator.setObjectName("comboBox_clf_adaboost_baseesitmator")
        self.comboBox_clf_adaboost_baseesitmator.addItem("")
        self.gridLayout_16.addWidget(self.comboBox_clf_adaboost_baseesitmator, 1, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.to_adaboost)
        self.label_31.setObjectName("label_31")
        self.gridLayout_16.addWidget(self.label_31, 1, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.to_adaboost)
        self.label_29.setObjectName("label_29")
        self.gridLayout_16.addWidget(self.label_29, 3, 0, 1, 1)
        self.spinBox_clf_adaboost_maxestimators = QtWidgets.QSpinBox(self.to_adaboost)
        self.spinBox_clf_adaboost_maxestimators.setProperty("value", 2)
        self.spinBox_clf_adaboost_maxestimators.setObjectName("spinBox_clf_adaboost_maxestimators")
        self.gridLayout_16.addWidget(self.spinBox_clf_adaboost_maxestimators, 2, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.to_adaboost)
        self.label_27.setObjectName("label_27")
        self.gridLayout_16.addWidget(self.label_27, 2, 0, 1, 1)
        self.spinBox_clf_adaboost_minestimators = QtWidgets.QSpinBox(self.to_adaboost)
        self.spinBox_clf_adaboost_minestimators.setProperty("value", 2)
        self.spinBox_clf_adaboost_minestimators.setObjectName("spinBox_clf_adaboost_minestimators")
        self.gridLayout_16.addWidget(self.spinBox_clf_adaboost_minestimators, 3, 1, 1, 1)
        self.stackedWidget_setting.addWidget(self.to_adaboost)
        self.gridLayout.addWidget(self.stackedWidget_setting, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_setting, 0, 2, 1, 1)
        self.tabWidget.addTab(self.classification, "")
        self.regression = QtWidgets.QWidget()
        self.regression.setObjectName("regression")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.regression)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.regression)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2.addWidget(self.groupBox_5, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.regression)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout_6.addWidget(self.radioButton_7, 0, 0, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_6.addWidget(self.radioButton_6, 3, 0, 1, 1)
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_10.setObjectName("radioButton_10")
        self.gridLayout_6.addWidget(self.radioButton_10, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.regression, "")
        self.clustering = QtWidgets.QWidget()
        self.clustering.setObjectName("clustering")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.clustering)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.clustering)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3.addWidget(self.groupBox_6, 0, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.clustering)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.tabWidget.addTab(self.clustering, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.radioButton_16 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_16.setObjectName("radioButton_16")
        self.gridLayout_8.addWidget(self.radioButton_16, 4, 0, 1, 1)
        self.radioButton_17 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_17.setObjectName("radioButton_17")
        self.gridLayout_8.addWidget(self.radioButton_17, 1, 0, 1, 1)
        self.radioButton_18 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_18.setObjectName("radioButton_18")
        self.gridLayout_8.addWidget(self.radioButton_18, 0, 0, 1, 1)
        self.radioButton_19 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_19.setObjectName("radioButton_19")
        self.gridLayout_8.addWidget(self.radioButton_19, 5, 0, 1, 1)
        self.radioButton_20 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_20.setObjectName("radioButton_20")
        self.gridLayout_8.addWidget(self.radioButton_20, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_4.addWidget(self.groupBox_8, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_17.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuConfiguration_file_F = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration_file_F.setObjectName("menuConfiguration_file_F")
        self.menuHelp_H = QtWidgets.QMenu(self.menubar)
        self.menuHelp_H.setObjectName("menuHelp_H")
        self.menuSkin = QtWidgets.QMenu(self.menubar)
        self.menuSkin.setObjectName("menuSkin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_configuration = QtWidgets.QAction(MainWindow)
        self.actionLoad_configuration.setObjectName("actionLoad_configuration")
        self.actionSave_configuration = QtWidgets.QAction(MainWindow)
        self.actionSave_configuration.setObjectName("actionSave_configuration")
        self.actionWeb = QtWidgets.QAction(MainWindow)
        self.actionWeb.setObjectName("actionWeb")
        self.actionPDF = QtWidgets.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")
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
        self.menuConfiguration_file_F.addAction(self.actionLoad_configuration)
        self.menuConfiguration_file_F.addAction(self.actionSave_configuration)
        self.menuHelp_H.addAction(self.actionWeb)
        self.menuHelp_H.addAction(self.actionPDF)
        self.menuSkin.addAction(self.actionDark)
        self.menuSkin.addAction(self.actionBlack)
        self.menuSkin.addAction(self.actionDarkOrange)
        self.menuSkin.addAction(self.actionGray)
        self.menuSkin.addAction(self.actionBlue)
        self.menuSkin.addAction(self.actionNavy)
        self.menuSkin.addAction(self.actionClassic)
        self.menubar.addAction(self.menuConfiguration_file_F.menuAction())
        self.menubar.addAction(self.menuHelp_H.menuAction())
        self.menubar.addAction(self.menuSkin.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_setting.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_method.setTitle(_translate("MainWindow", "Methods"))
        self.radioButton_classification_gaussianprocess.setText(_translate("MainWindow", "Gaussian process"))
        self.radioButton_classification_randomforest.setText(_translate("MainWindow", "Random forest"))
        self.radioButton_classification_svm.setText(_translate("MainWindow", "Support vector machine"))
        self.radioButton_classificaton_lr.setText(_translate("MainWindow", "Logistic regression"))
        self.radioButton_classification_adaboost.setText(_translate("MainWindow", "AdaBoost"))
        self.radioButton_classification_ridge.setText(_translate("MainWindow", "Ridge classification"))
        self.groupBox_setting.setTitle(_translate("MainWindow", "Setting"))
        self.label_7.setText(_translate("MainWindow", "Number"))
        self.label_5.setText(_translate("MainWindow", "Max_l1_ratio"))
        self.label_2.setText(_translate("MainWindow", "Min_l1_ratio"))
        self.comboBox_clf_svm_kernel.setItemText(0, _translate("MainWindow", "linear"))
        self.comboBox_clf_svm_kernel.setItemText(1, _translate("MainWindow", "poly"))
        self.comboBox_clf_svm_kernel.setItemText(2, _translate("MainWindow", "rbf"))
        self.comboBox_clf_svm_kernel.setItemText(3, _translate("MainWindow", "sigmoid"))
        self.label_clf_svm_kernel.setText(_translate("MainWindow", "Kernel"))
        self.label_6.setText(_translate("MainWindow", "Max_C"))
        self.label_4.setText(_translate("MainWindow", "Min_C"))
        self.label_10.setText(_translate("MainWindow", "Max_gamma"))
        self.label_9.setText(_translate("MainWindow", "Min_gamma"))
        self.label_8.setText(_translate("MainWindow", "Number_gamma"))
        self.label.setText(_translate("MainWindow", "Numer_C"))
        self.label_21.setText(_translate("MainWindow", "Max_alpha"))
        self.label_20.setText(_translate("MainWindow", "Min_alpha"))
        self.label_19.setText(_translate("MainWindow", "Numer"))
        self.label_22.setText(_translate("MainWindow", "Max_estimators"))
        self.label_23.setText(_translate("MainWindow", "Criterion"))
        self.label_24.setText(_translate("MainWindow", "Min_estimators"))
        self.label_26.setText(_translate("MainWindow", "Max_depth"))
        self.comboBox_clf_randomforest_criterion.setItemText(0, _translate("MainWindow", "gini"))
        self.comboBox_clf_randomforest_criterion.setItemText(1, _translate("MainWindow", "entropy"))
        self.comboBox_clf_adaboost_baseesitmator.setItemText(0, _translate("MainWindow", "DecisionTreeClassifier(max_depth=1)"))
        self.label_31.setText(_translate("MainWindow", "Base_estimator"))
        self.label_29.setText(_translate("MainWindow", "Min_estimators"))
        self.label_27.setText(_translate("MainWindow", "Max_estimators"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.classification), _translate("MainWindow", "Classification"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Setting"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Methods"))
        self.radioButton_7.setText(_translate("MainWindow", "Support vector machines"))
        self.radioButton_6.setText(_translate("MainWindow", "Random forest"))
        self.radioButton_10.setText(_translate("MainWindow", "Gaussian process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.regression), _translate("MainWindow", "Regression"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Setting"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Methods"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clustering), _translate("MainWindow", "Clustering"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Methods"))
        self.radioButton_16.setText(_translate("MainWindow", "Random forest classification"))
        self.radioButton_17.setText(_translate("MainWindow", "Support vector machines"))
        self.radioButton_18.setText(_translate("MainWindow", "Logistic regressio"))
        self.radioButton_19.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_20.setText(_translate("MainWindow", "Gaussian process classification"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Setting"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Deep learning"))
        self.menuConfiguration_file_F.setTitle(_translate("MainWindow", "Configuration file(&F)"))
        self.menuHelp_H.setTitle(_translate("MainWindow", "Help(&H)"))
        self.menuSkin.setTitle(_translate("MainWindow", "Skin"))
        self.actionLoad_configuration.setText(_translate("MainWindow", "Load configuration"))
        self.actionSave_configuration.setText(_translate("MainWindow", "Save configuration"))
        self.actionWeb.setText(_translate("MainWindow", "Web"))
        self.actionPDF.setText(_translate("MainWindow", "PDF"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionDarkOrange.setText(_translate("MainWindow", "DarkOrange"))
        self.actionGray.setText(_translate("MainWindow", "Gray"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionNavy.setText(_translate("MainWindow", "Navy"))
        self.actionClassic.setText(_translate("MainWindow", "Classic"))

