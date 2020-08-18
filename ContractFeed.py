# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ContractFeed.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QShortcut , QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog , QAction ,QShortcut
from PresentPause import Ui_PauseOtherTrust
from collections import Counter 

thisdict = {"Never":0,
            "Very Rarely":1,
            "Rarely":2,
            "Sometimes":3,
            "Often":4,
            "Always":5}


class Ui_ContractFeedPresent(object):

    def __init__(self,email,birth,edu,lead,workyears):

        self.email = email
        self.birth = birth
        self.edu = edu             #lines 16 to 20 are getting the detials from the login screen to call on the DB here
        self.lead = lead
        self.workyears = workyears

      #  print("contractFeed")


    def setupUi(self, ContractFeedPresent):
        ContractFeedPresent.setObjectName("ContractFeedPresent")
        ContractFeedPresent.resize(822, 840)
        ContractFeedPresent.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.label = QtWidgets.QLabel(ContractFeedPresent)
        self.label.setGeometry(QtCore.QRect(200, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ContractFeedPresent)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ContractFeedPresent)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ContractFeedPresent)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ContractFeedPresent)
        self.label_5.setGeometry(QtCore.QRect(10, 350, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(ContractFeedPresent)
        self.label_6.setGeometry(QtCore.QRect(10, 440, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(ContractFeedPresent)
        self.label_7.setGeometry(QtCore.QRect(10, 500, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.NextQuestions = QtWidgets.QPushButton(ContractFeedPresent)
        self.NextQuestions.setGeometry(QtCore.QRect(700, 790, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NextQuestions.setFont(font)
        self.NextQuestions.setAutoFillBackground(False)
        self.NextQuestions.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NextQuestions.setObjectName("NextQuestions")
        self.label_8 = QtWidgets.QLabel(ContractFeedPresent)
        self.label_8.setGeometry(QtCore.QRect(10, 590, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(ContractFeedPresent)
        self.label_9.setGeometry(QtCore.QRect(10, 710, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(ContractFeedPresent)
        self.label_10.setGeometry(QtCore.QRect(10, 650, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(ContractFeedPresent)
        self.line.setGeometry(QtCore.QRect(0, 140, 831, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(ContractFeedPresent)
        self.line_2.setGeometry(QtCore.QRect(0, 230, 831, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(ContractFeedPresent)
        self.line_3.setGeometry(QtCore.QRect(0, 320, 831, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(ContractFeedPresent)
        self.line_4.setGeometry(QtCore.QRect(0, 410, 831, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(ContractFeedPresent)
        self.line_5.setGeometry(QtCore.QRect(0, 470, 831, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(ContractFeedPresent)
        self.line_6.setGeometry(QtCore.QRect(0, 560, 831, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(ContractFeedPresent)
        self.line_7.setGeometry(QtCore.QRect(-10, 620, 831, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(ContractFeedPresent)
        self.line_8.setGeometry(QtCore.QRect(0, 690, 831, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(ContractFeedPresent)
        self.line_9.setGeometry(QtCore.QRect(0, 760, 831, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.Back = QtWidgets.QPushButton(ContractFeedPresent)
        self.Back.setGeometry(QtCore.QRect(10, 790, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setAutoFillBackground(False)
        self.Back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Back.setObjectName("Back")
        self.ContractQ1 = QtWidgets.QComboBox(ContractFeedPresent)
        self.ContractQ1.setGeometry(QtCore.QRect(680, 90, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ContractQ1.setFont(font)
        self.ContractQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ContractQ1.setMaxVisibleItems(6)
        self.ContractQ1.setObjectName("ContractQ1")
        self.ContractQ1.addItem("")
        self.ContractQ1.addItem("")
        self.ContractQ1.addItem("")
        self.ContractQ1.addItem("")
        self.ContractQ1.addItem("")
        self.ContractQ1.addItem("")
        self.ContractQ2 = QtWidgets.QComboBox(ContractFeedPresent)
        self.ContractQ2.setGeometry(QtCore.QRect(680, 180, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ContractQ2.setFont(font)
        self.ContractQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ContractQ2.setMaxVisibleItems(6)
        self.ContractQ2.setObjectName("ContractQ2")
        self.ContractQ2.addItem("")
        self.ContractQ2.addItem("")
        self.ContractQ2.addItem("")
        self.ContractQ2.addItem("")
        self.ContractQ2.addItem("")
        self.ContractQ2.addItem("")
        self.ContractQ3 = QtWidgets.QComboBox(ContractFeedPresent)
        self.ContractQ3.setGeometry(QtCore.QRect(680, 270, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ContractQ3.setFont(font)
        self.ContractQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ContractQ3.setMaxVisibleItems(6)
        self.ContractQ3.setObjectName("ContractQ3")
        self.ContractQ3.addItem("")
        self.ContractQ3.addItem("")
        self.ContractQ3.addItem("")
        self.ContractQ3.addItem("")
        self.ContractQ3.addItem("")
        self.ContractQ3.addItem("")
        self.FeedQ1 = QtWidgets.QComboBox(ContractFeedPresent)
        self.FeedQ1.setGeometry(QtCore.QRect(680, 360, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FeedQ1.setFont(font)
        self.FeedQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FeedQ1.setMaxVisibleItems(6)
        self.FeedQ1.setObjectName("FeedQ1")
        self.FeedQ1.addItem("")
        self.FeedQ1.addItem("")
        self.FeedQ1.addItem("")
        self.FeedQ1.addItem("")
        self.FeedQ1.addItem("")
        self.FeedQ1.addItem("")
        self.FeedQ2 = QtWidgets.QComboBox(ContractFeedPresent)
        self.FeedQ2.setGeometry(QtCore.QRect(680, 440, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FeedQ2.setFont(font)
        self.FeedQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FeedQ2.setMaxVisibleItems(6)
        self.FeedQ2.setObjectName("FeedQ2")
        self.FeedQ2.addItem("")
        self.FeedQ2.addItem("")
        self.FeedQ2.addItem("")
        self.FeedQ2.addItem("")
        self.FeedQ2.addItem("")
        self.FeedQ2.addItem("")
        self.FeedQ3 = QtWidgets.QComboBox(ContractFeedPresent)
        self.FeedQ3.setGeometry(QtCore.QRect(680, 510, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FeedQ3.setFont(font)
        self.FeedQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FeedQ3.setMaxVisibleItems(6)
        self.FeedQ3.setObjectName("FeedQ3")
        self.FeedQ3.addItem("")
        self.FeedQ3.addItem("")
        self.FeedQ3.addItem("")
        self.FeedQ3.addItem("")
        self.FeedQ3.addItem("")
        self.FeedQ3.addItem("")
        self.PresentQ1 = QtWidgets.QComboBox(ContractFeedPresent)
        self.PresentQ1.setGeometry(QtCore.QRect(680, 590, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PresentQ1.setFont(font)
        self.PresentQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PresentQ1.setMaxVisibleItems(6)
        self.PresentQ1.setObjectName("PresentQ1")
        self.PresentQ1.addItem("")
        self.PresentQ1.addItem("")
        self.PresentQ1.addItem("")
        self.PresentQ1.addItem("")
        self.PresentQ1.addItem("")
        self.PresentQ1.addItem("")
        self.PresentQ2 = QtWidgets.QComboBox(ContractFeedPresent)
        self.PresentQ2.setGeometry(QtCore.QRect(680, 660, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PresentQ2.setFont(font)
        self.PresentQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PresentQ2.setMaxVisibleItems(6)
        self.PresentQ2.setObjectName("PresentQ2")
        self.PresentQ2.addItem("")
        self.PresentQ2.addItem("")
        self.PresentQ2.addItem("")
        self.PresentQ2.addItem("")
        self.PresentQ2.addItem("")
        self.PresentQ2.addItem("")
        self.PresentQ3 = QtWidgets.QComboBox(ContractFeedPresent)
        self.PresentQ3.setGeometry(QtCore.QRect(680, 720, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PresentQ3.setFont(font)
        self.PresentQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PresentQ3.setMaxVisibleItems(6)
        self.PresentQ3.setObjectName("PresentQ3")
        self.PresentQ3.addItem("")
        self.PresentQ3.addItem("")
        self.PresentQ3.addItem("")
        self.PresentQ3.addItem("")
        self.PresentQ3.addItem("")
        self.PresentQ3.addItem("")

        self.retranslateUi(ContractFeedPresent)
        self.ContractQ1.setCurrentIndex(-1)
        self.ContractQ2.setCurrentIndex(-1)
        self.ContractQ3.setCurrentIndex(-1)
        self.FeedQ1.setCurrentIndex(-1)
        self.FeedQ2.setCurrentIndex(-1)
        self.FeedQ3.setCurrentIndex(-1)
        self.PresentQ1.setCurrentIndex(-1)
        self.PresentQ2.setCurrentIndex(-1)
        self.PresentQ3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ContractFeedPresent)

        self.NextQuestions.clicked.connect(self.pressed)
        self.h = ContractFeedPresent

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()   

    def pressed(self):

        self.contracting = 0
        self.feedback = 0
        self.present = 0

        self.pointsself = 0
        self.pointsother = 0
        self.trust = 0

        self.confidentiatly = 0
        self.awareness = 0
        self.perspectives = 0

        self.listening = 0
        self.creative = 0
        self.delegation = 0

        self.actions = 0
        self.reflection = 0
        self.selfaware = 0



        if(self.ContractQ1.currentText() == "" or self.ContractQ2.currentText() == "" or self.ContractQ3.currentText() == "" or self.FeedQ1.currentText() == "" or self.FeedQ2.currentText() == "" or self.FeedQ3.currentText() == "" or self.PresentQ1.currentText() == "" or self.PresentQ2.currentText() == "" or self.PresentQ3.currentText() == ""):

            self.messagebox("Error","Please enter all fields")

        else: 
            self.CQ1 = thisdict[self.ContractQ1.currentText()] 

            if(self.CQ1 == 5):

                self.CQ1 = 0
                self.contracting = self.contracting + (self.CQ1 * 10)
                self.pointsself = self.pointsself + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.awareness = self.awareness + (self.CQ1 * 2)
                self.perspectives = self.perspectives + (self.CQ1 * 2)
                self.creative = self.creative + (self.CQ1 * 2)
                self.actions = self.actions + (self.CQ1 * 1)
                self.reflection = self.reflection + (self.CQ1 * 1)
                self.selfaware = self.selfaware + (self.CQ1 * 2)
                
            elif(self.CQ1 == 4):

                self.CQ1 = 1
                self.contracting = self.contracting + (self.CQ1 * 10)
                self.pointsself = self.pointsself + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.awareness = self.awareness + (self.CQ1 * 2)
                self.perspectives = self.perspectives + (self.CQ1 * 2)
                self.creative = self.creative + (self.CQ1 * 2)
                self.actions = self.actions + (self.CQ1 * 1)
                self.reflection = self.reflection + (self.CQ1 * 1)
                self.selfaware = self.selfaware + (self.CQ1 * 2)
                
            elif(self.CQ1 == 3):
                self.CQ1 = 2
                self.contracting = self.contracting + (self.CQ1 * 10)
                self.pointsself = self.pointsself + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.awareness = self.awareness + (self.CQ1 * 2)
                self.perspectives = self.perspectives + (self.CQ1 * 2)
                self.creative = self.creative + (self.CQ1 * 2)
                self.actions = self.actions + (self.CQ1 * 1)
                self.reflection = self.reflection + (self.CQ1 * 1)
                self.selfaware = self.selfaware + (self.CQ1 * 2)

            elif(self.CQ1 == 2):

                self.CQ1 = 3
                self.contracting = self.contracting + (self.CQ1 * 10)
                self.pointsself = self.pointsself + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.awareness = self.awareness + (self.CQ1 * 2)
                self.perspectives = self.perspectives + (self.CQ1 * 2)
                self.creative = self.creative + (self.CQ1 * 2)
                self.actions = self.actions + (self.CQ1 * 1)
                self.reflection = self.reflection + (self.CQ1 * 1)
                self.selfaware = self.selfaware + (self.CQ1 * 2)

            elif(self.CQ1 == 1):

                self.CQ1 = 4
                self.contracting = self.contracting + (self.CQ1 * 10)
                self.pointsself = self.pointsself + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.awareness = self.awareness + (self.CQ1 * 2)
                self.perspectives = self.perspectives + (self.CQ1 * 2)
                self.creative = self.creative + (self.CQ1 * 2)
                self.actions = self.actions + (self.CQ1 * 1)
                self.reflection = self.reflection + (self.CQ1 * 1)
                self.selfaware = self.selfaware + (self.CQ1 * 2)
                
            elif(self.CQ1 == 0):

                self.CQ1 = 5
                self.contracting = self.contracting + (self.CQ1 * 10)
                self.pointsself = self.pointsself + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.awareness = self.awareness + (self.CQ1 * 2)
                self.perspectives = self.perspectives + (self.CQ1 * 2)
                self.creative = self.creative + (self.CQ1 * 2)
                self.actions = self.actions + (self.CQ1 * 1)
                self.reflection = self.reflection + (self.CQ1 * 1)
                self.selfaware = self.selfaware + (self.CQ1 * 2)

            self.CQ2 = thisdict[self.ContractQ2.currentText()]
            self.contracting = self.contracting + (self.CQ2 * 10)
            self.feedback = self.feedback + (self.CQ2 * 5)
            self.trust = self.trust + (self.CQ2 * 3)
            self.confidentiatly = self.confidentiatly + (self.CQ2 * 2)
            self.awareness = self.awareness + (self.CQ2 * 2)
            self.perspectives = self.perspectives + (self.CQ2 * 2)
            self.creative = self.creative + (self.CQ2 * 2)
            self.selfaware = self.selfaware + (self.CQ2 * 1)


            self.CQ3 = thisdict[self.ContractQ3.currentText()] 

            if(self.CQ3 == 5):

                self.CQ3 = 0
                self.contracting = self.contracting + (self.CQ3 * 10)
                self.feedback = self.feedback + (self.CQ3 * 3)
                self.present = self.present + (self.CQ3 * 1)
                self.pointsself = self.pointsself + (self.CQ3 * 1)
                self.pointsother = self.pointsother + (self.CQ3 * 2)
                self.trust = self.trust + (self.CQ3 * 2)
                self.awareness = self.awareness + (self.CQ3 * 2)
                self.perspectives = self.perspectives + (self.CQ3 * 2)
                self.listening = self.listening + (self.CQ3 * 2)
                self.creative = self.creative + (self.CQ3 * 2)
                self.actions = self.actions + (self.CQ3 * 1)
                self.delegation = self.delegation + (self.CQ3 * 3)
                self.selfaware = self.selfaware + (self.CQ3 * 2)
                
            elif(self.CQ3 == 4):

                self.CQ3 = 1
                self.contracting = self.contracting + (self.CQ3 * 10)
                self.feedback = self.feedback + (self.CQ3 * 3)
                self.present = self.present + (self.CQ3 * 1)
                self.pointsself = self.pointsself + (self.CQ3 * 1)
                self.pointsother = self.pointsother + (self.CQ3 * 2)
                self.trust = self.trust + (self.CQ3 * 2)
                self.awareness = self.awareness + (self.CQ3 * 2)
                self.perspectives = self.perspectives + (self.CQ3 * 2)
                self.listening = self.listening + (self.CQ3 * 2)
                self.creative = self.creative + (self.CQ3 * 2)
                self.actions = self.actions + (self.CQ3 * 1)
                self.delegation = self.delegation + (self.CQ3 * 3)
                self.selfaware = self.selfaware + (self.CQ3 * 2)
                
            elif(self.CQ3 == 3):
                self.CQ3 = 2
                self.contracting = self.contracting + (self.CQ3 * 10)
                self.feedback = self.feedback + (self.CQ3 * 3)
                self.present = self.present + (self.CQ3 * 1)
                self.pointsself = self.pointsself + (self.CQ3 * 1)
                self.pointsother = self.pointsother + (self.CQ3 * 2)
                self.trust = self.trust + (self.CQ3 * 2)
                self.awareness = self.awareness + (self.CQ3 * 2)
                self.perspectives = self.perspectives + (self.CQ3 * 2)
                self.listening = self.listening + (self.CQ3 * 2)
                self.creative = self.creative + (self.CQ3 * 2)
                self.actions = self.actions + (self.CQ3 * 1)
                self.delegation = self.delegation + (self.CQ3 * 3)
                self.selfaware = self.selfaware + (self.CQ3 * 2)

            elif(self.CQ3 == 2):

                self.CQ3 = 3
                self.contracting = self.contracting + (self.CQ3 * 10)
                self.feedback = self.feedback + (self.CQ3 * 3)
                self.present = self.present + (self.CQ3 * 1)
                self.pointsself = self.pointsself + (self.CQ3 * 1)
                self.pointsother = self.pointsother + (self.CQ3 * 2)
                self.trust = self.trust + (self.CQ3 * 2)
                self.awareness = self.awareness + (self.CQ3 * 2)
                self.perspectives = self.perspectives + (self.CQ3 * 2)
                self.listening = self.listening + (self.CQ3 * 2)
                self.creative = self.creative + (self.CQ3 * 2)
                self.actions = self.actions + (self.CQ3 * 1)
                self.delegation = self.delegation + (self.CQ3 * 3)
                self.selfaware = self.selfaware + (self.CQ3 * 2)

            elif(self.CQ3 == 1):

                self.CQ3 = 4
                self.contracting = self.contracting + (self.CQ3 * 10)
                self.feedback = self.feedback + (self.CQ3 * 3)
                self.present = self.present + (self.CQ3 * 1)
                self.pointsself = self.pointsself + (self.CQ3 * 1)
                self.pointsother = self.pointsother + (self.CQ3 * 2)
                self.trust = self.trust + (self.CQ3 * 2)
                self.awareness = self.awareness + (self.CQ3 * 2)
                self.perspectives = self.perspectives + (self.CQ3 * 2)
                self.listening = self.listening + (self.CQ3 * 2)
                self.creative = self.creative + (self.CQ3 * 2)
                self.actions = self.actions + (self.CQ3 * 1)
                self.delegation = self.delegation + (self.CQ3 * 3)
                self.selfaware = self.selfaware + (self.CQ3 * 2)
                
            elif(self.CQ3 == 0):

                self.CQ3 = 5
                self.contracting = self.contracting + (self.CQ3 * 10)
                self.feedback = self.feedback + (self.CQ3 * 3)
                self.present = self.present + (self.CQ3 * 1)
                self.pointsself = self.pointsself + (self.CQ3 * 1)
                self.pointsother = self.pointsother + (self.CQ3 * 2)
                self.trust = self.trust + (self.CQ3 * 2)
                self.awareness = self.awareness + (self.CQ3 * 2)
                self.perspectives = self.perspectives + (self.CQ3 * 2)
                self.listening = self.listening + (self.CQ3 * 2)
                self.creative = self.creative + (self.CQ3 * 2)
                self.actions = self.actions + (self.CQ3 * 1)
                self.delegation = self.delegation + (self.CQ3 * 3)
                self.selfaware = self.selfaware + (self.CQ3 * 2)
       

            self.FQ1 = thisdict[self.FeedQ1.currentText()] 

            if(self.FQ1 == 5):

                self.FQ1 = 0

                self.contracting = self.contracting + (self.FQ1 * 3)
                self.feedback = self.feedback + (self.FQ1 * 10)
                self.pointsself = self.pointsself + (self.FQ1 * 1)
                self.pointsother = self.pointsother + (self.FQ1 * 2)
                self.trust = self.trust + (self.FQ1 * 1)
                self.awareness = self.awareness + (self.FQ1 * 3)
                self.perspectives = self.perspectives + (self.FQ1 * 1)
                self.creative = self.creative + (self.FQ1 * 3)
                self.actions = self.actions + (self.FQ1 * 2)
                self.delegation = self.delegation + (self.FQ1 * 1)
                self.reflection = self.reflection + (self.FQ1 * 1)

                
            elif(self.FQ1 == 4):

                self.FQ1 = 1
                self.contracting = self.contracting + (self.FQ1 * 3)
                self.feedback = self.feedback + (self.FQ1 * 10)
                self.pointsself = self.pointsself + (self.FQ1 * 1)
                self.pointsother = self.pointsother + (self.FQ1 * 2)
                self.trust = self.trust + (self.FQ1 * 1)
                self.awareness = self.awareness + (self.FQ1 * 3)
                self.perspectives = self.perspectives + (self.FQ1 * 1)
                self.creative = self.creative + (self.FQ1 * 3)
                self.actions = self.actions + (self.FQ1 * 2)
                self.delegation = self.delegation + (self.FQ1 * 1)
                self.reflection = self.reflection + (self.FQ1 * 1)

                
            elif(self.FQ1 == 3):
                self.FQ1 = 2
                self.contracting = self.contracting + (self.FQ1 * 3)
                self.feedback = self.feedback + (self.FQ1 * 10)
                self.pointsself = self.pointsself + (self.FQ1 * 1)
                self.pointsother = self.pointsother + (self.FQ1 * 2)
                self.trust = self.trust + (self.FQ1 * 1)
                self.awareness = self.awareness + (self.FQ1 * 3)
                self.perspectives = self.perspectives + (self.FQ1 * 1)
                self.creative = self.creative + (self.FQ1 * 3)
                self.actions = self.actions + (self.FQ1 * 2)
                self.delegation = self.delegation + (self.FQ1 * 1)
                self.reflection = self.reflection + (self.FQ1 * 1)

            elif(self.FQ1 == 2):

                self.FQ1 = 3
                self.contracting = self.contracting + (self.FQ1 * 3)
                self.feedback = self.feedback + (self.FQ1 * 10)
                self.pointsself = self.pointsself + (self.FQ1 * 1)
                self.pointsother = self.pointsother + (self.FQ1 * 2)
                self.trust = self.trust + (self.FQ1 * 1)
                self.awareness = self.awareness + (self.FQ1 * 3)
                self.perspectives = self.perspectives + (self.FQ1 * 1)
                self.creative = self.creative + (self.FQ1 * 3)
                self.actions = self.actions + (self.FQ1 * 2)
                self.delegation = self.delegation + (self.FQ1 * 1)
                self.reflection = self.reflection + (self.FQ1 * 1)

            elif(self.FQ1 == 1):

                self.FQ1 = 4
                self.contracting = self.contracting + (self.FQ1 * 3)
                self.feedback = self.feedback + (self.FQ1 * 10)
                self.pointsself = self.pointsself + (self.FQ1 * 1)
                self.pointsother = self.pointsother + (self.FQ1 * 2)
                self.trust = self.trust + (self.FQ1 * 1)
                self.awareness = self.awareness + (self.FQ1 * 3)
                self.perspectives = self.perspectives + (self.FQ1 * 1)
                self.creative = self.creative + (self.FQ1 * 3)
                self.actions = self.actions + (self.FQ1 * 2)
                self.delegation = self.delegation + (self.FQ1 * 1)
                self.reflection = self.reflection + (self.FQ1 * 1)
                
            elif(self.FQ1 == 0):

                self.FQ1 = 5
                self.contracting = self.contracting + (self.FQ1 * 3)
                self.feedback = self.feedback + (self.FQ1 * 10)
                self.pointsself = self.pointsself + (self.FQ1 * 1)
                self.pointsother = self.pointsother + (self.FQ1 * 2)
                self.trust = self.trust + (self.FQ1 * 1)
                self.awareness = self.awareness + (self.FQ1 * 3)
                self.perspectives = self.perspectives + (self.FQ1 * 1)
                self.creative = self.creative + (self.FQ1 * 3)
                self.actions = self.actions + (self.FQ1 * 2)
                self.delegation = self.delegation + (self.FQ1 * 1)
                self.reflection = self.reflection + (self.FQ1 * 1)



            self.FQ2 = thisdict[self.FeedQ2.currentText()] 

            if(self.FQ2 == 5):

                self.FQ2 = 0

                self.feedback = self.feedback + (self.FQ2 * 10)
                self.present = self.present + (self.FQ2 * 1)
                self.pointsother = self.pointsother + (self.FQ2 * 2)
                self.awareness = self.awareness + (self.FQ2 * 3)
                self.perspectives = self.perspectives + (self.FQ2 * 1)
                self.creative = self.creative + (self.FQ2 * 3)
                self.listening = self.listening + (self.FQ2 * 2)
                self.actions = self.actions + (self.FQ2 * 2)
                

                
            elif(self.FQ2 == 4):

                self.FQ2 = 1
                self.feedback = self.feedback + (self.FQ2 * 10)
                self.present = self.present + (self.FQ2 * 1)
                self.pointsother = self.pointsother + (self.FQ2 * 2)
                self.awareness = self.awareness + (self.FQ2 * 3)
                self.perspectives = self.perspectives + (self.FQ2 * 1)
                self.creative = self.creative + (self.FQ2 * 3)
                self.listening = self.listening + (self.FQ2 * 2)
                self.actions = self.actions + (self.FQ2 * 2)

                
            elif(self.FQ2 == 3):
                self.FQ2 = 2
                self.feedback = self.feedback + (self.FQ2 * 10)
                self.present = self.present + (self.FQ2 * 1)
                self.pointsother = self.pointsother + (self.FQ2 * 2)
                self.awareness = self.awareness + (self.FQ2 * 3)
                self.perspectives = self.perspectives + (self.FQ2 * 1)
                self.creative = self.creative + (self.FQ2 * 3)
                self.listening = self.listening + (self.FQ2 * 2)
                self.actions = self.actions + (self.FQ2 * 2)

            elif(self.FQ2 == 2):

                self.FQ2 = 3

                self.feedback = self.feedback + (self.FQ2 * 10)
                self.present = self.present + (self.FQ2 * 1)
                self.pointsother = self.pointsother + (self.FQ2 * 2)
                self.awareness = self.awareness + (self.FQ2 * 3)
                self.perspectives = self.perspectives + (self.FQ2 * 1)
                self.creative = self.creative + (self.FQ2 * 3)
                self.listening = self.listening + (self.FQ2 * 2)
                self.actions = self.actions + (self.FQ2 * 2)     

            elif(self.FQ2 == 1):

                self.FQ2 = 4

                self.feedback = self.feedback + (self.FQ2 * 10)
                self.present = self.present + (self.FQ2 * 1)
                self.pointsother = self.pointsother + (self.FQ2 * 2)
                self.awareness = self.awareness + (self.FQ2 * 3)
                self.perspectives = self.perspectives + (self.FQ2 * 1)
                self.creative = self.creative + (self.FQ2 * 3)
                self.listening = self.listening + (self.FQ2 * 2)
                self.actions = self.actions + (self.FQ2 * 2) 
                
            elif(self.FQ2 == 0):

                self.FQ2 = 5

                self.feedback = self.feedback + (self.FQ2 * 10)
                self.present = self.present + (self.FQ2 * 2)
                self.pointsother = self.pointsother + (self.FQ2 * 2)
                self.awareness = self.awareness + (self.FQ2 * 3)
                self.perspectives = self.perspectives + (self.FQ2 * 1)
                self.creative = self.creative + (self.FQ2 * 3)
                self.listening = self.listening + (self.FQ2 * 2)
                self.actions = self.actions + (self.FQ2 * 2)

            self.FQ3 = thisdict[self.FeedQ3.currentText()] 

            if(self.FQ3 == 5):

                self.FQ3 = 0
                self.contracting = self.contracting + (self.FQ3 * 2)
                self.feedback = self.feedback + (self.FQ3 * 10)
                self.present = self.present + (self.FQ3 * 2)
                self.pointsother = self.pointsother + (self.FQ3 * 2)
                self.trust = self.trust + (self.FQ3 * 2)
                self.awareness = self.awareness + (self.FQ3 * 3)
                self.perspectives = self.perspectives + (self.FQ3 * 1)
                self.listening = self.listening + (self.FQ3 * 2)
     
            elif(self.FQ3 == 4):

                self.FQ3 = 1
                self.contracting = self.contracting + (self.FQ3 * 2)
                self.feedback = self.feedback + (self.FQ3 * 10)
                self.present = self.present + (self.FQ3 * 2)
                self.pointsother = self.pointsother + (self.FQ3 * 2)
                self.trust = self.trust + (self.FQ3 * 2)
                self.awareness = self.awareness + (self.FQ3 * 3)
                self.perspectives = self.perspectives + (self.FQ3 * 1)
                self.listening = self.listening + (self.FQ3 * 2)                

                
            elif(self.FQ3 == 3):
                self.FQ3 = 2
                self.contracting = self.contracting + (self.FQ3 * 2)
                self.feedback = self.feedback + (self.FQ3 * 10)
                self.present = self.present + (self.FQ3 * 2)
                self.pointsother = self.pointsother + (self.FQ3 * 2)
                self.trust = self.trust + (self.FQ3 * 2)
                self.awareness = self.awareness + (self.FQ3 * 3)
                self.perspectives = self.perspectives + (self.FQ3 * 1)
                self.listening = self.listening + (self.FQ3 * 2)             

            elif(self.FQ3 == 2):

                self.FQ3 = 3
                self.contracting = self.contracting + (self.FQ3 * 2)
                self.feedback = self.feedback + (self.FQ3 * 10)
                self.present = self.present + (self.FQ3 * 2)
                self.pointsother = self.pointsother + (self.FQ3 * 2)
                self.trust = self.trust + (self.FQ3 * 2)
                self.awareness = self.awareness + (self.FQ3 * 3)
                self.perspectives = self.perspectives + (self.FQ3 * 1)
                self.listening = self.listening + (self.FQ3 * 2)

            elif(self.FQ3 == 1):

                self.FQ3 = 4
                self.contracting = self.contracting + (self.FQ3 * 2)
                self.feedback = self.feedback + (self.FQ3 * 10)
                self.present = self.present + (self.FQ3 * 2)
                self.pointsother = self.pointsother + (self.FQ3 * 2)
                self.trust = self.trust + (self.FQ3 * 2)
                self.awareness = self.awareness + (self.FQ3 * 3)
                self.perspectives = self.perspectives + (self.FQ3 * 1)
                self.listening = self.listening + (self.FQ3 * 2)
                
            elif(self.FQ3 == 0):

                self.FQ3 = 5
                self.contracting = self.contracting + (self.FQ3 * 2)
                self.feedback = self.feedback + (self.FQ3 * 10)
                self.present = self.present + (self.FQ3 * 2)
                self.pointsother = self.pointsother + (self.FQ3 * 2)
                self.trust = self.trust + (self.FQ3 * 2)
                self.awareness = self.awareness + (self.FQ3 * 3)
                self.perspectives = self.perspectives + (self.FQ3 * 1)
                self.listening = self.listening + (self.FQ3 * 2)
                 
            self.PQ1 = thisdict[self.PresentQ1.currentText()]
            self.present = self.present + (self.PQ1 * 10)
            self.pointsself = self.pointsself + (self.PQ1 * 1)
            self.reflection = self.reflection + (self.PQ1 * 1)
            self.selfaware = self.selfaware + (self.PQ1 * 1)
  

            self.PQ2 = thisdict[self.PresentQ2.currentText()]
            self.present = self.present + (self.PQ2 * 10)
            self.pointsself = self.pointsself + (self.PQ2 * 2)
            self.trust = self.trust + (self.PQ2 * 1)
            self.perspectives = self.perspectives + (self.PQ2 * 1)
            self.listening = self.listening + (self.PQ2 * 2)
            self.selfaware = self.selfaware + (self.PQ2 * 1)

            self.PQ3 = thisdict[self.PresentQ3.currentText()]
            self.present = self.present + (self.PQ3 * 10)
            self.pointsself = self.pointsself + (self.PQ3 * 2)
            self.trust = self.trust + (self.PQ3 * 1)
            self.perspectives = self.perspectives + (self.PQ3 * 1)
            self.listening = self.listening + (self.PQ3 * 5)
            self.selfaware = self.selfaware + (self.PQ3 * 1)

            self.ContractFeedToPresentPause(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware)             
            self.h.hide()




    def ContractFeedToPresentPause(self,email,birth,edu,lead,workyears,contracting,feedback,present,pointsself,pointsother,trust,confidentiatly,awareness,perspectives,listening,creative,delegation,actions,reflection,selfaware):
        self.main = QtWidgets.QMainWindow() 
        self.ui = Ui_PauseOtherTrust(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware) 
        self.ui.setupUi(self.main)
        self.main.show()      

    def retranslateUi(self, ContractFeedPresent):
        _translate = QtCore.QCoreApplication.translate
        ContractFeedPresent.setWindowTitle(_translate("ContractFeedPresent", "COTG"))
        self.label.setText(_translate("ContractFeedPresent", "<html><head/><body><p align=\"center\">Please answer the following questions</p></body></html>"))
        self.label_2.setText(_translate("ContractFeedPresent", "<html><head/><body><p>If I\'m invited to join a meeting but I\'m not sure why, I will ask the leader to explain my </p><p>role if I can</p></body></html>"))
        self.label_3.setText(_translate("ContractFeedPresent", "<html><head/><body><p>There are undiscussables in my team that my boss leads, I dont know how to make </p><p>these undiscussables more discussable</p></body></html>"))
        self.label_4.setText(_translate("ContractFeedPresent", "<html><head/><body><p>In meetings and conversations, I check that the right people are in the conversation</p><p>for the right discussion</p></body></html>"))
        self.label_5.setText(_translate("ContractFeedPresent", "<html><head/><body><p>When I meet the people I work with, the focus is on individual development as well</p><p>as tasks and activities</p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("ContractFeedPresent", "I help others to develop their strengths"))
        self.label_7.setText(_translate("ContractFeedPresent", "<html><head/><body><p>I give feedback to others on how I view their performance and behaviours so that </p><p>they can develop and excel</p><p><br/></p><p><br/></p></body></html>"))
        self.NextQuestions.setStatusTip(_translate("ContractFeedPresent", "Click this to go to next questions"))
        self.NextQuestions.setText(_translate("ContractFeedPresent", "Next"))
        self.label_8.setText(_translate("ContractFeedPresent", "<html><head/><body><p>I find it difficult to stay focused on what is happening in the present</p></body></html>"))
        self.label_9.setText(_translate("ContractFeedPresent", "<html><head/><body><p>I find myself listening to someone with one ear, doing something else at the same time</p></body></html>"))
        self.label_10.setText(_translate("ContractFeedPresent", "<html><head/><body><p>I forget a person\'s name almost as soon as I have been told it for the first time</p></body></html>"))
        self.Back.setStatusTip(_translate("ContractFeedPresent", "Click this to go back"))
        self.Back.setText(_translate("ContractFeedPresent", "Back"))
        self.ContractQ1.setToolTip(_translate("ContractFeedPresent", "Please select from the following"))
        self.ContractQ1.setItemText(0, _translate("ContractFeedPresent", "Never"))
        self.ContractQ1.setItemText(1, _translate("ContractFeedPresent", "Very Rarely"))
        self.ContractQ1.setItemText(2, _translate("ContractFeedPresent", "Rarely"))
        self.ContractQ1.setItemText(3, _translate("ContractFeedPresent", "Sometimes"))
        self.ContractQ1.setItemText(4, _translate("ContractFeedPresent", "Often"))
        self.ContractQ1.setItemText(5, _translate("ContractFeedPresent", "Always"))
        self.ContractQ2.setToolTip(_translate("ContractFeedPresent", "Please select from the following"))
        self.ContractQ2.setItemText(0, _translate("ContractFeedPresent", "Never"))
        self.ContractQ2.setItemText(1, _translate("ContractFeedPresent", "Very Rarely"))
        self.ContractQ2.setItemText(2, _translate("ContractFeedPresent", "Rarely"))
        self.ContractQ2.setItemText(3, _translate("ContractFeedPresent", "Sometimes"))
        self.ContractQ2.setItemText(4, _translate("ContractFeedPresent", "Often"))
        self.ContractQ2.setItemText(5, _translate("ContractFeedPresent", "Always"))
        self.ContractQ3.setToolTip(_translate("ContractFeedPresent", "Please select from the following"))
        self.ContractQ3.setItemText(0, _translate("ContractFeedPresent", "Never"))
        self.ContractQ3.setItemText(1, _translate("ContractFeedPresent", "Very Rarely"))
        self.ContractQ3.setItemText(2, _translate("ContractFeedPresent", "Rarely"))
        self.ContractQ3.setItemText(3, _translate("ContractFeedPresent", "Sometimes"))
        self.ContractQ3.setItemText(4, _translate("ContractFeedPresent", "Often"))
        self.ContractQ3.setItemText(5, _translate("ContractFeedPresent", "Always"))
        self.FeedQ1.setToolTip(_translate("ContractFeedPresent", "Please select from the following"))
        self.FeedQ1.setItemText(0, _translate("ContractFeedPresent", "Never"))
        self.FeedQ1.setItemText(1, _translate("ContractFeedPresent", "Very Rarely"))
        self.FeedQ1.setItemText(2, _translate("ContractFeedPresent", "Rarely"))
        self.FeedQ1.setItemText(3, _translate("ContractFeedPresent", "Sometimes"))
        self.FeedQ1.setItemText(4, _translate("ContractFeedPresent", "Often"))
        self.FeedQ1.setItemText(5, _translate("ContractFeedPresent", "Always"))
        self.FeedQ2.setToolTip(_translate("ContractFeedPresent", "Please select from the following"))
        self.FeedQ2.setItemText(0, _translate("ContractFeedPresent", "Never"))
        self.FeedQ2.setItemText(1, _translate("ContractFeedPresent", "Very Rarely"))
        self.FeedQ2.setItemText(2, _translate("ContractFeedPresent", "Rarely"))
        self.FeedQ2.setItemText(3, _translate("ContractFeedPresent", "Sometimes"))
        self.FeedQ2.setItemText(4, _translate("ContractFeedPresent", "Often"))
        self.FeedQ2.setItemText(5, _translate("ContractFeedPresent", "Always"))
        self.FeedQ3.setToolTip(_translate("ContractFeedPresent", "Please select from the following"))
        self.FeedQ3.setItemText(0, _translate("ContractFeedPresent", "Never"))
        self.FeedQ3.setItemText(1, _translate("ContractFeedPresent", "Very Rarely"))
        self.FeedQ3.setItemText(2, _translate("ContractFeedPresent", "Rarely"))
        self.FeedQ3.setItemText(3, _translate("ContractFeedPresent", "Sometimes"))
        self.FeedQ3.setItemText(4, _translate("ContractFeedPresent", "Often"))
        self.FeedQ3.setItemText(5, _translate("ContractFeedPresent", "Always"))
        self.PresentQ1.setToolTip(_translate("ContractFeedPresent", "Please select from the following"))
        self.PresentQ1.setItemText(0, _translate("ContractFeedPresent", "Never"))
        self.PresentQ1.setItemText(1, _translate("ContractFeedPresent", "Very Rarely"))
        self.PresentQ1.setItemText(2, _translate("ContractFeedPresent", "Rarely"))
        self.PresentQ1.setItemText(3, _translate("ContractFeedPresent", "Sometimes"))
        self.PresentQ1.setItemText(4, _translate("ContractFeedPresent", "Often"))
        self.PresentQ1.setItemText(5, _translate("ContractFeedPresent", "Always"))
        self.PresentQ2.setToolTip(_translate("ContractFeedPresent", "Please select from the following"))
        self.PresentQ2.setItemText(0, _translate("ContractFeedPresent", "Never"))
        self.PresentQ2.setItemText(1, _translate("ContractFeedPresent", "Very Rarely"))
        self.PresentQ2.setItemText(2, _translate("ContractFeedPresent", "Rarely"))
        self.PresentQ2.setItemText(3, _translate("ContractFeedPresent", "Sometimes"))
        self.PresentQ2.setItemText(4, _translate("ContractFeedPresent", "Often"))
        self.PresentQ2.setItemText(5, _translate("ContractFeedPresent", "Always"))
        self.PresentQ3.setToolTip(_translate("ContractFeedPresent", "Please select from the following"))
        self.PresentQ3.setItemText(0, _translate("ContractFeedPresent", "Never"))
        self.PresentQ3.setItemText(1, _translate("ContractFeedPresent", "Very Rarely"))
        self.PresentQ3.setItemText(2, _translate("ContractFeedPresent", "Rarely"))
        self.PresentQ3.setItemText(3, _translate("ContractFeedPresent", "Sometimes"))
        self.PresentQ3.setItemText(4, _translate("ContractFeedPresent", "Often"))
        self.PresentQ3.setItemText(5, _translate("ContractFeedPresent", "Always"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContractFeedPresent = QtWidgets.QDialog()
    ui = Ui_ContractFeedPresent()
    ui.setupUi(ContractFeedPresent)
    ContractFeedPresent.show()
    app.exec_()
