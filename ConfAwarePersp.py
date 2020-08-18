# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfAwarePersp.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QShortcut , QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog , QAction ,QShortcut
from ListCreativeDelegation import Ui_ListCreativeDelegation

thisdict = {"Never":0,
            "Very Rarely":1,
            "Rarely":2,
            "Sometimes":3,
            "Often":4,
            "Always":5}


class Ui_ConfAwarePersp(object):


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



    def setupUi(self, ConfAwarePersp):
        ConfAwarePersp.setObjectName("ConfAwarePersp")
        ConfAwarePersp.resize(820, 864)
        ConfAwarePersp.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.label = QtWidgets.QLabel(ConfAwarePersp)
        self.label.setGeometry(QtCore.QRect(210, 20, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.ConfidentialityQ1 = QtWidgets.QComboBox(ConfAwarePersp)
        self.ConfidentialityQ1.setGeometry(QtCore.QRect(680, 90, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ConfidentialityQ1.setFont(font)
        self.ConfidentialityQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ConfidentialityQ1.setMaxVisibleItems(6)
        self.ConfidentialityQ1.setObjectName("ConfidentialityQ1")
        self.ConfidentialityQ1.addItem("")
        self.ConfidentialityQ1.addItem("")
        self.ConfidentialityQ1.addItem("")
        self.ConfidentialityQ1.addItem("")
        self.ConfidentialityQ1.addItem("")
        self.ConfidentialityQ1.addItem("")
        self.ConfidentialityQ2 = QtWidgets.QComboBox(ConfAwarePersp)
        self.ConfidentialityQ2.setGeometry(QtCore.QRect(680, 180, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ConfidentialityQ2.setFont(font)
        self.ConfidentialityQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ConfidentialityQ2.setMaxVisibleItems(6)
        self.ConfidentialityQ2.setObjectName("ConfidentialityQ2")
        self.ConfidentialityQ2.addItem("")
        self.ConfidentialityQ2.addItem("")
        self.ConfidentialityQ2.addItem("")
        self.ConfidentialityQ2.addItem("")
        self.ConfidentialityQ2.addItem("")
        self.ConfidentialityQ2.addItem("")
        self.label_2 = QtWidgets.QLabel(ConfAwarePersp)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ConfAwarePersp)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ConfAwarePersp)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ConfidentialityQ3 = QtWidgets.QComboBox(ConfAwarePersp)
        self.ConfidentialityQ3.setGeometry(QtCore.QRect(680, 270, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ConfidentialityQ3.setFont(font)
        self.ConfidentialityQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ConfidentialityQ3.setMaxVisibleItems(6)
        self.ConfidentialityQ3.setObjectName("ConfidentialityQ3")
        self.ConfidentialityQ3.addItem("")
        self.ConfidentialityQ3.addItem("")
        self.ConfidentialityQ3.addItem("")
        self.ConfidentialityQ3.addItem("")
        self.ConfidentialityQ3.addItem("")
        self.ConfidentialityQ3.addItem("")
        self.label_5 = QtWidgets.QLabel(ConfAwarePersp)
        self.label_5.setGeometry(QtCore.QRect(10, 350, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.AwarenessQ1 = QtWidgets.QComboBox(ConfAwarePersp)
        self.AwarenessQ1.setGeometry(QtCore.QRect(680, 350, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AwarenessQ1.setFont(font)
        self.AwarenessQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AwarenessQ1.setMaxVisibleItems(6)
        self.AwarenessQ1.setObjectName("AwarenessQ1")
        self.AwarenessQ1.addItem("")
        self.AwarenessQ1.addItem("")
        self.AwarenessQ1.addItem("")
        self.AwarenessQ1.addItem("")
        self.AwarenessQ1.addItem("")
        self.AwarenessQ1.addItem("")
        self.label_6 = QtWidgets.QLabel(ConfAwarePersp)
        self.label_6.setGeometry(QtCore.QRect(10, 410, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.AwarenessQ2 = QtWidgets.QComboBox(ConfAwarePersp)
        self.AwarenessQ2.setGeometry(QtCore.QRect(680, 420, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AwarenessQ2.setFont(font)
        self.AwarenessQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AwarenessQ2.setMaxVisibleItems(6)
        self.AwarenessQ2.setObjectName("AwarenessQ2")
        self.AwarenessQ2.addItem("")
        self.AwarenessQ2.addItem("")
        self.AwarenessQ2.addItem("")
        self.AwarenessQ2.addItem("")
        self.AwarenessQ2.addItem("")
        self.AwarenessQ2.addItem("")
        self.label_7 = QtWidgets.QLabel(ConfAwarePersp)
        self.label_7.setGeometry(QtCore.QRect(10, 500, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.AwarenessQ3 = QtWidgets.QComboBox(ConfAwarePersp)
        self.AwarenessQ3.setGeometry(QtCore.QRect(680, 500, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AwarenessQ3.setFont(font)
        self.AwarenessQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AwarenessQ3.setMaxVisibleItems(6)
        self.AwarenessQ3.setObjectName("AwarenessQ3")
        self.AwarenessQ3.addItem("")
        self.AwarenessQ3.addItem("")
        self.AwarenessQ3.addItem("")
        self.AwarenessQ3.addItem("")
        self.AwarenessQ3.addItem("")
        self.AwarenessQ3.addItem("")
        self.label_8 = QtWidgets.QLabel(ConfAwarePersp)
        self.label_8.setGeometry(QtCore.QRect(10, 560, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(ConfAwarePersp)
        self.label_9.setGeometry(QtCore.QRect(10, 650, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.PerspectiveQ1 = QtWidgets.QComboBox(ConfAwarePersp)
        self.PerspectiveQ1.setGeometry(QtCore.QRect(680, 570, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PerspectiveQ1.setFont(font)
        self.PerspectiveQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PerspectiveQ1.setMaxVisibleItems(6)
        self.PerspectiveQ1.setObjectName("PerspectiveQ1")
        self.PerspectiveQ1.addItem("")
        self.PerspectiveQ1.addItem("")
        self.PerspectiveQ1.addItem("")
        self.PerspectiveQ1.addItem("")
        self.PerspectiveQ1.addItem("")
        self.PerspectiveQ1.addItem("")
        self.label_10 = QtWidgets.QLabel(ConfAwarePersp)
        self.label_10.setGeometry(QtCore.QRect(10, 740, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.PerspectiveQ2 = QtWidgets.QComboBox(ConfAwarePersp)
        self.PerspectiveQ2.setGeometry(QtCore.QRect(680, 660, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PerspectiveQ2.setFont(font)
        self.PerspectiveQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PerspectiveQ2.setMaxVisibleItems(6)
        self.PerspectiveQ2.setObjectName("PerspectiveQ2")
        self.PerspectiveQ2.addItem("")
        self.PerspectiveQ2.addItem("")
        self.PerspectiveQ2.addItem("")
        self.PerspectiveQ2.addItem("")
        self.PerspectiveQ2.addItem("")
        self.PerspectiveQ2.addItem("")
        self.PerspectiveQ3 = QtWidgets.QComboBox(ConfAwarePersp)
        self.PerspectiveQ3.setGeometry(QtCore.QRect(680, 740, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PerspectiveQ3.setFont(font)
        self.PerspectiveQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PerspectiveQ3.setMaxVisibleItems(6)
        self.PerspectiveQ3.setObjectName("PerspectiveQ3")
        self.PerspectiveQ3.addItem("")
        self.PerspectiveQ3.addItem("")
        self.PerspectiveQ3.addItem("")
        self.PerspectiveQ3.addItem("")
        self.PerspectiveQ3.addItem("")
        self.PerspectiveQ3.addItem("")
        self.Back = QtWidgets.QPushButton(ConfAwarePersp)
        self.Back.setGeometry(QtCore.QRect(10, 810, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setAutoFillBackground(False)
        self.Back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Back.setObjectName("Back")
        self.NextQuestion2 = QtWidgets.QPushButton(ConfAwarePersp)
        self.NextQuestion2.setGeometry(QtCore.QRect(700, 810, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NextQuestion2.setFont(font)
        self.NextQuestion2.setAutoFillBackground(False)
        self.NextQuestion2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NextQuestion2.setObjectName("NextQuestion2")
        self.line = QtWidgets.QFrame(ConfAwarePersp)
        self.line.setGeometry(QtCore.QRect(0, 140, 831, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(ConfAwarePersp)
        self.line_2.setGeometry(QtCore.QRect(0, 230, 831, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(ConfAwarePersp)
        self.line_3.setGeometry(QtCore.QRect(0, 320, 831, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(ConfAwarePersp)
        self.line_4.setGeometry(QtCore.QRect(0, 380, 831, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(ConfAwarePersp)
        self.line_5.setGeometry(QtCore.QRect(0, 470, 831, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(ConfAwarePersp)
        self.line_6.setGeometry(QtCore.QRect(0, 530, 831, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(ConfAwarePersp)
        self.line_7.setGeometry(QtCore.QRect(0, 620, 831, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(ConfAwarePersp)
        self.line_8.setGeometry(QtCore.QRect(0, 710, 831, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(ConfAwarePersp)
        self.line_9.setGeometry(QtCore.QRect(-10, 780, 831, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.retranslateUi(ConfAwarePersp)
        self.ConfidentialityQ1.setCurrentIndex(-1)
        self.ConfidentialityQ2.setCurrentIndex(-1)
        self.ConfidentialityQ3.setCurrentIndex(-1)
        self.AwarenessQ1.setCurrentIndex(-1)
        self.AwarenessQ2.setCurrentIndex(-1)
        self.AwarenessQ3.setCurrentIndex(-1)
        self.PerspectiveQ1.setCurrentIndex(-1)
        self.PerspectiveQ2.setCurrentIndex(-1)
        self.PerspectiveQ3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ConfAwarePersp)

        self.NextQuestion2.clicked.connect(self.pressed)
        self.h = ConfAwarePersp

    def pressed(self):

        if(self.ConfidentialityQ1.currentText() == "" or self.ConfidentialityQ2.currentText() == "" or self.ConfidentialityQ3.currentText() == "" or self.AwarenessQ1.currentText() == "" or self.AwarenessQ2.currentText() == "" or self.AwarenessQ3.currentText() == "" or self.PerspectiveQ1.currentText() == "" or self.PerspectiveQ2.currentText() == "" or self.PerspectiveQ3.currentText() == ""):

            self.messagebox("Error","Please enter all fields")

        else: 

            self.ConQ1 = thisdict[self.ConfidentialityQ1.currentText()]

            self.contracting = self.contracting + (self.ConQ1 * 5)
            self.trust = self.trust + (self.ConQ1 * 5)
            self.confidentiatly = self.confidentiatly + (self.ConQ1 * 10)
            self.selfaware = self.selfaware + (self.ConQ1 * 3)

            self.ConQ2 = thisdict[self.ConfidentialityQ2.currentText()] 

            if(self.ConQ2 == 5):

                self.ConQ2 = 0
                self.contracting = self.contracting + (self.ConQ2 * 3)
                self.feedback = self.feedback + (self.ConQ2 * 2)
                self.trust = self.trust + (self.ConQ2 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ2 * 10)
                self.selfaware = self.selfaware + (self.ConQ2 * 3)
             

            elif(self.ConQ2 == 4):

                self.ConQ2 = 1
                self.contracting = self.contracting + (self.ConQ2 * 3)
                self.feedback = self.feedback + (self.ConQ2 * 2)
                self.trust = self.trust + (self.ConQ2 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ2 * 10)
                self.selfaware = self.selfaware + (self.ConQ2 * 3)  
                
            elif(self.ConQ2 == 3):
                self.ConQ2 = 2
                self.contracting = self.contracting + (self.ConQ2 * 3)
                self.feedback = self.feedback + (self.ConQ2 * 2)
                self.trust = self.trust + (self.ConQ2 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ2 * 10)
                self.selfaware = self.selfaware + (self.ConQ2 * 3)  

            elif(self.ConQ2 == 2):

                self.ConQ2 = 3
                self.contracting = self.contracting + (self.ConQ2 * 3)
                self.feedback = self.feedback + (self.ConQ2 * 2)
                self.trust = self.trust + (self.ConQ2 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ2 * 10)
                self.selfaware = self.selfaware + (self.ConQ2 * 3)  

            elif(self.ConQ2 == 1):

                self.ConQ2 = 4
                self.contracting = self.contracting + (self.ConQ2 * 3)
                self.feedback = self.feedback + (self.ConQ2 * 2)
                self.trust = self.trust + (self.ConQ2 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ2 * 10)
                self.selfaware = self.selfaware + (self.ConQ2 * 3)  
                
            elif(self.ConQ2 == 0):

                self.ConQ2 = 5
                self.contracting = self.contracting + (self.ConQ2 * 3)
                self.feedback = self.feedback + (self.ConQ2 * 2)
                self.trust = self.trust + (self.ConQ2 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ2 * 10)
                self.selfaware = self.selfaware + (self.ConQ2 * 3)  

            self.ConQ3 = thisdict[self.ConfidentialityQ3.currentText()] 

            if(self.ConQ3 == 5):

                self.ConQ3 = 0
                self.contracting = self.contracting + (self.ConQ3 * 5)
                self.trust = self.trust + (self.ConQ3 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ3 * 10)
                self.selfaware = self.selfaware + (self.ConQ3 * 3)
             

            elif(self.ConQ3 == 4):

                self.ConQ3 = 1
                self.contracting = self.contracting + (self.ConQ3 * 5)
                self.trust = self.trust + (self.ConQ3 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ3 * 10)
                self.selfaware = self.selfaware + (self.ConQ3 * 3)
                
            elif(self.ConQ3 == 3):
                self.ConQ3 = 2
                self.contracting = self.contracting + (self.ConQ3 * 5)
                self.trust = self.trust + (self.ConQ3 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ3 * 10)
                self.selfaware = self.selfaware + (self.ConQ3 * 3)

            elif(self.ConQ3 == 2):

                self.ConQ3 = 3
                self.contracting = self.contracting + (self.ConQ3 * 5)
                self.trust = self.trust + (self.ConQ3 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ3 * 10)
                self.selfaware = self.selfaware + (self.ConQ3 * 3)

            elif(self.ConQ3 == 1):

                self.ConQ3 = 4
                self.contracting = self.contracting + (self.ConQ3 * 5)
                self.trust = self.trust + (self.ConQ3 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ3 * 10)
                self.selfaware = self.selfaware + (self.ConQ3 * 3)
                
            elif(self.ConQ3 == 0):

                self.ConQ3 = 5
                self.contracting = self.contracting + (self.ConQ3 * 5)
                self.trust = self.trust + (self.ConQ3 * 5)
                self.confidentiatly = self.confidentiatly + (self.ConQ3 * 10)
                self.selfaware = self.selfaware + (self.ConQ3 * 3)


            self.AQ1 = thisdict[self.AwarenessQ1.currentText()] 

            if(self.AQ1 == 5):

                self.AQ1 = 0
                self.contracting = self.contracting + (self.AQ1 * 1)
                self.feedback = self.feedback + (self.AQ1 * 2)
                self.present = self.present + (self.AQ1 *2)
                self.pointsother = self.pointsother + (self.AQ1 * 3)
                self.trust = self.trust + (self.AQ1 * 3)
                self.awareness = self.awareness + (self.AQ1 * 10)
                self.perspectives = self.perspectives + (self.AQ1 * 4)
                self.listening = self.listening + (self.AQ1 * 4)
                self.creative = self.creative + (self.AQ1 * 5)
                self.actions = self.actions + (self.AQ1 * 1)
                self.selfaware = self.selfaware + (self.AQ1 * 2)
             

            elif(self.AQ1 == 4):

                self.AQ1 = 1
                self.contracting = self.contracting + (self.AQ1 * 1)
                self.feedback = self.feedback + (self.AQ1 * 2)
                self.present = self.present + (self.AQ1 *2)
                self.pointsother = self.pointsother + (self.AQ1 * 3)
                self.trust = self.trust + (self.AQ1 * 3)
                self.awareness = self.awareness + (self.AQ1 * 10)
                self.perspectives = self.perspectives + (self.AQ1 * 4)
                self.listening = self.listening + (self.AQ1 * 4)
                self.creative = self.creative + (self.AQ1 * 5)
                self.actions = self.actions + (self.AQ1 * 1)
                self.selfaware = self.selfaware + (self.AQ1 * 2)
                
            elif(self.AQ1 == 3):
                self.AQ1 = 2
                self.contracting = self.contracting + (self.AQ1 * 1)
                self.feedback = self.feedback + (self.AQ1 * 2)
                self.present = self.present + (self.AQ1 *2)
                self.pointsother = self.pointsother + (self.AQ1 * 3)
                self.trust = self.trust + (self.AQ1 * 3)
                self.awareness = self.awareness + (self.AQ1 * 10)
                self.perspectives = self.perspectives + (self.AQ1 * 4)
                self.listening = self.listening + (self.AQ1 * 4)
                self.creative = self.creative + (self.AQ1 * 5)
                self.actions = self.actions + (self.AQ1 * 1)
                self.selfaware = self.selfaware + (self.AQ1 * 2)

            elif(self.AQ1 == 2):

                self.AQ1 = 3
                self.contracting = self.contracting + (self.AQ1 * 1)
                self.feedback = self.feedback + (self.AQ1 * 2)
                self.present = self.present + (self.AQ1 *2)
                self.pointsother = self.pointsother + (self.AQ1 * 3)
                self.trust = self.trust + (self.AQ1 * 3)
                self.awareness = self.awareness + (self.AQ1 * 10)
                self.perspectives = self.perspectives + (self.AQ1 * 4)
                self.listening = self.listening + (self.AQ1 * 4)
                self.creative = self.creative + (self.AQ1 * 5)
                self.actions = self.actions + (self.AQ1 * 1)
                self.selfaware = self.selfaware + (self.AQ1 * 2)

            elif(self.AQ1 == 1):

                self.AQ1 = 4
                self.contracting = self.contracting + (self.AQ1 * 1)
                self.feedback = self.feedback + (self.AQ1 * 2)
                self.present = self.present + (self.AQ1 *2)
                self.pointsother = self.pointsother + (self.AQ1 * 3)
                self.trust = self.trust + (self.AQ1 * 3)
                self.awareness = self.awareness + (self.AQ1 * 10)
                self.perspectives = self.perspectives + (self.AQ1 * 4)
                self.listening = self.listening + (self.AQ1 * 4)
                self.creative = self.creative + (self.AQ1 * 5)
                self.actions = self.actions + (self.AQ1 * 1)
                self.selfaware = self.selfaware + (self.AQ1 * 2)
       
            elif(self.AQ1 == 0):

                self.AQ1 = 5

                self.contracting = self.contracting + (self.AQ1 * 1)
                self.feedback = self.feedback + (self.AQ1 * 2)
                self.present = self.present + (self.AQ1 *2)
                self.pointsother = self.pointsother + (self.AQ1 * 3)
                self.trust = self.trust + (self.AQ1 * 3)
                self.awareness = self.awareness + (self.AQ1 * 10)
                self.perspectives = self.perspectives + (self.AQ1 * 4)
                self.listening = self.listening + (self.AQ1 * 4)
                self.creative = self.creative + (self.AQ1 * 5)
                self.actions = self.actions + (self.AQ1 * 1)
                self.selfaware = self.selfaware + (self.AQ1 * 2)

            self.AQ2 = thisdict[self.AwarenessQ2.currentText()] 

            if(self.AQ2 == 5):

                self.AQ2 = 0
                self.contracting = self.contracting + (self.AQ2 * 1)
                self.feedback = self.feedback + (self.AQ2 * 2)
                self.pointsother = self.pointsother + (self.AQ2 * 4)
                self.trust = self.trust + (self.AQ2 * 4)
                self.awareness = self.awareness + (self.AQ2 * 10)
                self.perspectives = self.perspectives + (self.AQ2 * 3)
                self.listening = self.listening + (self.AQ2 * 4)
                self.creative = self.creative + (self.AQ2 * 5)
                self.actions = self.actions + (self.AQ2 * 1)
             

            elif(self.AQ2 == 4):

                self.AQ2 = 1
                self.contracting = self.contracting + (self.AQ2 * 1)
                self.feedback = self.feedback + (self.AQ2 * 2)
                self.pointsother = self.pointsother + (self.AQ2 * 4)
                self.trust = self.trust + (self.AQ2 * 4)
                self.awareness = self.awareness + (self.AQ2 * 10)
                self.perspectives = self.perspectives + (self.AQ2 * 3)
                self.listening = self.listening + (self.AQ2 * 4)
                self.creative = self.creative + (self.AQ2 * 5)
                self.actions = self.actions + (self.AQ2 * 1)
                
            elif(self.AQ2 == 3):
                self.AQ2 = 2
                self.contracting = self.contracting + (self.AQ2 * 1)
                self.feedback = self.feedback + (self.AQ2 * 2)
                self.pointsother = self.pointsother + (self.AQ2 * 4)
                self.trust = self.trust + (self.AQ2 * 4)
                self.awareness = self.awareness + (self.AQ2 * 10)
                self.perspectives = self.perspectives + (self.AQ2 * 3)
                self.listening = self.listening + (self.AQ2 * 4)
                self.creative = self.creative + (self.AQ2 * 5)
                self.actions = self.actions + (self.AQ2 * 1)

            elif(self.AQ2 == 2):

                self.AQ2 = 3
                self.contracting = self.contracting + (self.AQ2 * 1)
                self.feedback = self.feedback + (self.AQ2 * 2)
                self.pointsother = self.pointsother + (self.AQ2 * 4)
                self.trust = self.trust + (self.AQ2 * 4)
                self.awareness = self.awareness + (self.AQ2 * 10)
                self.perspectives = self.perspectives + (self.AQ2 * 3)
                self.listening = self.listening + (self.AQ2 * 4)
                self.creative = self.creative + (self.AQ2 * 5)
                self.actions = self.actions + (self.AQ2 * 1)

            elif(self.AQ2 == 1):

                self.AQ2 = 4
                self.contracting = self.contracting + (self.AQ2 * 1)
                self.feedback = self.feedback + (self.AQ2 * 2)
                self.pointsother = self.pointsother + (self.AQ2 * 4)
                self.trust = self.trust + (self.AQ2 * 4)
                self.awareness = self.awareness + (self.AQ2 * 10)
                self.perspectives = self.perspectives + (self.AQ2 * 3)
                self.listening = self.listening + (self.AQ2 * 4)
                self.creative = self.creative + (self.AQ2 * 5)
                self.actions = self.actions + (self.AQ2 * 1)
       
            elif(self.AQ2 == 0):

                self.AQ2 = 5
                self.contracting = self.contracting + (self.AQ2 * 1)
                self.feedback = self.feedback + (self.AQ2 * 2)
                self.pointsother = self.pointsother + (self.AQ2 * 4)
                self.trust = self.trust + (self.AQ2 * 4)
                self.awareness = self.awareness + (self.AQ2 * 10)
                self.perspectives = self.perspectives + (self.AQ2 * 3)
                self.listening = self.listening + (self.AQ2 * 4)
                self.creative = self.creative + (self.AQ2 * 5)
                self.actions = self.actions + (self.AQ2 * 1)
         
            self.AQ3 = thisdict[self.AwarenessQ3.currentText()] 

            if(self.AQ3 == 5):

                self.AQ3 = 0
                self.contracting = self.contracting + (self.AQ3 * 1)
                self.feedback = self.feedback + (self.AQ3 * 3)
                self.pointsother = self.pointsother + (self.AQ3 * 3)
                self.trust = self.trust + (self.AQ3 * 3)
                self.awareness = self.awareness + (self.AQ3 * 10)
                self.perspectives = self.perspectives + (self.AQ3 * 3)
                self.creative = self.creative + (self.AQ3 * 5)
                self.delegation = self.delegation + (self.AQ3 * 3)
                self.actions = self.actions + (self.AQ3 * 1)
             

            elif(self.AQ3 == 4):

                self.AQ3 = 1
                self.contracting = self.contracting + (self.AQ3 * 1)
                self.feedback = self.feedback + (self.AQ3 * 3)
                self.pointsother = self.pointsother + (self.AQ3 * 3)
                self.trust = self.trust + (self.AQ3 * 3)
                self.awareness = self.awareness + (self.AQ3 * 10)
                self.perspectives = self.perspectives + (self.AQ3 * 3)
                self.creative = self.creative + (self.AQ3 * 5)
                self.delegation = self.delegation + (self.AQ3 * 3)
                self.actions = self.actions + (self.AQ3 * 1)
                
            elif(self.AQ3 == 3):
                self.AQ3 = 2
                self.contracting = self.contracting + (self.AQ3 * 1)
                self.feedback = self.feedback + (self.AQ3 * 3)
                self.pointsother = self.pointsother + (self.AQ3 * 3)
                self.trust = self.trust + (self.AQ3 * 3)
                self.awareness = self.awareness + (self.AQ3 * 10)
                self.perspectives = self.perspectives + (self.AQ3 * 3)
                self.creative = self.creative + (self.AQ3 * 5)
                self.delegation = self.delegation + (self.AQ3 * 3)
                self.actions = self.actions + (self.AQ3 * 1)

            elif(self.AQ3 == 2):

                self.AQ3 = 3
                self.contracting = self.contracting + (self.AQ3 * 1)
                self.feedback = self.feedback + (self.AQ3 * 3)
                self.pointsother = self.pointsother + (self.AQ3 * 3)
                self.trust = self.trust + (self.AQ3 * 3)
                self.awareness = self.awareness + (self.AQ3 * 10)
                self.perspectives = self.perspectives + (self.AQ3 * 3)
                self.creative = self.creative + (self.AQ3 * 5)
                self.delegation = self.delegation + (self.AQ3 * 3)
                self.actions = self.actions + (self.AQ3 * 1)

            elif(self.AQ3 == 1):

                self.AQ3 = 4
                self.contracting = self.contracting + (self.AQ3 * 1)
                self.feedback = self.feedback + (self.AQ3 * 3)
                self.pointsother = self.pointsother + (self.AQ3 * 3)
                self.trust = self.trust + (self.AQ3 * 3)
                self.awareness = self.awareness + (self.AQ3 * 10)
                self.perspectives = self.perspectives + (self.AQ3 * 3)
                self.creative = self.creative + (self.AQ3 * 5)
                self.delegation = self.delegation + (self.AQ3 * 3)
                self.actions = self.actions + (self.AQ3 * 1)
       
            elif(self.AQ3 == 0):

                self.AQ3 = 5
                self.contracting = self.contracting + (self.AQ3 * 1)
                self.feedback = self.feedback + (self.AQ3 * 3)
                self.pointsother = self.pointsother + (self.AQ3 * 3)
                self.trust = self.trust + (self.AQ3 * 3)
                self.awareness = self.awareness + (self.AQ3 * 10)
                self.perspectives = self.perspectives + (self.AQ3 * 3)
                self.creative = self.creative + (self.AQ3 * 5)
                self.delegation = self.delegation + (self.AQ3 * 3)
                self.actions = self.actions + (self.AQ3 * 1)

            self.PerQ1 = thisdict[self.PerspectiveQ1.currentText()]

            self.feedback = self.feedback + (self.PerQ1 * 3)
            self.trust = self.trust + (self.PerQ1 * 2 )
            self.awareness = self.awareness + (self.PerQ1 * 2)
            self.perspectives = self.perspectives + (self.PerQ1 *10)
            self.delegation = self.delegation + (self.PerQ1 * 4)
            self.actions = self.actions + (self.PerQ1 * 2)
            self.selfaware = self.selfaware + (self.PerQ1 * 2)


            self.PerQ2 = thisdict[self.PerspectiveQ2.currentText()] 

            if(self.PerQ2 == 5):

                self.PerQ2 = 0
                self.feedback = self.feedback + (self.PerQ2 * 5)
                self.pointsother = self.pointsother + (self.PerQ2 * 2)
                self.trust = self.trust + (self.PerQ2 * 2 )
                self.confidentiatly = self.confidentiatly + (self.PerQ2 * 1)
                self.awareness = self.awareness + (self.PerQ2 * 5)
                self.perspectives = self.perspectives + (self.PerQ2 *10)
                self.listening = self.listening + (self.PerQ2 * 4)
                self.creative = self.creative + (self.PerQ2 * 5)
                self.delegation = self.delegation + (self.PerQ2 * 2)
                self.actions = self.actions + (self.PerQ2 * 2)
             

            elif(self.PerQ2 == 4):

                self.PerQ2 = 1
                self.feedback = self.feedback + (self.PerQ2 * 5)
                self.pointsother = self.pointsother + (self.PerQ2 * 2)
                self.trust = self.trust + (self.PerQ2 * 2 )
                self.confidentiatly = self.confidentiatly + (self.PerQ2 * 1)
                self.awareness = self.awareness + (self.PerQ2 * 5)
                self.perspectives = self.perspectives + (self.PerQ2 *10)
                self.listening = self.listening + (self.PerQ2 * 4)
                self.creative = self.creative + (self.PerQ2 * 5)
                self.delegation = self.delegation + (self.PerQ2 * 2)
                self.actions = self.actions + (self.PerQ2 * 2)
                
            elif(self.PerQ2 == 3):
                self.PerQ2 = 2
                self.feedback = self.feedback + (self.PerQ2 * 5)
                self.pointsother = self.pointsother + (self.PerQ2 * 2)
                self.trust = self.trust + (self.PerQ2 * 2 )
                self.confidentiatly = self.confidentiatly + (self.PerQ2 * 1)
                self.awareness = self.awareness + (self.PerQ2 * 5)
                self.perspectives = self.perspectives + (self.PerQ2 *10)
                self.listening = self.listening + (self.PerQ2 * 4)
                self.creative = self.creative + (self.PerQ2 * 5)
                self.delegation = self.delegation + (self.PerQ2 * 2)
                self.actions = self.actions + (self.PerQ2 * 2)

            elif(self.PerQ2 == 2):

                self.PerQ2 = 3
                self.feedback = self.feedback + (self.PerQ2 * 5)
                self.pointsother = self.pointsother + (self.PerQ2 * 2)
                self.trust = self.trust + (self.PerQ2 * 2 )
                self.confidentiatly = self.confidentiatly + (self.PerQ2 * 1)
                self.awareness = self.awareness + (self.PerQ2 * 5)
                self.perspectives = self.perspectives + (self.PerQ2 *10)
                self.listening = self.listening + (self.PerQ2 * 4)
                self.creative = self.creative + (self.PerQ2 * 5)
                self.delegation = self.delegation + (self.PerQ2 * 2)
                self.actions = self.actions + (self.PerQ2 * 2)

            elif(self.PerQ2 == 1):

                self.PerQ2 = 4
                self.feedback = self.feedback + (self.PerQ2 * 5)
                self.pointsother = self.pointsother + (self.PerQ2 * 2)
                self.trust = self.trust + (self.PerQ2 * 2 )
                self.confidentiatly = self.confidentiatly + (self.PerQ2 * 1)
                self.awareness = self.awareness + (self.PerQ2 * 5)
                self.perspectives = self.perspectives + (self.PerQ2 *10)
                self.listening = self.listening + (self.PerQ2 * 4)
                self.creative = self.creative + (self.PerQ2 * 5)
                self.delegation = self.delegation + (self.PerQ2 * 2)
                self.actions = self.actions + (self.PerQ2 * 2)
       
            elif(self.PerQ2 == 0):

                self.PerQ2 = 5
                self.feedback = self.feedback + (self.PerQ2 * 5)
                self.pointsother = self.pointsother + (self.PerQ2 * 2)
                self.trust = self.trust + (self.PerQ2 * 2 )
                self.confidentiatly = self.confidentiatly + (self.PerQ2 * 1)
                self.awareness = self.awareness + (self.PerQ2 * 5)
                self.perspectives = self.perspectives + (self.PerQ2 *10)
                self.listening = self.listening + (self.PerQ2 * 4)
                self.creative = self.creative + (self.PerQ2 * 5)
                self.delegation = self.delegation + (self.PerQ2 * 2)
                self.actions = self.actions + (self.PerQ2 * 2)

            self.PerQ3 = thisdict[self.PerspectiveQ3.currentText()] 

            if(self.PerQ3 == 5):

                self.PerQ3 = 0
                self.contracting = self.concontracting + (self.PerQ3 *2)
                self.present = self.present + (self.PerQ3 * 1)
                self.pointsother = self.pointsother + (self.PerQ3 * 2)
                self.trust = self.trust + (self.PerQ3 * 2 )
                self.awareness = self.awareness + (self.PerQ3 * 5)
                self.perspectives = self.perspectives + (self.PerQ3 *10)
                self.listening = self.listening + (self.PerQ3 * 3)
                self.creative = self.creative + (self.PerQ3 * 4)
                self.delegation = self.delegation + (self.PerQ3 * 2)
                self.actions = self.actions + (self.PerQ3 * 2)
             

            elif(self.PerQ3 == 4):

                self.PerQ3 = 1
                self.contracting = self.contracting + (self.PerQ3 *2)
                self.present = self.present + (self.PerQ3 * 1)
                self.pointsother = self.pointsother + (self.PerQ3 * 2)
                self.trust = self.trust + (self.PerQ3 * 2 )
                self.awareness = self.awareness + (self.PerQ3 * 5)
                self.perspectives = self.perspectives + (self.PerQ3 *10)
                self.listening = self.listening + (self.PerQ3 * 3)
                self.creative = self.creative + (self.PerQ3 * 4)
                self.delegation = self.delegation + (self.PerQ3 * 2)
                self.actions = self.actions + (self.PerQ3 * 2)

            elif(self.PerQ3 == 3):
                self.PerQ3 = 2
                self.contracting = self.contracting + (self.PerQ3 *2)
                self.present = self.present + (self.PerQ3 * 1)
                self.pointsother = self.pointsother + (self.PerQ3 * 2)
                self.trust = self.trust + (self.PerQ3 * 2 )
                self.awareness = self.awareness + (self.PerQ3 * 5)
                self.perspectives = self.perspectives + (self.PerQ3 *10)
                self.listening = self.listening + (self.PerQ3 * 3)
                self.creative = self.creative + (self.PerQ3 * 4)
                self.delegation = self.delegation + (self.PerQ3 * 2)
                self.actions = self.actions + (self.PerQ3 * 2)

            elif(self.PerQ3 == 2):

                self.PerQ3 = 3
                self.contracting = self.contracting + (self.PerQ3 *2)
                self.present = self.present + (self.PerQ3 * 1)
                self.pointsother = self.pointsother + (self.PerQ3 * 2)
                self.trust = self.trust + (self.PerQ3 * 2 )
                self.awareness = self.awareness + (self.PerQ3 * 5)
                self.perspectives = self.perspectives + (self.PerQ3 *10)
                self.listening = self.listening + (self.PerQ3 * 3)
                self.creative = self.creative + (self.PerQ3 * 4)
                self.delegation = self.delegation + (self.PerQ3 * 2)
                self.actions = self.actions + (self.PerQ3 * 2)

            elif(self.PerQ3 == 1):

                self.PerQ3 = 4
                self.contracting = self.contracting + (self.PerQ3 *2)
                self.present = self.present + (self.PerQ3 * 1)
                self.pointsother = self.pointsother + (self.PerQ3 * 2)
                self.trust = self.trust + (self.PerQ3 * 2 )
                self.awareness = self.awareness + (self.PerQ3 * 5)
                self.perspectives = self.perspectives + (self.PerQ3 *10)
                self.listening = self.listening + (self.PerQ3 * 3)
                self.creative = self.creative + (self.PerQ3 * 4)
                self.delegation = self.delegation + (self.PerQ3 * 2)
                self.actions = self.actions + (self.PerQ3 * 2)
       
            elif(self.PerQ3 == 0):

                self.PerQ3 = 5
                self.contracting = self.contracting + (self.PerQ3 *2)
                self.present = self.present + (self.PerQ3 * 1)
                self.pointsother = self.pointsother + (self.PerQ3 * 2)
                self.trust = self.trust + (self.PerQ3 * 2 )
                self.awareness = self.awareness + (self.PerQ3 * 5)
                self.perspectives = self.perspectives + (self.PerQ3 *10)
                self.listening = self.listening + (self.PerQ3 * 3)
                self.creative = self.creative + (self.PerQ3 * 4)
                self.delegation = self.delegation + (self.PerQ3 * 2)
                self.actions = self.actions + (self.PerQ3 * 2)

            self.ConfToList(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware)
            self.h.hide()
                

    def ConfToList(self,email,birth,edu,lead,workyears,contracting,feedback,present,pointsself,pointsother,trust,confidentiatly,awareness,perspectives,listening,creative,delegation,actions,reflection,selfaware):
        self.main = QtWidgets.QMainWindow() 
       
        self.ui = Ui_ListCreativeDelegation(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware) 
        self.ui.setupUi(self.main)
        self.main.show()     


    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()   

    def retranslateUi(self, ConfAwarePersp):
        _translate = QtCore.QCoreApplication.translate
        ConfAwarePersp.setWindowTitle(_translate("ConfAwarePersp", "COTG"))
        self.label.setText(_translate("ConfAwarePersp", "<html><head/><body><p align=\"center\">Please answer the following questions</p></body></html>"))
        self.ConfidentialityQ1.setToolTip(_translate("ConfAwarePersp", "Please select from the following"))
        self.ConfidentialityQ1.setItemText(0, _translate("ConfAwarePersp", "Never"))
        self.ConfidentialityQ1.setItemText(1, _translate("ConfAwarePersp", "Very Rarely"))
        self.ConfidentialityQ1.setItemText(2, _translate("ConfAwarePersp", "Rarely"))
        self.ConfidentialityQ1.setItemText(3, _translate("ConfAwarePersp", "Sometimes"))
        self.ConfidentialityQ1.setItemText(4, _translate("ConfAwarePersp", "Often"))
        self.ConfidentialityQ1.setItemText(5, _translate("ConfAwarePersp", "Always"))
        self.ConfidentialityQ2.setToolTip(_translate("ConfAwarePersp", "Please select from the following"))
        self.ConfidentialityQ2.setItemText(0, _translate("ConfAwarePersp", "Never"))
        self.ConfidentialityQ2.setItemText(1, _translate("ConfAwarePersp", "Very Rarely"))
        self.ConfidentialityQ2.setItemText(2, _translate("ConfAwarePersp", "Rarely"))
        self.ConfidentialityQ2.setItemText(3, _translate("ConfAwarePersp", "Sometimes"))
        self.ConfidentialityQ2.setItemText(4, _translate("ConfAwarePersp", "Often"))
        self.ConfidentialityQ2.setItemText(5, _translate("ConfAwarePersp", "Always"))
        self.label_2.setText(_translate("ConfAwarePersp", "<html><head/><body><p>I engage in gossip because it helps me fit in and I also learn things that I would not in any</p><p>other way</p></body></html>"))
        self.label_3.setText(_translate("ConfAwarePersp", "<html><head/><body><p>When sharing infromation with colleagues I am always keenly aware as to where I heard</p><p>it and the restrictions this may create</p></body></html>"))
        self.label_4.setText(_translate("ConfAwarePersp", "<html><head/><body><p>I am very good at respecting other people\'s privacy. If people ask me for advice they</p><p>can be confident I will not divulge this</p></body></html>"))
        self.ConfidentialityQ3.setToolTip(_translate("ConfAwarePersp", "Please select from the following"))
        self.ConfidentialityQ3.setItemText(0, _translate("ConfAwarePersp", "Never"))
        self.ConfidentialityQ3.setItemText(1, _translate("ConfAwarePersp", "Very Rarely"))
        self.ConfidentialityQ3.setItemText(2, _translate("ConfAwarePersp", "Rarely"))
        self.ConfidentialityQ3.setItemText(3, _translate("ConfAwarePersp", "Sometimes"))
        self.ConfidentialityQ3.setItemText(4, _translate("ConfAwarePersp", "Often"))
        self.ConfidentialityQ3.setItemText(5, _translate("ConfAwarePersp", "Always"))
        self.label_5.setText(_translate("ConfAwarePersp", "<html><head/><body><p>I\'m good at helping people to notice and celebrate their successes</p></body></html>"))
        self.AwarenessQ1.setToolTip(_translate("ConfAwarePersp", "Please select from the following"))
        self.AwarenessQ1.setItemText(0, _translate("ConfAwarePersp", "Never"))
        self.AwarenessQ1.setItemText(1, _translate("ConfAwarePersp", "Very Rarely"))
        self.AwarenessQ1.setItemText(2, _translate("ConfAwarePersp", "Rarely"))
        self.AwarenessQ1.setItemText(3, _translate("ConfAwarePersp", "Sometimes"))
        self.AwarenessQ1.setItemText(4, _translate("ConfAwarePersp", "Often"))
        self.AwarenessQ1.setItemText(5, _translate("ConfAwarePersp", "Always"))
        self.label_6.setText(_translate("ConfAwarePersp", "<html><head/><body><p>I encourage others to pause and reflect on their real responses to issues, not just</p><p>their automatic reactions</p></body></html>"))
        self.AwarenessQ2.setToolTip(_translate("ConfAwarePersp", "Please select from the following"))
        self.AwarenessQ2.setItemText(0, _translate("ConfAwarePersp", "Never"))
        self.AwarenessQ2.setItemText(1, _translate("ConfAwarePersp", "Very Rarely"))
        self.AwarenessQ2.setItemText(2, _translate("ConfAwarePersp", "Rarely"))
        self.AwarenessQ2.setItemText(3, _translate("ConfAwarePersp", "Sometimes"))
        self.AwarenessQ2.setItemText(4, _translate("ConfAwarePersp", "Often"))
        self.AwarenessQ2.setItemText(5, _translate("ConfAwarePersp", "Always"))
        self.label_7.setText(_translate("ConfAwarePersp", "<html><head/><body><p>I draw people\'s attention to their own ideas and skills that they be overlooking</p><p><br/></p></body></html>"))
        self.AwarenessQ3.setToolTip(_translate("ConfAwarePersp", "Please select from the following"))
        self.AwarenessQ3.setItemText(0, _translate("ConfAwarePersp", "Never"))
        self.AwarenessQ3.setItemText(1, _translate("ConfAwarePersp", "Very Rarely"))
        self.AwarenessQ3.setItemText(2, _translate("ConfAwarePersp", "Rarely"))
        self.AwarenessQ3.setItemText(3, _translate("ConfAwarePersp", "Sometimes"))
        self.AwarenessQ3.setItemText(4, _translate("ConfAwarePersp", "Often"))
        self.AwarenessQ3.setItemText(5, _translate("ConfAwarePersp", "Always"))
        self.label_8.setText(_translate("ConfAwarePersp", "<html><head/><body><p>I rely on the people I work with knocking on my door to say when it is appropriate</p><p>for us to meet</p></body></html>"))
        self.label_9.setText(_translate("ConfAwarePersp", "<html><head/><body><p>I am good at helping colleagues to see how different stakeholders might interpret</p><p>their actions</p></body></html>"))
        self.PerspectiveQ1.setToolTip(_translate("ConfAwarePersp", "Please select from the following"))
        self.PerspectiveQ1.setItemText(0, _translate("ConfAwarePersp", "Never"))
        self.PerspectiveQ1.setItemText(1, _translate("ConfAwarePersp", "Very Rarely"))
        self.PerspectiveQ1.setItemText(2, _translate("ConfAwarePersp", "Rarely"))
        self.PerspectiveQ1.setItemText(3, _translate("ConfAwarePersp", "Sometimes"))
        self.PerspectiveQ1.setItemText(4, _translate("ConfAwarePersp", "Often"))
        self.PerspectiveQ1.setItemText(5, _translate("ConfAwarePersp", "Always"))
        self.label_10.setText(_translate("ConfAwarePersp", "<html><head/><body><p>I enjoy helping others to think about their challenges from different perspectives</p></body></html>"))
        self.PerspectiveQ2.setToolTip(_translate("ConfAwarePersp", "Please select from the following"))
        self.PerspectiveQ2.setItemText(0, _translate("ConfAwarePersp", "Never"))
        self.PerspectiveQ2.setItemText(1, _translate("ConfAwarePersp", "Very Rarely"))
        self.PerspectiveQ2.setItemText(2, _translate("ConfAwarePersp", "Rarely"))
        self.PerspectiveQ2.setItemText(3, _translate("ConfAwarePersp", "Sometimes"))
        self.PerspectiveQ2.setItemText(4, _translate("ConfAwarePersp", "Often"))
        self.PerspectiveQ2.setItemText(5, _translate("ConfAwarePersp", "Always"))
        self.PerspectiveQ3.setToolTip(_translate("ConfAwarePersp", "Please select from the following"))
        self.PerspectiveQ3.setItemText(0, _translate("ConfAwarePersp", "Never"))
        self.PerspectiveQ3.setItemText(1, _translate("ConfAwarePersp", "Very Rarely"))
        self.PerspectiveQ3.setItemText(2, _translate("ConfAwarePersp", "Rarely"))
        self.PerspectiveQ3.setItemText(3, _translate("ConfAwarePersp", "Sometimes"))
        self.PerspectiveQ3.setItemText(4, _translate("ConfAwarePersp", "Often"))
        self.PerspectiveQ3.setItemText(5, _translate("ConfAwarePersp", "Always"))
        self.Back.setStatusTip(_translate("ConfAwarePersp", "Click this to go back a form"))
        self.Back.setText(_translate("ConfAwarePersp", "Back"))
        self.NextQuestion2.setStatusTip(_translate("ConfAwarePersp", "Click this to go to next questions"))
        self.NextQuestion2.setText(_translate("ConfAwarePersp", "Next"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfAwarePersp = QtWidgets.QDialog()
    ui = Ui_ConfAwarePersp()
    ui.setupUi(ConfAwarePersp)
    ConfAwarePersp.show()
    app.exec_()
