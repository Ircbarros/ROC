# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

# Form implementation generated from reading ui file 'tb1Settings.ui'
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
from PyQt5 import QtCore, QtGui, QtWidgets
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et


class sucessDialog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        sucessDialog = QtWidgets.QMessageBox()
        sucessDialog.setWindowTitle('Settings (TB1)')
        sucessDialog.setText('As modificações foram salvas com sucesso!')
        sucessDialog.setIcon(QtWidgets.QMessageBox.Information)
        sucessDialog.show()
        sucessDialog.exec_()


class Ui_robotOneConfig(object):
    """ Open the TB2 Settings and Configurations Widget"""
    def setupUi(self, robotOneConfig, *args):
        """ TB1 Configuration Widget """
        # Widget Design
        robotOneConfig.setObjectName("robotOneConfig")
        robotOneConfig.resize(340, 426)
        robotOneConfig.setMinimumSize(QtCore.QSize(340, 426))
        robotOneConfig.setMaximumSize(QtCore.QSize(340, 426))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vectors/Conection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        robotOneConfig.setWindowIcon(icon)
        robotOneConfig.setStyleSheet("background: #2A2E37;")
        self.settingsTB1 = QtWidgets.QGroupBox(robotOneConfig)
        self.settingsTB1.setGeometry(QtCore.QRect(5, 20, 326, 180))
        self.settingsTB1.setMinimumSize(QtCore.QSize(320, 140))
        self.settingsTB1.setStyleSheet("color: rgb(14, 172, 186);")
        self.settingsTB1.setObjectName("settingsTB1")
        # TB1_IP Text Edit
        self.ros_TB1_IP = QtWidgets.QLineEdit(self.settingsTB1)
        self.ros_TB1_IP.setGeometry(QtCore.QRect(90, 30, 231, 23))
        self.ros_TB1_IP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: rgb(199, 199, 199);")
        self.ros_TB1_IP.setDragEnabled(False)
        self.ros_TB1_IP.setObjectName("ros_TB1_IP")
        # Master_IP Text Edit
        self.ros_Master_IP = QtWidgets.QLineEdit(self.settingsTB1)
        self.ros_Master_IP.setGeometry(QtCore.QRect(90, 60, 231, 23))
        self.ros_Master_IP.setStyleSheet("color: rgb(199, 199, 199);\n"
                                         "background: rgba(29, 222, 216, 0.1);")
        self.ros_Master_IP.setObjectName("ros_Master_IP")
        # TB1 Hostname Text Edit
        self.ros_TB1_Hostname = QtWidgets.QLineEdit(self.settingsTB1)
        self.ros_TB1_Hostname.setGeometry(QtCore.QRect(90, 118, 231, 23))
        self.ros_TB1_Hostname.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                            "color: rgb(199, 199, 199);")
        self.ros_TB1_Hostname.setObjectName("ros_TB1_Hostname")
        # Namespace Text Edit
        self.ros_TB1_Namespace = QtWidgets.QLineEdit(self.settingsTB1)
        self.ros_TB1_Namespace.setGeometry(QtCore.QRect(90, 148, 231, 23))
        self.ros_TB1_Namespace.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                             "color: rgb(199, 199, 199);")
        self.ros_TB1_Namespace.setObjectName("ros_TB1_Namespace")
        # Master_URI Text Edit
        self.ros_Master_URI = QtWidgets.QLineEdit(self.settingsTB1)
        self.ros_Master_URI.setGeometry(QtCore.QRect(90, 88, 231, 23))
        self.ros_Master_URI.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                          "color: rgb(199, 199, 199);")
        self.ros_Master_URI.setObjectName("ros_Master_URI")
        # SSH Group Box
        self.sshTB1 = QtWidgets.QGroupBox(robotOneConfig)
        self.sshTB1.setGeometry(QtCore.QRect(5, 220, 326, 150))
        self.sshTB1.setStyleSheet("color: rgb(14, 172, 186);")
        self.sshTB1.setObjectName("sshTB1")
        # SSH User Text Edit
        self.ssh_TB1_User = QtWidgets.QLineEdit(self.sshTB1)
        self.ssh_TB1_User.setGeometry(QtCore.QRect(110, 58, 210, 23))
        self.ssh_TB1_User.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.ssh_TB1_User.setObjectName("ssh_TB1_User")
        # SSH Password Text Edit
        self.ssh_TB1_Password = QtWidgets.QLineEdit(self.sshTB1)
        self.ssh_TB1_Password.setGeometry(QtCore.QRect(110, 88, 210, 23))
        self.ssh_TB1_Password.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                            "color: rgb(199, 199, 199);")
        self.ssh_TB1_Password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.ssh_TB1_Password.setObjectName("ssh_TB1_Password")
        # SSH Port Text Edit
        self.ssh_TB1_Port = QtWidgets.QLineEdit(self.sshTB1)
        self.ssh_TB1_Port.setGeometry(QtCore.QRect(110, 118, 210, 23))
        self.ssh_TB1_Port.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.ssh_TB1_Port.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.ssh_TB1_Port.setObjectName("ssh_TB1_Port")
        # SSH IP Text Edit
        self.ssh_TB1_IP = QtWidgets.QLineEdit(self.sshTB1)
        self.ssh_TB1_IP.setGeometry(QtCore.QRect(110, 28, 210, 23))
        self.ssh_TB1_IP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: rgb(199, 199, 199);")
        self.ssh_TB1_IP.setObjectName("ssh_TB1_IP")
        # Widget Labels
        self.my_IP_TB1_Label = QtWidgets.QLabel(self.settingsTB1)
        self.my_IP_TB1_Label.setGeometry(QtCore.QRect(5, 32, 71, 16))
        self.my_IP_TB1_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.my_IP_TB1_Label.setObjectName("my_IP_TB1_Label")
        self.master_IP_TB1_Label = QtWidgets.QLabel(self.settingsTB1)
        self.master_IP_TB1_Label.setGeometry(QtCore.QRect(5, 62, 71, 16))
        self.master_IP_TB1_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_IP_TB1_Label.setObjectName("master_IP_TB1_Label")
        self.hostname_TB1_Label = QtWidgets.QLabel(self.settingsTB1)
        self.hostname_TB1_Label.setGeometry(QtCore.QRect(5, 120, 71, 16))
        self.hostname_TB1_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.hostname_TB1_Label.setObjectName("hostname_TB1_Label")
        self.namespace_TB1_Label = QtWidgets.QLabel(self.settingsTB1)
        self.namespace_TB1_Label.setGeometry(QtCore.QRect(5, 150, 81, 16))
        self.namespace_TB1_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.namespace_TB1_Label.setObjectName("namespace_TB1_Label")
        self.master_URI_TB1_Label = QtWidgets.QLabel(self.settingsTB1)
        self.master_URI_TB1_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.master_URI_TB1_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_URI_TB1_Label.setObjectName("master_URI_TB1_Label")
        self.ssh_Port_TB1_Label = QtWidgets.QLabel(self.sshTB1)
        self.ssh_Port_TB1_Label.setGeometry(QtCore.QRect(5, 120, 81, 16))
        self.ssh_Port_TB1_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_Port_TB1_Label.setObjectName("ssh_Port_TB1_Label")
        self.ssh_User_TB1_Label = QtWidgets.QLabel(self.sshTB1)
        self.ssh_User_TB1_Label.setGeometry(QtCore.QRect(5, 60, 71, 16))
        self.ssh_User_TB1_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_User_TB1_Label.setObjectName("ssh_User_TB1_Label")
        self.ssh_Password_TB1_Label = QtWidgets.QLabel(self.sshTB1)
        self.ssh_Password_TB1_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.ssh_Password_TB1_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_Password_TB1_Label.setObjectName("ssh_Password_TB1_Label")
        self.ssh_TB1_IP_Label = QtWidgets.QLabel(self.sshTB1)
        self.ssh_TB1_IP_Label.setGeometry(QtCore.QRect(5, 30, 91, 16))
        self.ssh_TB1_IP_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_TB1_IP_Label.setObjectName("ssh_TB1_IP_Label")
        # OK and Cancel Buttons
        self.buttons_Config_TB1 = QtWidgets.QDialogButtonBox(robotOneConfig)
        self.buttons_Config_TB1.setGeometry(QtCore.QRect(80, 390, 166, 24))
        self.buttons_Config_TB1.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons_Config_TB1.setObjectName("buttons_Config_TB1")
        self.buttons_Config_TB1.accepted.connect(self.okButton)
        # Buddy Set
        self.my_IP_TB1_Label.setBuddy(self.ros_TB1_IP)
        self.master_IP_TB1_Label.setBuddy(self.ros_Master_IP)
        self.hostname_TB1_Label.setBuddy(self.ros_TB1_Hostname)
        self.namespace_TB1_Label.setBuddy(self.ros_TB1_Namespace)
        self.master_URI_TB1_Label.setBuddy(self.ros_Master_URI)
        self.ssh_Port_TB1_Label.setBuddy(self.ssh_TB1_Port)
        self.ssh_User_TB1_Label.setBuddy(self.ssh_TB1_User)
        self.ssh_Password_TB1_Label.setBuddy(self.ssh_TB1_Password)
        self.ssh_TB1_IP_Label.setBuddy(self.ssh_TB1_IP)

        self.retranslateUi(robotOneConfig)
        self.buttons_Config_TB1.rejected.connect(robotOneConfig.reject)
        QtCore.QMetaObject.connectSlotsByName(robotOneConfig)

    def retranslateUi(self, robotOneConfig):
        """ This function is responsible to Translate the Names
        and Place the Button Tips Informations
        """
        _translate = QtCore.QCoreApplication.translate
        robotOneConfig.setWindowTitle(_translate("robotOneConfig", "Settings (TB1)"))
        self.settingsTB1.setTitle(_translate("robotOneConfig", "Variables and Settings:"))
        self.ros_TB1_IP.setPlaceholderText(_translate("robotOneConfig", "ex.:192.168.43.87"))
        self.ros_Master_IP.setPlaceholderText(_translate("robotOneConfig", "ex.: 192.168.43.87"))
        self.ros_TB1_Hostname.setPlaceholderText(_translate("robotOneConfig", "ex.:192.168.43.87"))
        self.ros_TB1_Namespace.setPlaceholderText(_translate("robotOneConfig", "ex.: robot_0"))
        self.my_IP_TB1_Label.setText(_translate("robotOneConfig", "ROS_MY_IP:"))
        self.master_IP_TB1_Label.setText(_translate("robotOneConfig", "MASTER_IP:"))
        self.hostname_TB1_Label.setText(_translate("robotOneConfig", "HOSTNAME:"))
        self.namespace_TB1_Label.setText(_translate("robotOneConfig", "NAMESPACE:"))
        self.master_URI_TB1_Label.setText(_translate("robotOneConfig", "MASTER_URI:"))
        self.ros_Master_URI.setPlaceholderText(_translate("robotOneConfig", "ex.: http://localhost:11311"))
        self.sshTB1.setTitle(_translate("robotOneConfig", "SSH Configuration:"))
        self.ssh_TB1_User.setPlaceholderText(_translate("robotOneConfig", "ex.: turtlebot"))
        self.ssh_TB1_Password.setPlaceholderText(_translate("robotOneConfig", "ex.: turtlebot"))
        self.ssh_Port_TB1_Label.setText(_translate("robotOneConfig", "PORT:"))
        self.ssh_TB1_Port.setPlaceholderText(_translate("robotOneConfig", "ex.: 80"))
        self.ssh_User_TB1_Label.setText(_translate("robotOneConfig", "USER:"))
        self.ssh_TB1_IP.setPlaceholderText(_translate("robotOneConfig", "ex.: 192.168.43.87"))
        self.ssh_Password_TB1_Label.setText(_translate("robotOneConfig", "PASSWORD:"))
        self.ssh_TB1_IP_Label.setText(_translate("robotOneConfig", "TURTLEBOT IP:"))
    
    def okButton(self):
        # ENV CONFIG
        ros_TB1_IP_Value = self.ros_TB1_IP.text()
        ros_Master_IP_Value = self.ros_Master_IP.text()
        ros_Master_URI_Value = self.ros_Master_URI.text()
        ros_Hostname_Value = self.ros_TB1_Hostname.text()
        ros_TB1_Namespace_Value = self.ros_TB1_Namespace.text()
        # SSH CONNECTION
        ssh_TB1_IP_Value = self.ssh_TB1_IP.text()
        ssh_TB1_User_Value = self.ssh_TB1_User.text()
        ssh_TB1_Password_Value = self.ssh_TB1_Password.text()
        ssh_TB1_Port_Value = self.ssh_TB1_Port.text()
        # XML CREATION
        environmentXMLFile = et.Element('TB1_Settings')
        comment = et.Comment("TB1 ROS Environment and Configuration Variables")
        environmentXMLFile.append(comment)
        environmentConfig = et.SubElement(environmentXMLFile, 'TB1_MY_IP')
        environmentConfig.text = str(ros_TB1_IP_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_MASTER_IP')
        environmentConfig.text = str(ros_Master_IP_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_MASTER_URI')
        environmentConfig.text = str(ros_Master_URI_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'TB1_ROS_HOSTNAME')
        environmentConfig.text = str(ros_Hostname_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'TB1_ROS_NAMESPACE')
        environmentConfig.text = str(ros_TB1_Namespace_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB1_IP')
        environmentConfig.text = str(ssh_TB1_IP_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB1_USERNAME')
        environmentConfig.text = str(ssh_TB1_User_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB1_PASSWORD')
        environmentConfig.text = str(ssh_TB1_Password_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB1_PORT')
        environmentConfig.text = str(ssh_TB1_Port_Value)
        tree = et.ElementTree(environmentXMLFile)
        tree.write('tb1Settings.xml', encoding='utf8')
        # CHANGE THE PLACEHOLDER
        _translate = QtCore.QCoreApplication.translate
        self.ros_TB1_IP.setPlaceholderText(_translate("robotOneConfig", ros_TB1_IP_Value))
        self.ros_Master_IP.setPlaceholderText(_translate("robotOneConfig", ros_Master_IP_Value))
        self.ros_Master_URI.setPlaceholderText(_translate("robotOneConfig", ros_Master_URI_Value))
        self.ros_TB1_Hostname.setPlaceholderText(_translate("robotOneConfig", ros_Hostname_Value))
        self.ros_TB1_Namespace.setPlaceholderText(_translate("robotOneConfig", ros_TB1_Namespace_Value))
        self.ssh_TB1_IP.setPlaceholderText(_translate("robotOneConfig", ssh_TB1_IP_Value))
        self.ssh_TB1_User.setPlaceholderText(_translate("robotOneConfig", ssh_TB1_User_Value))
        self.ssh_TB1_Password.setPlaceholderText(_translate("robotOneConfig", ssh_TB1_Password_Value))
        self.ssh_TB1_Port.setPlaceholderText(_translate("robotOneConfig", ssh_TB1_Port_Value))
        sucessDialog()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    robotOneConfig = QtWidgets.QDialog()
    ui = Ui_robotOneConfig()
    ui.setupUi(robotOneConfig)
    robotOneConfig.show()
    sys.exit(app.exec_())

