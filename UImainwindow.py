# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dj/School/COMP3000A Fall 2016/project/Comp3000Group5/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.appTableView = QtWidgets.QTableView(self.tab)
        self.appTableView.setAutoScroll(False)
        self.appTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.appTableView.setProperty("showDropIndicator", False)
        self.appTableView.setDragDropOverwriteMode(False)
        self.appTableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.appTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.appTableView.setSortingEnabled(True)
        self.appTableView.setObjectName("appTableView")
        self.appTableView.horizontalHeader().setDefaultSectionSize(120)
        self.appTableView.horizontalHeader().setSortIndicatorShown(False)
        self.appTableView.horizontalHeader().setStretchLastSection(True)
        self.appTableView.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_6.addWidget(self.appTableView, 0, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(528, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 0, 1, 1)
        self.endTaskButton = QtWidgets.QPushButton(self.tab)
        self.endTaskButton.setObjectName("endTaskButton")
        self.gridLayout_6.addWidget(self.endTaskButton, 1, 1, 1, 1)
        self.switchToButton = QtWidgets.QPushButton(self.tab)
        self.switchToButton.setObjectName("switchToButton")
        self.gridLayout_6.addWidget(self.switchToButton, 1, 2, 1, 1)
        self.newTaskButton = QtWidgets.QPushButton(self.tab)
        self.newTaskButton.setObjectName("newTaskButton")
        self.gridLayout_6.addWidget(self.newTaskButton, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tabProcesses = QtWidgets.QWidget()
        self.tabProcesses.setObjectName("tabProcesses")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabProcesses)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableView = QtWidgets.QTableView(self.tabProcesses)
        self.tableView.setAutoScroll(False)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(120)
        self.tableView.horizontalHeader().setSortIndicatorShown(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_5.addWidget(self.tableView, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 1, 0, 1, 1)
        self.endProcessButton = QtWidgets.QPushButton(self.tabProcesses)
        self.endProcessButton.setObjectName("endProcessButton")
        self.gridLayout_5.addWidget(self.endProcessButton, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabProcesses, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_6)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew_Task_Run = QtWidgets.QAction(MainWindow)
        self.actionNew_Task_Run.setObjectName("actionNew_Task_Run")
        self.actionExit_Overseer = QtWidgets.QAction(MainWindow)
        self.actionExit_Overseer.setObjectName("actionExit_Overseer")
        self.actionExit_Overseer_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_Overseer_2.setObjectName("actionExit_Overseer_2")
        self.actionAbout_Overseer = QtWidgets.QAction(MainWindow)
        self.actionAbout_Overseer.setObjectName("actionAbout_Overseer")
        self.actionRefresh_Now = QtWidgets.QAction(MainWindow)
        self.actionRefresh_Now.setObjectName("actionRefresh_Now")
        self.actionUpdate_Speed = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Speed.setObjectName("actionUpdate_Speed")
        self.actionBoot_on_Startup = QtWidgets.QAction(MainWindow)
        self.actionBoot_on_Startup.setObjectName("actionBoot_on_Startup")
        self.actionAlways_ontop = QtWidgets.QAction(MainWindow)
        self.actionAlways_ontop.setObjectName("actionAlways_ontop")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Overseer"))
        self.endTaskButton.setText(_translate("MainWindow", "End Task"))
        self.switchToButton.setText(_translate("MainWindow", "Switch To"))
        self.newTaskButton.setText(_translate("MainWindow", "New Task..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Applications"))
        self.endProcessButton.setText(_translate("MainWindow", "End Process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProcesses), _translate("MainWindow", "Processes"))
        self.label.setText(_translate("MainWindow", "Under Development"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Services"))
        self.label_2.setText(_translate("MainWindow", "Under Development"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Performance"))
        self.label_3.setText(_translate("MainWindow", "Under Development"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Networking"))
        self.label_4.setText(_translate("MainWindow", "Under Development"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Users"))
        self.actionNew_Task_Run.setText(_translate("MainWindow", "New Task (Run...)"))
        self.actionExit_Overseer.setText(_translate("MainWindow", "Exit Overseer"))
        self.actionExit_Overseer_2.setText(_translate("MainWindow", "Exit Overseer"))
        self.actionAbout_Overseer.setText(_translate("MainWindow", "About Overseer"))
        self.actionRefresh_Now.setText(_translate("MainWindow", "Refresh Now"))
        self.actionUpdate_Speed.setText(_translate("MainWindow", "Update Speed"))
        self.actionBoot_on_Startup.setText(_translate("MainWindow", "Boot on Startup"))
        self.actionAlways_ontop.setText(_translate("MainWindow", "Always On Top"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

