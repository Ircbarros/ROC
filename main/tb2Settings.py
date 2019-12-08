# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

# Form implementation generated from reading ui file 'tb2Settings.ui'
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
        sucessDialog.setWindowTitle('Settings (TB2)')
        sucessDialog.setText('As modificações foram salvas com sucesso!')
        sucessDialog.setIcon(QtWidgets.QMessageBox.Information)
        sucessDialog.show()
        sucessDialog.exec_()


class Ui_robotTwoConfig(object):
    """ Open the TB2 Settings and Configurations Widget"""
    def setupUi(self, robotTwoConfig):
        robotTwoConfig.setObjectName("robotTwoConfig")
        robotTwoConfig.resize(340, 426)
        robotTwoConfig.setMinimumSize(QtCore.QSize(340, 426))
        robotTwoConfig.setMaximumSize(QtCore.QSize(340, 426))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vectors/Conection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        robotTwoConfig.setWindowIcon(icon)
        robotTwoConfig.setStyleSheet("background: #2A2E37;")
        self.settingsTB2 = QtWidgets.QGroupBox(robotTwoConfig)
        self.settingsTB2.setGeometry(QtCore.QRect(5, 20, 326, 180))
        self.settingsTB2.setMinimumSize(QtCore.QSize(320, 140))
        self.settingsTB2.setStyleSheet("color: rgb(14, 172, 186);")
        self.settingsTB2.setObjectName("settingsTB2")
        self.ros_TB2_IP = QtWidgets.QLineEdit(self.settingsTB2)
        self.ros_TB2_IP.setGeometry(QtCore.QRect(90, 30, 231, 23))
        self.ros_TB2_IP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: rgb(199, 199, 199);")
        self.ros_TB2_IP.setDragEnabled(False)
        self.ros_TB2_IP.setObjectName("ros_TB2_IP")
        self.ros_Master_IP = QtWidgets.QLineEdit(self.settingsTB2)
        self.ros_Master_IP.setGeometry(QtCore.QRect(90, 60, 231, 23))
        self.ros_Master_IP.setStyleSheet("color: rgb(199, 199, 199);\n"
                                         "background: rgba(29, 222, 216, 0.1);")
        self.ros_Master_IP.setObjectName("ros_Master_IP")
        self.ros_TB2_Hostname = QtWidgets.QLineEdit(self.settingsTB2)
        self.ros_TB2_Hostname.setGeometry(QtCore.QRect(90, 118, 231, 23))
        self.ros_TB2_Hostname.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                            "color: rgb(199, 199, 199);")
        self.ros_TB2_Hostname.setObjectName("ros_TB2_Hostname")
        self.ros_TB2_Namespace = QtWidgets.QLineEdit(self.settingsTB2)
        self.ros_TB2_Namespace.setGeometry(QtCore.QRect(90, 148, 231, 23))
        self.ros_TB2_Namespace.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                             "color: rgb(199, 199, 199);")
        self.ros_TB2_Namespace.setObjectName("ros_TB2_Namespace")
        self.my_IP_TB2_Label = QtWidgets.QLabel(self.settingsTB2)
        self.my_IP_TB2_Label.setGeometry(QtCore.QRect(5, 32, 71, 16))
        self.my_IP_TB2_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.my_IP_TB2_Label.setObjectName("my_IP_TB2_Label")
        self.master_IP_TB2_Label = QtWidgets.QLabel(self.settingsTB2)
        self.master_IP_TB2_Label.setGeometry(QtCore.QRect(5, 62, 71, 16))
        self.master_IP_TB2_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_IP_TB2_Label.setObjectName("master_IP_TB2_Label")
        self.hostname_TB2_Label = QtWidgets.QLabel(self.settingsTB2)
        self.hostname_TB2_Label.setGeometry(QtCore.QRect(5, 120, 71, 16))
        self.hostname_TB2_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.hostname_TB2_Label.setObjectName("hostname_TB2_Label")
        self.namespace_TB2_Label = QtWidgets.QLabel(self.settingsTB2)
        self.namespace_TB2_Label.setGeometry(QtCore.QRect(5, 150, 81, 16))
        self.namespace_TB2_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.namespace_TB2_Label.setObjectName("namespace_TB2_Label")
        self.master_URI_TB2_Label = QtWidgets.QLabel(self.settingsTB2)
        self.master_URI_TB2_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.master_URI_TB2_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_URI_TB2_Label.setObjectName("master_URI_TB2_Label")
        self.ros_Master_URI = QtWidgets.QLineEdit(self.settingsTB2)
        self.ros_Master_URI.setGeometry(QtCore.QRect(90, 88, 231, 23))
        self.ros_Master_URI.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                          "color: rgb(199, 199, 199);")
        self.ros_Master_URI.setObjectName("ros_Master_URI")
        self.sshTB2 = QtWidgets.QGroupBox(robotTwoConfig)
        self.sshTB2.setGeometry(QtCore.QRect(5, 220, 326, 150))
        self.sshTB2.setStyleSheet("color: rgb(14, 172, 186);")
        self.sshTB2.setObjectName("sshTB2")
        self.ssh_TB2_User = QtWidgets.QLineEdit(self.sshTB2)
        self.ssh_TB2_User.setGeometry(QtCore.QRect(110, 58, 210, 23))
        self.ssh_TB2_User.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.ssh_TB2_User.setObjectName("ssh_TB2_User")
        self.ssh_TB2_Password = QtWidgets.QLineEdit(self.sshTB2)
        self.ssh_TB2_Password.setGeometry(QtCore.QRect(110, 88, 210, 23))
        self.ssh_TB2_Password.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                            "color: rgb(199, 199, 199);")
        self.ssh_TB2_Password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.ssh_TB2_Password.setObjectName("ssh_TB2_Password")
        self.ssh_Port_TB2_Label = QtWidgets.QLabel(self.sshTB2)
        self.ssh_Port_TB2_Label.setGeometry(QtCore.QRect(5, 120, 81, 16))
        self.ssh_Port_TB2_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_Port_TB2_Label.setObjectName("ssh_Port_TB2_Label")
        self.ssh_TB2_Port = QtWidgets.QLineEdit(self.sshTB2)
        self.ssh_TB2_Port.setGeometry(QtCore.QRect(110, 118, 210, 23))
        self.ssh_TB2_Port.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.ssh_TB2_Port.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.ssh_TB2_Port.setObjectName("ssh_TB2_Port")
        self.ssh_User_TB2_Label = QtWidgets.QLabel(self.sshTB2)
        self.ssh_User_TB2_Label.setGeometry(QtCore.QRect(5, 60, 71, 16))
        self.ssh_User_TB2_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_User_TB2_Label.setObjectName("ssh_User_TB2_Label")
        self.ssh_TB2_IP = QtWidgets.QLineEdit(self.sshTB2)
        self.ssh_TB2_IP.setGeometry(QtCore.QRect(110, 28, 210, 23))
        self.ssh_TB2_IP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: rgb(199, 199, 199);")
        self.ssh_TB2_IP.setObjectName("ssh_TB2_IP")
        self.ssh_Password_TB2_Label = QtWidgets.QLabel(self.sshTB2)
        self.ssh_Password_TB2_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.ssh_Password_TB2_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_Password_TB2_Label.setObjectName("ssh_Password_TB2_Label")
        self.ssh_TB2_IP_Label = QtWidgets.QLabel(self.sshTB2)
        self.ssh_TB2_IP_Label.setGeometry(QtCore.QRect(5, 30, 91, 16))
        self.ssh_TB2_IP_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_TB2_IP_Label.setObjectName("ssh_TB2_IP_Label")
        self.buttons_Config_TB2 = QtWidgets.QDialogButtonBox(robotTwoConfig)
        self.buttons_Config_TB2.setGeometry(QtCore.QRect(80, 390, 166, 24))
        self.buttons_Config_TB2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons_Config_TB2.setObjectName("buttons_Config_TB2")
        self.buttons_Config_TB2.accepted.connect(self.okButton)

        self.my_IP_TB2_Label.setBuddy(self.ros_TB2_IP)
        self.master_IP_TB2_Label.setBuddy(self.ros_Master_IP)
        self.hostname_TB2_Label.setBuddy(self.ros_TB2_Hostname)
        self.namespace_TB2_Label.setBuddy(self.ros_TB2_Namespace)
        self.master_URI_TB2_Label.setBuddy(self.ros_Master_URI)
        self.ssh_Port_TB2_Label.setBuddy(self.ssh_TB2_Port)
        self.ssh_User_TB2_Label.setBuddy(self.ssh_TB2_User)
        self.ssh_Password_TB2_Label.setBuddy(self.ssh_TB2_Password)
        self.ssh_TB2_IP_Label.setBuddy(self.ssh_TB2_IP)

        self.retranslateUi(robotTwoConfig)
        self.buttons_Config_TB2.rejected.connect(robotTwoConfig.reject)
        QtCore.QMetaObject.connectSlotsByName(robotTwoConfig)

    def retranslateUi(self, robotTwoConfig):
        _translate = QtCore.QCoreApplication.translate
        robotTwoConfig.setWindowTitle(_translate("robotTwoConfig", "Settings (TB2)"))
        self.settingsTB2.setTitle(_translate("robotTwoConfig", "Variables and Settings:"))
        self.ros_TB2_IP.setPlaceholderText(_translate("robotTwoConfig", "ex.:192.168.43.87"))
        self.ros_Master_IP.setPlaceholderText(_translate("robotTwoConfig", "ex.: 192.168.43.87"))
        self.ros_TB2_Hostname.setPlaceholderText(_translate("robotTwoConfig", "ex.:192.168.43.87"))
        self.ros_TB2_Namespace.setPlaceholderText(_translate("robotTwoConfig", "ex.: robot_0"))
        self.my_IP_TB2_Label.setText(_translate("robotTwoConfig", "ROS_MY_IP:"))
        self.master_IP_TB2_Label.setText(_translate("robotTwoConfig", "MASTER_IP:"))
        self.hostname_TB2_Label.setText(_translate("robotTwoConfig", "HOSTNAME:"))
        self.namespace_TB2_Label.setText(_translate("robotTwoConfig", "NAMESPACE:"))
        self.master_URI_TB2_Label.setText(_translate("robotTwoConfig", "MASTER_URI:"))
        self.ros_Master_URI.setPlaceholderText(_translate("robotTwoConfig", "ex.: http://localhost:11311"))
        self.sshTB2.setTitle(_translate("robotTwoConfig", "SSH Configuration:"))
        self.ssh_TB2_User.setPlaceholderText(_translate("robotTwoConfig", "ex.: turtlebot"))
        self.ssh_TB2_Password.setPlaceholderText(_translate("robotTwoConfig", "ex.: turtlebot"))
        self.ssh_Port_TB2_Label.setText(_translate("robotTwoConfig", "PORT:"))
        self.ssh_TB2_Port.setPlaceholderText(_translate("robotTwoConfig", "ex.: 80"))
        self.ssh_User_TB2_Label.setText(_translate("robotTwoConfig", "USER:"))
        self.ssh_TB2_IP.setPlaceholderText(_translate("robotTwoConfig", "ex.: 192.168.43.87"))
        self.ssh_Password_TB2_Label.setText(_translate("robotTwoConfig", "PASSWORD:"))
        self.ssh_TB2_IP_Label.setText(_translate("robotTwoConfig", "TURTLEBOT IP:"))

    def okButton(self):
        # ENV CONFIG
        ros_TB2_IP_Value = self.ros_TB2_IP.text()
        ros_Master_IP_Value = self.ros_Master_IP.text()
        ros_Master_URI_Value = self.ros_Master_URI.text()
        ros_Hostname_Value = self.ros_TB2_Hostname.text()
        ros_TB2_Namespace_Value = self.ros_TB2_Namespace.text()
        # SSH CONNECTION
        ssh_TB2_IP_Value = self.ssh_TB2_IP.text()
        ssh_TB2_User_Value = self.ssh_TB2_User.text()
        ssh_TB2_Password_Value = self.ssh_TB2_Password.text()
        ssh_TB2_Port_Value = self.ssh_TB2_Port.text()
        # XML CREATION
        environmentXMLFile = et.Element('TB2_Settings')
        comment = et.Comment("TB2 ROS Environment and Configuration Variables")
        environmentXMLFile.append(comment)
        environmentConfig = et.SubElement(environmentXMLFile, 'TB2_MY_IP')
        environmentConfig.text = str(ros_TB2_IP_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_MASTER_IP')
        environmentConfig.text = str(ros_Master_IP_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_MASTER_URI')
        environmentConfig.text = str(ros_Master_URI_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'TB2_ROS_HOSTNAME')
        environmentConfig.text = str(ros_Hostname_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'TB2_ROS_NAMESPACE')
        environmentConfig.text = str(ros_TB2_Namespace_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB2_IP')
        environmentConfig.text = str(ssh_TB2_IP_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB2_USERNAME')
        environmentConfig.text = str(ssh_TB2_User_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB2_PASSWORD')
        environmentConfig.text = str(ssh_TB2_Password_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB2_PORT')
        environmentConfig.text = str(ssh_TB2_Port_Value)
        tree = et.ElementTree(environmentXMLFile)
        tree.write('tb2Settings.xml', encoding='utf8')
        # CHANGE THE PLACEHOLDER
        _translate = QtCore.QCoreApplication.translate
        self.ros_TB2_IP.setPlaceholderText(_translate("robotTwoConfig", ros_TB2_IP_Value))
        self.ros_Master_IP.setPlaceholderText(_translate("robotTwoConfig", ros_Master_IP_Value))
        self.ros_Master_URI.setPlaceholderText(_translate("robotTwoConfig", ros_Master_URI_Value))
        self.ros_TB2_Hostname.setPlaceholderText(_translate("robotTwoConfig", ros_Hostname_Value))
        self.ros_TB2_Namespace.setPlaceholderText(_translate("robotTwoConfig", ros_TB2_Namespace_Value))
        self.ssh_TB2_IP.setPlaceholderText(_translate("robotTwoConfig", ssh_TB2_IP_Value))
        self.ssh_TB2_User.setPlaceholderText(_translate("robotTwoConfig", ssh_TB2_User_Value))
        self.ssh_TB2_Password.setPlaceholderText(_translate("robotOneConfig", ssh_TB2_Password_Value))
        self.ssh_TB2_Port.setPlaceholderText(_translate("robotTwoConfig", ssh_TB2_Port_Value))
        sucessDialog()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    robotTwoConfig = QtWidgets.QDialog()
    ui = Ui_robotTwoConfig()
    ui.setupUi(robotTwoConfig)
    robotTwoConfig.show()
    sys.exit(app.exec_())

