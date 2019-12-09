# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

# Form implementation generated from reading ui file 'tb4Settings.ui'
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

class Ui_robotFourConfig(object):
    def setupUi(self, robotFourConfig):
        robotFourConfig.setObjectName("robotFourConfig")
        robotFourConfig.resize(340, 426)
        robotFourConfig.setMinimumSize(QtCore.QSize(340, 426))
        robotFourConfig.setMaximumSize(QtCore.QSize(340, 426))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vectors/Conection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        robotFourConfig.setWindowIcon(icon)
        robotFourConfig.setStyleSheet("background: #2A2E37;")
        self.settingsTB4 = QtWidgets.QGroupBox(robotFourConfig)
        self.settingsTB4.setGeometry(QtCore.QRect(5, 20, 326, 180))
        self.settingsTB4.setMinimumSize(QtCore.QSize(320, 140))
        self.settingsTB4.setStyleSheet("color: rgb(14, 172, 186);")
        self.settingsTB4.setObjectName("settingsTB4")
        self.ros_TB4_IP = QtWidgets.QLineEdit(self.settingsTB4)
        self.ros_TB4_IP.setGeometry(QtCore.QRect(90, 30, 231, 23))
        self.ros_TB4_IP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: rgb(199, 199, 199);")
        self.ros_TB4_IP.setDragEnabled(False)
        self.ros_TB4_IP.setObjectName("ros_TB4_IP")
        self.ros_Master_IP = QtWidgets.QLineEdit(self.settingsTB4)
        self.ros_Master_IP.setGeometry(QtCore.QRect(90, 60, 231, 23))
        self.ros_Master_IP.setStyleSheet("color: rgb(199, 199, 199);\n"
                                         "background: rgba(29, 222, 216, 0.1);")
        self.ros_Master_IP.setObjectName("ros_Master_IP")
        self.ros_TB4_Hostname = QtWidgets.QLineEdit(self.settingsTB4)
        self.ros_TB4_Hostname.setGeometry(QtCore.QRect(90, 118, 231, 23))
        self.ros_TB4_Hostname.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                            "color: rgb(199, 199, 199);")
        self.ros_TB4_Hostname.setObjectName("ros_TB4_Hostname")
        self.ros_TB4_Namespace = QtWidgets.QLineEdit(self.settingsTB4)
        self.ros_TB4_Namespace.setGeometry(QtCore.QRect(90, 148, 231, 23))
        self.ros_TB4_Namespace.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                             "color: rgb(199, 199, 199);")
        self.ros_TB4_Namespace.setObjectName("ros_TB4_Namespace")
        self.my_IP_TB4_Label = QtWidgets.QLabel(self.settingsTB4)
        self.my_IP_TB4_Label.setGeometry(QtCore.QRect(5, 32, 71, 16))
        self.my_IP_TB4_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.my_IP_TB4_Label.setObjectName("my_IP_TB4_Label")
        self.master_IP_TB4_Label = QtWidgets.QLabel(self.settingsTB4)
        self.master_IP_TB4_Label.setGeometry(QtCore.QRect(5, 62, 71, 16))
        self.master_IP_TB4_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_IP_TB4_Label.setObjectName("master_IP_TB4_Label")
        self.hostname_TB4_Label = QtWidgets.QLabel(self.settingsTB4)
        self.hostname_TB4_Label.setGeometry(QtCore.QRect(5, 120, 71, 16))
        self.hostname_TB4_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.hostname_TB4_Label.setObjectName("hostname_TB4_Label")
        self.namespace_TB4_Label = QtWidgets.QLabel(self.settingsTB4)
        self.namespace_TB4_Label.setGeometry(QtCore.QRect(5, 150, 81, 16))
        self.namespace_TB4_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.namespace_TB4_Label.setObjectName("namespace_TB4_Label")
        self.master_URI_TB4_Label = QtWidgets.QLabel(self.settingsTB4)
        self.master_URI_TB4_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.master_URI_TB4_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_URI_TB4_Label.setObjectName("master_URI_TB4_Label")
        self.ros_Master_URI = QtWidgets.QLineEdit(self.settingsTB4)
        self.ros_Master_URI.setGeometry(QtCore.QRect(90, 88, 231, 23))
        self.ros_Master_URI.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                          "color: rgb(199, 199, 199);")
        self.ros_Master_URI.setObjectName("ros_Master_URI")
        self.sshTB4 = QtWidgets.QGroupBox(robotFourConfig)
        self.sshTB4.setGeometry(QtCore.QRect(5, 220, 326, 150))
        self.sshTB4.setStyleSheet("color: rgb(14, 172, 186);")
        self.sshTB4.setObjectName("sshTB4")
        self.ssh_TB4_User = QtWidgets.QLineEdit(self.sshTB4)
        self.ssh_TB4_User.setGeometry(QtCore.QRect(110, 58, 210, 23))
        self.ssh_TB4_User.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.ssh_TB4_User.setObjectName("ssh_TB4_User")
        self.ssh_TB4_Password = QtWidgets.QLineEdit(self.sshTB4)
        self.ssh_TB4_Password.setGeometry(QtCore.QRect(110, 88, 210, 23))
        self.ssh_TB4_Password.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                            "color: rgb(199, 199, 199);")
        self.ssh_TB4_Password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.ssh_TB4_Password.setObjectName("ssh_TB4_Password")
        self.ssh_Port_TB4_Label = QtWidgets.QLabel(self.sshTB4)
        self.ssh_Port_TB4_Label.setGeometry(QtCore.QRect(5, 120, 81, 16))
        self.ssh_Port_TB4_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_Port_TB4_Label.setObjectName("ssh_Port_TB4_Label")
        self.ssh_TB4_Port = QtWidgets.QLineEdit(self.sshTB4)
        self.ssh_TB4_Port.setGeometry(QtCore.QRect(110, 118, 210, 23))
        self.ssh_TB4_Port.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.ssh_TB4_Port.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.ssh_TB4_Port.setObjectName("ssh_TB4_Port")
        self.ssh_User_TB4_Label = QtWidgets.QLabel(self.sshTB4)
        self.ssh_User_TB4_Label.setGeometry(QtCore.QRect(5, 60, 71, 16))
        self.ssh_User_TB4_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_User_TB4_Label.setObjectName("ssh_User_TB4_Label")
        self.ssh_TB4_IP = QtWidgets.QLineEdit(self.sshTB4)
        self.ssh_TB4_IP.setGeometry(QtCore.QRect(110, 28, 210, 23))
        self.ssh_TB4_IP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: rgb(199, 199, 199);")
        self.ssh_TB4_IP.setObjectName("ssh_TB4_IP")
        self.ssh_Password_TB4_Label = QtWidgets.QLabel(self.sshTB4)
        self.ssh_Password_TB4_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.ssh_Password_TB4_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_Password_TB4_Label.setObjectName("ssh_Password_TB4_Label")
        self.ssh_TB4_IP_Label = QtWidgets.QLabel(self.sshTB4)
        self.ssh_TB4_IP_Label.setGeometry(QtCore.QRect(5, 30, 91, 16))
        self.ssh_TB4_IP_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_TB4_IP_Label.setObjectName("ssh_TB4_IP_Label")
        self.buttons_Config_TB4 = QtWidgets.QDialogButtonBox(robotFourConfig)
        self.buttons_Config_TB4.setGeometry(QtCore.QRect(80, 390, 166, 24))
        self.buttons_Config_TB4.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons_Config_TB4.setObjectName("buttons_Config_TB4")
        self.buttons_Config_TB4.accepted.connect(self.okButton)

        self.my_IP_TB4_Label.setBuddy(self.ros_TB4_IP)
        self.master_IP_TB4_Label.setBuddy(self.ros_Master_IP)
        self.hostname_TB4_Label.setBuddy(self.ros_TB4_Hostname)
        self.namespace_TB4_Label.setBuddy(self.ros_TB4_Namespace)
        self.master_URI_TB4_Label.setBuddy(self.ros_Master_URI)
        self.ssh_Port_TB4_Label.setBuddy(self.ssh_TB4_Port)
        self.ssh_User_TB4_Label.setBuddy(self.ssh_TB4_User)
        self.ssh_Password_TB4_Label.setBuddy(self.ssh_TB4_Password)
        self.ssh_TB4_IP_Label.setBuddy(self.ssh_TB4_IP)

        self.retranslateUi(robotFourConfig)
        self.buttons_Config_TB4.rejected.connect(robotFourConfig.reject)
        QtCore.QMetaObject.connectSlotsByName(robotFourConfig)

    def retranslateUi(self, robotFourConfig):
        _translate = QtCore.QCoreApplication.translate
        robotFourConfig.setWindowTitle(_translate("robotFourConfig", "Settings (TB4)"))
        self.settingsTB4.setTitle(_translate("robotFourConfig", "Variables and Settings:"))
        self.ros_TB4_IP.setPlaceholderText(_translate("robotFourConfig", "ex.:192.168.43.87"))
        self.ros_Master_IP.setPlaceholderText(_translate("robotFourConfig", "ex.: 192.168.43.87"))
        self.ros_TB4_Hostname.setPlaceholderText(_translate("robotFourConfig", "ex.:192.168.43.87"))
        self.ros_TB4_Namespace.setPlaceholderText(_translate("robotFourConfig", "ex.: robot_0"))
        self.my_IP_TB4_Label.setText(_translate("robotFourConfig", "ROS_MY_IP:"))
        self.master_IP_TB4_Label.setText(_translate("robotFourConfig", "MASTER_IP:"))
        self.hostname_TB4_Label.setText(_translate("robotFourConfig", "HOSTNAME:"))
        self.namespace_TB4_Label.setText(_translate("robotFourConfig", "NAMESPACE:"))
        self.master_URI_TB4_Label.setText(_translate("robotFourConfig", "MASTER_URI:"))
        self.ros_Master_URI.setPlaceholderText(_translate("robotFourConfig", "ex.: http://localhost:11311"))
        self.sshTB4.setTitle(_translate("robotFourConfig", "SSH Configuration:"))
        self.ssh_TB4_User.setPlaceholderText(_translate("robotFourConfig", "ex.: turtlebot"))
        self.ssh_TB4_Password.setPlaceholderText(_translate("robotFourConfig", "ex.: turtlebot"))
        self.ssh_Port_TB4_Label.setText(_translate("robotFourConfig", "PORT:"))
        self.ssh_TB4_Port.setPlaceholderText(_translate("robotFourConfig", "ex.: 80"))
        self.ssh_User_TB4_Label.setText(_translate("robotFourConfig", "USER:"))
        self.ssh_TB4_IP.setPlaceholderText(_translate("robotFourConfig", "ex.: 192.168.43.87"))
        self.ssh_Password_TB4_Label.setText(_translate("robotFourConfig", "PASSWORD:"))
        self.ssh_TB4_IP_Label.setText(_translate("robotFourConfig", "TURTLEBOT IP:"))

    def okButton(self):
        # ENV CONFIG
        ros_TB4_IP_Value = self.ros_TB4_IP.text()
        ros_Master_IP_Value = self.ros_Master_IP.text()
        ros_Master_URI_Value = self.ros_Master_URI.text()
        ros_Hostname_Value = self.ros_TB4_Hostname.text()
        ros_TB4_Namespace_Value = self.ros_TB4_Namespace.text()
        # SSH CONNECTION
        ssh_TB4_IP_Value = self.ssh_TB4_IP.text()
        ssh_TB4_User_Value = self.ssh_TB4_User.text()
        ssh_TB4_Password_Value = self.ssh_TB4_Password.text()
        ssh_TB4_Port_Value = self.ssh_TB4_Port.text()
        # XML CREATION
        environmentXMLFile = et.Element('TB4_Settings')
        comment = et.Comment("TB4 ROS Environment and Configuration Variables")
        environmentXMLFile.append(comment)
        environmentConfig = et.SubElement(environmentXMLFile, 'TB4_MY_IP')
        environmentConfig.text = str(ros_TB4_IP_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_MASTER_IP')
        environmentConfig.text = str(ros_Master_IP_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_MASTER_URI')
        environmentConfig.text = str(ros_Master_URI_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'TB4_ROS_HOSTNAME')
        environmentConfig.text = str(ros_Hostname_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'TB4_ROS_NAMESPACE')
        environmentConfig.text = str(ros_TB4_Namespace_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB4_IP')
        environmentConfig.text = str(ssh_TB4_IP_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB4_USERNAME')
        environmentConfig.text = str(ssh_TB4_User_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB4_PASSWORD')
        environmentConfig.text = str(ssh_TB4_Password_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_TB4_PORT')
        environmentConfig.text = str(ssh_TB4_Port_Value)
        tree = et.ElementTree(environmentXMLFile)
        tree.write('tb4Settings.xml', encoding='utf8')
        # CHANGE THE PLACEHOLDER
        _translate = QtCore.QCoreApplication.translate
        self.ros_TB4_IP.setPlaceholderText(_translate("robotFourConfig", ros_TB4_IP_Value))
        self.ros_Master_IP.setPlaceholderText(_translate("robotFourConfig", ros_Master_IP_Value))
        self.ros_Master_URI.setPlaceholderText(_translate("robotFourConfig", ros_Master_URI_Value))
        self.ros_TB4_Hostname.setPlaceholderText(_translate("robotFourConfig", ros_Hostname_Value))
        self.ros_TB4_Namespace.setPlaceholderText(_translate("robotFourConfig", ros_TB4_Namespace_Value))
        self.ssh_TB4_IP.setPlaceholderText(_translate("robotFourConfig", ssh_TB4_IP_Value))
        self.ssh_TB4_User.setPlaceholderText(_translate("robotFourConfig", ssh_TB4_User_Value))
        self.ssh_TB4_Password.setPlaceholderText(_translate("robotFourConfig", ssh_TB4_Password_Value))
        self.ssh_TB4_Port.setPlaceholderText(_translate("robotFourConfig", ssh_TB4_Port_Value))
        sucessDialog()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    robotFourConfig = QtWidgets.QDialog()
    ui = Ui_robotFourConfig()
    ui.setupUi(robotFourConfig)
    robotFourConfig.show()
    sys.exit(app.exec_())

