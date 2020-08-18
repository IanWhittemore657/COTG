# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Navigation.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog
from WorkQuestions import Ui_Dialog
from ContractFeed import Ui_ContractFeedPresent

class Ui_Secondwindow(object):

    def __init__(self,email,birth,edu,lead,workyears):

        self.email = email
        self.birth = birth
        self.edu = edu             
        self.lead = lead
        self.workyears = workyears

    def setupUi(self, Secondwindow):
        Secondwindow.setObjectName("Secondwindow")
        Secondwindow.resize(798, 592)
        Secondwindow.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.centralwidget = QtWidgets.QWidget(Secondwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 591, 181))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.YesRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.YesRadioButton.setGeometry(QtCore.QRect(190, 250, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.YesRadioButton.setFont(font)
        self.YesRadioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.YesRadioButton.setObjectName("YesRadioButton")
        self.YesButNotworkingRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.YesButNotworkingRadioButton.setGeometry(QtCore.QRect(190, 340, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.YesButNotworkingRadioButton.setFont(font)
        self.YesButNotworkingRadioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.YesButNotworkingRadioButton.setObjectName("YesButNotworkingRadioButton")
        self.NoRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.NoRadioButton.setGeometry(QtCore.QRect(190, 430, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NoRadioButton.setFont(font)
        self.NoRadioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.NoRadioButton.setObjectName("NoRadioButton")
        self.NextForm = QtWidgets.QPushButton(self.centralwidget)
        self.NextForm.setGeometry(QtCore.QRect(700, 540, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NextForm.setFont(font)
        self.NextForm.setAutoFillBackground(False)
        self.NextForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NextForm.setObjectName("NextForm")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(10, 540, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setAutoFillBackground(False)
        self.Back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Back.setObjectName("Back")
        Secondwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Secondwindow)
        self.statusbar.setObjectName("statusbar")
        Secondwindow.setStatusBar(self.statusbar)

        self.retranslateUi(Secondwindow)
        QtCore.QMetaObject.connectSlotsByName(Secondwindow)

        self.NextForm.clicked.connect(self.pressed)
        self.NextForm.clicked.connect(Secondwindow.close)
        self.YesRadioButton.setChecked(True) # start with it selected to yes to remove errors if they click next (No empty field)

    def pressed(self):

        if(self.YesRadioButton.isChecked()):
            print("working")
            self.NavigationToWork(self.email,self.birth,self.edu,self.lead,self.workyears)
            

        elif(self.YesButNotworkingRadioButton.isChecked()):
            print("not working but has")
            self.NavigationToWork(self.email,self.birth,self.edu,self.lead,self.workyears)
            
           
        elif(self.NoRadioButton.isChecked()):
            print("never worked")
            self.NavigationToQuestions(self.email,self.birth,self.edu,self.lead,self.workyears)
            


    def NavigationToQuestions(self,email,birth,edu,lead,workyears):
        self.main = QtWidgets.QMainWindow() 

        self.ui = Ui_ContractFeedPresent(self.email,self.birth,self.edu,self.lead,self.workyears) 
        self.ui.setupUi(self.main)
        self.main.show()        
            
    
    def NavigationToWork(self,email,birth,edu,lead,workyears):
        self.main = QtWidgets.QMainWindow() 

        self.ui = Ui_Dialog(self.email,self.birth,self.edu,self.lead,self.workyears) 
        self.ui.setupUi(self.main)
        self.main.show()        

    def retranslateUi(self, Secondwindow):
        _translate = QtCore.QCoreApplication.translate
        Secondwindow.setWindowTitle(_translate("Secondwindow", "COTG"))
        self.label.setText(_translate("Secondwindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Are you / Have you worked in an organisation </span></p><p align=\"center\"><span style=\" font-size:22pt;\">either recently or currently?</span></p></body></html>"))
        self.YesRadioButton.setToolTip(_translate("Secondwindow", "Click this if you are currently working"))
        self.YesRadioButton.setText(_translate("Secondwindow", "Currently working in an organisation         "))
        self.YesButNotworkingRadioButton.setToolTip(_translate("Secondwindow", "Click this if you have previously worked"))
        self.YesButNotworkingRadioButton.setText(_translate("Secondwindow", "Not working but have worked before         "))
        self.NoRadioButton.setToolTip(_translate("Secondwindow", "Click this if you have never worked in an organisation before "))
        self.NoRadioButton.setText(_translate("Secondwindow", "Have not worked in an organisation           "))
        self.NextForm.setStatusTip(_translate("Secondwindow", "Click this to go to next stages of questions"))
        self.NextForm.setText(_translate("Secondwindow", "Next"))
        self.Back.setStatusTip(_translate("Secondwindow", "Click this to return to previous form"))
        self.Back.setText(_translate("Secondwindow", "Back"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Secondwindow = QtWidgets.QMainWindow()
    ui = Ui_Secondwindow()
    ui.setupUi(Secondwindow)
    Secondwindow.show()
    app.exec_()