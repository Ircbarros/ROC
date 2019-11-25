# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import vectors
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

class Ui_aboutDialog(object):

    """About and Informations Dialog Screen"""

    def aboutWebActions(self, **kwargs):
        """ Responsible to Handle all the Buttons that lead to an web page """
        # If the dictionary item value 'button' is 'tiago' open his webpage
        if kwargs['button']=='tiago':
            # Only 1 click at every 5 seconds
            self.tiago_Contact.setDown(True)
            QTimer.singleShot(5000, lambda: self.tiago_Contact.setDown(False))
            webbrowser.open('https://sites.google.com/view/tiagopn/')

        # If the dictionary item value 'button' is 'italo' open his webpage
        elif kwargs['button']=='italo':
            # Only 1 click at every 5 seconds
            self.italo_Contact.setDown(True)
            QTimer.singleShot(5000, lambda: self.italo_Contact.setDown(False))
            webbrowser.open('https://www.linkedin.com/in/ircbarros/?locale=en_US')

    def setupUi(self, aboutDialog):
        """ Here starts the Code and Definitions  for The Dialog Application """
        # About Design
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(400, 300)
        aboutDialog.setMinimumSize(QtCore.QSize(400, 300))
        aboutDialog.setMaximumSize(QtCore.QSize(400, 300))
        aboutDialog.setStyleSheet("background: #2A2E37;")
        self.main_Text = QtWidgets.QLabel(aboutDialog)
        self.main_Text.setGeometry(QtCore.QRect(70, 40, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.main_Text.setFont(font)
        self.main_Text.setStyleSheet("color: rgb(252, 255, 255);\n"
                                     "")
        self.main_Text.setObjectName("main_Text")
        self.roc_Logo = QtWidgets.QFrame(aboutDialog)
        self.roc_Logo.setGeometry(QtCore.QRect(220, 50, 161, 211))
        self.roc_Logo.setAutoFillBackground(False)
        self.roc_Logo.setStyleSheet("image: url(:/logos/roc_Logo.png);")
        self.roc_Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.roc_Logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roc_Logo.setObjectName("roc_Logo")
        self.laser_Logo = QtWidgets.QFrame(aboutDialog)
        self.laser_Logo.setGeometry(QtCore.QRect(168, 5, 51, 31))
        self.laser_Logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.laser_Logo.setAutoFillBackground(False)
        self.laser_Logo.setStyleSheet("image: url(:/logos/laser_logo.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.laser_Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.laser_Logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.laser_Logo.setObjectName("laser_Logo")
        self.superior_Line = QtWidgets.QFrame(aboutDialog)
        self.superior_Line.setGeometry(QtCore.QRect(30, 60, 340, 1))
        self.superior_Line.setStyleSheet("background-color:  rgb(142, 255, 242);")
        self.superior_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.superior_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.superior_Line.setObjectName("superior_Line")
        self.inferior_Line = QtWidgets.QFrame(aboutDialog)
        self.inferior_Line.setGeometry(QtCore.QRect(30, 240, 340, 1))
        self.inferior_Line.setStyleSheet("background-color:  rgb(142, 255, 242);")
        self.inferior_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.inferior_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.inferior_Line.setObjectName("inferior_Line")
        self.roc_Text = QtWidgets.QLabel(aboutDialog)
        self.roc_Text.setGeometry(QtCore.QRect(40, 130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.roc_Text.setFont(font)
        self.roc_Text.setStyleSheet("color: rgb(252, 255, 255);\n"
                                    "")
        self.roc_Text.setObjectName("roc_Text")
        self.version_Text = QtWidgets.QLabel(aboutDialog)
        self.version_Text.setGeometry(QtCore.QRect(75, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.version_Text.setFont(font)
        self.version_Text.setStyleSheet("color: rgb(252, 255, 255);\n"
                                        "")
        self.version_Text.setObjectName("version_Text")
        # Tiago Nascimento Command Link Button
        self.tiago_Contact = QtWidgets.QCommandLinkButton(aboutDialog)
        self.tiago_Contact.setGeometry(QtCore.QRect(56, 260, 135, 35))
        font = QtGui.QFont()
        font.setFamily("Droid Arabic Naskh")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.tiago_Contact.setFont(font)
        self.tiago_Contact.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tiago_Contact.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(142, 255, 242);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vectors/Contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tiago_Contact.setIcon(icon)
        self.tiago_Contact.setIconSize(QtCore.QSize(15, 15))
        self.tiago_Contact.setObjectName("tiago_Contact")
        self.tiago_Contact.clicked.connect(lambda: self.aboutWebActions(button='tiago'))
        self.tiago_Text = QtWidgets.QLabel(aboutDialog)
        self.tiago_Text.setGeometry(QtCore.QRect(60, 245, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.tiago_Text.setFont(font)
        self.tiago_Text.setStyleSheet("color: rgb(252, 255, 255);\n"
                                      "")
        self.tiago_Text.setObjectName("tiago_Text")
        # Italo Button
        self.italo_Contact = QtWidgets.QCommandLinkButton(aboutDialog)
        self.italo_Contact.setGeometry(QtCore.QRect(208, 260, 161, 35))
        font = QtGui.QFont()
        font.setFamily("Droid Arabic Naskh")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.italo_Contact.setFont(font)
        self.italo_Contact.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.italo_Contact.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(142, 255, 242);")
        self.italo_Contact.setIcon(icon)
        self.italo_Contact.setIconSize(QtCore.QSize(15, 15))
        self.italo_Contact.setObjectName("italo_Contact")
        self.italo_Contact.clicked['bool'].connect(lambda: self.aboutWebActions(button='italo'))
        self.italo_Text = QtWidgets.QLabel(aboutDialog)
        self.italo_Text.setGeometry(QtCore.QRect(260, 246, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.italo_Text.setFont(font)
        self.italo_Text.setStyleSheet("color: rgb(252, 255, 255);\n"
                                      "")
        self.italo_Text.setObjectName("italo_Text")
        # Raises this widget to the top of the parent widget’s stack
        self.roc_Logo.raise_()
        self.laser_Logo.raise_()
        self.main_Text.raise_()
        self.superior_Line.raise_()
        self.inferior_Line.raise_()
        self.tiago_Text.raise_()
        self.tiago_Contact.raise_()
        self.italo_Text.raise_()
        self.italo_Contact.raise_()
        self.roc_Text.raise_()
        self.version_Text.raise_()

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        """ This function is responsible to Translate the Names 
        and Place the Button Tips Informations
        """
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About and Contact"))
        self.main_Text.setText(_translate("aboutDialog", "Laboratory of Systems Engineering and Robotics"))
        self.tiago_Contact.setToolTip(_translate("aboutDialog", "Contact Tiago Nascimento"))
        self.tiago_Contact.setText(_translate("aboutDialog", "tiagopn@ci.ufpb.br"))
        self.laser_Logo.setToolTip(_translate("aboutDialog", "Go to LASER Website"))
        self.tiago_Text.setText(_translate("aboutDialog", "Laboratory Header/Faculty Member"))
        self.italo_Contact.setToolTip(_translate("aboutDialog", "Contact Ítalo Barros"))
        self.italo_Contact.setText(_translate("aboutDialog", "italorenan_@hotmail.com"))
        self.italo_Text.setText(_translate("aboutDialog", "Main Developer"))
        self.roc_Text.setText(_translate("aboutDialog", "Robot Operational Controller (ROC)"))
        self.version_Text.setText(_translate("aboutDialog", "Version Alpha 0.1"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutDialog = QtWidgets.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())