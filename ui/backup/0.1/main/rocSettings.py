# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

# Form implementation generated from reading ui file 'rocSettings.ui'
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
import subprocess
from subprocess import call, Popen, PIPE, check_output
from PyQt5 import QtCore, QtGui, QtWidgets
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et


class operationSucess(QtWidgets.QWidget):
    """
    Sucess Dialog Button
    """
    def __init__(self, parent=None):
        Error = QtWidgets.QMessageBox()
        Error.setText('Os dados foram salvos com sucesso! Por favor, reinicie o computador.')
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


class Ui_rocConfigure(object):
    """ Open the ROC Configurations Widget"""
    def setupUi(self, rocConfigure):
        rocConfigure.setObjectName("rocConfigure")
        rocConfigure.resize(340, 426)
        rocConfigure.setMinimumSize(QtCore.QSize(340, 426))
        rocConfigure.setMaximumSize(QtCore.QSize(340, 426))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vectors/Conection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        rocConfigure.setWindowIcon(icon)
        rocConfigure.setStyleSheet("background: #2A2E37;")
        self.rosSettingsROC = QtWidgets.QGroupBox(rocConfigure)
        self.rosSettingsROC.setGeometry(QtCore.QRect(7, 200, 326, 181))
        self.rosSettingsROC.setMinimumSize(QtCore.QSize(320, 140))
        self.rosSettingsROC.setStyleSheet("color: rgb(14, 172, 186);")
        self.rosSettingsROC.setObjectName("rosSettingsROC")
        self.my_IP_ROC = QtWidgets.QLineEdit(self.rosSettingsROC)
        self.my_IP_ROC.setGeometry(QtCore.QRect(90, 30, 231, 23))
        self.my_IP_ROC.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                     "color: rgb(199, 199, 199);")
        self.my_IP_ROC.setDragEnabled(False)
        self.my_IP_ROC.setObjectName("my_IP_ROC")
        self.master_IP_ROC = QtWidgets.QLineEdit(self.rosSettingsROC)
        self.master_IP_ROC.setGeometry(QtCore.QRect(90, 60, 231, 23))
        self.master_IP_ROC.setStyleSheet("color: rgb(199, 199, 199);\n"
                                         "background: rgba(29, 222, 216, 0.1);")
        self.master_IP_ROC.setObjectName("master_IP_ROC")
        self.hostname_ROC = QtWidgets.QLineEdit(self.rosSettingsROC)
        self.hostname_ROC.setGeometry(QtCore.QRect(90, 118, 231, 23))
        self.hostname_ROC.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.hostname_ROC.setObjectName("hostname_ROC")
        self.namespace_ROC = QtWidgets.QLineEdit(self.rosSettingsROC)
        self.namespace_ROC.setGeometry(QtCore.QRect(90, 148, 231, 23))
        self.namespace_ROC.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                         "color: rgb(199, 199, 199);")
        self.namespace_ROC.setObjectName("namespace_ROC")
        self.my_IP_ROC_Label = QtWidgets.QLabel(self.rosSettingsROC)
        self.my_IP_ROC_Label.setGeometry(QtCore.QRect(5, 32, 71, 16))
        self.my_IP_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.my_IP_ROC_Label.setObjectName("my_IP_ROC_Label")
        self.master_IP_ROC_Label = QtWidgets.QLabel(self.rosSettingsROC)
        self.master_IP_ROC_Label.setGeometry(QtCore.QRect(5, 62, 71, 16))
        self.master_IP_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_IP_ROC_Label.setObjectName("master_IP_ROC_Label")
        self.hostname_ROC_Label = QtWidgets.QLabel(self.rosSettingsROC)
        self.hostname_ROC_Label.setGeometry(QtCore.QRect(5, 120, 71, 16))
        self.hostname_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.hostname_ROC_Label.setObjectName("hostname_ROC_Label")
        self.namespace_ROC_Label = QtWidgets.QLabel(self.rosSettingsROC)
        self.namespace_ROC_Label.setGeometry(QtCore.QRect(5, 150, 81, 16))
        self.namespace_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.namespace_ROC_Label.setObjectName("namespace_ROC_Label")
        self.master_URI_ROC_Label = QtWidgets.QLabel(self.rosSettingsROC)
        self.master_URI_ROC_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.master_URI_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.master_URI_ROC_Label.setObjectName("master_URI_ROC_Label")
        self.master_URI_ROC = QtWidgets.QLineEdit(self.rosSettingsROC)
        self.master_URI_ROC.setGeometry(QtCore.QRect(90, 88, 231, 23))
        self.master_URI_ROC.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                          "color: rgb(199, 199, 199);")
        self.master_URI_ROC.setObjectName("master_URI_ROC")
        self.connectionROC = QtWidgets.QGroupBox(rocConfigure)
        self.connectionROC.setGeometry(QtCore.QRect(7, 10, 326, 181))
        self.connectionROC.setStyleSheet("color: rgb(14, 172, 186);")
        self.connectionROC.setObjectName("connectionROC")
        self.user_ROC = QtWidgets.QLineEdit(self.connectionROC)
        self.user_ROC.setGeometry(QtCore.QRect(110, 58, 210, 23))
        self.user_ROC.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                    "color: rgb(199, 199, 199);")
        self.user_ROC.setObjectName("user_ROC")
        self.password_ROC = QtWidgets.QLineEdit(self.connectionROC)
        self.password_ROC.setGeometry(QtCore.QRect(110, 88, 210, 23))
        self.password_ROC.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                        "color: rgb(199, 199, 199);")
        self.password_ROC.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_ROC.setObjectName("password_ROC")
        self.port_ROC_Label = QtWidgets.QLabel(self.connectionROC)
        self.port_ROC_Label.setGeometry(QtCore.QRect(5, 120, 81, 16))
        self.port_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.port_ROC_Label.setObjectName("port_ROC_Label")
        self.port_ROC = QtWidgets.QLineEdit(self.connectionROC)
        self.port_ROC.setGeometry(QtCore.QRect(110, 118, 210, 23))
        self.port_ROC.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                    "color: rgb(199, 199, 199);")
        self.port_ROC.setObjectName("port_ROC")
        self.user_ROC_Label = QtWidgets.QLabel(self.connectionROC)
        self.user_ROC_Label.setGeometry(QtCore.QRect(5, 60, 71, 16))
        self.user_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.user_ROC_Label.setObjectName("user_ROC_Label")
        self.password_ROC_Label = QtWidgets.QLabel(self.connectionROC)
        self.password_ROC_Label.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.password_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.password_ROC_Label.setObjectName("password_ROC_Label")
        self.ssh_Hostname_ROC = QtWidgets.QLineEdit(self.connectionROC)
        self.ssh_Hostname_ROC.setGeometry(QtCore.QRect(110, 148, 210, 23))
        self.ssh_Hostname_ROC.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                   "color: rgb(199, 199, 199);")
        self.ssh_Hostname_ROC.setObjectName("ssh_Hostname_ROC")
        self.ssh_Hostname_ROC_Label = QtWidgets.QLabel(self.connectionROC)
        self.ssh_Hostname_ROC_Label.setGeometry(QtCore.QRect(5, 150, 81, 16))
        self.ssh_Hostname_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.ssh_Hostname_ROC_Label.setObjectName("ssh_Hostname_ROC_Label")
        self.type_ROC_Label = QtWidgets.QLabel(self.connectionROC)
        self.type_ROC_Label.setGeometry(QtCore.QRect(5, 30, 71, 16))
        self.type_ROC_Label.setStyleSheet("color: rgb(199, 199, 199);")
        self.type_ROC_Label.setObjectName("type_ROC_Label")
        self.type_ROC = QtWidgets.QComboBox(self.connectionROC)
        self.type_ROC.setGeometry(QtCore.QRect(110, 28, 211, 23))
        self.type_ROC.setStyleSheet("color: rgb(199, 199, 199);")
        self.type_ROC.setObjectName("type_ROC")
        self.type_ROC.addItem("")
        self.type_ROC.addItem("")
        self.type_ROC.addItem("")
        self.buttons_Config_ROC = QtWidgets.QDialogButtonBox(rocConfigure)
        self.buttons_Config_ROC.setGeometry(QtCore.QRect(90, 393, 166, 24))
        self.buttons_Config_ROC.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons_Config_ROC.setObjectName("buttons_Config_ROC")
        self.buttons_Config_ROC.accepted.connect(self.okButton)

        self.my_IP_ROC_Label.setBuddy(self.my_IP_ROC)
        self.master_IP_ROC_Label.setBuddy(self.master_IP_ROC)
        self.hostname_ROC_Label.setBuddy(self.hostname_ROC)
        self.namespace_ROC_Label.setBuddy(self.namespace_ROC)
        self.master_URI_ROC_Label.setBuddy(self.master_URI_ROC)
        self.port_ROC_Label.setBuddy(self.port_ROC)
        self.user_ROC_Label.setBuddy(self.user_ROC)
        self.password_ROC_Label.setBuddy(self.password_ROC)
        self.ssh_Hostname_ROC_Label.setBuddy(self.port_ROC)
        self.type_ROC_Label.setBuddy(self.user_ROC)

        self.retranslateUi(rocConfigure)
        self.buttons_Config_ROC.rejected.connect(rocConfigure.reject)
        rocConfigure.accepted.connect(rocConfigure.accept)
        QtCore.QMetaObject.connectSlotsByName(rocConfigure)

    def retranslateUi(self, rocConfigure):
        _translate = QtCore.QCoreApplication.translate
        rocConfigure.setWindowTitle(_translate("rocConfigure", "Settings and Configurations"))
        self.rosSettingsROC.setTitle(_translate("rocConfigure", "ROC Environment Variables:"))
        self.my_IP_ROC.setPlaceholderText(_translate("rocConfigure", "ex.:192.168.43.87"))
        self.master_IP_ROC.setPlaceholderText(_translate("rocConfigure", "ex.: 192.168.43.87"))
        self.hostname_ROC.setPlaceholderText(_translate("rocConfigure", "ex.:192.168.43.87"))
        self.namespace_ROC.setPlaceholderText(_translate("rocConfigure", "ex.:roc"))
        self.my_IP_ROC_Label.setText(_translate("rocConfigure", "ROS_MY_IP:"))
        self.master_IP_ROC_Label.setText(_translate("rocConfigure", "MASTER_IP:"))
        self.hostname_ROC_Label.setText(_translate("rocConfigure", "HOSTNAME:"))
        self.namespace_ROC_Label.setText(_translate("rocConfigure", "NAMESPACE:"))
        self.master_URI_ROC_Label.setText(_translate("rocConfigure", "MASTER_URI:"))
        self.master_URI_ROC.setPlaceholderText(_translate("rocConfigure", "ex.: http://localhost:11311"))
        self.connectionROC.setTitle(_translate("rocConfigure", "Connection Setup"))
        self.user_ROC.setPlaceholderText(_translate("rocConfigure", "ex.: turtlebot"))
        self.password_ROC.setPlaceholderText(_translate("rocConfigure", "ex.: turtlebot"))
        self.port_ROC_Label.setText(_translate("rocConfigure", "PORT:"))
        self.port_ROC.setPlaceholderText(_translate("rocConfigure", "ex.: 80"))
        self.user_ROC_Label.setText(_translate("rocConfigure", "USER:"))
        self.password_ROC_Label.setText(_translate("rocConfigure", "PASSWORD:"))
        self.ssh_Hostname_ROC.setPlaceholderText(_translate("rocConfigure", "ex.:192.168.43.87"))
        self.ssh_Hostname_ROC_Label.setText(_translate("rocConfigure", "HOSTNAME"))
        self.type_ROC_Label.setText(_translate("rocConfigure", "TYPE:"))
        self.type_ROC.setItemText(0, _translate("rocConfigure", "DEFAULT"))
        self.type_ROC.setItemText(1, _translate("rocConfigure", "IP/UTP"))
        self.type_ROC.setItemText(2, _translate("rocConfigure", "CLOUD"))

    def okButton(self, *kwargs):
        # ENV CONFIG
        connection_Value = self.type_ROC.currentText()
        my_IP_ROC_Value = self.my_IP_ROC.text()
        master_IP_ROC_Value = self.master_IP_ROC.text()
        master_URI_ROC_Value = self.master_URI_ROC.text()
        hostname_ROC_Value = self.hostname_ROC.text()
        namespace_ROC_Value = self.namespace_ROC.text()
        # SSH CONNECTION
        user_ROC_Value = self.user_ROC.text()
        password_ROC_Value = self.password_ROC.text()
        port_ROC_Value = self.port_ROC.text()
        ssh_Hostname_ROC_Value = self.ssh_Hostname_ROC.text()
        # XML CREATION
        environmentXMLFile = et.Element('ROC_Settings')
        comment = et.Comment("ROC Environment and Configurations Variables")
        environmentXMLFile.append(comment)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROC_CONNECTION')
        environmentConfig.text = str(connection_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROC_MY_IP')
        environmentConfig.text = str(my_IP_ROC_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROC_MASTER_IP')
        environmentConfig.text = str(master_IP_ROC_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROC_MASTER_URI')
        environmentConfig.text = str(master_URI_ROC_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROC_HOSTNAME')
        environmentConfig.text = str(hostname_ROC_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROC_NAMESPACE')
        environmentConfig.text = str(namespace_ROC_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_ROC_USER')
        environmentConfig.text = str(user_ROC_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_ROC_PASSWORD')
        environmentConfig.text = str(password_ROC_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_ROC_PORT')
        environmentConfig.text = str(port_ROC_Value)
        environmentConfig = et.SubElement(environmentXMLFile, 'SSH_ROC_KEY')
        environmentConfig.text = str(ssh_Hostname_ROC_Value)
        tree = et.ElementTree(environmentXMLFile)
        tree.write('rocSettings.xml', encoding='utf8')
        # CHANGE THE PLACEHOLDER
        _translate = QtCore.QCoreApplication.translate
        self.my_IP_ROC.setPlaceholderText(_translate("rocConfigure",  my_IP_ROC_Value))
        self.master_IP_ROC.setPlaceholderText(_translate("rocConfigure", master_IP_ROC_Value))
        self.master_URI_ROC.setPlaceholderText(_translate("rocConfigure", master_URI_ROC_Value))
        self.hostname_ROC.setPlaceholderText(_translate("rocConfigure", hostname_ROC_Value))
        self.namespace_ROC.setPlaceholderText(_translate("rocConfigure", namespace_ROC_Value))
        self.user_ROC.setPlaceholderText(_translate("rocConfigure", user_ROC_Value))
        self.password_ROC.setPlaceholderText(_translate("rocConfigure", password_ROC_Value))
        self.port_ROC.setPlaceholderText(_translate("rocConfigure", port_ROC_Value))
        self.ssh_Hostname_ROC.setPlaceholderText(_translate("rocConfigure", ssh_Hostname_ROC_Value))
        # Reads the XML File
        xmlFile = et.parse('rocSettings.xml')
        # Find the root element from the file (in this case "environment")
        root = xmlFile.getroot()
        # Load the XML values from environment file and Create an String to Run with Popen
        exportMyIP = str('export ROS_MY_IP='+ root.findtext('ROC_MY_IP'))
        exportMasterIP = str('export ROS_MASTER_IP='+ root.findtext('ROC_MASTER_IP'))
        exportMasterIPURI = str('export ROS_MASTER_URI='+ str(root.findtext('ROC_MASTER_URI')))
        exportHostname = str('export ROS_HOSTNAME='+ root.findtext('ROC_HOSTNAME'))
        exportNamespace = str('export ROS_NAMESPACE='+ str(root.findtext('ROC_NAMESPACE')))
        # Export the values to "~/.bashrc"
        exportMyIPCommand = str("echo "+exportMyIP+" >> ~/.bashrc")
        exportMasterIPCommand = str("echo "+exportMasterIP+" >> ~/.bashrc")
        exportIPURICommand = str("echo '"+'"'+exportMasterIPURI+'"'+" >> ~/.bashrc")
        exportHostnameCommand = str("echo "+exportHostname+" >> ~/.bashrc")
        exportNamespaceCommand = str("echo '"+'"'+exportNamespace+'"'+" >> ~/.bashrc")

        # print(exportMyIPCommand)
        # print(exportMasterIPCommand)
        # print(exportIPURICommand)
        # print(exportHostnameCommand)
        # print(exportNamespaceCommand)

        try:
            exportMyIPProcess = subprocess.Popen(exportMyIPCommand, stdout=PIPE,
                                                 stdin=PIPE, shell=True)
            exportMasterIPProcess = subprocess.Popen(exportMasterIPCommand, stdout=PIPE,
                                                     stdin=PIPE, shell=True)
            exportIPURIProcess = subprocess.Popen(exportIPURICommand, stdout=PIPE,
                                                  stdin=PIPE, shell=True)
            exportHostnameProcess = subprocess.Popen(exportHostnameCommand, stdout=PIPE,
                                                     stdin=PIPE, shell=True)
            exportNamespaceProcess = subprocess.Popen(exportNamespaceCommand, stdout=PIPE,
                                                      stdin=PIPE, shell=True)
            operationSucess()
            self.close()
        
        except:
            operationError()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rocConfigure = QtWidgets.QDialog()
    ui = Ui_rocConfigure()
    ui.setupUi(rocConfigure)
    rocConfigure.show()
    sys.exit(app.exec_())

