# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PresentPause.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QShortcut , QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog , QAction ,QShortcut
from ConfAwarePersp import Ui_ConfAwarePersp

thisdict = {"Never":0,
            "Very Rarely":1,
            "Rarely":2,
            "Sometimes":3,
            "Often":4,
            "Always":5}

class Ui_PauseOtherTrust(object):

    def __init__(self,email,birth,edu,lead,workyears,contracting,feedback,present,pointsself,pointsother,trust,confidentiatly,awareness,perspectives,listening,creative,delegation,actions,reflection,selfaware):

        self.email = email
        self.birth = birth
        self.edu = edu             
        self.lead = lead
        self.workyears = workyears


        self.contracting = contracting
        self.feedback = feedback
        self.present=present
        self.pointsself = pointsself
        self.pointsother = pointsother
        self.trust = trust
        self.confidentiatly = confidentiatly
        self.awareness = awareness
        self.perspectives = perspectives
        self.listening = listening
        self.creative = creative
        self.delegation = delegation
        self.actions = actions
        self.reflection = reflection
        self.selfaware = selfaware




    def setupUi(self, PauseOtherTrust):
        PauseOtherTrust.setObjectName("PauseOtherTrust")
        PauseOtherTrust.resize(820, 807)
        PauseOtherTrust.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.label = QtWidgets.QLabel(PauseOtherTrust)
        self.label.setGeometry(QtCore.QRect(190, 20, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.PauseQ1 = QtWidgets.QComboBox(PauseOtherTrust)
        self.PauseQ1.setGeometry(QtCore.QRect(680, 90, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PauseQ1.setFont(font)
        self.PauseQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PauseQ1.setMaxVisibleItems(6)
        self.PauseQ1.setObjectName("PauseQ1")
        self.PauseQ1.addItem("")
        self.PauseQ1.addItem("")
        self.PauseQ1.addItem("")
        self.PauseQ1.addItem("")
        self.PauseQ1.addItem("")
        self.PauseQ1.addItem("")
        self.label_2 = QtWidgets.QLabel(PauseOtherTrust)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.PauseQ2 = QtWidgets.QComboBox(PauseOtherTrust)
        self.PauseQ2.setGeometry(QtCore.QRect(680, 170, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PauseQ2.setFont(font)
        self.PauseQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PauseQ2.setMaxVisibleItems(6)
        self.PauseQ2.setObjectName("PauseQ2")
        self.PauseQ2.addItem("")
        self.PauseQ2.addItem("")
        self.PauseQ2.addItem("")
        self.PauseQ2.addItem("")
        self.PauseQ2.addItem("")
        self.PauseQ2.addItem("")
        self.label_4 = QtWidgets.QLabel(PauseOtherTrust)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.PauseQ3 = QtWidgets.QComboBox(PauseOtherTrust)
        self.PauseQ3.setGeometry(QtCore.QRect(680, 240, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PauseQ3.setFont(font)
        self.PauseQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PauseQ3.setMaxVisibleItems(6)
        self.PauseQ3.setObjectName("PauseQ3")
        self.PauseQ3.addItem("")
        self.PauseQ3.addItem("")
        self.PauseQ3.addItem("")
        self.PauseQ3.addItem("")
        self.PauseQ3.addItem("")
        self.PauseQ3.addItem("")
        self.label_5 = QtWidgets.QLabel(PauseOtherTrust)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(PauseOtherTrust)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(PauseOtherTrust)
        self.label_7.setGeometry(QtCore.QRect(10, 410, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(PauseOtherTrust)
        self.label_8.setGeometry(QtCore.QRect(10, 470, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.OtherQ1 = QtWidgets.QComboBox(PauseOtherTrust)
        self.OtherQ1.setGeometry(QtCore.QRect(680, 330, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OtherQ1.setFont(font)
        self.OtherQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OtherQ1.setMaxVisibleItems(6)
        self.OtherQ1.setObjectName("OtherQ1")
        self.OtherQ1.addItem("")
        self.OtherQ1.addItem("")
        self.OtherQ1.addItem("")
        self.OtherQ1.addItem("")
        self.OtherQ1.addItem("")
        self.OtherQ1.addItem("")
        self.OtherQ2 = QtWidgets.QComboBox(PauseOtherTrust)
        self.OtherQ2.setGeometry(QtCore.QRect(680, 410, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OtherQ2.setFont(font)
        self.OtherQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OtherQ2.setMaxVisibleItems(6)
        self.OtherQ2.setObjectName("OtherQ2")
        self.OtherQ2.addItem("")
        self.OtherQ2.addItem("")
        self.OtherQ2.addItem("")
        self.OtherQ2.addItem("")
        self.OtherQ2.addItem("")
        self.OtherQ2.addItem("")
        self.OtherQ3 = QtWidgets.QComboBox(PauseOtherTrust)
        self.OtherQ3.setGeometry(QtCore.QRect(680, 470, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OtherQ3.setFont(font)
        self.OtherQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OtherQ3.setMaxVisibleItems(6)
        self.OtherQ3.setObjectName("OtherQ3")
        self.OtherQ3.addItem("")
        self.OtherQ3.addItem("")
        self.OtherQ3.addItem("")
        self.OtherQ3.addItem("")
        self.OtherQ3.addItem("")
        self.OtherQ3.addItem("")
        self.label_9 = QtWidgets.QLabel(PauseOtherTrust)
        self.label_9.setGeometry(QtCore.QRect(10, 530, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(PauseOtherTrust)
        self.label_10.setGeometry(QtCore.QRect(10, 590, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(PauseOtherTrust)
        self.label_11.setGeometry(QtCore.QRect(10, 680, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.TrustQ1 = QtWidgets.QComboBox(PauseOtherTrust)
        self.TrustQ1.setGeometry(QtCore.QRect(680, 530, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TrustQ1.setFont(font)
        self.TrustQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TrustQ1.setMaxVisibleItems(6)
        self.TrustQ1.setObjectName("TrustQ1")
        self.TrustQ1.addItem("")
        self.TrustQ1.addItem("")
        self.TrustQ1.addItem("")
        self.TrustQ1.addItem("")
        self.TrustQ1.addItem("")
        self.TrustQ1.addItem("")
        self.TrustQ2 = QtWidgets.QComboBox(PauseOtherTrust)
        self.TrustQ2.setGeometry(QtCore.QRect(680, 600, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TrustQ2.setFont(font)
        self.TrustQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TrustQ2.setMaxVisibleItems(6)
        self.TrustQ2.setObjectName("TrustQ2")
        self.TrustQ2.addItem("")
        self.TrustQ2.addItem("")
        self.TrustQ2.addItem("")
        self.TrustQ2.addItem("")
        self.TrustQ2.addItem("")
        self.TrustQ2.addItem("")
        self.TrustQ3 = QtWidgets.QComboBox(PauseOtherTrust)
        self.TrustQ3.setGeometry(QtCore.QRect(680, 680, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TrustQ3.setFont(font)
        self.TrustQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TrustQ3.setMaxVisibleItems(6)
        self.TrustQ3.setObjectName("TrustQ3")
        self.TrustQ3.addItem("")
        self.TrustQ3.addItem("")
        self.TrustQ3.addItem("")
        self.TrustQ3.addItem("")
        self.TrustQ3.addItem("")
        self.TrustQ3.addItem("")
        self.NextQuestion2 = QtWidgets.QPushButton(PauseOtherTrust)
        self.NextQuestion2.setGeometry(QtCore.QRect(700, 760, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NextQuestion2.setFont(font)
        self.NextQuestion2.setAutoFillBackground(False)
        self.NextQuestion2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NextQuestion2.setObjectName("NextQuestion2")
        self.Back = QtWidgets.QPushButton(PauseOtherTrust)
        self.Back.setGeometry(QtCore.QRect(20, 760, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setAutoFillBackground(False)
        self.Back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Back.setObjectName("Back")
        self.line = QtWidgets.QFrame(PauseOtherTrust)
        self.line.setGeometry(QtCore.QRect(0, 140, 821, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(PauseOtherTrust)
        self.line_2.setGeometry(QtCore.QRect(0, 210, 821, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(PauseOtherTrust)
        self.line_3.setGeometry(QtCore.QRect(0, 290, 821, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(PauseOtherTrust)
        self.line_4.setGeometry(QtCore.QRect(0, 380, 821, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(PauseOtherTrust)
        self.line_5.setGeometry(QtCore.QRect(0, 440, 821, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(PauseOtherTrust)
        self.line_6.setGeometry(QtCore.QRect(0, 500, 821, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(PauseOtherTrust)
        self.line_7.setGeometry(QtCore.QRect(0, 560, 821, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(PauseOtherTrust)
        self.line_8.setGeometry(QtCore.QRect(0, 650, 821, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(PauseOtherTrust)
        self.line_9.setGeometry(QtCore.QRect(0, 720, 821, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.retranslateUi(PauseOtherTrust)
        self.PauseQ1.setCurrentIndex(-1)
        self.PauseQ2.setCurrentIndex(-1)
        self.PauseQ3.setCurrentIndex(-1)
        self.OtherQ1.setCurrentIndex(-1)
        self.OtherQ2.setCurrentIndex(-1)
        self.OtherQ3.setCurrentIndex(-1)
        self.TrustQ1.setCurrentIndex(-1)
        self.TrustQ2.setCurrentIndex(-1)
        self.TrustQ3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(PauseOtherTrust)

        self.NextQuestion2.clicked.connect(self.pressed)
        self.h = PauseOtherTrust

    def pressed(self):
        

        if(self.PauseQ1.currentText() == "" or self.PauseQ2.currentText() == "" or self.PauseQ3.currentText() == "" or self.OtherQ1.currentText() == "" or self.OtherQ2.currentText() == "" or self.OtherQ3.currentText() == "" or self.TrustQ1.currentText() == "" or self.TrustQ2.currentText() == "" or self.TrustQ3.currentText() == ""):

            self.messagebox("Error","Please enter all fields")

        else: 
            self.PQ1 = thisdict[self.PauseQ1.currentText()]         

            self.contracting = self.contracting + (self.PQ1 * 3)
            self.present = self.present + (self.PQ1 * 3)

            self.pointsself = self.pointsself + (self.PQ1 * 10)
            self.trust = self.trust +(self.PQ1 * 2)

            self.awareness = self.awareness + (self.PQ1 * 1)
            self.perspectives = self.perspectives + (self.PQ1 * 2)
            self.listening = self.listening + (self.PQ1 * 1)
            self.actions = self.actions + (self.PQ1 * 3)
            self.reflection = self.reflection +(self.PQ1 * 2)
            self.selfaware = self.selfaware + (self.PQ1 * 2)

            self.PQ2 = thisdict[self.PauseQ2.currentText()] 

            if(self.PQ2 == 5):

                self.PQ2 = 0

                self.pointsself = self.pointsself + (self.PQ2 * 10)
                self.trust = self.trust +(self.PQ2 * 2)
                self.perspectives = self.perspectives + (self.PQ2 * 4)
                self.actions = self.actions + (self.PQ2 * 1)
                self.selfaware = self.selfaware + (self.PQ2 * 3)

            elif(self.PQ2 == 4):

                self.PQ2 = 1
                self.pointsself = self.pointsself + (self.PQ2 * 10)
                self.trust = self.trust +(self.PQ2 * 2)
                self.perspectives = self.perspectives + (self.PQ2 * 4)
                self.actions = self.actions + (self.PQ2 * 1)
                self.selfaware = self.selfaware + (self.PQ2 * 3)
                
            elif(self.PQ2 == 3):
                self.PQ2 = 2
                self.pointsself = self.pointsself + (self.PQ2 * 10)
                self.trust = self.trust +(self.PQ2 * 2)
                self.perspectives = self.perspectives + (self.PQ2 * 4)
                self.actions = self.actions + (self.PQ2 * 1)
                self.selfaware = self.selfaware + (self.PQ2 * 3)

            elif(self.PQ2 == 2):

                self.PQ2 = 3
                self.pointsself = self.pointsself + (self.PQ2 * 10)
                self.trust = self.trust +(self.PQ2 * 2)
                self.perspectives = self.perspectives + (self.PQ2 * 4)
                self.actions = self.actions + (self.PQ2 * 1)
                self.selfaware = self.selfaware + (self.PQ2 * 3)

            elif(self.PQ2 == 1):

                self.PQ2 = 4
                self.pointsself = self.pointsself + (self.PQ2 * 10)
                self.trust = self.trust +(self.PQ2 * 2)
                self.perspectives = self.perspectives + (self.PQ2 * 4)
                self.actions = self.actions + (self.PQ2 * 1)
                self.selfaware = self.selfaware + (self.PQ2 * 3)         
                
            elif(self.PQ2 == 0):

                self.PQ2 = 5
                self.pointsself = self.pointsself + (self.PQ2 * 10)
                self.trust = self.trust +(self.PQ2 * 2)
                self.perspectives = self.perspectives + (self.PQ2 * 4)
                self.actions = self.actions + (self.PQ2 * 1)
                self.selfaware = self.selfaware + (self.PQ2 * 3)

            self.PQ3 = thisdict[self.PauseQ3.currentText()] 

            if(self.PQ3 == 5):

                self.PQ3 = 0

                self.contracting = self.contracting + (self.PQ3 * 2)
                self.present = self.present + (self.PQ3 * 5)
                self.pointsself = self.pointsself + (self.PQ3 * 10)
                self.trust = self.trust +(self.PQ3 * 2)
                self.perspectives = self.perspectives + (self.PQ3 * 3)
                self.actions = self.actions + (self.PQ3 * 1)
                self.reflection = self.reflection + (self.PQ3 * 2)
                self.selfaware = self.selfaware + (self.PQ3 * 3)

            elif(self.PQ3 == 4):

                self.PQ3 = 1

                self.contracting = self.contracting + (self.PQ3 * 2)
                self.present = self.present + (self.PQ3 * 5)
                self.pointsself = self.pointsself + (self.PQ3 * 10)
                self.trust = self.trust +(self.PQ3 * 2)
                self.perspectives = self.perspectives + (self.PQ3 * 3)
                self.actions = self.actions + (self.PQ3 * 1)
                self.reflection = self.reflection + (self.PQ3 * 2)
                self.selfaware = self.selfaware + (self.PQ3 * 3)         
                
            elif(self.PQ3 == 3):
                self.PQ3 = 2
                self.contracting = self.contracting + (self.PQ3 * 2)
                self.present = self.present + (self.PQ3 * 5)
                self.pointsself = self.pointsself + (self.PQ3 * 10)
                self.trust = self.trust +(self.PQ3 * 2)
                self.perspectives = self.perspectives + (self.PQ3 * 3)
                self.actions = self.actions + (self.PQ3 * 1)
                self.reflection = self.reflection + (self.PQ3 * 2)
                self.selfaware = self.selfaware + (self.PQ3 * 3) 

            elif(self.PQ3 == 2):

                self.PQ3 = 3
                self.contracting = self.contracting + (self.PQ3 * 2)
                self.present = self.present + (self.PQ3 * 5)
                self.pointsself = self.pointsself + (self.PQ3 * 10)
                self.trust = self.trust +(self.PQ3 * 2)
                self.perspectives = self.perspectives + (self.PQ3 * 3)
                self.actions = self.actions + (self.PQ3 * 1)
                self.reflection = self.reflection + (self.PQ3 * 2)
                self.selfaware = self.selfaware + (self.PQ3 * 3) 

            elif(self.PQ3 == 1):

                self.PQ3 = 4
                self.contracting = self.contracting + (self.PQ3 * 2)
                self.present = self.present + (self.PQ3 * 5)
                self.pointsself = self.pointsself + (self.PQ3 * 10)
                self.trust = self.trust +(self.PQ3 * 2)
                self.perspectives = self.perspectives + (self.PQ3 * 3)
                self.actions = self.actions + (self.PQ3 * 1)
                self.reflection = self.reflection + (self.PQ3 * 2)
                self.selfaware = self.selfaware + (self.PQ3 * 3)  
                
            elif(self.PQ3 == 0):

                self.PQ3 = 5
                self.contracting = self.contracting + (self.PQ3 * 2)
                self.present = self.present + (self.PQ3 * 5)
                self.pointsself = self.pointsself + (self.PQ3 * 10)
                self.trust = self.trust +(self.PQ3 * 2)
                self.perspectives = self.perspectives + (self.PQ3 * 3)
                self.actions = self.actions + (self.PQ3 * 1)
                self.reflection = self.reflection + (self.PQ3 * 2)
                self.selfaware = self.selfaware + (self.PQ3 * 3)


            self.OQ1 = thisdict[self.OtherQ1.currentText()] 

            if(self.OQ1 == 5):

                self.OQ1 = 0
                self.contracting = self.contracting + (self.OQ1 * 2)
                self.feedback = self.feedback + (self.OQ1 * 3)
                self.present = self.present + (self.OQ1 * 2)
                self.pointsother = self.pointsother + (self.OQ1 * 10)
                self.trust = self.trust +(self.OQ1 * 5)
                self.confidentiatly = self.confidentiatly + (self.OQ1 * 3)
                self.awareness = self.awareness + (self.OQ1 * 5)
                self.perspectives = self.perspectives + (self.OQ1 * 5)
                self.listening = self.listening + (self.OQ1 * 3)
                self.creative = self.creative + (self.OQ1 * 4)
                self.delegation = self.delegation + (self.OQ1 * 3)
                self.actions = self.actions + (self.OQ1 * 2)

            elif(self.OQ1 == 4):

                self.OQ1 = 1
                self.contracting = self.contracting + (self.OQ1 * 2)
                self.feedback = self.feedback + (self.OQ1 * 3)
                self.present = self.present + (self.OQ1 * 2)
                self.pointsother = self.pointsother + (self.OQ1 * 10)
                self.trust = self.trust +(self.OQ1 * 5)
                self.confidentiatly = self.confidentiatly + (self.OQ1 * 3)
                self.awareness = self.awareness + (self.OQ1 * 5)
                self.perspectives = self.perspectives + (self.OQ1 * 5)
                self.listening = self.listening + (self.OQ1 * 3)
                self.creative = self.creative + (self.OQ1 * 4)
                self.delegation = self.delegation + (self.OQ1 * 3)
                self.actions = self.actions + (self.OQ1 * 2)    
                
            elif(self.OQ1 == 3):
                self.OQ1 = 2
                self.contracting = self.contracting + (self.OQ1 * 2)
                self.feedback = self.feedback + (self.OQ1 * 3)
                self.present = self.present + (self.OQ1 * 2)
                self.pointsother = self.pointsother + (self.OQ1 * 10)
                self.trust = self.trust +(self.OQ1 * 5)
                self.confidentiatly = self.confidentiatly + (self.OQ1 * 3)
                self.awareness = self.awareness + (self.OQ1 * 5)
                self.perspectives = self.perspectives + (self.OQ1 * 5)
                self.listening = self.listening + (self.OQ1 * 3)
                self.creative = self.creative + (self.OQ1 * 4)
                self.delegation = self.delegation + (self.OQ1 * 3)
                self.actions = self.actions + (self.OQ1 * 2) 
            elif(self.OQ1 == 2):

                self.OQ1 = 3
                self.contracting = self.contracting + (self.OQ1 * 2)
                self.feedback = self.feedback + (self.OQ1 * 3)
                self.present = self.present + (self.OQ1 * 2)
                self.pointsother = self.pointsother + (self.OQ1 * 10)
                self.trust = self.trust +(self.OQ1 * 5)
                self.confidentiatly = self.confidentiatly + (self.OQ1 * 3)
                self.awareness = self.awareness + (self.OQ1 * 5)
                self.perspectives = self.perspectives + (self.OQ1 * 5)
                self.listening = self.listening + (self.OQ1 * 3)
                self.creative = self.creative + (self.OQ1 * 4)
                self.delegation = self.delegation + (self.OQ1 * 3)
                self.actions = self.actions + (self.OQ1 * 2)    

            elif(self.OQ1 == 1):

                self.OQ1 = 4
                self.contracting = self.contracting + (self.OQ1 * 2)
                self.feedback = self.feedback + (self.OQ1 * 3)
                self.present = self.present + (self.OQ1 * 2)
                self.pointsother = self.pointsother + (self.OQ1 * 10)
                self.trust = self.trust +(self.OQ1 * 5)
                self.confidentiatly = self.confidentiatly + (self.OQ1 * 3)
                self.awareness = self.awareness + (self.OQ1 * 5)
                self.perspectives = self.perspectives + (self.OQ1 * 5)
                self.listening = self.listening + (self.OQ1 * 3)
                self.creative = self.creative + (self.OQ1 * 4)
                self.delegation = self.delegation + (self.OQ1 * 3)
                self.actions = self.actions + (self.OQ1 * 2)
                
            elif(self.OQ1 == 0):

                self.OQ1 = 5
                self.contracting = self.contracting + (self.OQ1 * 2)
                self.feedback = self.feedback + (self.OQ1 * 3)
                self.present = self.present + (self.OQ1 * 2)
                self.pointsother = self.pointsother + (self.OQ1 * 10)
                self.trust = self.trust +(self.OQ1 * 5)
                self.confidentiatly = self.confidentiatly + (self.OQ1 * 3)
                self.awareness = self.awareness + (self.OQ1 * 5)
                self.perspectives = self.perspectives + (self.OQ1 * 5)
                self.listening = self.listening + (self.OQ1 * 3)
                self.creative = self.creative + (self.OQ1 * 4)
                self.delegation = self.delegation + (self.OQ1 * 3)
                self.actions = self.actions + (self.OQ1 * 2)     

            self.OQ2 = thisdict[self.OtherQ2.currentText()] 

            if(self.OQ2 == 5):

                self.OQ2 = 0

                self.present = self.present + (self.OQ2 * 3)
                self.pointsself = self.pointsself + (self.OQ2 * 4)
                self.pointsother = self.pointsother + (self.OQ2 * 10)
                self.trust = self.trust +(self.OQ2 * 3)
                self.awareness = self.awareness + (self.OQ2 * 3)
                self.listening = self.listening + (self.OQ2 * 3)
                self.creative = self.creative + (self.OQ2 * 3)
                self.reflection = self.reflection + (self.OQ2 * 2)
                self.selfaware = self.selfaware + (self.OQ2 * 2)

            elif(self.OQ2 == 4):

                self.OQ2 = 1
                self.present = self.present + (self.OQ2 * 3)
                self.pointsself = self.pointsself + (self.OQ2 * 4)
                self.pointsother = self.pointsother + (self.OQ2 * 10)
                self.trust = self.trust +(self.OQ2 * 3)
                self.awareness = self.awareness + (self.OQ2 * 3)
                self.listening = self.listening + (self.OQ2 * 3)
                self.creative = self.creative + (self.OQ2 * 3)
                self.reflection = self.reflection + (self.OQ2 * 2)
                self.selfaware = self.selfaware + (self.OQ2 * 2)    
                
            elif(self.OQ2 == 3):
                self.OQ2 = 2
                self.present = self.present + (self.OQ2 * 3)
                self.pointsself = self.pointsself + (self.OQ2 * 4)
                self.pointsother = self.pointsother + (self.OQ2 * 10)
                self.trust = self.trust +(self.OQ2 * 3)
                self.awareness = self.awareness + (self.OQ2 * 3)
                self.listening = self.listening + (self.OQ2 * 3)
                self.creative = self.creative + (self.OQ2 * 3)
                self.reflection = self.reflection + (self.OQ2 * 2)
                self.selfaware = self.selfaware + (self.OQ2 * 2)

            elif(self.OQ2 == 2):

                self.OQ2 = 3
                self.present = self.present + (self.OQ2 * 3)
                self.pointsself = self.pointsself + (self.OQ2 * 4)
                self.pointsother = self.pointsother + (self.OQ2 * 10)
                self.trust = self.trust +(self.OQ2 * 3)
                self.awareness = self.awareness + (self.OQ2 * 3)
                self.listening = self.listening + (self.OQ2 * 3)
                self.creative = self.creative + (self.OQ2 * 3)
                self.reflection = self.reflection + (self.OQ2 * 2)
                self.selfaware = self.selfaware + (self.OQ2 * 2)

            elif(self.OQ2 == 1):

                self.OQ2 = 4
                self.present = self.present + (self.OQ2 * 3)
                self.pointsself = self.pointsself + (self.OQ2 * 4)
                self.pointsother = self.pointsother + (self.OQ2 * 10)
                self.trust = self.trust +(self.OQ2 * 3)
                self.awareness = self.awareness + (self.OQ2 * 3)
                self.listening = self.listening + (self.OQ2 * 3)
                self.creative = self.creative + (self.OQ2 * 3)
                self.reflection = self.reflection + (self.OQ2 * 2)
                self.selfaware = self.selfaware + (self.OQ2 * 2)
                
            elif(self.OQ2 == 0):

                self.OQ2 = 5
                self.present = self.present + (self.OQ2 * 3)
                self.pointsself = self.pointsself + (self.OQ2 * 4)
                self.pointsother = self.pointsother + (self.OQ2 * 10)
                self.trust = self.trust +(self.OQ2 * 3)
                self.awareness = self.awareness + (self.OQ2 * 3)
                self.listening = self.listening + (self.OQ2 * 3)
                self.creative = self.creative + (self.OQ2 * 3)
                self.reflection = self.reflection + (self.OQ2 * 2)
                self.selfaware = self.selfaware + (self.OQ2 * 2)

            self.OQ3 = thisdict[self.OtherQ3.currentText()] 

            if(self.OQ3 == 5):

                self.OQ3 = 0

                self.contracting = self.contracting + (self.OQ3 * 2)
                self.feedback = self.feedback + (self.OQ3 * 2)
                self.pointsother = self.pointsother + (self.OQ3 * 10)
                self.trust = self.trust +(self.OQ3 * 3)
                self.confidentiatly = self.confidentiatly + (self.OQ3 * 2)
                self.awareness = self.awareness + (self.OQ3 * 3)
                self.perspectives = self.perspectives + (self.OQ3 * 2)
                self.listening = self.listening + (self.OQ3 * 2)
                self.delegation = self.delegation + (self.OQ3 * 1)
                self.actions = self.actions + (self.OQ3 * 2)

            elif(self.OQ3 == 4):

                self.OQ3 = 1
                self.contracting = self.contracting + (self.OQ3 * 2)
                self.feedback = self.feedback + (self.OQ3 * 2)
                self.pointsother = self.pointsother + (self.OQ3 * 10)
                self.trust = self.trust +(self.OQ3 * 3)
                self.confidentiatly = self.confidentiatly + (self.OQ3 * 2)
                self.awareness = self.awareness + (self.OQ3 * 3)
                self.perspectives = self.perspectives + (self.OQ3 * 2)
                self.listening = self.listening + (self.OQ3 * 2)
                self.delegation = self.delegation + (self.OQ3 * 1)
                self.actions = self.actions + (self.OQ3 * 2)
                
            elif(self.OQ3 == 3):
                self.OQ3 = 2
                self.contracting = self.contracting + (self.OQ3 * 2)
                self.feedback = self.feedback + (self.OQ3 * 2)
                self.pointsother = self.pointsother + (self.OQ3 * 10)
                self.trust = self.trust +(self.OQ3 * 3)
                self.confidentiatly = self.confidentiatly + (self.OQ3 * 2)
                self.awareness = self.awareness + (self.OQ3 * 3)
                self.perspectives = self.perspectives + (self.OQ3 * 2)
                self.listening = self.listening + (self.OQ3 * 2)
                self.delegation = self.delegation + (self.OQ3 * 1)
                self.actions = self.actions + (self.OQ3 * 2)

            elif(self.OQ3 == 2):

                self.OQ3 = 3
                self.contracting = self.contracting + (self.OQ3 * 2)
                self.feedback = self.feedback + (self.OQ3 * 2)
                self.pointsother = self.pointsother + (self.OQ3 * 10)
                self.trust = self.trust +(self.OQ3 * 3)
                self.confidentiatly = self.confidentiatly + (self.OQ3 * 2)
                self.awareness = self.awareness + (self.OQ3 * 3)
                self.perspectives = self.perspectives + (self.OQ3 * 2)
                self.listening = self.listening + (self.OQ3 * 2)
                self.delegation = self.delegation + (self.OQ3 * 1)
                self.actions = self.actions + (self.OQ3 * 2)

            elif(self.OQ3 == 1):

                self.OQ3 = 4
                self.contracting = self.contracting + (self.OQ3 * 2)
                self.feedback = self.feedback + (self.OQ3 * 2)
                self.pointsother = self.pointsother + (self.OQ3 * 10)
                self.trust = self.trust +(self.OQ3 * 3)
                self.confidentiatly = self.confidentiatly + (self.OQ3 * 2)
                self.awareness = self.awareness + (self.OQ3 * 3)
                self.perspectives = self.perspectives + (self.OQ3 * 2)
                self.listening = self.listening + (self.OQ3 * 2)
                self.delegation = self.delegation + (self.OQ3 * 1)
                self.actions = self.actions + (self.OQ3 * 2)

            elif(self.OQ3 == 0):

                self.OQ3 = 5
                self.contracting = self.contracting + (self.OQ3 * 2)
                self.feedback = self.feedback + (self.OQ3 * 2)
                self.pointsother = self.pointsother + (self.OQ3 * 10)
                self.trust = self.trust +(self.OQ3 * 3)
                self.confidentiatly = self.confidentiatly + (self.OQ3 * 2)
                self.awareness = self.awareness + (self.OQ3 * 3)
                self.perspectives = self.perspectives + (self.OQ3 * 2)
                self.listening = self.listening + (self.OQ3 * 2)
                self.delegation = self.delegation + (self.OQ3 * 1)
                self.actions = self.actions + (self.OQ3 * 2)
  
            self.TQ1 = thisdict[self.TrustQ1.currentText()] 

            if(self.TQ1 == 5):

                self.TQ1 = 0

                self.contracting = self.contracting + (self.TQ1 * 3)
                self.feedback = self.feedback + (self.TQ1 * 5)
                self.present = self.present + (self.TQ1 *2)
                self.pointsself = self.pointsself + (self.TQ1 * 2)
                self.trust = self.trust +(self.TQ1 * 10)
                self.awareness = self.awareness + (self.TQ1 * 1)
                self.perspectives = self.perspectives + (self.TQ1 * 2)
                self.listening = self.listening + (self.TQ1 * 2)
                self.creative = self.creative + (self.TQ1 * 3)
                self.selfaware = self.selfaware + (self.TQ1 * 2)

            elif(self.TQ1 == 4):

                self.TQ1 = 1
                self.contracting = self.contracting + (self.TQ1 * 3)
                self.feedback = self.feedback + (self.TQ1 * 5)
                self.present = self.present + (self.TQ1 *2)
                self.pointsself = self.pointsself + (self.TQ1 * 2)
                self.trust = self.trust +(self.TQ1 * 10)
                self.awareness = self.awareness + (self.TQ1 * 1)
                self.perspectives = self.perspectives + (self.TQ1 * 2)
                self.listening = self.listening + (self.TQ1 * 2)
                self.creative = self.creative + (self.TQ1 * 3)
                self.selfaware = self.selfaware + (self.TQ1 * 2)
                
            elif(self.TQ1 == 3):
                self.TQ1 = 2
                self.contracting = self.contracting + (self.TQ1 * 3)
                self.feedback = self.feedback + (self.TQ1 * 5)
                self.present = self.present + (self.TQ1 *2)
                self.pointsself = self.pointsself + (self.TQ1 * 2)
                self.trust = self.trust +(self.TQ1 * 10)
                self.awareness = self.awareness + (self.TQ1 * 1)
                self.perspectives = self.perspectives + (self.TQ1 * 2)
                self.listening = self.listening + (self.TQ1 * 2)
                self.creative = self.creative + (self.TQ1 * 3)
                self.selfaware = self.selfaware + (self.TQ1 * 2)

            elif(self.TQ1 == 2):

                self.TQ1 = 3
                self.contracting = self.contracting + (self.TQ1 * 3)
                self.feedback = self.feedback + (self.TQ1 * 5)
                self.present = self.present + (self.TQ1 *2)
                self.pointsself = self.pointsself + (self.TQ1 * 2)
                self.trust = self.trust +(self.TQ1 * 10)
                self.awareness = self.awareness + (self.TQ1 * 1)
                self.perspectives = self.perspectives + (self.TQ1 * 2)
                self.listening = self.listening + (self.TQ1 * 2)
                self.creative = self.creative + (self.TQ1 * 3)
                self.selfaware = self.selfaware + (self.TQ1 * 2)

            elif(self.TQ1 == 1):

                self.TQ1 = 4
                self.contracting = self.contracting + (self.TQ1 * 3)
                self.feedback = self.feedback + (self.TQ1 * 5)
                self.present = self.present + (self.TQ1 *2)
                self.pointsself = self.pointsself + (self.TQ1 * 2)
                self.trust = self.trust +(self.TQ1 * 10)
                self.awareness = self.awareness + (self.TQ1 * 1)
                self.perspectives = self.perspectives + (self.TQ1 * 2)
                self.listening = self.listening + (self.TQ1 * 2)
                self.creative = self.creative + (self.TQ1 * 3)
                self.selfaware = self.selfaware + (self.TQ1 * 2)

            elif(self.TQ1 == 0):

                self.TQ1 = 5
                self.contracting = self.contracting + (self.TQ1 * 3)
                self.feedback = self.feedback + (self.TQ1 * 5)
                self.present = self.present + (self.TQ1 *2)
                self.pointsself = self.pointsself + (self.TQ1 * 2)
                self.trust = self.trust +(self.TQ1 * 10)
                self.awareness = self.awareness + (self.TQ1 * 1)
                self.perspectives = self.perspectives + (self.TQ1 * 2)
                self.listening = self.listening + (self.TQ1 * 2)
                self.creative = self.creative + (self.TQ1 * 3)
                self.selfaware = self.selfaware + (self.TQ1 * 2)


            self.TQ2 = thisdict[self.TrustQ2.currentText()] 

            if(self.TQ2 == 5):

                self.TQ2 = 0

                self.contracting = self.contracting + (self.TQ2 * 3)
                self.feedback = self.feedback + (self.TQ2 * 5)
                self.present = self.present + (self.TQ2 *2)
                self.pointsself = self.pointsself + (self.TQ2 * 2)
                self.trust = self.trust +(self.TQ2 * 10)
                self.awareness = self.awareness + (self.TQ2 * 1)
                self.perspectives = self.perspectives + (self.TQ2 * 2)
                self.listening = self.listening + (self.TQ2 * 2)
                self.creative = self.creative + (self.TQ2 * 3)
                self.selfaware = self.selfaware + (self.TQ2 * 2)

            elif(self.TQ2 == 4):

                self.TQ2 = 1
                self.contracting = self.contracting + (self.TQ2 * 3)
                self.feedback = self.feedback + (self.TQ2 * 5)
                self.present = self.present + (self.TQ2 *2)
                self.pointsself = self.pointsself + (self.TQ2 * 2)
                self.trust = self.trust +(self.TQ2 * 10)
                self.awareness = self.awareness + (self.TQ2 * 1)
                self.perspectives = self.perspectives + (self.TQ2 * 2)
                self.listening = self.listening + (self.TQ2 * 2)
                self.creative = self.creative + (self.TQ2 * 3)
                self.selfaware = self.selfaware + (self.TQ2 * 2)    
                
            elif(self.TQ2 == 3):
                self.TQ2 = 2
                self.contracting = self.contracting + (self.TQ2 * 3)
                self.feedback = self.feedback + (self.TQ2 * 5)
                self.present = self.present + (self.TQ2 *2)
                self.pointsself = self.pointsself + (self.TQ2 * 2)
                self.trust = self.trust +(self.TQ2 * 10)
                self.awareness = self.awareness + (self.TQ2 * 1)
                self.perspectives = self.perspectives + (self.TQ2 * 2)
                self.listening = self.listening + (self.TQ2 * 2)
                self.creative = self.creative + (self.TQ2 * 3)
                self.selfaware = self.selfaware + (self.TQ2 * 2)

            elif(self.TQ2 == 2):

                self.TQ2 = 3
                self.contracting = self.contracting + (self.TQ2 * 3)
                self.feedback = self.feedback + (self.TQ2 * 5)
                self.present = self.present + (self.TQ2 *2)
                self.pointsself = self.pointsself + (self.TQ2 * 2)
                self.trust = self.trust +(self.TQ2 * 10)
                self.awareness = self.awareness + (self.TQ2 * 1)
                self.perspectives = self.perspectives + (self.TQ2 * 2)
                self.listening = self.listening + (self.TQ2 * 2)
                self.creative = self.creative + (self.TQ2 * 3)
                self.selfaware = self.selfaware + (self.TQ2 * 2)      

            elif(self.TQ2 == 1):

                self.TQ2 = 4
                self.contracting = self.contracting + (self.TQ2 * 3)
                self.feedback = self.feedback + (self.TQ2 * 5)
                self.present = self.present + (self.TQ2 *2)
                self.pointsself = self.pointsself + (self.TQ2 * 2)
                self.trust = self.trust +(self.TQ2 * 10)
                self.awareness = self.awareness + (self.TQ2 * 1)
                self.perspectives = self.perspectives + (self.TQ2 * 2)
                self.listening = self.listening + (self.TQ2 * 2)
                self.creative = self.creative + (self.TQ2 * 3)
                self.selfaware = self.selfaware + (self.TQ2 * 2)

            elif(self.TQ2 == 0):

                self.TQ2 = 5
                self.contracting = self.contracting + (self.TQ2 * 3)
                self.feedback = self.feedback + (self.TQ2 * 5)
                self.present = self.present + (self.TQ2 *2)
                self.pointsself = self.pointsself + (self.TQ2 * 2)
                self.trust = self.trust +(self.TQ2 * 10)
                self.awareness = self.awareness + (self.TQ2 * 1)
                self.perspectives = self.perspectives + (self.TQ2 * 2)
                self.listening = self.listening + (self.TQ2 * 2)
                self.creative = self.creative + (self.TQ2 * 3)
                self.selfaware = self.selfaware + (self.TQ2 * 2)

            self.TQ3 = thisdict[self.TrustQ3.currentText()] 

            if(self.TQ3 == 5):

                self.TQ3 = 0

                self.feedback = self.feedback + (self.TQ3 * 1)
                self.present = self.present + (self.TQ3 *5)
                self.trust = self.trust +(self.TQ3 * 10)
                self.confidentiatly = self.confidentiatly + (self.TQ3 * 1)
                self.listening = self.listening + (self.TQ3 * 3)
                self.creative = self.creative + (self.TQ3 * 3)
                self.selfaware = self.selfaware + (self.TQ3 * 2)

            elif(self.TQ3 == 4):

                self.TQ3 = 1
                self.feedback = self.feedback + (self.TQ3 * 1)
                self.present = self.present + (self.TQ3 *5)
                self.trust = self.trust +(self.TQ3 * 10)
                self.confidentiatly = self.confidentiatly + (self.TQ3 * 1)
                self.listening = self.listening + (self.TQ3 * 3)
                self.creative = self.creative + (self.TQ3 * 3)
                self.selfaware = self.selfaware + (self.TQ3 * 2) 
                
            elif(self.TQ3 == 3):
                self.TQ3 = 2
                self.feedback = self.feedback + (self.TQ3 * 1)
                self.present = self.present + (self.TQ3 *5)
                self.trust = self.trust +(self.TQ3 * 10)
                self.confidentiatly = self.confidentiatly + (self.TQ3 * 1)
                self.listening = self.listening + (self.TQ3 * 3)
                self.creative = self.creative + (self.TQ3 * 3)
                self.selfaware = self.selfaware + (self.TQ3 * 2)

            elif(self.TQ3 == 2):

                self.TQ3 = 3
                self.feedback = self.feedback + (self.TQ3 * 1)
                self.present = self.present + (self.TQ3 *5)
                self.trust = self.trust +(self.TQ3 * 10)
                self.confidentiatly = self.confidentiatly + (self.TQ3 * 1)
                self.listening = self.listening + (self.TQ3 * 3)
                self.creative = self.creative + (self.TQ3 * 3)
                self.selfaware = self.selfaware + (self.TQ3 * 2)

            elif(self.TQ3 == 1):

                self.TQ3 = 4
                self.feedback = self.feedback + (self.TQ3 * 1)
                self.present = self.present + (self.TQ3 *5)
                self.trust = self.trust +(self.TQ3 * 10)
                self.confidentiatly = self.confidentiatly + (self.TQ3 * 1)
                self.listening = self.listening + (self.TQ3 * 3)
                self.creative = self.creative + (self.TQ3 * 3)
                self.selfaware = self.selfaware + (self.TQ3 * 2)

            elif(self.TQ3 == 0):

                self.TQ3 = 5
                self.feedback = self.feedback + (self.TQ3 * 1)
                self.present = self.present + (self.TQ3 *5)
                self.trust = self.trust +(self.TQ3 * 10)
                self.confidentiatly = self.confidentiatly + (self.TQ3 * 1)
                self.listening = self.listening + (self.TQ3 * 3)
                self.creative = self.creative + (self.TQ3 * 3)
                self.selfaware = self.selfaware + (self.TQ3 * 2)

            self.PresentToConf(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware)
            self.h.hide()


    def PresentToConf(self,email,birth,edu,lead,workyears,contracting,feedback,present,pointsself,pointsother,trust,confidentiatly,awareness,perspectives,listening,creative,delegation,actions,reflection,selfaware):
        self.main = QtWidgets.QMainWindow() 
        print("end")
        self.ui = Ui_ConfAwarePersp(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware) 
        self.ui.setupUi(self.main)
        
        self.main.show()      

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()   

    def retranslateUi(self, PauseOtherTrust):
        _translate = QtCore.QCoreApplication.translate
        PauseOtherTrust.setWindowTitle(_translate("PauseOtherTrust", "COTG"))
        self.label.setText(_translate("PauseOtherTrust", "<html><head/><body><p align=\"center\">Please answer the following questions</p></body></html>"))
        self.PauseQ1.setToolTip(_translate("PauseOtherTrust", "Please select from the following"))
        self.PauseQ1.setItemText(0, _translate("PauseOtherTrust", "Never"))
        self.PauseQ1.setItemText(1, _translate("PauseOtherTrust", "Very Rarely"))
        self.PauseQ1.setItemText(2, _translate("PauseOtherTrust", "Rarely"))
        self.PauseQ1.setItemText(3, _translate("PauseOtherTrust", "Sometimes"))
        self.PauseQ1.setItemText(4, _translate("PauseOtherTrust", "Often"))
        self.PauseQ1.setItemText(5, _translate("PauseOtherTrust", "Always"))
        self.label_2.setText(_translate("PauseOtherTrust", "<html><head/><body><p>When I have an important deadline I tend to ignore everything else and focus on getting </p><p>it done</p></body></html>"))
        self.PauseQ2.setToolTip(_translate("PauseOtherTrust", "Please select from the following"))
        self.PauseQ2.setItemText(0, _translate("PauseOtherTrust", "Never"))
        self.PauseQ2.setItemText(1, _translate("PauseOtherTrust", "Very Rarely"))
        self.PauseQ2.setItemText(2, _translate("PauseOtherTrust", "Rarely"))
        self.PauseQ2.setItemText(3, _translate("PauseOtherTrust", "Sometimes"))
        self.PauseQ2.setItemText(4, _translate("PauseOtherTrust", "Often"))
        self.PauseQ2.setItemText(5, _translate("PauseOtherTrust", "Always"))
        self.label_4.setText(_translate("PauseOtherTrust", "<html><head/><body><p>I attend to the \'\'big picture\'\'</p></body></html>"))
        self.PauseQ3.setToolTip(_translate("PauseOtherTrust", "Please select from the following"))
        self.PauseQ3.setItemText(0, _translate("PauseOtherTrust", "Never"))
        self.PauseQ3.setItemText(1, _translate("PauseOtherTrust", "Very Rarely"))
        self.PauseQ3.setItemText(2, _translate("PauseOtherTrust", "Rarely"))
        self.PauseQ3.setItemText(3, _translate("PauseOtherTrust", "Sometimes"))
        self.PauseQ3.setItemText(4, _translate("PauseOtherTrust", "Often"))
        self.PauseQ3.setItemText(5, _translate("PauseOtherTrust", "Always"))
        self.label_5.setText(_translate("PauseOtherTrust", "<html><head/><body><p>When everything seems chaotic or out of control I am good at taking a moment to step </p><p>back and notice what\'s going on</p></body></html>"))
        self.label_6.setText(_translate("PauseOtherTrust", "<html><head/><body><p>I am good at helping colleagues or team members to step back when they are getting</p><p>lost in the detail or experiencing stress</p></body></html>"))
        self.label_7.setText(_translate("PauseOtherTrust", "<html><head/><body><p>I am unafraid of silence in a conversation</p></body></html>"))
        self.label_8.setText(_translate("PauseOtherTrust", "<html><head/><body><p>Sometimes, I suggest to a colleagure that they \'sleep on it\' rather than rush ahead</p></body></html>"))
        self.OtherQ1.setToolTip(_translate("PauseOtherTrust", "Please select from the following"))
        self.OtherQ1.setItemText(0, _translate("PauseOtherTrust", "Never"))
        self.OtherQ1.setItemText(1, _translate("PauseOtherTrust", "Very Rarely"))
        self.OtherQ1.setItemText(2, _translate("PauseOtherTrust", "Rarely"))
        self.OtherQ1.setItemText(3, _translate("PauseOtherTrust", "Sometimes"))
        self.OtherQ1.setItemText(4, _translate("PauseOtherTrust", "Often"))
        self.OtherQ1.setItemText(5, _translate("PauseOtherTrust", "Always"))
        self.OtherQ2.setToolTip(_translate("PauseOtherTrust", "Please select from the following"))
        self.OtherQ2.setItemText(0, _translate("PauseOtherTrust", "Never"))
        self.OtherQ2.setItemText(1, _translate("PauseOtherTrust", "Very Rarely"))
        self.OtherQ2.setItemText(2, _translate("PauseOtherTrust", "Rarely"))
        self.OtherQ2.setItemText(3, _translate("PauseOtherTrust", "Sometimes"))
        self.OtherQ2.setItemText(4, _translate("PauseOtherTrust", "Often"))
        self.OtherQ2.setItemText(5, _translate("PauseOtherTrust", "Always"))
        self.OtherQ3.setToolTip(_translate("PauseOtherTrust", "Please select from the following"))
        self.OtherQ3.setItemText(0, _translate("PauseOtherTrust", "Never"))
        self.OtherQ3.setItemText(1, _translate("PauseOtherTrust", "Very Rarely"))
        self.OtherQ3.setItemText(2, _translate("PauseOtherTrust", "Rarely"))
        self.OtherQ3.setItemText(3, _translate("PauseOtherTrust", "Sometimes"))
        self.OtherQ3.setItemText(4, _translate("PauseOtherTrust", "Often"))
        self.OtherQ3.setItemText(5, _translate("PauseOtherTrust", "Always"))
        self.label_9.setText(_translate("PauseOtherTrust", "<html><head/><body><p>I know how to question suspicious dynamics between peers or with my boss(es)</p></body></html>"))
        self.label_10.setText(_translate("PauseOtherTrust", "<html><head/><body><p>I have skills that allow me to confront/ foreground/ uncover/ comment on unhelpful</p><p>behaviour of others even if they are my peers or boss</p><p><br/></p></body></html>"))
        self.label_11.setText(_translate("PauseOtherTrust", "<html><head/><body><p>I treat others as individuals rather than just as a member of a group</p></body></html>"))
        self.TrustQ1.setToolTip(_translate("PauseOtherTrust", "Please select from the following"))
        self.TrustQ1.setItemText(0, _translate("PauseOtherTrust", "Never"))
        self.TrustQ1.setItemText(1, _translate("PauseOtherTrust", "Very Rarely"))
        self.TrustQ1.setItemText(2, _translate("PauseOtherTrust", "Rarely"))
        self.TrustQ1.setItemText(3, _translate("PauseOtherTrust", "Sometimes"))
        self.TrustQ1.setItemText(4, _translate("PauseOtherTrust", "Often"))
        self.TrustQ1.setItemText(5, _translate("PauseOtherTrust", "Always"))
        self.TrustQ2.setToolTip(_translate("PauseOtherTrust", "Please select from the following"))
        self.TrustQ2.setItemText(0, _translate("PauseOtherTrust", "Never"))
        self.TrustQ2.setItemText(1, _translate("PauseOtherTrust", "Very Rarely"))
        self.TrustQ2.setItemText(2, _translate("PauseOtherTrust", "Rarely"))
        self.TrustQ2.setItemText(3, _translate("PauseOtherTrust", "Sometimes"))
        self.TrustQ2.setItemText(4, _translate("PauseOtherTrust", "Often"))
        self.TrustQ2.setItemText(5, _translate("PauseOtherTrust", "Always"))
        self.TrustQ3.setToolTip(_translate("PauseOtherTrust", "Please select from the following"))
        self.TrustQ3.setItemText(0, _translate("PauseOtherTrust", "Never"))
        self.TrustQ3.setItemText(1, _translate("PauseOtherTrust", "Very Rarely"))
        self.TrustQ3.setItemText(2, _translate("PauseOtherTrust", "Rarely"))
        self.TrustQ3.setItemText(3, _translate("PauseOtherTrust", "Sometimes"))
        self.TrustQ3.setItemText(4, _translate("PauseOtherTrust", "Often"))
        self.TrustQ3.setItemText(5, _translate("PauseOtherTrust", "Always"))
        self.NextQuestion2.setStatusTip(_translate("PauseOtherTrust", "Click this to go to next questions"))
        self.NextQuestion2.setText(_translate("PauseOtherTrust", "Next"))
        self.Back.setStatusTip(_translate("PauseOtherTrust", "Click this to go back a form"))
        self.Back.setText(_translate("PauseOtherTrust", "Back"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PauseOtherTrust = QtWidgets.QDialog()
    ui = Ui_PauseOtherTrust()
    ui.setupUi(PauseOtherTrust)
    PauseOtherTrust.show()
    app.exec_()
