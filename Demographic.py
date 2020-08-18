# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Demographic.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QShortcut , QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog , QAction ,QShortcut
from Navigation import Ui_Secondwindow


class Ui_StartScreen(object):
    def setupUi(self, StartScreen):
        StartScreen.setObjectName("StartScreen")
        StartScreen.resize(799, 574)
        StartScreen.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.label = QtWidgets.QLabel(StartScreen)
        self.label.setGeometry(QtCore.QRect(160, 10, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(StartScreen)
        self.label_2.setGeometry(QtCore.QRect(180, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.EmailAddress = QtWidgets.QLineEdit(StartScreen)
        self.EmailAddress.setGeometry(QtCore.QRect(410, 100, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EmailAddress.setFont(font)
        self.EmailAddress.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EmailAddress.setObjectName("EmailAddress")
        self.CountryBirth = QtWidgets.QComboBox(StartScreen)
        self.CountryBirth.setGeometry(QtCore.QRect(410, 180, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CountryBirth.setFont(font)
        self.CountryBirth.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CountryBirth.setMaxVisibleItems(10)
        self.CountryBirth.setObjectName("CountryBirth")
        self.CountryBirth.addItem("")
        self.CountryBirth.addItem("")
        self.CountryBirth.addItem("")
        self.label_3 = QtWidgets.QLabel(StartScreen)
        self.label_3.setGeometry(QtCore.QRect(180, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Education = QtWidgets.QComboBox(StartScreen)
        self.Education.setGeometry(QtCore.QRect(410, 260, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Education.setFont(font)
        self.Education.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Education.setMaxVisibleItems(10)
        self.Education.setObjectName("Education")
        self.Education.addItem("")
        self.Education.addItem("")
        self.Education.addItem("")
        self.Education.addItem("")
        self.label_4 = QtWidgets.QLabel(StartScreen)
        self.label_4.setGeometry(QtCore.QRect(180, 260, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(StartScreen)
        self.label_5.setGeometry(QtCore.QRect(180, 340, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.TeamLead = QtWidgets.QComboBox(StartScreen)
        self.TeamLead.setGeometry(QtCore.QRect(410, 340, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TeamLead.setFont(font)
        self.TeamLead.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TeamLead.setMaxVisibleItems(10)
        self.TeamLead.setObjectName("TeamLead")
        self.TeamLead.addItem("")
        self.TeamLead.addItem("")
        self.TeamLead.addItem("")
        self.label_6 = QtWidgets.QLabel(StartScreen)
        self.label_6.setGeometry(QtCore.QRect(180, 420, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.YearsWork = QtWidgets.QComboBox(StartScreen)
        self.YearsWork.setGeometry(QtCore.QRect(410, 420, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.YearsWork.setFont(font)
        self.YearsWork.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YearsWork.setMaxVisibleItems(10)
        self.YearsWork.setObjectName("YearsWork")
        self.YearsWork.addItem("")
        self.YearsWork.addItem("")
        self.YearsWork.addItem("")
        self.YearsWork.addItem("")
        self.YearsWork.addItem("")
        self.NextPage = QtWidgets.QPushButton(StartScreen)
        self.NextPage.setGeometry(QtCore.QRect(340, 510, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NextPage.setFont(font)
        self.NextPage.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.NextPage.setObjectName("NextPage")

        self.NextPage.clicked.connect(self.pressed)
        

        self.retranslateUi(StartScreen)
        self.CountryBirth.setCurrentIndex(-1)
        self.Education.setCurrentIndex(-1)
        self.TeamLead.setCurrentIndex(-1)
        self.YearsWork.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(StartScreen)

    def pressed(self):

        if(self.EmailAddress.text() == "" or self.CountryBirth.currentText() == "" or self.Education.currentText() == "" or self.TeamLead.currentText() == "" or self.YearsWork.currentText() == ""):
            self.messagebox("Error","Please enter all fields")
        else:
            self.email = self.EmailAddress.text()
            self.birth = self.CountryBirth.currentText()
            self.edu = self.Education.currentText()
            self.lead = self.TeamLead.currentText()
            self.workyears = self.YearsWork.currentText()
           
            self.DemoToNavigation(self.email,self.birth,self.edu,self.lead,self.workyears)
            StartScreen.hide()


    def DemoToNavigation(self,email,birth,edu,lead,workyears): 

        self.main = QtWidgets.QMainWindow() 

        self.ui = Ui_Secondwindow(self.email,self.birth,self.edu,self.lead,self.workyears) 
        self.ui.setupUi(self.main)
        self.main.show()        

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()   

    def retranslateUi(self, StartScreen):
        _translate = QtCore.QCoreApplication.translate
        StartScreen.setWindowTitle(_translate("StartScreen", "COTG"))
        self.label.setText(_translate("StartScreen", "Please enter the following questions"))
        self.label_2.setText(_translate("StartScreen", "Email Address"))
        self.EmailAddress.setToolTip(_translate("StartScreen", "Please enter your email address"))
        self.CountryBirth.setToolTip(_translate("StartScreen", "Please enter your country of birth"))
        self.CountryBirth.setItemText(0, _translate("StartScreen", "United Kingdom"))
        self.CountryBirth.setItemText(1, _translate("StartScreen", "South Africa"))
        self.CountryBirth.setItemText(2, _translate("StartScreen", "United States"))
        self.label_3.setText(_translate("StartScreen", "Country of Birth"))
        self.Education.setToolTip(_translate("StartScreen", "Please enter your highest level of education"))
        self.Education.setItemText(0, _translate("StartScreen", "A Levels"))
        self.Education.setItemText(1, _translate("StartScreen", "Undergaduate Degree"))
        self.Education.setItemText(2, _translate("StartScreen", "Masters Degree"))
        self.Education.setItemText(3, _translate("StartScreen", "PhD"))
        self.label_4.setText(_translate("StartScreen", "Highest Education"))
        self.label_5.setText(_translate("StartScreen", "The team you lead"))
        self.TeamLead.setToolTip(_translate("StartScreen", "Please enter what team you lead"))
        self.TeamLead.setItemText(0, _translate("StartScreen", "Project Team"))
        self.TeamLead.setItemText(1, _translate("StartScreen", "Organisational Team"))
        self.TeamLead.setItemText(2, _translate("StartScreen", "None"))
        self.label_6.setText(_translate("StartScreen", "Years in active work"))
        self.YearsWork.setToolTip(_translate("StartScreen", "Please enter how many years in active work you have"))
        self.YearsWork.setItemText(0, _translate("StartScreen", "Less than 1 Year"))
        self.YearsWork.setItemText(1, _translate("StartScreen", "2  -  5   Years"))
        self.YearsWork.setItemText(2, _translate("StartScreen", "6  - 10  Years"))
        self.YearsWork.setItemText(3, _translate("StartScreen", "11 - 15 Years"))
        self.YearsWork.setItemText(4, _translate("StartScreen", "More than 16 Years"))
        self.NextPage.setToolTip(_translate("StartScreen", "Click this when ready to continue"))
        self.NextPage.setText(_translate("StartScreen", "Next"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartScreen = QtWidgets.QDialog()
    ui = Ui_StartScreen()
    ui.setupUi(StartScreen)
    StartScreen.show()
    app.exec_()
