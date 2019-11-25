# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tb3Settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import vectors
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_robotThreeConfig(object):
    def setupUi(self, robotThreeConfig):
        robotThreeConfig.setObjectName("robotThreeConfig")
        robotThreeConfig.resize(340, 426)
        robotThreeConfig.setMinimumSize(QtCore.QSize(340, 426))
        robotThreeConfig.setMaximumSize(QtCore.QSize(340, 426))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vectors/Conection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        robotThreeConfig.setWindowIcon(icon)
        robotThreeConfig.setStyleSheet("background: #2A2E37;")
        self.settingsTB3 = QtWidgets.QGroupBox(robotThreeConfig)
        self.settingsTB3.setGeometry(QtCore.QRect(5, 20, 326, 180))
        self.settingsTB3.setMinimumSize(QtCore.QSize(320, 140))
        self.settingsTB3.setStyleSheet("color: rgb(14, 172, 186);")
        self.settingsTB3.setObjectName("settingsTB3")
        self.ros_TB3_IP = QtWidgets.QLineEdit(self.settingsTB3)
        self.ros_TB3_IP.setGeometry(QtCore.QRect(90, 30, 231, 23))
        self.ros_TB3_IP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: rgb(199, 199, 199);")
        self.ros_TB3_IP.setDragEnabled(False)
        self.ros_TB3_IP.setObjectName("ros_TB3_IP")
        self.ros_Master_IP = QtWidgets.QLineEdit(self.settingsTB3)
        self.ros_Master_IP.setGeometry(QtCore.QRect(90, 60, 231, 23))
        self.ros_Master_IP.setStyleSheet("color: rgb(199, 199, 199);\n"
                                         "background: rgba(29, 222, 216, 0.1);")
        self.ros_Master_IP.setObjectName("ros_Master_IP")
        self.ros_TB3_Hostname = QtWidgets.QLineEdit(self.settingsTB3)
        self.ros_TB3_Hostname.setGeometry(QtCore.QRect(90, 118, 231, 23))
        self.ros_TB3_Hostname.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                            "color: rgb(199, 199, 199);")
        self.ros_TB3_Hostname.setObjectName("ros_TB3_Hostname")
        self.ros_TB3_Namespace = QtWidgets.QLineEdit(self.settingsTB3)
        self.ros_TB3_Namespace.setGeometry(QtCore.QRect(90, 148, 231, 23))
        self.ros_TB3_Namespace.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                             "color: rgb(199, 199, 199);")
        self.ros_TB3_Namespace.setObjectName("ros_TB3_Namespace")
        self.my_IP_TB3_Label = QtWidgets.QLabel(self.settingsTB3)
        self.my_IP_TB3_Label.setGeometry(QtCore.QRect(5, 32, 71, 16))
        self.my_IP_TB3_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.my_IP_TB3_Label.setObjectName("my_IP_TB3_Label")
        self.master_IP_TB3_Label = QtWidgets.QLabel(self.settingsTB3)
        self.master_IP_TB3_Label.setGeometry(QtCore.QRect(5, 62, 71, 16))
        self.master_IP_TB3_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_IP_TB3_Label.setObjectName("master_IP_TB3_Label")
        self.hostname_TB3_Label = QtWidgets.QLabel(self.settingsTB3)
        self.hostname_TB3_Label.setGeometry(QtCore.QRect(5, 120, 71, 16))
        self.hostname_TB3_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.hostname_TB3_Label.setObjectName("hostname_TB3_Label")
        self.namespace_TB3_Label = QtWidgets.QLabel(self.settingsTB3)
        self.namespace_TB3_Label.setGeometry(QtCore.QRect(5, 150, 81, 16))
        self.namespace_TB3_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.namespace_TB3_Label.setObjectName("namespace_TB3_Label")
        self.master_URI_TB3_Label = QtWidgets.QLabel(self.settingsTB3)
        self.master_URI_TB3_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.master_URI_TB3_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_URI_TB3_Label.setObjectName("master_URI_TB3_Label")
        self.ros_Master_URI = QtWidgets.QLineEdit(self.settingsTB3)
        self.ros_Master_URI.setGeometry(QtCore.QRect(90, 88, 231, 23))
        self.ros_Master_URI.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                          "color: rgb(199, 199, 199);")
        self.ros_Master_URI.setObjectName("ros_Master_URI")
        self.sshTB3 = QtWidgets.QGroupBox(robotThreeConfig)
        self.sshTB3.setGeometry(QtCore.QRect(5, 220, 326, 150))
        self.sshTB3.setStyleSheet("color: rgb(14, 172, 186);")
        self.sshTB3.setObjectName("sshTB3")
        self.ssh_TB3_User = QtWidgets.QLineEdit(self.sshTB3)
        self.ssh_TB3_User.setGeometry(QtCore.QRect(110, 58, 210, 23))
        self.ssh_TB3_User.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.ssh_TB3_User.setObjectName("ssh_TB3_User")
        self.ssh_TB3_Password = QtWidgets.QLineEdit(self.sshTB3)
        self.ssh_TB3_Password.setGeometry(QtCore.QRect(110, 88, 210, 23))
        self.ssh_TB3_Password.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                            "color: rgb(199, 199, 199);")
        self.ssh_TB3_Password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.ssh_TB3_Password.setObjectName("ssh_TB3_Password")
        self.ssh_Port_TB3_Label = QtWidgets.QLabel(self.sshTB3)
        self.ssh_Port_TB3_Label.setGeometry(QtCore.QRect(5, 120, 81, 16))
        self.ssh_Port_TB3_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_Port_TB3_Label.setObjectName("ssh_Port_TB3_Label")
        self.ssh_TB3_Port = QtWidgets.QLineEdit(self.sshTB3)
        self.ssh_TB3_Port.setGeometry(QtCore.QRect(110, 118, 210, 23))
        self.ssh_TB3_Port.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.ssh_TB3_Port.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.ssh_TB3_Port.setObjectName("ssh_TB3_Port")
        self.ssh_User_TB3_Label = QtWidgets.QLabel(self.sshTB3)
        self.ssh_User_TB3_Label.setGeometry(QtCore.QRect(5, 60, 71, 16))
        self.ssh_User_TB3_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_User_TB3_Label.setObjectName("ssh_User_TB3_Label")
        self.ssh_TB3_IP = QtWidgets.QLineEdit(self.sshTB3)
        self.ssh_TB3_IP.setGeometry(QtCore.QRect(110, 28, 210, 23))
        self.ssh_TB3_IP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: rgb(199, 199, 199);")
        self.ssh_TB3_IP.setObjectName("ssh_TB3_IP")
        self.ssh_Password_TB3_Label = QtWidgets.QLabel(self.sshTB3)
        self.ssh_Password_TB3_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.ssh_Password_TB3_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_Password_TB3_Label.setObjectName("ssh_Password_TB3_Label")
        self.ssh_TB3_IP_Label = QtWidgets.QLabel(self.sshTB3)
        self.ssh_TB3_IP_Label.setGeometry(QtCore.QRect(5, 30, 91, 16))
        self.ssh_TB3_IP_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_TB3_IP_Label.setObjectName("ssh_TB3_IP_Label")
        self.buttons_Config_TB3 = QtWidgets.QDialogButtonBox(robotThreeConfig)
        self.buttons_Config_TB3.setGeometry(QtCore.QRect(80, 390, 166, 24))
        self.buttons_Config_TB3.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons_Config_TB3.setObjectName("buttons_Config_TB3")
        self.my_IP_TB3_Label.setBuddy(self.ros_TB3_IP)
        self.master_IP_TB3_Label.setBuddy(self.ros_Master_IP)
        self.hostname_TB3_Label.setBuddy(self.ros_TB3_Hostname)
        self.namespace_TB3_Label.setBuddy(self.ros_TB3_Namespace)
        self.master_URI_TB3_Label.setBuddy(self.ros_Master_URI)
        self.ssh_Port_TB3_Label.setBuddy(self.ssh_TB3_Port)
        self.ssh_User_TB3_Label.setBuddy(self.ssh_TB3_User)
        self.ssh_Password_TB3_Label.setBuddy(self.ssh_TB3_Password)
        self.ssh_TB3_IP_Label.setBuddy(self.ssh_TB3_IP)

        self.retranslateUi(robotThreeConfig)
        self.buttons_Config_TB3.accepted.connect(self.ssh_TB3_Port.copy)
        self.buttons_Config_TB3.accepted.connect(self.ssh_TB3_Password.copy)
        self.buttons_Config_TB3.accepted.connect(self.ssh_TB3_User.copy)
        self.buttons_Config_TB3.accepted.connect(self.ssh_TB3_IP.copy)
        self.buttons_Config_TB3.accepted.connect(self.ros_TB3_Namespace.copy)
        self.buttons_Config_TB3.accepted.connect(self.ros_TB3_Hostname.copy)
        self.buttons_Config_TB3.accepted.connect(self.ros_Master_URI.copy)
        self.buttons_Config_TB3.accepted.connect(self.ros_Master_IP.copy)
        self.buttons_Config_TB3.accepted.connect(self.ros_TB3_IP.copy)
        QtCore.QMetaObject.connectSlotsByName(robotThreeConfig)

    def retranslateUi(self, robotThreeConfig):
        _translate = QtCore.QCoreApplication.translate
        robotThreeConfig.setWindowTitle(_translate("robotThreeConfig", "Settings (TB3)"))
        self.settingsTB3.setTitle(_translate("robotThreeConfig", "Variables and Settings:"))
        self.ros_TB3_IP.setPlaceholderText(_translate("robotThreeConfig", "ex.:192.168.43.87"))
        self.ros_Master_IP.setPlaceholderText(_translate("robotThreeConfig", "ex.: 192.168.43.87"))
        self.ros_TB3_Hostname.setPlaceholderText(_translate("robotThreeConfig", "ex.:192.168.43.87"))
        self.ros_TB3_Namespace.setPlaceholderText(_translate("robotThreeConfig", "ex.: robot_0"))
        self.my_IP_TB3_Label.setText(_translate("robotThreeConfig", "ROS_MY_IP:"))
        self.master_IP_TB3_Label.setText(_translate("robotThreeConfig", "MASTER_IP:"))
        self.hostname_TB3_Label.setText(_translate("robotThreeConfig", "HOSTNAME:"))
        self.namespace_TB3_Label.setText(_translate("robotThreeConfig", "NAMESPACE:"))
        self.master_URI_TB3_Label.setText(_translate("robotThreeConfig", "MASTER_URI:"))
        self.ros_Master_URI.setPlaceholderText(_translate("robotThreeConfig", "ex.: http://localhost:11311"))
        self.sshTB3.setTitle(_translate("robotThreeConfig", "SSH Configuration:"))
        self.ssh_TB3_User.setPlaceholderText(_translate("robotThreeConfig", "ex.: turtlebot"))
        self.ssh_TB3_Password.setPlaceholderText(_translate("robotThreeConfig", "ex.: turtlebot"))
        self.ssh_Port_TB3_Label.setText(_translate("robotThreeConfig", "PORT:"))
        self.ssh_TB3_Port.setPlaceholderText(_translate("robotThreeConfig", "ex.: 80"))
        self.ssh_User_TB3_Label.setText(_translate("robotThreeConfig", "USER:"))
        self.ssh_TB3_IP.setPlaceholderText(_translate("robotThreeConfig", "ex.: 192.168.43.87"))
        self.ssh_Password_TB3_Label.setText(_translate("robotThreeConfig", "PASSWORD:"))
        self.ssh_TB3_IP_Label.setText(_translate("robotThreeConfig", "TURTLEBOT IP:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    robotThreeConfig = QtWidgets.QDialog()
    ui = Ui_robotThreeConfig()
    ui.setupUi(robotThreeConfig)
    robotThreeConfig.show()
    sys.exit(app.exec_())
