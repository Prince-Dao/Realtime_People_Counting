# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'countwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 1004)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.drop_shadow = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow.setStyleSheet("background-color: rgb(24,78,119);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.drop_shadow.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow.setFrameShadow(QtWidgets.QFrame.Plain)
        self.drop_shadow.setObjectName("drop_shadow")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.drop_shadow)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow)
        self.title_bar.setMinimumSize(QtCore.QSize(0, 50))
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color: none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_6.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_6.addWidget(self.label_title, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_6.addWidget(self.frame_title)
        self.frame_btn = QtWidgets.QFrame(self.title_bar)
        self.frame_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btn.setStyleSheet("color: rgb(0, 0, 0)")
        self.frame_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn.setObjectName("frame_btn")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_btn)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btn)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: rgb(85, 255, 127);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(85, 255, 127, 150)\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_7.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btn)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: rgb(255, 170, 0);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 170, 0, 150)\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_7.addWidget(self.btn_maximize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btn)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_close.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 0, 0, 150)\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_7.addWidget(self.btn_close)
        self.horizontalLayout_6.addWidget(self.frame_btn)
        self.verticalLayout_2.addWidget(self.title_bar)
        self.stackedWidget = QtWidgets.QStackedWidget(self.drop_shadow)
        self.stackedWidget.setStyleSheet("background-color: none;")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 178, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(386, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_description = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_description.setStyleSheet("color: rgb(26, 117, 159);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.verticalLayout_4.addWidget(self.label_description, 0, QtCore.Qt.AlignHCenter)
        self.B_Start = QtWidgets.QPushButton(self.frame_3)
        self.B_Start.setMinimumSize(QtCore.QSize(150, 50))
        self.B_Start.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.B_Start.setFont(font)
        self.B_Start.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.B_Start.setStyleSheet("QPushButton{\n"
"    color: #168aad;\n"
"     background-color: rgb(240, 240, 240);\n"
"    border-radius:20px;\n"
"    border: 2px solid #168aad;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background: #168aad;\n"
"    border-radius:20px;\n"
"    color:rgb(240, 240, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"background: #168aad;\n"
"    border-radius:20px;\n"
"    color:rgb(240, 240, 240);\n"
"}")
        self.B_Start.setObjectName("B_Start")
        self.verticalLayout_4.addWidget(self.B_Start, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.verticalLayout_5.addWidget(self.frame_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setStyleSheet("color: rgb(0, 0, 0)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_Settings = QtWidgets.QPushButton(self.frame)
        self.btn_Settings.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_Settings.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_Settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/settingsIcon/settingss.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Settings.setIcon(icon)
        self.btn_Settings.setIconSize(QtCore.QSize(50, 50))
        self.btn_Settings.setObjectName("btn_Settings")
        self.horizontalLayout_8.addWidget(self.btn_Settings)
        self.verticalLayout_5.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.stackedWidget.addWidget(self.page)
        self.Mainpage = QtWidgets.QWidget()
        self.Mainpage.setObjectName("Mainpage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Mainpage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.Mainpage)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setStyleSheet("QPushButton{\n"
"    color: #168aad;\n"
"     background-color: rgb(240, 240, 240);\n"
"    border-radius:5px;\n"
"    border: 2px solid #168aad;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background: #168aad;\n"
"    border-radius:5px;\n"
"    color:rgb(240, 240, 240);\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #168aad;\n"
"     background-color: rgb(240, 240, 240);\n"
"    border-radius:5px;\n"
"    border: 2px solid #168aad;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_setCurrent = QtWidgets.QPushButton(self.frame_6)
        self.btn_setCurrent.setObjectName("btn_setCurrent")
        self.verticalLayout_8.addWidget(self.btn_setCurrent)
        self.btn_setMaximum = QtWidgets.QPushButton(self.frame_6)
        self.btn_setMaximum.setObjectName("btn_setMaximum")
        self.verticalLayout_8.addWidget(self.btn_setMaximum)
        self.horizontalLayout_2.addWidget(self.frame_6, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(9999999, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.Time_Label = QtWidgets.QLabel(self.frame_4)
        self.Time_Label.setMinimumSize(QtCore.QSize(150, 0))
        self.Time_Label.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(18)
        font.setBold(True)
        self.Time_Label.setFont(font)
        self.Time_Label.setObjectName("Time_Label")
        self.horizontalLayout.addWidget(self.Time_Label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.Date_Label = QtWidgets.QLabel(self.frame_4)
        self.Date_Label.setMinimumSize(QtCore.QSize(300, 0))
        self.Date_Label.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(18)
        font.setBold(True)
        self.Date_Label.setFont(font)
        self.Date_Label.setObjectName("Date_Label")
        self.horizontalLayout.addWidget(self.Date_Label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignRight)
        self.frame_5 = QtWidgets.QFrame(self.Mainpage)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.legend = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setBold(False)
        self.legend.setFont(font)
        self.legend.setObjectName("legend")
        self.horizontalLayout_5.addWidget(self.legend)
        self.verticalLayout.addWidget(self.frame_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.counterFrame = QtWidgets.QFrame(self.Mainpage)
        self.counterFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.counterFrame.setStyleSheet("")
        self.counterFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.counterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.counterFrame.setObjectName("counterFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.counterFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.warningLabel = QtWidgets.QLabel(self.counterFrame)
        self.warningLabel.setText("")
        self.warningLabel.setObjectName("warningLabel")
        self.horizontalLayout_4.addWidget(self.warningLabel)
        self.peopleCounter = QtWidgets.QLabel(self.counterFrame)
        self.peopleCounter.setMinimumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        self.peopleCounter.setFont(font)
        self.peopleCounter.setStyleSheet("QLabel{\n"
"    border: 8px solid rgb(179, 255, 174);\n"
"    border-radius: 300px;\n"
"}")
        self.peopleCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.peopleCounter.setObjectName("peopleCounter")
        self.horizontalLayout_4.addWidget(self.peopleCounter, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.warningLabel2 = QtWidgets.QLabel(self.counterFrame)
        self.warningLabel2.setText("")
        self.warningLabel2.setObjectName("warningLabel2")
        self.horizontalLayout_4.addWidget(self.warningLabel2)
        self.verticalLayout.addWidget(self.counterFrame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.statusFrame = QtWidgets.QFrame(self.Mainpage)
        self.statusFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.statusFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statusFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusFrame.setObjectName("statusFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.statusFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.statusFrame)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(24)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Status_Label = QtWidgets.QLabel(self.statusFrame)
        self.Status_Label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setStrikeOut(False)
        self.Status_Label.setFont(font)
        self.Status_Label.setLineWidth(0)
        self.Status_Label.setScaledContents(False)
        self.Status_Label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Status_Label.setWordWrap(False)
        self.Status_Label.setObjectName("Status_Label")
        self.horizontalLayout_3.addWidget(self.Status_Label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.statusFrame)
        self.stackedWidget.addWidget(self.Mainpage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout_7.addWidget(self.drop_shadow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSave_and_Exit = QtWidgets.QAction(MainWindow)
        self.actionSave_and_Exit.setObjectName("actionSave_and_Exit")
        self.actionSet_Maximum_Capacity = QtWidgets.QAction(MainWindow)
        self.actionSet_Maximum_Capacity.setObjectName("actionSet_Maximum_Capacity")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#aaff7f;\">People Counter </span><span style=\" font-size:12pt; color:#aaff7f;\">Monitoring System</span></p></body></html>"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; color:#aaff7f;\">People Counter </span><span style=\" font-size:28pt; color:#aaff7f;\">Monitoring System</span></p></body></html>"))
        self.label_description.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">A THESIS</span> PROJECT</p></body></html>"))
        self.B_Start.setText(_translate("MainWindow", "START"))
        self.btn_setCurrent.setText(_translate("MainWindow", "Set Current People Inside"))
        self.btn_setMaximum.setText(_translate("MainWindow", "  Set Maximum People Inside  "))
        self.label_3.setText(_translate("MainWindow", "Time :"))
        self.Time_Label.setText(_translate("MainWindow", "-"))
        self.label_2.setText(_translate("MainWindow", "Date :"))
        self.Date_Label.setText(_translate("MainWindow", "-"))
        self.legend.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#b3ffae;\">Green</span><span style=\" font-size:36pt;\"> = Go</span></p><p><span style=\" font-size:36pt; color:#ff6464;\">Red</span><span style=\" font-size:36pt;\"> =     Stop / Wait</span></p></body></html>"))
        self.peopleCounter.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#00ff7f;\">....</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Status :"))
        self.Status_Label.setText(_translate("MainWindow", "waiting"))
        self.actionSave_and_Exit.setText(_translate("MainWindow", "Save and Exit"))
        self.actionSet_Maximum_Capacity.setText(_translate("MainWindow", "Set Maximum Capacity"))
import resource_rc
