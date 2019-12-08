# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

# Form implementation generated from reading ui file 'roc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

__author__ = "Ítalo Barros"
__copyright__ = "Copyright 2019, LASER - UFPB"
__license__ = "X11"
__version__ = "alpha 0.1"
__maintainer__ = "Ítalo Barros"
__email__ = "italorenan_@hotmail.com"
__status__ = "In Development"

import vectors
import webbrowser
import paramiko
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from qrApp import Ui_qrReaderApp
from tb1Settings import Ui_robotOneConfig
from tb1Settings import Ui_robotOneConfig
from tb2Settings import Ui_robotTwoConfig
from tb3Settings import Ui_robotThreeConfig
from tb4Settings import Ui_robotFourConfig
from rocSettings import Ui_rocConfigure
from about import Ui_aboutDialog
from paramiko import SSHClient
from paramiko import SSHException
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

# Global Variables
robot_Selected_Value = 'None'


class Ui_MainWindow(object):
    """
    ROC - Robot Operational Controler Main Window Class

    """
    def setExperiment(self, **kwargs):
        """ Responsible to Handle the Set Experiment Button """
        # If the dictionary robot value is 'tb1' then change the button Style
        global robot_Selected_Value
        if kwargs['robot'] =='1':
            robot_Selected_Value = 'TB1'
        elif kwargs['robot'] =='2':
            robot_Selected_Value = 'TB2'
        elif kwargs['robot'] =='3':
            robot_Selected_Value = 'TB3'
        elif kwargs['robot'] =='4':
            robot_Selected_Value = 'TB4'
        elif kwargs['set'] =='OK':
            # CONFIGURATION VARIABLES
            robot_Type_Value = self.robot_Selection_Type.currentText()
            robot_Role_Value = self.robot_Selection_Role.currentText()
            robot_Task_Value = self.robot_Selection_Task.currentText()
            robot_Behavior_Value = self.robot_Selection_Behavior.currentText()
            robot_Experiment_Value = self.robot_Selection_Experiment.currentText()
            # XML CREATION
            environmentXMLFile = et.Element('EXP_CONFIGURATIONS')
            comment = et.Comment("Experiment Configuration and Variables")
            environmentXMLFile.append(comment)
            environmentConfig = et.SubElement(environmentXMLFile, 'ROBOT_SELECTED')
            environmentConfig.text = str(robot_Selected_Value)
            environmentConfig = et.SubElement(environmentXMLFile, 'ROBOT_TYPE')
            environmentConfig.text = str(robot_Type_Value)
            environmentConfig = et.SubElement(environmentXMLFile, 'ROBOT_ROLE')
            environmentConfig.text = str(robot_Role_Value)
            environmentConfig = et.SubElement(environmentXMLFile, 'ROBOT_TASK')
            environmentConfig.text = str(robot_Task_Value)
            environmentConfig = et.SubElement(environmentXMLFile, 'ROBOT_BEHAVIOR')
            environmentConfig.text = str(robot_Behavior_Value)
            environmentConfig = et.SubElement(environmentXMLFile, 'ROBOT_EXPERIMENT')
            environmentConfig.text = str(robot_Experiment_Value)
            try:
                tree = et.ElementTree(environmentXMLFile)
                tree.write('experimentConfig.xml', encoding='utf8')
                operationSucess()
            except:
                operationError()


    def openQrApp(self):
        """ Open the QR Reader Applicaton """
        self.qrApp_Window = QtWidgets.QDialog()
        self.openQrApp_ui = Ui_qrReaderApp()
        self.openQrApp_ui.setupUi(self.qrApp_Window)
        self.qrApp_Window.show()

    def openAboutApp(self):
        """ Open the About Screen """
        self.about_Window = QtWidgets.QDialog()
        self.about_ui = Ui_aboutDialog()
        self.about_ui.setupUi(self.about_Window)
        self.about_Window.show()
    
    def openRocConfig(self):
        """ Open the ROC Configurations Screen """
        self.rocConfig_Window = QtWidgets.QDialog()
        self.rocConfig_ui = Ui_rocConfigure()
        self.rocConfig_ui.setupUi(self.rocConfig_Window)
        self.rocConfig_Window.show()

    def openTB1Settings(self):
        """ Open the TB1 Settings and Configurations """
        self.TB1_Window = QtWidgets.QDialog()
        self.TB1_ui = Ui_robotOneConfig()
        self.TB1_ui.setupUi(self.TB1_Window)
        self.TB1_Window.show()

    def openTB2Settings(self):
        """ Open the TB2 Settings and Configurations """
        self.TB2_Window = QtWidgets.QDialog()
        self.TB2_ui = Ui_robotTwoConfig()
        self.TB2_ui.setupUi(self.TB2_Window)
        self.TB2_Window.show()

    def openTB3Settings(self):
        """ Open the TB3 Settings and Configurations """
        self.TB3_Window = QtWidgets.QDialog()
        self.TB3_ui = Ui_robotThreeConfig()
        self.TB3_ui.setupUi(self.TB3_Window)
        self.TB3_Window.show()

    def openTB4Settings(self):
        """ Open the TB4 Settings and Configurations """
        self.TB4_Window = QtWidgets.QDialog()
        self.TB4_ui = Ui_robotFourConfig()
        self.TB4_ui.setupUi(self.TB4_Window)
        self.TB4_Window.show()

    def mainWebActions(self, **kwargs):
        """ Responsible to Handle all the Buttons that lead to an web page """
        # If the dictionary item value is the required opens the webpage
        if kwargs['button']=='tiago':
            # Only 1 click at every 5 seconds
            self.tiago_Contact.setDown(True)
            QTimer.singleShot(5000, lambda: self.tiago_Contact.setDown(False))
            webbrowser.open('https://sites.google.com/view/tiagopn/')

    def buttonStatusChange(self,**kwargs):
        """ Responsible to Handle the Status Buttons Color Change """
        # If the dictionary robot value is 'tb1' then change the button Style
        if kwargs['robot']=='tb1':
            if self.robot_TB1_Viewer.isChecked() is True:
                self.robot_TB1_Status.setStyleSheet("background: rgba(25, 27, 33, 0.2);\n"
                                                    "color: rgb(193, 69, 69);\n"
                                                    "font: 7pt \"Khmer OS\";")
            else:
                self.robot_TB1_Status.setStyleSheet("color: rgb(193, 69, 69);\n"
                                                    "font: 7pt \"Khmer OS\";")
        # If the dictionary robot value is 'tb2' then change the button Style
        if kwargs['robot']=='tb2':
            if self.robot_TB2_Viewer.isChecked() is True:
                self.robot_TB2_Status.setStyleSheet("background: rgba(25, 27, 33, 0.2);\n"
                                                    "color: rgb(193, 69, 69);\n"
                                                    "font: 7pt \"Khmer OS\";")
            else:
                self.robot_TB2_Status.setStyleSheet("color: rgb(193, 69, 69);\n"
                                                    "font: 7pt \"Khmer OS\";")
        # If the dictionary robot value is 'tb3' then change the button Style
        if kwargs['robot']=='tb3':
            if self.robot_TB3_Viewer.isChecked() is True:
                self.robot_TB3_Status.setStyleSheet("background: rgba(25, 27, 33, 0.2);\n"
                                                    "color: rgb(193, 69, 69);\n"
                                                    "font: 7pt \"Khmer OS\";")
            else:
                self.robot_TB3_Status.setStyleSheet("color: rgb(193, 69, 69);\n"
                                                    "font: 7pt \"Khmer OS\";")
        # If the dictionary robot value is 'tb4' then change the button Style
        if kwargs['robot']=='tb4':
            if self.robot_TB4_Viewer.isChecked() is True:
                self.robot_TB4_Status.setStyleSheet("background: rgba(25, 27, 33, 0.2);\n"
                                                    "color: rgb(193, 69, 69);\n"
                                                    "font: 7pt \"Khmer OS\";")
            else:
                self.robot_TB4_Status.setStyleSheet("color: rgb(193, 69, 69);\n"
                                                    "font: 7pt \"Khmer OS\";")
        
    def resetButtons(self, **kwargs):
        """ Responsible to Handle the RESET Buttons Actions """
        pass
    
    def robotsTerminals(self, **kwargs):
        """ Responsible to Open and Close Robot Terminals after Selection """
        # If the dictionary robot value is 'tb1' then change the button Style
        if kwargs['robot']=='tb1':
            if self.robot_TB1_Viewer.isChecked() is True:
                self.robot_TB1_Viewer.setDown(True)
                QTimer.singleShot(5000, lambda: self.robot_TB1_Viewer.setDown(False))
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap(":/vectors/ShellWhite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.terminalWidget.insertTab(0, robotOneTerminal(), icon6, "Robot 1")
                index = self.terminalWidget.indexOf(self.terminalWidget)
                print(index)
            else:
                self.terminalWidget.removeTab(0)

        if kwargs['robot']=='tb2':
            if self.robot_TB2_Viewer.isChecked() is True:
                self.robot_TB2_Viewer.setDown(True)
                QTimer.singleShot(5000, lambda: self.robot_TB2_Viewer.setDown(False))
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap(":/vectors/ShellWhite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.terminalWidget.insertTab(2, robotTwoTerminal(), icon6, "Robot 2")
            else:
                self.terminalWidget.removeTab(2)

        if kwargs['robot']=='tb3':
            if self.robot_TB3_Viewer.isChecked() is True:
                self.robot_TB3_Viewer.setDown(True)
                QTimer.singleShot(5000, lambda: self.robot_TB3_Viewer.setDown(False))
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap(":/vectors/ShellWhite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.terminalWidget.insertTab(3, robotThreeTerminal(), icon6, "Robot 3")
            else:
                self.terminalWidget.removeTab(3)

        if kwargs['robot']=='tb4':
            if self.robot_TB4_Viewer.isChecked() is True:
                self.robot_TB4_Viewer.setDown(True)
                QTimer.singleShot(5000, lambda: self.robot_TB4_Viewer.setDown(False))
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap(":/vectors/ShellWhite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.terminalWidget.insertTab(4, robotFourTerminal(), icon6, "Robot 4")
            else:
                self.terminalWidget.removeTab(4)

    def setupUi(self, MainWindow):
        """ Here starts the Main Code and Definitions for The Base Applicaton """
        MainWindow.setObjectName("MainWindow")
        # Window Sizes
        MainWindow.resize(1280, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 600))
        # Main Window
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/roc_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(10, 10))
        self.mainWindowBase = QtWidgets.QWidget(MainWindow)
        self.mainWindowBase.setStyleSheet("background: #2A2E37;")
        self.mainWindowBase.setObjectName("mainWindowBase")
        # Side Menu
        self.menu_Logo = QtWidgets.QFrame(self.mainWindowBase)
        self.menu_Logo.setGeometry(QtCore.QRect(0, 0, 120, 120))
        self.menu_Logo.setStyleSheet("background: rgba(25, 27, 33, 0.2);\n"
                                     "image: url(:/logos/roc_Logo.png);")
        self.menu_Logo.setObjectName("menu_Logo")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_Logo)
        self.gridLayout.setObjectName("gridLayout")
        self.menuFrame = QtWidgets.QFrame(self.mainWindowBase)
        self.menuFrame.setGeometry(QtCore.QRect(0, 0, 120, 600))
        self.menuFrame.setStyleSheet("background: #313640;\n"
                                     "")
        self.menuFrame.setObjectName("menuFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.menuFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.menu_Line = QtWidgets.QFrame(self.mainWindowBase)
        self.menu_Line.setGeometry(QtCore.QRect(120, 0, 2, 600))
        self.menu_Line.setStyleSheet("background: rgba(41, 63, 71, 0.75);")
        self.menu_Line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_Line.setFrameShape(QtWidgets.QFrame.VLine)
        self.menu_Line.setObjectName("menu_Line")
        # QR Code Button
        self.qrcode_App_Button = QtWidgets.QCommandLinkButton(self.mainWindowBase)
        self.qrcode_App_Button.setGeometry(QtCore.QRect(5, 200, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.qrcode_App_Button.setFont(font)
        self.qrcode_App_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.qrcode_App_Button.setToolTipDuration(3000)
        self.qrcode_App_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                             "color: white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/vectors/qrcode.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.qrcode_App_Button.setIcon(icon1)
        self.qrcode_App_Button.setIconSize(QtCore.QSize(45, 45))
        self.qrcode_App_Button.setObjectName("qrcode_App_Button")
        self.qrcode_App_Button.clicked.connect(self.openQrApp)
        # Data Button
        self.data_Button = QtWidgets.QCommandLinkButton(self.mainWindowBase)
        self.data_Button.setGeometry(QtCore.QRect(5, 300, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.data_Button.setFont(font)
        self.data_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.data_Button.setToolTipDuration(3000)
        self.data_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                       "color: white;\n"
                                       "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/vectors/data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.data_Button.setIcon(icon2)
        self.data_Button.setIconSize(QtCore.QSize(45, 45))
        self.data_Button.setObjectName("data_Button")
        self.data_Button.clicked.connect(InProgress)
        # Config Button
        self.config_Button = QtWidgets.QCommandLinkButton(self.mainWindowBase)
        self.config_Button.setGeometry(QtCore.QRect(5, 400, 110, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.config_Button.setFont(font)
        self.config_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.config_Button.setToolTipDuration(3000)
        self.config_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                         "color: white;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/vectors/config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.config_Button.setIcon(icon3)
        self.config_Button.setIconSize(QtCore.QSize(45, 45))
        self.config_Button.setObjectName("config_Button")
        self.config_Button.clicked.connect(self.openRocConfig)
        # Docummentation Button
        self.docs_Button = QtWidgets.QCommandLinkButton(self.mainWindowBase)
        self.docs_Button.setGeometry(QtCore.QRect(1080, 15, 100, 50))
        self.docs_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.docs_Button.setToolTipDuration(3000)
        self.docs_Button.setStyleSheet("color: white;\n"
                                       "background: rgba(41, 63, 71, 0.75);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/vectors/docs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.docs_Button.setIcon(icon4)
        self.docs_Button.setIconSize(QtCore.QSize(40, 32))
        self.docs_Button.setObjectName("docs_Button")
        # About Button
        self.about_Button = QtWidgets.QCommandLinkButton(self.mainWindowBase)
        self.about_Button.setGeometry(QtCore.QRect(1180, 15, 91, 50))
        self.about_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_Button.setToolTipDuration(3000)
        self.about_Button.setStyleSheet("color: white;\n"
                                        "background: rgba(41, 63, 71, 0.75);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/vectors/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_Button.setIcon(icon5)
        self.about_Button.setIconSize(QtCore.QSize(30, 30))
        self.about_Button.setObjectName("about_Button")
        self.about_Button.clicked.connect(self.openAboutApp)
        # Viewer Base Design
        self.viewer_Superior_Line = QtWidgets.QFrame(self.mainWindowBase)
        self.viewer_Superior_Line.setGeometry(QtCore.QRect(1061, 70, 220, 2))
        self.viewer_Superior_Line.setStyleSheet("background: #1DDED8;")
        self.viewer_Superior_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.viewer_Superior_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.viewer_Superior_Line.setObjectName("viewer_Superior_Line")
        self.inferior_Line_Base = QtWidgets.QFrame(self.mainWindowBase)
        self.inferior_Line_Base.setGeometry(QtCore.QRect(121, 460, 1280, 2))
        self.inferior_Line_Base.setStyleSheet("background: #1DDED8;")
        self.inferior_Line_Base.setFrameShape(QtWidgets.QFrame.HLine)
        self.inferior_Line_Base.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.inferior_Line_Base.setObjectName("inferior_Line_Base")
        self.lateral_Line_Base = QtWidgets.QFrame(self.mainWindowBase)
        self.lateral_Line_Base.setGeometry(QtCore.QRect(1061, 0, 2, 462))
        self.lateral_Line_Base.setStyleSheet("background: #1DDED8;")
        self.lateral_Line_Base.setFrameShape(QtWidgets.QFrame.VLine)
        self.lateral_Line_Base.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lateral_Line_Base.setObjectName("lateral_Line_Base")
        self.robot_Viewer_Frame = QtWidgets.QFrame(self.mainWindowBase)
        self.robot_Viewer_Frame.setGeometry(QtCore.QRect(1063, 72, 218, 30))
        self.robot_Viewer_Frame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.robot_Viewer_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.robot_Viewer_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.robot_Viewer_Frame.setObjectName("robot_Viewer_Frame")
        self.robot_Viewer_Label = QtWidgets.QLabel(self.robot_Viewer_Frame)
        self.robot_Viewer_Label.setGeometry(QtCore.QRect(60, 9, 131, 16))
        self.robot_Viewer_Label.setStyleSheet("background: transparent;\n"
                                              "font: 10pt \"Khmer OS System\";\n"
                                              "color: white;")
        self.robot_Viewer_Label.setObjectName("robot_Viewer_Label")
        self.robotViewerBase = QtWidgets.QFrame(self.mainWindowBase)
        self.robotViewerBase.setGeometry(QtCore.QRect(1063, 100, 216, 110))
        self.robotViewerBase.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.robotViewerBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.robotViewerBase.setObjectName("robotViewerBase")
        self.robot_Viewer_Line = QtWidgets.QFrame(self.robotViewerBase)
        self.robot_Viewer_Line.setGeometry(QtCore.QRect(105, 15, 2, 80))
        self.robot_Viewer_Line.setStyleSheet("background: #1DDED8;")
        self.robot_Viewer_Line.setFrameShape(QtWidgets.QFrame.VLine)
        self.robot_Viewer_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.robot_Viewer_Line.setObjectName("robot_Viewer_Line")
        # Terminal Widget
        self.terminalWidget = QtWidgets.QTabWidget(self.mainWindowBase)
        self.terminalWidget.setGeometry(QtCore.QRect(121, 462, 1158, 139))
        self.terminalWidget.setMinimumSize(QtCore.QSize(1158, 139))
        self.terminalWidget.setMaximumSize(QtCore.QSize(1158, 139))
        self.terminalWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.terminalWidget.setIconSize(QtCore.QSize(10, 10))
        self.terminalWidget.setObjectName("terminalWidget")
        self.urxvtWidget = QtWidgets.QWidget()
        self.urxvtWidget.setObjectName("urxvtWidget")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/vectors/ShellWhite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # To add new tabs use the line above
        # self.terminalWidget.addTab(self.urxvtWidget, icon6, "")
        # Starts the Terminal within a New Tab
        self.terminalWidget.insertTab(0, embeddedTerminal(), icon6, "urvxt")
        # Robot TB1 Viwer Checkbox
        self.robot_TB1_Viewer = QtWidgets.QCheckBox(self.robotViewerBase)
        self.robot_TB1_Viewer.setGeometry(QtCore.QRect(15, 15, 80, 21))
        self.robot_TB1_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB1_Viewer.setToolTipDuration(3000)
        self.robot_TB1_Viewer.setStyleSheet("color: white;")
        self.robot_TB1_Viewer.setObjectName("robot_TB1_Viewer")
        # Robot TB2 Viwer Checkbox
        self.robot_TB2_Viewer = QtWidgets.QCheckBox(self.robotViewerBase)
        self.robot_TB2_Viewer.setGeometry(QtCore.QRect(15, 35, 81, 21))
        self.robot_TB2_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB2_Viewer.setToolTipDuration(3000)
        self.robot_TB2_Viewer.setStyleSheet("color: white;")
        self.robot_TB2_Viewer.setObjectName("robot_TB2_Viewer")
        # Robot TB3 Viwer Checkbox
        self.robot_TB3_Viewer = QtWidgets.QCheckBox(self.robotViewerBase)
        self.robot_TB3_Viewer.setGeometry(QtCore.QRect(15, 55, 81, 21))
        self.robot_TB3_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB3_Viewer.setToolTipDuration(3000)
        self.robot_TB3_Viewer.setStyleSheet("color: white;")
        self.robot_TB3_Viewer.setObjectName("robot_TB3_Viewer")
        # Robot TB4 Viwer Checkbox
        self.robot_TB4_Viewer = QtWidgets.QCheckBox(self.robotViewerBase)
        self.robot_TB4_Viewer.setGeometry(QtCore.QRect(15, 75, 81, 21))
        self.robot_TB4_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB4_Viewer.setToolTipDuration(3000)
        self.robot_TB4_Viewer.setStyleSheet("color: white;")
        self.robot_TB4_Viewer.setObjectName("robot_TB4_Viewer")
        # Robot TB1 Status Button
        self.robot_TB1_Status = QtWidgets.QPushButton(self.robotViewerBase)
        self.robot_TB1_Status.setGeometry(QtCore.QRect(119, 16, 90, 18))
        self.robot_TB1_Status.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB1_Status.setToolTipDuration(6000)
        self.robot_TB1_Status.setStyleSheet("color: rgb(193, 69, 69);\n"
                                            "font: 7pt \"Khmer OS\";")
        self.robot_TB1_Status.setObjectName("robot_TB1_Status")
       # Robot TB2 Status Button
        self.robot_TB2_Status = QtWidgets.QPushButton(self.robotViewerBase)
        self.robot_TB2_Status.setGeometry(QtCore.QRect(120, 36, 90, 18))
        self.robot_TB2_Status.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB2_Status.setToolTipDuration(6000)
        self.robot_TB2_Status.setStyleSheet("color: rgb(193, 69, 69);\n"
                                            "font: 7pt \"Khmer OS\";")
        self.robot_TB2_Status.setObjectName("robot_TB2_Status")
        # Robot TB3 Status Button
        self.robot_TB3_Status = QtWidgets.QPushButton(self.robotViewerBase)
        self.robot_TB3_Status.setGeometry(QtCore.QRect(120, 56, 90, 18))
        self.robot_TB3_Status.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB3_Status.setToolTipDuration(6000)
        self.robot_TB3_Status.setStyleSheet("color: rgb(193, 69, 69);\n"
                                            "font: 7pt \"Khmer OS\";")
        self.robot_TB3_Status.setObjectName("robot_TB3_Status")
        # Robot TB4 Status Button
        self.robot_TB4_Status = QtWidgets.QPushButton(self.robotViewerBase)
        self.robot_TB4_Status.setGeometry(QtCore.QRect(120, 76, 90, 18))
        self.robot_TB4_Status.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB4_Status.setToolTipDuration(6000)
        self.robot_TB4_Status.setStyleSheet("color: rgb(193, 69, 69);\n"
                                            "font: 7pt \"Khmer OS\";")
        self.robot_TB4_Status.setObjectName("robot_TB4_Status")
        # Robot TB1 Main Widget
        self.robot_TB1 = QtWidgets.QGroupBox(self.mainWindowBase)
        self.robot_TB1.setEnabled(True)
        self.robot_TB1.setGeometry(QtCore.QRect(150, 10, 439, 219))
        self.robot_TB1.setStyleSheet("\n"
                                     "color: rgb(206, 255, 188);")
        self.robot_TB1.setObjectName("robot_TB1")
        self.robot_TB1.setHidden(True)
        self.options_TB1 = QtWidgets.QFrame(self.robot_TB1)
        self.options_TB1.setGeometry(QtCore.QRect(215, 21, 221, 196))
        self.options_TB1.setStyleSheet("")
        self.options_TB1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_TB1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_TB1.setObjectName("options_TB1")
        self.line_TB1_1 = QtWidgets.QFrame(self.options_TB1)
        self.line_TB1_1.setGeometry(QtCore.QRect(90, 11, 2, 80))
        self.line_TB1_1.setStyleSheet("background: #1DDED8;")
        self.line_TB1_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB1_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB1_1.setObjectName("line_TB1_1")
        # TB1 Settings and Configuration Button
        self.configure_TB1_Button = QtWidgets.QPushButton(self.options_TB1)
        self.configure_TB1_Button.setGeometry(QtCore.QRect(100, 70, 111, 18))
        self.configure_TB1_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configure_TB1_Button.setToolTipDuration(3000)
        self.configure_TB1_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                                "color: rgb(22, 22, 22)")
        self.configure_TB1_Button.setObjectName("configure_TB1_Button")
        self.configure_TB1_Button.clicked.connect(self.openTB1Settings)
        # TB1 Logs Button
        self.logs_TB1_Button = QtWidgets.QPushButton(self.options_TB1)
        self.logs_TB1_Button.setGeometry(QtCore.QRect(100, 45, 111, 18))
        self.logs_TB1_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logs_TB1_Button.setToolTipDuration(3000)
        self.logs_TB1_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                           "color: rgb(22, 22, 22)")
        self.logs_TB1_Button.setObjectName("logs_TB1_Button")
        self.floor_TB1_Show = QtWidgets.QCheckBox(self.options_TB1)
        self.floor_TB1_Show.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.floor_TB1_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.floor_TB1_Show.setToolTipDuration(3000)
        self.floor_TB1_Show.setStyleSheet("color: white;")
        self.floor_TB1_Show.setObjectName("floor_TB1_Show")
        self.kinect_TB1_Show = QtWidgets.QCheckBox(self.options_TB1)
        self.kinect_TB1_Show.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.kinect_TB1_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kinect_TB1_Show.setToolTipDuration(3000)
        self.kinect_TB1_Show.setStyleSheet("color: white;")
        self.kinect_TB1_Show.setObjectName("kinect_TB1_Show")
        self.gmapp_TB1_Show = QtWidgets.QCheckBox(self.options_TB1)
        self.gmapp_TB1_Show.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.gmapp_TB1_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gmapp_TB1_Show.setToolTipDuration(3000)
        self.gmapp_TB1_Show.setStyleSheet("color: white;")
        self.gmapp_TB1_Show.setObjectName("gmapp_TB1_Show")
        self.camera_TB1_Show = QtWidgets.QCheckBox(self.options_TB1)
        self.camera_TB1_Show.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.camera_TB1_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camera_TB1_Show.setStyleSheet("color: white;")
        self.camera_TB1_Show.setObjectName("camera_TB1_Show")
        self.on_TB1_Viewer = QtWidgets.QRadioButton(self.options_TB1)
        self.on_TB1_Viewer.setGeometry(QtCore.QRect(100, 10, 51, 21))
        self.on_TB1_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.on_TB1_Viewer.setToolTipDuration(3000)
        self.on_TB1_Viewer.setObjectName("on_TB1_Viewer")
        self.off_TB1_Viewer = QtWidgets.QRadioButton(self.options_TB1)
        self.off_TB1_Viewer.setGeometry(QtCore.QRect(160, 10, 51, 21))
        self.off_TB1_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.off_TB1_Viewer.setToolTipDuration(3000)
        self.off_TB1_Viewer.setObjectName("off_TB1_Viewer")
        self.line_TB1_2 = QtWidgets.QFrame(self.options_TB1)
        self.line_TB1_2.setGeometry(QtCore.QRect(100, 35, 110, 1))
        self.line_TB1_2.setStyleSheet("")
        self.line_TB1_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_TB1_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB1_2.setObjectName("line_TB1_2")
        self.reload_TB1 = QtWidgets.QPushButton(self.options_TB1)
        self.reload_TB1.setGeometry(QtCore.QRect(114, 162, 90, 20))
        self.reload_TB1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reload_TB1.setToolTipDuration(3000)
        self.reload_TB1.setStyleSheet("color: rgb(193, 69, 69);\n"
                                      "font: 75 9pt \"Clean\";\n"
                                      "background: rgba(25, 27, 33, 0.2);")
        self.reload_TB1.setObjectName("reload_TB1")
        self.line_TB1_4 = QtWidgets.QFrame(self.options_TB1)
        self.line_TB1_4.setGeometry(QtCore.QRect(209, 160, 2, 25))
        self.line_TB1_4.setStyleSheet("background: #313640;")
        self.line_TB1_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB1_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB1_4.setObjectName("line_TB1_4")
        self.line_TB1_3 = QtWidgets.QFrame(self.options_TB1)
        self.line_TB1_3.setGeometry(QtCore.QRect(10, 160, 2, 25))
        self.line_TB1_3.setStyleSheet("background: #313640;")
        self.line_TB1_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB1_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB1_3.setObjectName("line_TB1_3")
        #
        self.reset_TB1 = QtWidgets.QPushButton(self.options_TB1)
        self.reset_TB1.setGeometry(QtCore.QRect(15, 162, 90, 20))
        self.reset_TB1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_TB1.setToolTipDuration(3000)
        self.reset_TB1.setStyleSheet("color: rgb(193, 69, 69);\n"
                                     "font: 75 9pt \"Clean\";\n"
                                     "background: rgba(25, 27, 33, 0.2);")
        self.reset_TB1.setObjectName("reset_TB1")
        self.valuesTB1Frame = QtWidgets.QFrame(self.options_TB1)
        self.valuesTB1Frame.setGeometry(QtCore.QRect(10, 100, 201, 51))
        self.valuesTB1Frame.setToolTipDuration(3000)
        self.valuesTB1Frame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.valuesTB1Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.valuesTB1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.valuesTB1Frame.setObjectName("valuesTB1Frame")
        self.x_TB1_Value = QtWidgets.QLCDNumber(self.valuesTB1Frame)
        self.x_TB1_Value.setGeometry(QtCore.QRect(30, 7, 31, 16))
        self.x_TB1_Value.setObjectName("x_TB1_Value")
        self.x_TB1_Label = QtWidgets.QLabel(self.valuesTB1Frame)
        self.x_TB1_Label.setGeometry(QtCore.QRect(10, 7, 16, 16))
        self.x_TB1_Label.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);")
        self.x_TB1_Label.setObjectName("x_TB1_Label")
        self.y_TB1_Label = QtWidgets.QLabel(self.valuesTB1Frame)
        self.y_TB1_Label.setGeometry(QtCore.QRect(10, 31, 16, 16))
        self.y_TB1_Label.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);")
        self.y_TB1_Label.setObjectName("y_TB1_Label")
        self.y_TB1_Value = QtWidgets.QLCDNumber(self.valuesTB1Frame)
        self.y_TB1_Value.setGeometry(QtCore.QRect(30, 31, 31, 16))
        self.y_TB1_Value.setObjectName("y_TB1_Value")
        self.velocity_TB1_Label = QtWidgets.QLabel(self.valuesTB1Frame)
        self.velocity_TB1_Label.setGeometry(QtCore.QRect(75, 7, 61, 16))
        self.velocity_TB1_Label.setStyleSheet("background: transparent;\n"
                                              "color: rgb(206, 255, 188);")
        self.velocity_TB1_Label.setObjectName("velocity_TB1_Label")
        self.linear_TB1_Value = QtWidgets.QLCDNumber(self.valuesTB1Frame)
        self.linear_TB1_Value.setGeometry(QtCore.QRect(130, 7, 31, 16))
        self.linear_TB1_Value.setObjectName("linear_TB1_Value")
        self.battery_TB1_Label = QtWidgets.QLabel(self.valuesTB1Frame)
        self.battery_TB1_Label.setGeometry(QtCore.QRect(75, 31, 61, 16))
        self.battery_TB1_Label.setStyleSheet("background: transparent;\n"
                                             "color: rgb(206, 255, 188);")
        self.battery_TB1_Label.setObjectName("battery_TB1_Label")
        self.turtleBat_TB1_Value = QtWidgets.QLCDNumber(self.valuesTB1Frame)
        self.turtleBat_TB1_Value.setGeometry(QtCore.QRect(130, 30, 31, 16))
        self.turtleBat_TB1_Value.setObjectName("turtleBat_TB1_Value")
        self.noteBat_TB1_Value = QtWidgets.QLCDNumber(self.valuesTB1Frame)
        self.noteBat_TB1_Value.setGeometry(QtCore.QRect(165, 30, 31, 16))
        self.noteBat_TB1_Value.setObjectName("noteBat_TB1_Value")
        self.angular_TB1_Value = QtWidgets.QLCDNumber(self.valuesTB1Frame)
        self.angular_TB1_Value.setGeometry(QtCore.QRect(165, 7, 31, 16))
        self.angular_TB1_Value.setObjectName("angular_TB1_Value")
        self.viewer_TB1 = QtWidgets.QTabWidget(self.robot_TB1)
        self.viewer_TB1.setGeometry(QtCore.QRect(0, 20, 221, 198))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.viewer_TB1.setFont(font)
        self.viewer_TB1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewer_TB1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.viewer_TB1.setStyleSheet("color: white;")
        self.viewer_TB1.setTabPosition(QtWidgets.QTabWidget.West)
        self.viewer_TB1.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.viewer_TB1.setElideMode(QtCore.Qt.ElideLeft)
        self.viewer_TB1.setObjectName("viewer_TB1")
        self.kinnect_TB1_Screen = QtWidgets.QWidget()
        self.kinnect_TB1_Screen.setObjectName("kinnect_TB1_Screen")
        self.viewer_TB1.addTab(self.kinnect_TB1_Screen, "")
        self.gmapp_TB1_Screen = QtWidgets.QWidget()
        self.gmapp_TB1_Screen.setObjectName("gmapp_TB1_Screen")
        self.viewer_TB1.addTab(self.gmapp_TB1_Screen, "")
        self.floor_TB1_Screen = QtWidgets.QWidget()
        self.floor_TB1_Screen.setObjectName("floor_TB1_Screen")
        self.viewer_TB1.addTab(self.floor_TB1_Screen, "")
        self.camera_TB1_Screen = QtWidgets.QWidget()
        self.camera_TB1_Screen.setObjectName("camera_TB1_Screen")
        self.viewer_TB1.addTab(self.camera_TB1_Screen, "")
        self.robot_Selection_Frame = QtWidgets.QFrame(self.mainWindowBase)
        self.robot_Selection_Frame.setGeometry(QtCore.QRect(1063, 208, 218, 30))
        self.robot_Selection_Frame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.robot_Selection_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.robot_Selection_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.robot_Selection_Frame.setObjectName("robot_Selection_Frame")
        self.robot_Selection_Label = QtWidgets.QLabel(self.robot_Selection_Frame)
        self.robot_Selection_Label.setGeometry(QtCore.QRect(52, 9, 131, 16))
        self.robot_Selection_Label.setStyleSheet("background: transparent;\n"
                                                 "font: 10pt \"Khmer OS System\";\n"
                                                 "color: white;")
        self.robot_Selection_Label.setObjectName("robot_Selection_Label")
        self.robotSelectionBase = QtWidgets.QFrame(self.mainWindowBase)
        self.robotSelectionBase.setGeometry(QtCore.QRect(1063, 235, 216, 224))
        self.robotSelectionBase.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.robotSelectionBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.robotSelectionBase.setObjectName("robotSelectionBase")
        self.robot_Selection_TypeLabel = QtWidgets.QLabel(self.robotSelectionBase)
        self.robot_Selection_TypeLabel.setGeometry(QtCore.QRect(20, 74, 91, 21))
        self.robot_Selection_TypeLabel.setStyleSheet("color: white;")
        self.robot_Selection_TypeLabel.setObjectName("robot_Selection_TypeLabel")
        self.robot_Selection_Type = QtWidgets.QComboBox(self.robotSelectionBase)
        self.robot_Selection_Type.setGeometry(QtCore.QRect(110, 72, 91, 23))
        self.robot_Selection_Type.setStyleSheet("color: white;\n"
                                                "font: 8pt \"Sans Serif\";")
        self.robot_Selection_Type.setObjectName("robot_Selection_Type")
        self.robot_Selection_Type.addItem("")
        self.robot_Selection_Type.addItem("")
        self.robot_Selection_Type.addItem("")
        self.robot_Selection_Role = QtWidgets.QComboBox(self.robotSelectionBase)
        self.robot_Selection_Role.setGeometry(QtCore.QRect(110, 100, 91, 23))
        self.robot_Selection_Role.setStyleSheet("color: white;\n"
                                                "font: 8pt \"Sans Serif\";")
        self.robot_Selection_Role.setObjectName("robot_Selection_Role")
        self.robot_Selection_Role.addItem("")
        self.robot_Selection_Role.addItem("")
        self.robot_Selection_Role.addItem("")
        self.robot_Selection_RoleLabel = QtWidgets.QLabel(self.robotSelectionBase)
        self.robot_Selection_RoleLabel.setGeometry(QtCore.QRect(20, 102, 91, 21))
        self.robot_Selection_RoleLabel.setStyleSheet("color: white;")
        self.robot_Selection_RoleLabel.setObjectName("robot_Selection_RoleLabel")
        self.robot_Selection_TaskLabel = QtWidgets.QLabel(self.robotSelectionBase)
        self.robot_Selection_TaskLabel.setGeometry(QtCore.QRect(20, 134, 91, 21))
        self.robot_Selection_TaskLabel.setStyleSheet("color: white;")
        self.robot_Selection_TaskLabel.setObjectName("robot_Selection_TaskLabel")
        self.robot_Selection_Task = QtWidgets.QComboBox(self.robotSelectionBase)
        self.robot_Selection_Task.setGeometry(QtCore.QRect(110, 132, 91, 23))
        self.robot_Selection_Task.setStyleSheet("color: white;\n"
                                                "font: 8pt \"Sans Serif\";")
        self.robot_Selection_Task.setObjectName("robot_Selection_Task")
        self.robot_Selection_Task.addItem("")
        self.robot_Selection_Task.addItem("")
        self.robot_Selection_Task.addItem("")
        self.robot_Selection_BehaviorLabel = QtWidgets.QLabel(self.robotSelectionBase)
        self.robot_Selection_BehaviorLabel.setGeometry(QtCore.QRect(20, 164, 91, 21))
        self.robot_Selection_BehaviorLabel.setStyleSheet("color: white;")
        self.robot_Selection_BehaviorLabel.setObjectName("robot_Selection_BehaviorLabel")
        self.robot_Selection_Behavior = QtWidgets.QComboBox(self.robotSelectionBase)
        self.robot_Selection_Behavior.setGeometry(QtCore.QRect(110, 162, 91, 23))
        self.robot_Selection_Behavior.setStyleSheet("color: white;\n"
                                                    "font: 8pt \"Sans Serif\";")
        self.robot_Selection_Behavior.setObjectName("robot_Selection_Behavior")
        self.robot_Selection_Behavior.addItem("")
        self.robot_Selection_Behavior.addItem("")
        self.robot_Selection_Behavior.addItem("")
        self.robot_Selection_Experiment = QtWidgets.QComboBox(self.robotSelectionBase)
        self.robot_Selection_Experiment.setGeometry(QtCore.QRect(110, 190, 91, 23))
        self.robot_Selection_Experiment.setStyleSheet("color: white;\n"
                                                      "font: 8pt \"Sans Serif\";")
        self.robot_Selection_Experiment.setObjectName("robot_Selection_Experiment")
        self.robot_Selection_Experiment.addItem("")
        self.robot_Selection_Experiment.addItem("")
        self.robot_Selection_Experiment.addItem("")
        self.robot_Selection_ExpLabel = QtWidgets.QLabel(self.robotSelectionBase)
        self.robot_Selection_ExpLabel.setGeometry(QtCore.QRect(20, 192, 91, 21))
        self.robot_Selection_ExpLabel.setStyleSheet("color: white;")
        self.robot_Selection_ExpLabel.setObjectName("robot_Selection_ExpLabel")
        # Set de Experiment Button
        self.set_Selection_Values = QtWidgets.QPushButton(self.robotSelectionBase)
        self.set_Selection_Values.setGeometry(QtCore.QRect(77, 8, 50, 22))
        self.set_Selection_Values.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_Selection_Values.setToolTipDuration(3000)
        self.set_Selection_Values.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                                "color: rgb(22, 22, 22);\n"
                                                "font: 7pt \"Khmer OS\";")
        self.set_Selection_Values.setObjectName("set_Selection_Values")
        self.set_Selection_Values.clicked.connect(lambda: self.setExperiment(robot='None', set='OK'))
        # Reset de Experiment Button
        self.reset_Selection_Values = QtWidgets.QPushButton(self.robotSelectionBase)
        self.reset_Selection_Values.setGeometry(QtCore.QRect(169, 8, 31, 22))
        self.reset_Selection_Values.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_Selection_Values.setToolTipDuration(3000)
        self.reset_Selection_Values.setStyleSheet("color: rgb(193, 69, 69);\n"
                                                  "font: 7pt \"Khmer OS\";\n"
                                                  "background: rgba(25, 27, 33, 0.2);")
        self.reset_Selection_Values.setObjectName("reset_Selection_Values")
        self.robot_Selection_InternalLine = QtWidgets.QFrame(self.robotSelectionBase)
        self.robot_Selection_InternalLine.setGeometry(QtCore.QRect(20, 35, 180, 3))
        self.robot_Selection_InternalLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.robot_Selection_InternalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.robot_Selection_InternalLine.setObjectName("robot_Selection_InternalLine")
        self.robot_TB1_Selection = QtWidgets.QRadioButton(self.robotSelectionBase)
        self.robot_TB1_Selection.setGeometry(QtCore.QRect(25, 45, 40, 20))
        self.robot_TB1_Selection.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB1_Selection.setToolTipDuration(3000)
        self.robot_TB1_Selection.setStyleSheet("color: white;")
        self.robot_TB1_Selection.setObjectName("robot_TB1_Selection")
        self.robot_TB2_Selection = QtWidgets.QRadioButton(self.robotSelectionBase)
        self.robot_TB2_Selection.setGeometry(QtCore.QRect(70, 45, 40, 20))
        self.robot_TB2_Selection.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB2_Selection.setToolTipDuration(3000)
        self.robot_TB2_Selection.setStyleSheet("color: white;")
        self.robot_TB2_Selection.setObjectName("robot_TB2_Selection")
        self.robot_TB4_Selection = QtWidgets.QRadioButton(self.robotSelectionBase)
        self.robot_TB4_Selection.setGeometry(QtCore.QRect(165, 45, 40, 20))
        self.robot_TB4_Selection.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB4_Selection.setToolTipDuration(3000)
        self.robot_TB4_Selection.setStyleSheet("color: white;")
        self.robot_TB4_Selection.setObjectName("robot_TB4_Selection")
        self.robot_TB3_Selection = QtWidgets.QRadioButton(self.robotSelectionBase)
        self.robot_TB3_Selection.setGeometry(QtCore.QRect(120, 45, 41, 20))
        self.robot_TB3_Selection.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.robot_TB3_Selection.setToolTipDuration(3000)
        self.robot_TB3_Selection.setStyleSheet("color: white;")
        self.robot_TB3_Selection.setObjectName("robot_TB3_Selection")
        # Run the Experiment/Others Button
        self.run_Selection_Values = QtWidgets.QPushButton(self.robotSelectionBase)
        self.run_Selection_Values.setGeometry(QtCore.QRect(20, 8, 50, 22))
        self.run_Selection_Values.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.run_Selection_Values.setToolTipDuration(3000)
        self.run_Selection_Values.setStyleSheet("background-color: rgb(188, 255, 143);\n"
                                                "color: rgb(22, 22, 22);\n"
                                                "font: 7pt \"Khmer OS\";")
        self.run_Selection_Values.setObjectName("run_Selection_Values")
        self.run_Selection_Values.clicked.connect(InProgress)
        # Down the Experiment/Others Button
        self.down_Selection_Values = QtWidgets.QPushButton(self.robotSelectionBase)
        self.down_Selection_Values.setGeometry(QtCore.QRect(135, 8, 31, 22))
        self.down_Selection_Values.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.down_Selection_Values.setToolTipDuration(3000)
        self.down_Selection_Values.setStyleSheet("color: rgb(0, 0, 0);\n"
                                                 "font: 7pt \"Khmer OS\";\n"
                                                 "background-color: rgb(107, 21, 18);")
        self.down_Selection_Values.setObjectName("down_Selection_Values")
        self.down_Selection_Values.clicked.connect(InProgress)
        # Selection Section Design
        self.selection_Superior_Line = QtWidgets.QFrame(self.mainWindowBase)
        self.selection_Superior_Line.setGeometry(QtCore.QRect(1061, 205, 220, 3))
        self.selection_Superior_Line.setStyleSheet("background: #1DDED8;")
        self.selection_Superior_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.selection_Superior_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.selection_Superior_Line.setObjectName("selection_Superior_Line")
        self.robot_TB2 = QtWidgets.QGroupBox(self.mainWindowBase)
        self.robot_TB2.setGeometry(QtCore.QRect(150, 235, 439, 219))
        self.robot_TB2.setStyleSheet("\n"
                                     "color: rgb(206, 255, 188);")
        self.robot_TB2.setObjectName("robot_TB2")
        self.robot_TB2.setHidden(True)
        self.options_TB2 = QtWidgets.QFrame(self.robot_TB2)
        self.options_TB2.setGeometry(QtCore.QRect(215, 21, 221, 196))
        self.options_TB2.setStyleSheet("")
        self.options_TB2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_TB2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_TB2.setObjectName("options_TB2")
        self.line_TB2_2 = QtWidgets.QFrame(self.options_TB2)
        self.line_TB2_2.setGeometry(QtCore.QRect(90, 11, 2, 80))
        self.line_TB2_2.setStyleSheet("background: #1DDED8;")
        self.line_TB2_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB2_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB2_2.setObjectName("line_TB2_2")
        # TB2 Settings and Configurations Button
        self.configure_TB2_Button = QtWidgets.QPushButton(self.options_TB2)
        self.configure_TB2_Button.setGeometry(QtCore.QRect(100, 70, 111, 18))
        self.configure_TB2_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configure_TB2_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                                "color: rgb(22, 22, 22)")
        self.configure_TB2_Button.setObjectName("configure_TB2_Button")
        self.configure_TB2_Button.clicked.connect(self.openTB2Settings)
        # TB2 Logs Button
        self.logs_TB2_Button = QtWidgets.QPushButton(self.options_TB2)
        self.logs_TB2_Button.setGeometry(QtCore.QRect(100, 45, 111, 18))
        self.logs_TB2_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logs_TB2_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                           "color: rgb(22, 22, 22)")
        self.logs_TB2_Button.setObjectName("logs_TB2_Button")
        self.floor_TB2_Show = QtWidgets.QCheckBox(self.options_TB2)
        self.floor_TB2_Show.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.floor_TB2_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.floor_TB2_Show.setStyleSheet("color: white;")
        self.floor_TB2_Show.setObjectName("floor_TB2_Show")
        self.kinect_TB2_Show = QtWidgets.QCheckBox(self.options_TB2)
        self.kinect_TB2_Show.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.kinect_TB2_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kinect_TB2_Show.setStyleSheet("color: white;")
        self.kinect_TB2_Show.setObjectName("kinect_TB2_Show")
        self.gmapp_TB2_Show = QtWidgets.QCheckBox(self.options_TB2)
        self.gmapp_TB2_Show.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.gmapp_TB2_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gmapp_TB2_Show.setStyleSheet("color: white;")
        self.gmapp_TB2_Show.setObjectName("gmapp_TB2_Show")
        self.camera_TB2_Show = QtWidgets.QCheckBox(self.options_TB2)
        self.camera_TB2_Show.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.camera_TB2_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camera_TB2_Show.setStyleSheet("color: white;")
        self.camera_TB2_Show.setObjectName("camera_TB2_Show")
        self.on_TB2_Viewer = QtWidgets.QRadioButton(self.options_TB2)
        self.on_TB2_Viewer.setGeometry(QtCore.QRect(100, 10, 51, 21))
        self.on_TB2_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.on_TB2_Viewer.setObjectName("on_TB2_Viewer")
        self.off_TB2_Viewer = QtWidgets.QRadioButton(self.options_TB2)
        self.off_TB2_Viewer.setGeometry(QtCore.QRect(160, 10, 51, 21))
        self.off_TB2_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.off_TB2_Viewer.setObjectName("off_TB2_Viewer")
        self.line_TB2_1 = QtWidgets.QFrame(self.options_TB2)
        self.line_TB2_1.setGeometry(QtCore.QRect(100, 35, 110, 1))
        self.line_TB2_1.setStyleSheet("")
        self.line_TB2_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_TB2_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB2_1.setObjectName("line_TB2_1")
        self.reload_TB2 = QtWidgets.QPushButton(self.options_TB2)
        self.reload_TB2.setGeometry(QtCore.QRect(114, 162, 90, 20))
        self.reload_TB2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reload_TB2.setStyleSheet("color: rgb(193, 69, 69);\n"
                                      "font: 75 9pt \"Clean\";\n"
                                      "background: rgba(25, 27, 33, 0.2);")
        self.reload_TB2.setObjectName("reload_TB2")
        self.line_TB2_4 = QtWidgets.QFrame(self.options_TB2)
        self.line_TB2_4.setGeometry(QtCore.QRect(209, 160, 2, 25))
        self.line_TB2_4.setStyleSheet("background: #313640;")
        self.line_TB2_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB2_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB2_4.setObjectName("line_TB2_4")
        self.line_TB2_3 = QtWidgets.QFrame(self.options_TB2)
        self.line_TB2_3.setGeometry(QtCore.QRect(10, 160, 2, 25))
        self.line_TB2_3.setStyleSheet("background: #313640;")
        self.line_TB2_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB2_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB2_3.setObjectName("line_TB2_3")
        self.reset_TB2 = QtWidgets.QPushButton(self.options_TB2)
        self.reset_TB2.setGeometry(QtCore.QRect(15, 162, 90, 20))
        self.reset_TB2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_TB2.setStyleSheet("color: rgb(193, 69, 69);\n"
                                     "font: 75 9pt \"Clean\";\n"
                                     "background: rgba(25, 27, 33, 0.2);")
        self.reset_TB2.setObjectName("reset_TB2")
        self.valuesTB2Frame = QtWidgets.QFrame(self.options_TB2)
        self.valuesTB2Frame.setGeometry(QtCore.QRect(10, 100, 201, 51))
        self.valuesTB2Frame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.valuesTB2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.valuesTB2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.valuesTB2Frame.setObjectName("valuesTB2Frame")
        self.x_TB2_Value = QtWidgets.QLCDNumber(self.valuesTB2Frame)
        self.x_TB2_Value.setGeometry(QtCore.QRect(30, 7, 31, 16))
        self.x_TB2_Value.setObjectName("x_TB2_Value")
        self.x_TB2_Label = QtWidgets.QLabel(self.valuesTB2Frame)
        self.x_TB2_Label.setGeometry(QtCore.QRect(10, 7, 16, 16))
        self.x_TB2_Label.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);")
        self.x_TB2_Label.setObjectName("x_TB2_Label")
        self.y_TB2_Label = QtWidgets.QLabel(self.valuesTB2Frame)
        self.y_TB2_Label.setGeometry(QtCore.QRect(10, 31, 16, 16))
        self.y_TB2_Label.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);")
        self.y_TB2_Label.setObjectName("y_TB2_Label")
        self.y_TB2_Value = QtWidgets.QLCDNumber(self.valuesTB2Frame)
        self.y_TB2_Value.setGeometry(QtCore.QRect(30, 31, 31, 16))
        self.y_TB2_Value.setObjectName("y_TB2_Value")
        self.velocity_TB2_Label = QtWidgets.QLabel(self.valuesTB2Frame)
        self.velocity_TB2_Label.setGeometry(QtCore.QRect(75, 7, 61, 16))
        self.velocity_TB2_Label.setStyleSheet("background: transparent;\n"
                                              "color: rgb(206, 255, 188);")
        self.velocity_TB2_Label.setObjectName("velocity_TB2_Label")
        self.linear_TB2_Value = QtWidgets.QLCDNumber(self.valuesTB2Frame)
        self.linear_TB2_Value.setGeometry(QtCore.QRect(130, 7, 31, 16))
        self.linear_TB2_Value.setObjectName("linear_TB2_Value")
        self.battery_TB2_Label = QtWidgets.QLabel(self.valuesTB2Frame)
        self.battery_TB2_Label.setGeometry(QtCore.QRect(75, 31, 61, 16))
        self.battery_TB2_Label.setStyleSheet("background: transparent;\n"
                                             "color: rgb(206, 255, 188);")
        self.battery_TB2_Label.setObjectName("battery_TB2_Label")
        self.turtleBat_TB2_Value = QtWidgets.QLCDNumber(self.valuesTB2Frame)
        self.turtleBat_TB2_Value.setGeometry(QtCore.QRect(130, 30, 31, 16))
        self.turtleBat_TB2_Value.setObjectName("turtleBat_TB2_Value")
        self.noteBat_TB2_Value = QtWidgets.QLCDNumber(self.valuesTB2Frame)
        self.noteBat_TB2_Value.setGeometry(QtCore.QRect(165, 30, 31, 16))
        self.noteBat_TB2_Value.setObjectName("noteBat_TB2_Value")
        self.angular_TB2_Value = QtWidgets.QLCDNumber(self.valuesTB2Frame)
        self.angular_TB2_Value.setGeometry(QtCore.QRect(165, 7, 31, 16))
        self.angular_TB2_Value.setObjectName("angular_TB2_Value")
        self.viewer_TB2 = QtWidgets.QTabWidget(self.robot_TB2)
        self.viewer_TB2.setGeometry(QtCore.QRect(0, 20, 221, 198))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.viewer_TB2.setFont(font)
        self.viewer_TB2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewer_TB2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.viewer_TB2.setStyleSheet("color: white;")
        self.viewer_TB2.setTabPosition(QtWidgets.QTabWidget.West)
        self.viewer_TB2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.viewer_TB2.setElideMode(QtCore.Qt.ElideLeft)
        self.viewer_TB2.setObjectName("viewer_TB2")
        self.kinnect_TB2_Screen = QtWidgets.QWidget()
        self.kinnect_TB2_Screen.setObjectName("kinnect_TB2_Screen")
        self.viewer_TB2.addTab(self.kinnect_TB2_Screen, "")
        self.gmapp_TB2_Screen = QtWidgets.QWidget()
        self.gmapp_TB2_Screen.setObjectName("gmapp_TB2_Screen")
        self.viewer_TB2.addTab(self.gmapp_TB2_Screen, "")
        self.floor_TB2_Screen = QtWidgets.QWidget()
        self.floor_TB2_Screen.setObjectName("floor_TB2_Screen")
        self.viewer_TB2.addTab(self.floor_TB2_Screen, "")
        self.camera_TB2_Screen = QtWidgets.QWidget()
        self.camera_TB2_Screen.setObjectName("camera_TB2_Screen")
        self.viewer_TB2.addTab(self.camera_TB2_Screen, "")
        self.label = QtWidgets.QLabel(self.mainWindowBase)
        self.label.setGeometry(QtCore.QRect(25, 570, 71, 16))
        self.label.setToolTipDuration(3000)
        self.label.setStyleSheet("background: transparent;\n"
                                 "color: white;")
        self.label.setObjectName("label")
        self.robot_TB3 = QtWidgets.QGroupBox(self.mainWindowBase)
        self.robot_TB3.setGeometry(QtCore.QRect(610, 10, 439, 219))
        self.robot_TB3.setStyleSheet("\n"
                                     "color: rgb(206, 255, 188);")
        self.robot_TB3.setObjectName("robot_TB3")
        self.robot_TB3.setHidden(True)
        self.options_TB3 = QtWidgets.QFrame(self.robot_TB3)
        self.options_TB3.setGeometry(QtCore.QRect(215, 21, 221, 196))
        self.options_TB3.setStyleSheet("")
        self.options_TB3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_TB3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_TB3.setObjectName("options_TB3")
        self.line_TB3_1 = QtWidgets.QFrame(self.options_TB3)
        self.line_TB3_1.setGeometry(QtCore.QRect(90, 11, 2, 80))
        self.line_TB3_1.setStyleSheet("background: #1DDED8;")
        self.line_TB3_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB3_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB3_1.setObjectName("line_TB3_1")
        # TB3 Settings and Configurations Buton
        self.configure_TB3_Button = QtWidgets.QPushButton(self.options_TB3)
        self.configure_TB3_Button.setGeometry(QtCore.QRect(100, 70, 111, 18))
        self.configure_TB3_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configure_TB3_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                                "color: rgb(22, 22, 22)")
        self.configure_TB3_Button.setObjectName("configure_TB3_Button")
        self.configure_TB3_Button.clicked.connect(self.openTB3Settings)
        # TB3 Logs Button
        self.logs_TB3_Button = QtWidgets.QPushButton(self.options_TB3)
        self.logs_TB3_Button.setGeometry(QtCore.QRect(100, 45, 111, 18))
        self.logs_TB3_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logs_TB3_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                           "color: rgb(22, 22, 22)")
        self.logs_TB3_Button.setObjectName("logs_TB3_Button")
        self.floor_TB3_Show = QtWidgets.QCheckBox(self.options_TB3)
        self.floor_TB3_Show.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.floor_TB3_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.floor_TB3_Show.setStyleSheet("color: white;")
        self.floor_TB3_Show.setObjectName("floor_TB3_Show")
        self.kinect_TB3_Show = QtWidgets.QCheckBox(self.options_TB3)
        self.kinect_TB3_Show.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.kinect_TB3_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kinect_TB3_Show.setStyleSheet("color: white;")
        self.kinect_TB3_Show.setObjectName("kinect_TB3_Show")
        self.gmapp_TB3_Show = QtWidgets.QCheckBox(self.options_TB3)
        self.gmapp_TB3_Show.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.gmapp_TB3_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gmapp_TB3_Show.setStyleSheet("color: white;")
        self.gmapp_TB3_Show.setObjectName("gmapp_TB3_Show")
        self.camera_TB3_Show = QtWidgets.QCheckBox(self.options_TB3)
        self.camera_TB3_Show.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.camera_TB3_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camera_TB3_Show.setStyleSheet("color: white;")
        self.camera_TB3_Show.setObjectName("camera_TB3_Show")
        self.on_TB3_Viewer = QtWidgets.QRadioButton(self.options_TB3)
        self.on_TB3_Viewer.setGeometry(QtCore.QRect(100, 10, 51, 21))
        self.on_TB3_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.on_TB3_Viewer.setObjectName("on_TB3_Viewer")
        self.off_TB3_Viewer = QtWidgets.QRadioButton(self.options_TB3)
        self.off_TB3_Viewer.setGeometry(QtCore.QRect(160, 10, 51, 21))
        self.off_TB3_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.off_TB3_Viewer.setObjectName("off_TB3_Viewer")
        self.line_TB3_2 = QtWidgets.QFrame(self.options_TB3)
        self.line_TB3_2.setGeometry(QtCore.QRect(100, 35, 110, 1))
        self.line_TB3_2.setStyleSheet("")
        self.line_TB3_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_TB3_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB3_2.setObjectName("line_TB3_2")
        self.reload_TB3 = QtWidgets.QPushButton(self.options_TB3)
        self.reload_TB3.setGeometry(QtCore.QRect(114, 162, 90, 20))
        self.reload_TB3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reload_TB3.setStyleSheet("color: rgb(193, 69, 69);\n"
                                      "font: 75 9pt \"Clean\";\n"
                                      "background: rgba(25, 27, 33, 0.2);")
        self.reload_TB3.setObjectName("reload_TB3")
        self.line_TB3_4 = QtWidgets.QFrame(self.options_TB3)
        self.line_TB3_4.setGeometry(QtCore.QRect(209, 160, 2, 25))
        self.line_TB3_4.setStyleSheet("background: #313640;")
        self.line_TB3_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB3_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB3_4.setObjectName("line_TB3_4")
        self.line_TB3_3 = QtWidgets.QFrame(self.options_TB3)
        self.line_TB3_3.setGeometry(QtCore.QRect(10, 160, 2, 25))
        self.line_TB3_3.setStyleSheet("background: #313640;")
        self.line_TB3_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB3_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB3_3.setObjectName("line_TB3_3")
        self.reset_TB3 = QtWidgets.QPushButton(self.options_TB3)
        self.reset_TB3.setGeometry(QtCore.QRect(15, 162, 90, 20))
        self.reset_TB3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_TB3.setStyleSheet("color: rgb(193, 69, 69);\n"
                                     "font: 75 9pt \"Clean\";\n"
                                     "background: rgba(25, 27, 33, 0.2);")
        self.reset_TB3.setObjectName("reset_TB3")
        self.valuesTB3Frame = QtWidgets.QFrame(self.options_TB3)
        self.valuesTB3Frame.setGeometry(QtCore.QRect(10, 100, 201, 51))
        self.valuesTB3Frame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.valuesTB3Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.valuesTB3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.valuesTB3Frame.setObjectName("valuesTB3Frame")
        self.x_TB3_Value = QtWidgets.QLCDNumber(self.valuesTB3Frame)
        self.x_TB3_Value.setGeometry(QtCore.QRect(30, 7, 31, 16))
        self.x_TB3_Value.setObjectName("x_TB3_Value")
        self.x_TB3_Label = QtWidgets.QLabel(self.valuesTB3Frame)
        self.x_TB3_Label.setGeometry(QtCore.QRect(10, 7, 16, 16))
        self.x_TB3_Label.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);")
        self.x_TB3_Label.setObjectName("x_TB3_Label")
        self.y_TB3_Label = QtWidgets.QLabel(self.valuesTB3Frame)
        self.y_TB3_Label.setGeometry(QtCore.QRect(10, 31, 16, 16))
        self.y_TB3_Label.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);")
        self.y_TB3_Label.setObjectName("y_TB3_Label")
        self.y_TB3_Value = QtWidgets.QLCDNumber(self.valuesTB3Frame)
        self.y_TB3_Value.setGeometry(QtCore.QRect(30, 31, 31, 16))
        self.y_TB3_Value.setObjectName("y_TB3_Value")
        self.velocity_TB3_Label = QtWidgets.QLabel(self.valuesTB3Frame)
        self.velocity_TB3_Label.setGeometry(QtCore.QRect(75, 7, 61, 16))
        self.velocity_TB3_Label.setStyleSheet("background: transparent;\n"
                                              "color: rgb(206, 255, 188);")
        self.velocity_TB3_Label.setObjectName("velocity_TB3_Label")
        self.linear_TB3_Value = QtWidgets.QLCDNumber(self.valuesTB3Frame)
        self.linear_TB3_Value.setGeometry(QtCore.QRect(130, 7, 31, 16))
        self.linear_TB3_Value.setObjectName("linear_TB3_Value")
        self.battery_TB3_Label = QtWidgets.QLabel(self.valuesTB3Frame)
        self.battery_TB3_Label.setGeometry(QtCore.QRect(75, 31, 61, 16))
        self.battery_TB3_Label.setStyleSheet("background: transparent;\n"
                                             "color: rgb(206, 255, 188);")
        self.battery_TB3_Label.setObjectName("battery_TB3_Label")
        self.turtleBat_TB3_Value = QtWidgets.QLCDNumber(self.valuesTB3Frame)
        self.turtleBat_TB3_Value.setGeometry(QtCore.QRect(130, 30, 31, 16))
        self.turtleBat_TB3_Value.setObjectName("turtleBat_TB3_Value")
        self.noteBat_TB3_Value = QtWidgets.QLCDNumber(self.valuesTB3Frame)
        self.noteBat_TB3_Value.setGeometry(QtCore.QRect(165, 30, 31, 16))
        self.noteBat_TB3_Value.setObjectName("noteBat_TB3_Value")
        self.angular_TB3_Value = QtWidgets.QLCDNumber(self.valuesTB3Frame)
        self.angular_TB3_Value.setGeometry(QtCore.QRect(165, 7, 31, 16))
        self.angular_TB3_Value.setObjectName("angular_TB3_Value")
        self.viewer_TB3 = QtWidgets.QTabWidget(self.robot_TB3)
        self.viewer_TB3.setGeometry(QtCore.QRect(0, 20, 221, 198))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.viewer_TB3.setFont(font)
        self.viewer_TB3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewer_TB3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.viewer_TB3.setStyleSheet("color: white;")
        self.viewer_TB3.setTabPosition(QtWidgets.QTabWidget.West)
        self.viewer_TB3.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.viewer_TB3.setElideMode(QtCore.Qt.ElideLeft)
        self.viewer_TB3.setObjectName("viewer_TB3")
        self.kinnect_TB3_Screen = QtWidgets.QWidget()
        self.kinnect_TB3_Screen.setObjectName("kinnect_TB3_Screen")
        self.viewer_TB3.addTab(self.kinnect_TB3_Screen, "")
        self.gmapp_TB3_Screen = QtWidgets.QWidget()
        self.gmapp_TB3_Screen.setObjectName("gmapp_TB3_Screen")
        self.viewer_TB3.addTab(self.gmapp_TB3_Screen, "")
        self.floor_TB3_Screen = QtWidgets.QWidget()
        self.floor_TB3_Screen.setObjectName("floor_TB3_Screen")
        self.viewer_TB3.addTab(self.floor_TB3_Screen, "")
        self.camera_TB3_Screen = QtWidgets.QWidget()
        self.camera_TB3_Screen.setObjectName("camera_TB3_Screen")
        self.viewer_TB3.addTab(self.camera_TB3_Screen, "")
        self.robot_TB4 = QtWidgets.QGroupBox(self.mainWindowBase)
        self.robot_TB4.setGeometry(QtCore.QRect(610, 235, 439, 219))
        self.robot_TB4.setStyleSheet("\n"
                                     "color: rgb(206, 255, 188);")
        self.robot_TB4.setObjectName("robot_TB4")
        self.robot_TB4.setHidden(True)
        self.options_TB4 = QtWidgets.QFrame(self.robot_TB4)
        self.options_TB4.setGeometry(QtCore.QRect(215, 21, 221, 196))
        self.options_TB4.setStyleSheet("")
        self.options_TB4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_TB4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_TB4.setObjectName("options_TB4")
        self.line_TB4_1 = QtWidgets.QFrame(self.options_TB4)
        self.line_TB4_1.setGeometry(QtCore.QRect(90, 11, 2, 80))
        self.line_TB4_1.setStyleSheet("background: #1DDED8;")
        self.line_TB4_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB4_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB4_1.setObjectName("line_TB4_1")
        # TB4 Settings and Configurations Button
        self.configure_TB4_Button = QtWidgets.QPushButton(self.options_TB4)
        self.configure_TB4_Button.setGeometry(QtCore.QRect(100, 70, 111, 18))
        self.configure_TB4_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configure_TB4_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                                "color: rgb(22, 22, 22)")
        self.configure_TB4_Button.setObjectName("configure_TB4_Button")
        self.configure_TB4_Button.clicked.connect(self.openTB4Settings)
        # TB4 Logs Button
        self.logs_TB4_Button = QtWidgets.QPushButton(self.options_TB4)
        self.logs_TB4_Button.setGeometry(QtCore.QRect(100, 45, 111, 18))
        self.logs_TB4_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logs_TB4_Button.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                           "color: rgb(22, 22, 22)")
        self.logs_TB4_Button.setObjectName("logs_TB4_Button")
        self.floor_TB4_Show = QtWidgets.QCheckBox(self.options_TB4)
        self.floor_TB4_Show.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.floor_TB4_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.floor_TB4_Show.setStyleSheet("color: white;")
        self.floor_TB4_Show.setObjectName("floor_TB4_Show")
        self.kinect_TB4_Show = QtWidgets.QCheckBox(self.options_TB4)
        self.kinect_TB4_Show.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.kinect_TB4_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kinect_TB4_Show.setStyleSheet("color: white;")
        self.kinect_TB4_Show.setObjectName("kinect_TB4_Show")
        self.gmapp_TB4_Show = QtWidgets.QCheckBox(self.options_TB4)
        self.gmapp_TB4_Show.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.gmapp_TB4_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gmapp_TB4_Show.setStyleSheet("color: white;")
        self.gmapp_TB4_Show.setObjectName("gmapp_TB4_Show")
        self.camera_TB4_Show = QtWidgets.QCheckBox(self.options_TB4)
        self.camera_TB4_Show.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.camera_TB4_Show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camera_TB4_Show.setStyleSheet("color: white;")
        self.camera_TB4_Show.setObjectName("camera_TB4_Show")
        self.on_TB4_Viewer = QtWidgets.QRadioButton(self.options_TB4)
        self.on_TB4_Viewer.setGeometry(QtCore.QRect(100, 10, 51, 21))
        self.on_TB4_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.on_TB4_Viewer.setObjectName("on_TB4_Viewer")
        self.off_TB4_Viewer = QtWidgets.QRadioButton(self.options_TB4)
        self.off_TB4_Viewer.setGeometry(QtCore.QRect(160, 10, 51, 21))
        self.off_TB4_Viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.off_TB4_Viewer.setObjectName("off_TB4_Viewer")
        self.line_TB4_2 = QtWidgets.QFrame(self.options_TB4)
        self.line_TB4_2.setGeometry(QtCore.QRect(100, 35, 110, 1))
        self.line_TB4_2.setStyleSheet("")
        self.line_TB4_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_TB4_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB4_2.setObjectName("line_TB4_2")
        self.reload_TB4 = QtWidgets.QPushButton(self.options_TB4)
        self.reload_TB4.setGeometry(QtCore.QRect(114, 162, 90, 20))
        self.reload_TB4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reload_TB4.setStyleSheet("color: rgb(193, 69, 69);\n"
                                      "font: 75 9pt \"Clean\";\n"
                                      "background: rgba(25, 27, 33, 0.2);")
        self.reload_TB4.setObjectName("reload_TB4")
        self.line_TB4_4 = QtWidgets.QFrame(self.options_TB4)
        self.line_TB4_4.setGeometry(QtCore.QRect(209, 160, 2, 25))
        self.line_TB4_4.setStyleSheet("background: #313640;")
        self.line_TB4_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB4_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB4_4.setObjectName("line_TB4_4")
        self.line_TB4_5 = QtWidgets.QFrame(self.options_TB4)
        self.line_TB4_5.setGeometry(QtCore.QRect(10, 160, 2, 25))
        self.line_TB4_5.setStyleSheet("background: #313640;")
        self.line_TB4_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_TB4_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_TB4_5.setObjectName("line_TB4_5")
        self.reset_TB4 = QtWidgets.QPushButton(self.options_TB4)
        self.reset_TB4.setGeometry(QtCore.QRect(15, 162, 90, 20))
        self.reset_TB4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_TB4.setStyleSheet("color: rgb(193, 69, 69);\n"
                                     "font: 75 9pt \"Clean\";\n"
                                     "background: rgba(25, 27, 33, 0.2);")
        self.reset_TB4.setObjectName("reset_TB4")
        self.valuesTB4Frame = QtWidgets.QFrame(self.options_TB4)
        self.valuesTB4Frame.setGeometry(QtCore.QRect(10, 100, 201, 51))
        self.valuesTB4Frame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.valuesTB4Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.valuesTB4Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.valuesTB4Frame.setObjectName("valuesTB4Frame")
        self.x_TB4_Value = QtWidgets.QLCDNumber(self.valuesTB4Frame)
        self.x_TB4_Value.setGeometry(QtCore.QRect(30, 7, 31, 16))
        self.x_TB4_Value.setObjectName("x_TB4_Value")
        self.x_TB4_Label = QtWidgets.QLabel(self.valuesTB4Frame)
        self.x_TB4_Label.setGeometry(QtCore.QRect(10, 7, 16, 16))
        self.x_TB4_Label.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);")
        self.x_TB4_Label.setObjectName("x_TB4_Label")
        self.y_TB4_Label = QtWidgets.QLabel(self.valuesTB4Frame)
        self.y_TB4_Label.setGeometry(QtCore.QRect(10, 31, 16, 16))
        self.y_TB4_Label.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);")
        self.y_TB4_Label.setObjectName("y_TB4_Label")
        self.y_TB4_Value = QtWidgets.QLCDNumber(self.valuesTB4Frame)
        self.y_TB4_Value.setGeometry(QtCore.QRect(30, 31, 31, 16))
        self.y_TB4_Value.setObjectName("y_TB4_Value")
        self.velocity_TB4_Label = QtWidgets.QLabel(self.valuesTB4Frame)
        self.velocity_TB4_Label.setGeometry(QtCore.QRect(75, 7, 61, 16))
        self.velocity_TB4_Label.setStyleSheet("background: transparent;\n"
                                              "color: rgb(206, 255, 188);")
        self.velocity_TB4_Label.setObjectName("velocity_TB4_Label")
        self.linear_TB4_Value = QtWidgets.QLCDNumber(self.valuesTB4Frame)
        self.linear_TB4_Value.setGeometry(QtCore.QRect(130, 7, 31, 16))
        self.linear_TB4_Value.setObjectName("linear_TB4_Value")
        self.battery_TB4_Label = QtWidgets.QLabel(self.valuesTB4Frame)
        self.battery_TB4_Label.setGeometry(QtCore.QRect(75, 31, 61, 16))
        self.battery_TB4_Label.setStyleSheet("background: transparent;\n"
                                             "color: rgb(206, 255, 188);")
        self.battery_TB4_Label.setObjectName("battery_TB4_Label")
        self.turtleBat_TB4_Value = QtWidgets.QLCDNumber(self.valuesTB4Frame)
        self.turtleBat_TB4_Value.setGeometry(QtCore.QRect(130, 30, 31, 16))
        self.turtleBat_TB4_Value.setObjectName("turtleBat_TB4_Value")
        self.noteBat_TB4_Value = QtWidgets.QLCDNumber(self.valuesTB4Frame)
        self.noteBat_TB4_Value.setGeometry(QtCore.QRect(165, 30, 31, 16))
        self.noteBat_TB4_Value.setObjectName("noteBat_TB4_Value")
        self.angular_TB4_Value = QtWidgets.QLCDNumber(self.valuesTB4Frame)
        self.angular_TB4_Value.setGeometry(QtCore.QRect(165, 7, 31, 16))
        self.angular_TB4_Value.setObjectName("angular_TB4_Value")
        self.viewer_TB4 = QtWidgets.QTabWidget(self.robot_TB4)
        self.viewer_TB4.setGeometry(QtCore.QRect(0, 20, 221, 198))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.viewer_TB4.setFont(font)
        self.viewer_TB4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewer_TB4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.viewer_TB4.setStyleSheet("color: white;")
        self.viewer_TB4.setTabPosition(QtWidgets.QTabWidget.West)
        self.viewer_TB4.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.viewer_TB4.setElideMode(QtCore.Qt.ElideLeft)
        self.viewer_TB4.setObjectName("viewer_TB4")
        self.kinnect_TB4_Screen = QtWidgets.QWidget()
        self.kinnect_TB4_Screen.setObjectName("kinnect_TB4_Screen")
        self.viewer_TB4.addTab(self.kinnect_TB4_Screen, "")
        self.gmapp_TB4_Screen = QtWidgets.QWidget()
        self.gmapp_TB4_Screen.setObjectName("gmapp_TB4_Screen")
        self.viewer_TB4.addTab(self.gmapp_TB4_Screen, "")
        self.floor_TB4_Screen = QtWidgets.QWidget()
        self.floor_TB4_Screen.setObjectName("floor_TB4_Screen")
        self.viewer_TB4.addTab(self.floor_TB4_Screen, "")
        self.camera_TB4_Screen = QtWidgets.QWidget()
        self.camera_TB4_Screen.setObjectName("camera_TB4_Screen")
        self.viewer_TB4.addTab(self.camera_TB4_Screen, "")
        self.robot_TB1.raise_()
        self.menuFrame.raise_()
        self.menu_Logo.raise_()
        self.menu_Line.raise_()
        self.qrcode_App_Button.raise_()
        self.data_Button.raise_()
        self.config_Button.raise_()
        self.docs_Button.raise_()
        self.about_Button.raise_()
        self.viewer_Superior_Line.raise_()
        self.inferior_Line_Base.raise_()
        self.lateral_Line_Base.raise_()
        self.robot_Viewer_Frame.raise_()
        self.terminalWidget.raise_()
        self.robotViewerBase.raise_()
        self.robot_Selection_Frame.raise_()
        self.robotSelectionBase.raise_()
        self.selection_Superior_Line.raise_()
        self.robot_TB2.raise_()
        self.label.raise_()
        self.robot_TB3.raise_()
        self.robot_TB4.raise_()
        MainWindow.setCentralWidget(self.mainWindowBase)
        self.retranslateUi(MainWindow)
        self.viewer_TB1.setCurrentIndex(0)
        self.viewer_TB2.setCurrentIndex(3)
        self.viewer_TB3.setCurrentIndex(3)
        self.viewer_TB4.setCurrentIndex(3)
        # Shows the Robots Viewers and Change the Button State Style
        self.robot_TB1_Viewer.clicked['bool'].connect(self.robot_TB1.setVisible)
        self.robot_TB2_Viewer.clicked['bool'].connect(self.robot_TB2.setVisible)
        self.robot_TB3_Viewer.clicked['bool'].connect(self.robot_TB3.setVisible)
        self.robot_TB4_Viewer.clicked['bool'].connect(self.robot_TB4.setVisible)
        self.robot_TB1_Viewer.toggled['bool'].connect(lambda: self.buttonStatusChange(robot='tb1'))
        self.robot_TB1_Viewer.toggled['bool'].connect(lambda: self.robotsTerminals(robot='tb1'))
        self.robot_TB2_Viewer.toggled['bool'].connect(lambda: self.buttonStatusChange(robot='tb2'))
        self.robot_TB2_Viewer.toggled['bool'].connect(lambda: self.robotsTerminals(robot='tb2') )
        self.robot_TB3_Viewer.toggled['bool'].connect(lambda: self.buttonStatusChange(robot='tb3'))
        self.robot_TB3_Viewer.toggled['bool'].connect(lambda: self.robotsTerminals(robot='tb3'))
        self.robot_TB4_Viewer.toggled['bool'].connect(lambda: self.buttonStatusChange(robot='tb4'))
        self.robot_TB4_Viewer.toggled['bool'].connect(lambda: self.robotsTerminals(robot='tb4'))
        # Configuration Robot Selection
        self.robot_TB1_Selection.clicked.connect(lambda: self.setExperiment(robot='1', set='None'))
        self.robot_TB2_Selection.clicked.connect(lambda: self.setExperiment(robot='2', set='None'))
        self.robot_TB3_Selection.clicked.connect(lambda: self.setExperiment(robot='3', set='None'))
        self.robot_TB4_Selection.clicked.connect(lambda: self.setExperiment(robot='4', set='None'))
        # TB1 Reset Screen
        self.reset_TB1.clicked.connect(lambda: self.gmapp_TB1_Show.setChecked(False))
        self.reset_TB1.clicked.connect(lambda: self.floor_TB1_Show.setChecked(False))
        self.reset_TB1.clicked.connect(lambda: self.kinect_TB1_Show.setChecked(False))
        self.reset_TB1.clicked.connect(lambda: self.camera_TB1_Show.setChecked(False))
        self.reset_TB1.clicked.connect(lambda: self.linear_TB1_Value.display(0))
        self.reset_TB1.clicked.connect(lambda: self.angular_TB1_Value.display(0))
        self.reset_TB1.clicked.connect(lambda: self.x_TB1_Value.display(0))
        self.reset_TB1.clicked.connect(lambda: self.y_TB1_Value.display(0))
        self.reset_TB1.clicked.connect(lambda: self.turtleBat_TB1_Value.display(0))
        self.reset_TB1.clicked.connect(lambda: self.noteBat_TB1_Value.display(0))
        # TB2 Reset Screen
        self.reset_TB2.clicked.connect(lambda: self.gmapp_TB2_Show.setChecked(False))
        self.reset_TB2.clicked.connect(lambda: self.floor_TB2_Show.setChecked(False))
        self.reset_TB2.clicked.connect(lambda: self.kinect_TB2_Show.setChecked(False))
        self.reset_TB2.clicked.connect(lambda: self.camera_TB2_Show.setChecked(False))
        self.reset_TB2.clicked.connect(lambda: self.linear_TB2_Value.display(0))
        self.reset_TB2.clicked.connect(lambda: self.angular_TB2_Value.display(0))
        self.reset_TB2.clicked.connect(lambda: self.x_TB2_Value.display(0))
        self.reset_TB2.clicked.connect(lambda: self.y_TB2_Value.display(0))
        self.reset_TB2.clicked.connect(lambda: self.turtleBat_TB2_Value.display(0))
        self.reset_TB2.clicked.connect(lambda: self.noteBat_TB2_Value.display(0))
        # TB3 Reset Screen
        self.reset_TB3.clicked.connect(lambda: self.gmapp_TB3_Show.setChecked(False))
        self.reset_TB3.clicked.connect(lambda: self.floor_TB3_Show.setChecked(False))
        self.reset_TB3.clicked.connect(lambda: self.kinect_TB3_Show.setChecked(False))
        self.reset_TB3.clicked.connect(lambda: self.camera_TB3_Show.setChecked(False))
        self.reset_TB3.clicked.connect(lambda: self.linear_TB3_Value.display(0))
        self.reset_TB3.clicked.connect(lambda: self.angular_TB3_Value.display(0))
        self.reset_TB3.clicked.connect(lambda: self.x_TB3_Value.display(0))
        self.reset_TB3.clicked.connect(lambda: self.y_TB3_Value.display(0))
        self.reset_TB3.clicked.connect(lambda: self.turtleBat_TB3_Value.display(0))
        self.reset_TB3.clicked.connect(lambda: self.noteBat_TB3_Value.display(0))
        # TB4 Reset Screen
        self.reset_TB4.clicked.connect(lambda: self.gmapp_TB4_Show.setChecked(False))
        self.reset_TB4.clicked.connect(lambda: self.floor_TB4_Show.setChecked(False))
        self.reset_TB4.clicked.connect(lambda: self.kinect_TB4_Show.setChecked(False))
        self.reset_TB4.clicked.connect(lambda: self.camera_TB4_Show.setChecked(False))
        self.reset_TB4.clicked.connect(lambda: self.linear_TB4_Value.display(0))
        self.reset_TB4.clicked.connect(lambda: self.angular_TB4_Value.display(0))
        self.reset_TB4.clicked.connect(lambda: self.x_TB4_Value.display(0))
        self.reset_TB4.clicked.connect(lambda: self.y_TB4_Value.display(0))
        self.reset_TB4.clicked.connect(lambda: self.turtleBat_TB4_Value.display(0))
        self.reset_TB4.clicked.connect(lambda: self.noteBat_TB4_Value.display(0))
        # Configuration Reset Button
        
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_TB1_Selection.setAutoExclusive(False))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_TB1_Selection.setChecked(False))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_TB2_Selection.setAutoExclusive(False))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_TB2_Selection.setChecked(False))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_TB3_Selection.setAutoExclusive(False))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_TB3_Selection.setChecked(False))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_TB4_Selection.setAutoExclusive(False))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_TB4_Selection.setChecked(False))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_Selection_Type.setCurrentIndex(0))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_Selection_Role.setCurrentIndex(0))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_Selection_Task.setCurrentIndex(0))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_Selection_Behavior.setCurrentIndex(0))
        self.reset_Selection_Values.clicked.connect(lambda: self.robot_Selection_Experiment.setCurrentIndex(0))
        self.qrcode_App_Button.clicked.connect(MainWindow.show)
        self.data_Button.clicked.connect(MainWindow.show)
        self.logs_TB4_Button.clicked.connect(self.logs_TB4_Button.show)
        self.configure_TB4_Button.clicked.connect(self.configure_TB4_Button.show)
        self.logs_TB3_Button.clicked.connect(self.logs_TB3_Button.show)
        self.configure_TB3_Button.clicked['bool'].connect(self.configure_TB3_Button.show)
        self.logs_TB1_Button.clicked.connect(self.logs_TB1_Button.show)
        self.configure_TB1_Button.clicked.connect(self.configure_TB1_Button.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """ This function is responsible to Translate the Names
        and Place the Button Tips Informations
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ROC - Robot Operational Controller"))
        self.qrcode_App_Button.setToolTip(_translate("MainWindow", "Opens the QR Code Reader"))
        self.qrcode_App_Button.setText(_translate("MainWindow", "QR App"))
        self.data_Button.setToolTip(_translate("MainWindow", "Opens the Data Dashboard"))
        self.data_Button.setText(_translate("MainWindow", "Data"))
        self.config_Button.setToolTip(_translate("MainWindow", "Configure the ROC"))
        self.config_Button.setText(_translate("MainWindow", "Options"))
        self.docs_Button.setToolTip(_translate("MainWindow", "Go to the Documentation Website"))
        self.docs_Button.setText(_translate("MainWindow", "Docs"))
        self.about_Button.setToolTip(_translate("MainWindow", "Contact and About"))
        self.about_Button.setText(_translate("MainWindow", "About"))
        self.robot_Viewer_Label.setText(_translate("MainWindow", "ROBOT VIEWER"))
        self.terminalWidget.setTabText(self.terminalWidget.indexOf(self.urxvtWidget), _translate("MainWindow", "urxvt"))
        self.robot_TB1_Status.setToolTip(_translate("MainWindow", "Ping and Show Robot 1 Status (GREY = DESABLED, BLACK = OFF, LIGHT = ON, RED = INACTIVE)"))
        self.robot_TB1_Status.setText(_translate("MainWindow", "TB1 STATUS"))
        self.robot_TB1_Viewer.setToolTip(_translate("MainWindow", "Open Robot 1 Viewer"))
        self.robot_TB1_Viewer.setText(_translate("MainWindow", "ROBOT 1"))
        self.robot_TB2_Viewer.setToolTip(_translate("MainWindow", "Open Robot 2 Viewer"))
        self.robot_TB2_Viewer.setText(_translate("MainWindow", "ROBOT 2"))
        self.robot_TB3_Viewer.setToolTip(_translate("MainWindow", "Open Robot 3 Viewer"))
        self.robot_TB3_Viewer.setText(_translate("MainWindow", "ROBOT 3"))
        self.robot_TB4_Viewer.setToolTip(_translate("MainWindow", "Open Robot 4 Viewer"))
        self.robot_TB4_Viewer.setText(_translate("MainWindow", "ROBOT 4"))
        self.robot_TB2_Status.setToolTip(_translate("MainWindow", "Ping and Show Robot 2 Status (GREY = DESABLED, BLACK = OFF, LIGHT = ON, RED = INACTIVE)"))
        self.robot_TB2_Status.setText(_translate("MainWindow", "TB2 STATUS"))
        self.robot_TB3_Status.setToolTip(_translate("MainWindow", "Ping and Show Robot 3 Status (GREY = DESABLED, BLACK = OFF, LIGHT = ON, RED = INACTIVE)"))
        self.robot_TB3_Status.setText(_translate("MainWindow", "TB3 STATUS"))
        self.robot_TB4_Status.setToolTip(_translate("MainWindow", "Ping and Show Robot 4 Status (GREY = DESABLED, BLACK = OFF, LIGHT = ON, RED = INACTIVE)"))
        self.robot_TB4_Status.setText(_translate("MainWindow", "TB4 STATUS"))
        self.robot_TB1.setTitle(_translate("MainWindow", "                                                Robot 1  (TB1)"))
        self.configure_TB1_Button.setToolTip(_translate("MainWindow", "Opens the Settings for Robot 1 (TB1)"))
        self.configure_TB1_Button.setText(_translate("MainWindow", "Settings"))
        self.logs_TB1_Button.setToolTip(_translate("MainWindow", "Open the Logs for Robot 1 (TB1)"))
        self.logs_TB1_Button.setText(_translate("MainWindow", "Logs"))
        self.floor_TB1_Show.setToolTip(_translate("MainWindow", "Shows the Floor Map"))
        self.floor_TB1_Show.setText(_translate("MainWindow", "FLOOR"))
        self.kinect_TB1_Show.setToolTip(_translate("MainWindow", "Shows the Kinect Camera"))
        self.kinect_TB1_Show.setText(_translate("MainWindow", "KINECT"))
        self.gmapp_TB1_Show.setToolTip(_translate("MainWindow", "Shows the GMAPP"))
        self.gmapp_TB1_Show.setText(_translate("MainWindow", "GMAPP"))
        self.camera_TB1_Show.setToolTip(_translate("MainWindow", "Shows the Notebook Camera"))
        self.camera_TB1_Show.setText(_translate("MainWindow", "CAMERA"))
        self.on_TB1_Viewer.setToolTip(_translate("MainWindow", "Turn Viewer On"))
        self.on_TB1_Viewer.setText(_translate("MainWindow", "ON"))
        self.off_TB1_Viewer.setToolTip(_translate("MainWindow", "Turn Viewer Off"))
        self.off_TB1_Viewer.setText(_translate("MainWindow", "OFF"))
        self.reload_TB1.setToolTip(_translate("MainWindow", "Reload the Viewer"))
        self.reload_TB1.setText(_translate("MainWindow", "RELOAD"))
        self.reset_TB1.setToolTip(_translate("MainWindow", "Reset the Viewer"))
        self.reset_TB1.setText(_translate("MainWindow", "RESET"))
        self.valuesTB1Frame.setToolTip(_translate("MainWindow", "Shows Robot 1 (TB1) Data"))
        self.x_TB1_Label.setText(_translate("MainWindow", "X:"))
        self.y_TB1_Label.setText(_translate("MainWindow", "Y:"))
        self.velocity_TB1_Label.setText(_translate("MainWindow", "Velocity:"))
        self.battery_TB1_Label.setText(_translate("MainWindow", "Battery:"))
        self.kinnect_TB1_Screen.setToolTip(_translate("MainWindow", "Image from the Kinnect"))
        self.viewer_TB1.setTabText(self.viewer_TB1.indexOf(self.kinnect_TB1_Screen), _translate("MainWindow", "ROBOT"))
        self.viewer_TB1.setTabText(self.viewer_TB1.indexOf(self.gmapp_TB1_Screen), _translate("MainWindow", "GMAPP"))
        self.viewer_TB1.setTabText(self.viewer_TB1.indexOf(self.floor_TB1_Screen), _translate("MainWindow", "FLOOR"))
        self.viewer_TB1.setTabText(self.viewer_TB1.indexOf(self.camera_TB1_Screen), _translate("MainWindow", "CAMERA"))
        self.robot_Selection_Label.setText(_translate("MainWindow", "CONFIGURATIONS"))
        self.robot_Selection_TypeLabel.setText(_translate("MainWindow", "ROBOT TYPE:"))
        self.robot_Selection_Type.setToolTip(_translate("MainWindow", "Select the Robot Type"))
        self.robot_Selection_Type.setItemText(0, _translate("MainWindow", "NONE"))
        self.robot_Selection_Type.setItemText(1, _translate("MainWindow", "TURTLEBOT"))
        self.robot_Selection_Type.setItemText(2, _translate("MainWindow", "DRONE"))
        self.robot_Selection_Role.setToolTip(_translate("MainWindow", "Select the Robot Role"))
        self.robot_Selection_Role.setItemText(0, _translate("MainWindow", "NONE"))
        self.robot_Selection_Role.setItemText(1, _translate("MainWindow", "ROLE 1"))
        self.robot_Selection_Role.setItemText(2, _translate("MainWindow", "ROLE 2"))
        self.robot_Selection_RoleLabel.setText(_translate("MainWindow", "ROBOT ROLE:"))
        self.robot_Selection_TaskLabel.setText(_translate("MainWindow", "ROBOT TASK:"))
        self.robot_Selection_Task.setToolTip(_translate("MainWindow", "Select the Robot Task"))
        self.robot_Selection_Task.setItemText(0, _translate("MainWindow", "NONE"))
        self.robot_Selection_Task.setItemText(1, _translate("MainWindow", "TASK 1"))
        self.robot_Selection_Task.setItemText(2, _translate("MainWindow", "TASK 2"))
        self.robot_Selection_BehaviorLabel.setText(_translate("MainWindow", "BEHAVIOR:"))
        self.robot_Selection_Behavior.setToolTip(_translate("MainWindow", "Select an Behavior"))
        self.robot_Selection_Behavior.setItemText(0, _translate("MainWindow", "NONE"))
        self.robot_Selection_Behavior.setItemText(1, _translate("MainWindow", "TASK 1"))
        self.robot_Selection_Behavior.setItemText(2, _translate("MainWindow", "TASK 2"))
        self.robot_Selection_Experiment.setToolTip(_translate("MainWindow", "Select a Experiment"))
        self.robot_Selection_Experiment.setItemText(0, _translate("MainWindow", "NONE"))
        self.robot_Selection_Experiment.setItemText(1, _translate("MainWindow", "EXP. 1"))
        self.robot_Selection_Experiment.setItemText(2, _translate("MainWindow", "EXP. 2"))
        self.robot_Selection_ExpLabel.setText(_translate("MainWindow", "EXPERIMENT:"))
        self.set_Selection_Values.setToolTip(_translate("MainWindow", "Set the Values Selected"))
        self.set_Selection_Values.setText(_translate("MainWindow", "SET"))
        self.reset_Selection_Values.setToolTip(_translate("MainWindow", "Reset the Values Selected"))
        self.reset_Selection_Values.setText(_translate("MainWindow", "R"))
        self.robot_TB1_Selection.setToolTip(_translate("MainWindow", "Select Robot 1"))
        self.robot_TB1_Selection.setText(_translate("MainWindow", "1"))
        self.robot_TB2_Selection.setToolTip(_translate("MainWindow", "Select Robot 2"))
        self.robot_TB2_Selection.setText(_translate("MainWindow", "2"))
        self.robot_TB4_Selection.setToolTip(_translate("MainWindow", "Select Robot 4"))
        self.robot_TB4_Selection.setText(_translate("MainWindow", "4"))
        self.robot_TB3_Selection.setToolTip(_translate("MainWindow", "Select Robot 3"))
        self.robot_TB3_Selection.setText(_translate("MainWindow", "3"))
        self.run_Selection_Values.setToolTip(_translate("MainWindow", "Run / Start the Experiment"))
        self.run_Selection_Values.setText(_translate("MainWindow", "RUN"))
        self.down_Selection_Values.setToolTip(_translate("MainWindow", "Shut Down the Robot"))
        self.down_Selection_Values.setText(_translate("MainWindow", "D"))
        self.robot_TB2.setTitle(_translate("MainWindow", "                                                 Robot 2  (TB2)"))
        self.configure_TB2_Button.setText(_translate("MainWindow", "Settings"))
        self.logs_TB2_Button.setText(_translate("MainWindow", "Logs"))
        self.floor_TB2_Show.setText(_translate("MainWindow", "FLOOR"))
        self.kinect_TB2_Show.setText(_translate("MainWindow", "KINECT"))
        self.gmapp_TB2_Show.setText(_translate("MainWindow", "GMAPP"))
        self.camera_TB2_Show.setText(_translate("MainWindow", "CAMERA"))
        self.on_TB2_Viewer.setText(_translate("MainWindow", "ON"))
        self.off_TB2_Viewer.setText(_translate("MainWindow", "OFF"))
        self.reload_TB2.setText(_translate("MainWindow", "RELOAD"))
        self.reset_TB2.setText(_translate("MainWindow", "RESET"))
        self.x_TB2_Label.setText(_translate("MainWindow", "X:"))
        self.y_TB2_Label.setText(_translate("MainWindow", "Y:"))
        self.velocity_TB2_Label.setText(_translate("MainWindow", "Velocity:"))
        self.battery_TB2_Label.setText(_translate("MainWindow", "Battery:"))
        self.kinnect_TB2_Screen.setToolTip(_translate("MainWindow", "Image from the Kinnect"))
        self.viewer_TB2.setTabText(self.viewer_TB2.indexOf(self.kinnect_TB2_Screen), _translate("MainWindow", "ROBOT"))
        self.viewer_TB2.setTabText(self.viewer_TB2.indexOf(self.gmapp_TB2_Screen), _translate("MainWindow", "GMAPP"))
        self.viewer_TB2.setTabText(self.viewer_TB2.indexOf(self.floor_TB2_Screen), _translate("MainWindow", "FLOOR"))
        self.viewer_TB2.setTabText(self.viewer_TB2.indexOf(self.camera_TB2_Screen), _translate("MainWindow", "CAMERA"))
        self.label.setToolTip(_translate("MainWindow", "ROC Version"))
        self.label.setText(_translate("MainWindow", "Alpha v0.1"))
        self.robot_TB3.setTitle(_translate("MainWindow", "                                                Robot 3  (TB3)"))
        self.configure_TB3_Button.setText(_translate("MainWindow", "Settings"))
        self.logs_TB3_Button.setText(_translate("MainWindow", "Logs"))
        self.floor_TB3_Show.setText(_translate("MainWindow", "FLOOR"))
        self.kinect_TB3_Show.setText(_translate("MainWindow", "KINECT"))
        self.gmapp_TB3_Show.setText(_translate("MainWindow", "GMAPP"))
        self.camera_TB3_Show.setText(_translate("MainWindow", "CAMERA"))
        self.on_TB3_Viewer.setText(_translate("MainWindow", "ON"))
        self.off_TB3_Viewer.setText(_translate("MainWindow", "OFF"))
        self.reload_TB3.setText(_translate("MainWindow", "RELOAD"))
        self.reset_TB3.setText(_translate("MainWindow", "RESET"))
        self.x_TB3_Label.setText(_translate("MainWindow", "X:"))
        self.y_TB3_Label.setText(_translate("MainWindow", "Y:"))
        self.velocity_TB3_Label.setText(_translate("MainWindow", "Velocity:"))
        self.battery_TB3_Label.setText(_translate("MainWindow", "Battery:"))
        self.kinnect_TB3_Screen.setToolTip(_translate("MainWindow", "Image from the Kinnect"))
        self.viewer_TB3.setTabText(self.viewer_TB3.indexOf(self.kinnect_TB3_Screen), _translate("MainWindow", "ROBOT"))
        self.viewer_TB3.setTabText(self.viewer_TB3.indexOf(self.gmapp_TB3_Screen), _translate("MainWindow", "GMAPP"))
        self.viewer_TB3.setTabText(self.viewer_TB3.indexOf(self.floor_TB3_Screen), _translate("MainWindow", "FLOOR"))
        self.viewer_TB3.setTabText(self.viewer_TB3.indexOf(self.camera_TB3_Screen), _translate("MainWindow", "CAMERA"))
        self.robot_TB4.setTitle(_translate("MainWindow", "                                                Robot 4  (TB4)"))
        self.configure_TB4_Button.setText(_translate("MainWindow", "Settings"))
        self.logs_TB4_Button.setText(_translate("MainWindow", "Logs"))
        self.floor_TB4_Show.setText(_translate("MainWindow", "FLOOR"))
        self.kinect_TB4_Show.setText(_translate("MainWindow", "KINECT"))
        self.gmapp_TB4_Show.setText(_translate("MainWindow", "GMAPP"))
        self.camera_TB4_Show.setText(_translate("MainWindow", "CAMERA"))
        self.on_TB4_Viewer.setText(_translate("MainWindow", "ON"))
        self.off_TB4_Viewer.setText(_translate("MainWindow", "OFF"))
        self.reload_TB4.setText(_translate("MainWindow", "RELOAD"))
        self.reset_TB4.setText(_translate("MainWindow", "RESET"))
        self.x_TB4_Label.setText(_translate("MainWindow", "X:"))
        self.y_TB4_Label.setText(_translate("MainWindow", "Y:"))
        self.velocity_TB4_Label.setText(_translate("MainWindow", "Velocity:"))
        self.battery_TB4_Label.setText(_translate("MainWindow", "Battery:"))
        self.kinnect_TB4_Screen.setToolTip(_translate("MainWindow", "Image from the Kinnect"))
        self.viewer_TB4.setTabText(self.viewer_TB4.indexOf(self.kinnect_TB4_Screen), _translate("MainWindow", "ROBOT"))
        self.viewer_TB4.setTabText(self.viewer_TB4.indexOf(self.gmapp_TB4_Screen), _translate("MainWindow", "GMAPP"))
        self.viewer_TB4.setTabText(self.viewer_TB4.indexOf(self.floor_TB4_Screen), _translate("MainWindow", "FLOOR"))
        self.viewer_TB4.setTabText(self.viewer_TB4.indexOf(self.camera_TB4_Screen), _translate("MainWindow", "CAMERA"))


class operationSucess(QtWidgets.QWidget):
    """
    Sucess Dialog Button
    """
    def __init__(self, parent=None):
        Error = QtWidgets.QMessageBox()
        Error.setText('Os dados foram salvos com sucesso!')
        Error.setIcon(QtWidgets.QMessageBox.Information)
        Error.setWindowTitle('ROC - Information')
        Error.show()
        Error.exec_()


class operationError(QtWidgets.QWidget):
    """
    Sucess Dialog Button
    """
    def __init__(self, parent=None):
        Error = QtWidgets.QMessageBox()
        Error.setText('Um erro inesperado ocorreu!')
        Error.setIcon(QtWidgets.QMessageBox.Warning)
        Error.setWindowTitle('ROC - Information')
        Error.show()
        Error.exec_()


class InProgress(QtWidgets.QWidget):
    """
    In Progress Dialog Button
    """
    def __init__(self, parent=None):
        Error = QtWidgets.QMessageBox()
        Error.setText('Desculpe, opção em desenvolvimento.')
        Error.setIcon(QtWidgets.QMessageBox.Information)
        Error.setWindowTitle('ROC - Information')
        Error.show()
        Error.exec_()


class embeddedTerminal(QtWidgets.QWidget):
    """
    Starts an Embeddet urxvt-unicode terminal in the ROC

    """
    def __init__(self, parent=None):
        """
        Opens an new urxvt process inside the TabWidget
        on the botton of the application.

        """
        super(embeddedTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.urxvtTerminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.urxvtTerminal)
        # Works also with urxvt:
        self.process.start('urxvt', ['-embed', str(int(self.winId()))])
        self.setGeometry(90, 460, 1160, 125)


class robotOneTerminal(QtWidgets.QWidget):
    """
    Starts an Embeddet urxvt-unicode terminal in the ROC

    """
    def __init__(self, parent=None):
        """
        Opens an new urxvt process inside the TabWidget
        on the botton of the application.

        """
        super(robotOneTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.urxvtTerminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.urxvtTerminal)
        # Works also with urxvt:
        self.process.start('urxvt', ['-embed', str(int(self.winId()))])
        self.setGeometry(90, 460, 1160, 125)

class robotTwoTerminal(QtWidgets.QWidget):
    """
    Starts an Embeddet urxvt-unicode terminal in the ROC

    """
    def __init__(self, parent=None):
        """
        Opens an new urxvt process inside the TabWidget
        on the botton of the application.

        """
        super(robotTwoTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.urxvtTerminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.urxvtTerminal)
        # Works also with urxvt:
        self.process.start('urxvt', ['-embed', str(int(self.winId()))])
        self.setGeometry(90, 460, 1160, 125)


class robotThreeTerminal(QtWidgets.QWidget):
    """
    Starts an Embeddet urxvt-unicode terminal in the ROC

    """
    def __init__(self, parent=None):
        """
        Opens an new urxvt process inside the TabWidget
        on the botton of the application.

        """
        super(robotThreeTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.urxvtTerminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.urxvtTerminal)
        # Works also with urxvt:
        self.process.start('urxvt', ['-embed', str(int(self.winId()))])
        self.setGeometry(90, 460, 1160, 125)


class robotFourTerminal(QtWidgets.QWidget):
    """
    Starts an Embeddet urxvt-unicode terminal in the ROC

    """
    def __init__(self, parent=None):
        """
        Opens an new urxvt process inside the TabWidget
        on the botton of the application.

        """
        super(robotFourTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.urxvtTerminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.urxvtTerminal)
        # Works also with urxvt:
        self.process.start('urxvt', ['-embed', str(int(self.winId()))])
        self.setGeometry(90, 460, 1160, 125)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
