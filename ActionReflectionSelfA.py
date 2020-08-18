# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ActionReflectionSelfA.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QShortcut , QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog , QAction ,QShortcut
from Choice import Ui_Status

thisdict = {"Never":0,
            "Very Rarely":1,
            "Rarely":2,
            "Sometimes":3,
            "Often":4,
            "Always":5}

class Ui_ActionReflectionSelfA(object):

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


    def setupUi(self, ActionReflectionSelfA):
        ActionReflectionSelfA.setObjectName("ActionReflectionSelfA")
        ActionReflectionSelfA.resize(818, 754)
        ActionReflectionSelfA.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.label = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label.setGeometry(QtCore.QRect(200, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ActionsQ1 = QtWidgets.QComboBox(ActionReflectionSelfA)
        self.ActionsQ1.setGeometry(QtCore.QRect(690, 80, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ActionsQ1.setFont(font)
        self.ActionsQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ActionsQ1.setMaxVisibleItems(6)
        self.ActionsQ1.setObjectName("ActionsQ1")
        self.ActionsQ1.addItem("")
        self.ActionsQ1.addItem("")
        self.ActionsQ1.addItem("")
        self.ActionsQ1.addItem("")
        self.ActionsQ1.addItem("")
        self.ActionsQ1.addItem("")
        self.ActionsQ2 = QtWidgets.QComboBox(ActionReflectionSelfA)
        self.ActionsQ2.setGeometry(QtCore.QRect(690, 150, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ActionsQ2.setFont(font)
        self.ActionsQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ActionsQ2.setMaxVisibleItems(6)
        self.ActionsQ2.setObjectName("ActionsQ2")
        self.ActionsQ2.addItem("")
        self.ActionsQ2.addItem("")
        self.ActionsQ2.addItem("")
        self.ActionsQ2.addItem("")
        self.ActionsQ2.addItem("")
        self.ActionsQ2.addItem("")
        self.label_3 = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ActionsQ3 = QtWidgets.QComboBox(ActionReflectionSelfA)
        self.ActionsQ3.setGeometry(QtCore.QRect(690, 230, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ActionsQ3.setFont(font)
        self.ActionsQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ActionsQ3.setMaxVisibleItems(6)
        self.ActionsQ3.setObjectName("ActionsQ3")
        self.ActionsQ3.addItem("")
        self.ActionsQ3.addItem("")
        self.ActionsQ3.addItem("")
        self.ActionsQ3.addItem("")
        self.ActionsQ3.addItem("")
        self.ActionsQ3.addItem("")
        self.label_5 = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label_5.setGeometry(QtCore.QRect(20, 290, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label_6.setGeometry(QtCore.QRect(20, 350, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label_7.setGeometry(QtCore.QRect(20, 410, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.ReflectionQ1 = QtWidgets.QComboBox(ActionReflectionSelfA)
        self.ReflectionQ1.setGeometry(QtCore.QRect(690, 290, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ReflectionQ1.setFont(font)
        self.ReflectionQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ReflectionQ1.setMaxVisibleItems(6)
        self.ReflectionQ1.setObjectName("ReflectionQ1")
        self.ReflectionQ1.addItem("")
        self.ReflectionQ1.addItem("")
        self.ReflectionQ1.addItem("")
        self.ReflectionQ1.addItem("")
        self.ReflectionQ1.addItem("")
        self.ReflectionQ1.addItem("")
        self.ReflectionQ2 = QtWidgets.QComboBox(ActionReflectionSelfA)
        self.ReflectionQ2.setGeometry(QtCore.QRect(690, 350, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ReflectionQ2.setFont(font)
        self.ReflectionQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ReflectionQ2.setMaxVisibleItems(6)
        self.ReflectionQ2.setObjectName("ReflectionQ2")
        self.ReflectionQ2.addItem("")
        self.ReflectionQ2.addItem("")
        self.ReflectionQ2.addItem("")
        self.ReflectionQ2.addItem("")
        self.ReflectionQ2.addItem("")
        self.ReflectionQ2.addItem("")
        self.ReflectionQ3 = QtWidgets.QComboBox(ActionReflectionSelfA)
        self.ReflectionQ3.setGeometry(QtCore.QRect(690, 410, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ReflectionQ3.setFont(font)
        self.ReflectionQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ReflectionQ3.setMaxVisibleItems(6)
        self.ReflectionQ3.setObjectName("ReflectionQ3")
        self.ReflectionQ3.addItem("")
        self.ReflectionQ3.addItem("")
        self.ReflectionQ3.addItem("")
        self.ReflectionQ3.addItem("")
        self.ReflectionQ3.addItem("")
        self.ReflectionQ3.addItem("")
        self.label_8 = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label_8.setGeometry(QtCore.QRect(20, 470, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label_9.setGeometry(QtCore.QRect(20, 530, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(ActionReflectionSelfA)
        self.label_10.setGeometry(QtCore.QRect(20, 590, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.SelfAwareQ1 = QtWidgets.QComboBox(ActionReflectionSelfA)
        self.SelfAwareQ1.setGeometry(QtCore.QRect(690, 470, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SelfAwareQ1.setFont(font)
        self.SelfAwareQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SelfAwareQ1.setMaxVisibleItems(6)
        self.SelfAwareQ1.setObjectName("SelfAwareQ1")
        self.SelfAwareQ1.addItem("")
        self.SelfAwareQ1.addItem("")
        self.SelfAwareQ1.addItem("")
        self.SelfAwareQ1.addItem("")
        self.SelfAwareQ1.addItem("")
        self.SelfAwareQ1.addItem("")
        self.SelfAwareQ2 = QtWidgets.QComboBox(ActionReflectionSelfA)
        self.SelfAwareQ2.setGeometry(QtCore.QRect(690, 530, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SelfAwareQ2.setFont(font)
        self.SelfAwareQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SelfAwareQ2.setMaxVisibleItems(6)
        self.SelfAwareQ2.setObjectName("SelfAwareQ2")
        self.SelfAwareQ2.addItem("")
        self.SelfAwareQ2.addItem("")
        self.SelfAwareQ2.addItem("")
        self.SelfAwareQ2.addItem("")
        self.SelfAwareQ2.addItem("")
        self.SelfAwareQ2.addItem("")
        self.SelfAwareQ3 = QtWidgets.QComboBox(ActionReflectionSelfA)
        self.SelfAwareQ3.setGeometry(QtCore.QRect(690, 600, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SelfAwareQ3.setFont(font)
        self.SelfAwareQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SelfAwareQ3.setMaxVisibleItems(6)
        self.SelfAwareQ3.setObjectName("SelfAwareQ3")
        self.SelfAwareQ3.addItem("")
        self.SelfAwareQ3.addItem("")
        self.SelfAwareQ3.addItem("")
        self.SelfAwareQ3.addItem("")
        self.SelfAwareQ3.addItem("")
        self.SelfAwareQ3.addItem("")
        self.Final = QtWidgets.QPushButton(ActionReflectionSelfA)
        self.Final.setGeometry(QtCore.QRect(720, 690, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Final.setFont(font)
        self.Final.setAutoFillBackground(False)
        self.Final.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Final.setObjectName("Final")
        self.Back = QtWidgets.QPushButton(ActionReflectionSelfA)
        self.Back.setGeometry(QtCore.QRect(20, 690, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setAutoFillBackground(False)
        self.Back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Back.setObjectName("Back")
        self.line_5 = QtWidgets.QFrame(ActionReflectionSelfA)
        self.line_5.setGeometry(QtCore.QRect(0, 110, 821, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(ActionReflectionSelfA)
        self.line_6.setGeometry(QtCore.QRect(0, 200, 821, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(ActionReflectionSelfA)
        self.line_7.setGeometry(QtCore.QRect(0, 260, 821, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(ActionReflectionSelfA)
        self.line_8.setGeometry(QtCore.QRect(0, 320, 821, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(ActionReflectionSelfA)
        self.line_9.setGeometry(QtCore.QRect(0, 380, 821, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(ActionReflectionSelfA)
        self.line_10.setGeometry(QtCore.QRect(0, 440, 821, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(ActionReflectionSelfA)
        self.line_11.setGeometry(QtCore.QRect(0, 500, 821, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(ActionReflectionSelfA)
        self.line_12.setGeometry(QtCore.QRect(0, 560, 821, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(ActionReflectionSelfA)
        self.line_13.setGeometry(QtCore.QRect(0, 660, 821, 20))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")

        self.retranslateUi(ActionReflectionSelfA)
        self.ActionsQ1.setCurrentIndex(-1)
        self.ActionsQ2.setCurrentIndex(-1)
        self.ActionsQ3.setCurrentIndex(-1)
        self.ReflectionQ1.setCurrentIndex(-1)
        self.ReflectionQ2.setCurrentIndex(-1)
        self.ReflectionQ3.setCurrentIndex(-1)
        self.SelfAwareQ1.setCurrentIndex(-1)
        self.SelfAwareQ2.setCurrentIndex(-1)
        self.SelfAwareQ3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ActionReflectionSelfA)
        self.Final.clicked.connect(self.pressed)
        self.h = ActionReflectionSelfA

    def pressed(self):
        

        if(self.ActionsQ1.currentText() == "" or self.ActionsQ2.currentText() == "" or self.ActionsQ3.currentText() == "" or self.ReflectionQ1.currentText() == "" or self.ReflectionQ2.currentText() == "" or self.ReflectionQ3.currentText() == "" or self.SelfAwareQ1.currentText() == "" or self.SelfAwareQ2.currentText() == "" or self.SelfAwareQ3.currentText() == ""):

            self.messagebox("Error","Please enter all fields")

        else: 
            self.AQ1 = thisdict[self.ActionsQ1.currentText()] 

            if(self.AQ1 == 5):

                self.AQ1 = 0
                self.contracting = self.contracting + (self.AQ1 * 2)
                self.pointsother = self.pointsother +(self.AQ1 * 2)
                self.trust = self.trust + (self.AQ1 * 2)
                self.creative = self.creative + (self.AQ1 * 2)
                self.actions = self.actions + (self.AQ1 * 10)

            elif(self.AQ1 == 4):

                self.AQ1 = 1
                self.contracting = self.contracting + (self.AQ1 * 2)
                self.pointsother = self.pointsother +(self.AQ1 * 2)
                self.trust = self.trust + (self.AQ1 * 2)
                self.creative = self.creative + (self.AQ1 * 2)
                self.actions = self.actions + (self.AQ1 * 10)
                
            elif(self.AQ1 == 3):
                self.AQ1 = 2
                self.contracting = self.contracting + (self.AQ1 * 2)
                self.pointsother = self.pointsother +(self.AQ1 * 2)
                self.trust = self.trust + (self.AQ1 * 2)
                self.creative = self.creative + (self.AQ1 * 2)
                self.actions = self.actions + (self.AQ1 * 10)

            elif(self.AQ1 == 2):

                self.AQ1 = 3
                self.contracting = self.contracting + (self.AQ1 * 2)
                self.pointsother = self.pointsother +(self.AQ1 * 2)
                self.trust = self.trust + (self.AQ1 * 2)
                self.creative = self.creative + (self.AQ1 * 2)
                self.actions = self.actions + (self.AQ1 * 10)

            elif(self.AQ1 == 1):

                self.AQ1 = 4
                self.contracting = self.contracting + (self.AQ1 * 2)
                self.pointsother = self.pointsother +(self.AQ1 * 2)
                self.trust = self.trust + (self.AQ1 * 2)
                self.creative = self.creative + (self.AQ1 * 2)
                self.actions = self.actions + (self.AQ1 * 10)
                
            elif(self.AQ1 == 0):

                self.AQ1 = 5
                self.contracting = self.contracting + (self.AQ1 * 2)
                self.pointsother = self.pointsother +(self.AQ1 * 2)
                self.trust = self.trust + (self.AQ1 * 2)
                self.creative = self.creative + (self.AQ1 * 2)
                self.actions = self.actions + (self.AQ1 * 10)

            self.AQ2 = thisdict[self.ActionsQ2.currentText()] 

            if(self.AQ2 == 5):

                self.AQ2 = 0
                self.trust = self.trust + (self.AQ2 * 1)
                self.awareness = self.awareness + (self.AQ2 * 1)
                self.creative = self.creative + (self.AQ2 * 2)
                self.actions = self.actions + (self.AQ2 * 10)
                self.reflection = self.reflection + (self.AQ2 * 1)

            elif(self.AQ2 == 4):

                self.AQ2 = 1
                self.trust = self.trust + (self.AQ2 * 1)
                self.awareness = self.awareness + (self.AQ2 * 1)
                self.creative = self.creative + (self.AQ2 * 2)
                self.actions = self.actions + (self.AQ2 * 10)
                self.reflection = self.reflection + (self.AQ2 * 1)
                
            elif(self.AQ2 == 3):
                self.AQ2 = 2
                self.trust = self.trust + (self.AQ2 * 1)
                self.awareness = self.awareness + (self.AQ2 * 1)
                self.creative = self.creative + (self.AQ2 * 2)
                self.actions = self.actions + (self.AQ2 * 10)
                self.reflection = self.reflection + (self.AQ2 * 1)

            elif(self.AQ2 == 2):

                self.AQ2 = 3
                self.trust = self.trust + (self.AQ2 * 1)
                self.awareness = self.awareness + (self.AQ2 * 1)
                self.creative = self.creative + (self.AQ2 * 2)
                self.actions = self.actions + (self.AQ2 * 10)
                self.reflection = self.reflection + (self.AQ2 * 1)

            elif(self.AQ2 == 1):

                self.AQ2 = 4
                self.trust = self.trust + (self.AQ2 * 1)
                self.awareness = self.awareness + (self.AQ2 * 1)
                self.creative = self.creative + (self.AQ2 * 2)
                self.actions = self.actions + (self.AQ2 * 10)
                self.reflection = self.reflection + (self.AQ2 * 1)
                
            elif(self.AQ2 == 0):

                self.AQ2 = 5
                self.trust = self.trust + (self.AQ2 * 1)
                self.awareness = self.awareness + (self.AQ2 * 1)
                self.creative = self.creative + (self.AQ2 * 2)
                self.actions = self.actions + (self.AQ2 * 10)
                self.reflection = self.reflection + (self.AQ2 * 1)

            self.AQ3 = thisdict[self.ActionsQ3.currentText()] 

            if(self.AQ3 == 5):

                self.AQ3 = 0
                self.feedback = self.feedback + (self.AQ3 * 1)
                self.pointsother = self.pointsother + (self.AQ3 * 2)
                self.trust = self.trust + (self.AQ3 * 1)
                self.awareness = self.awareness + (self.AQ3 * 3)
                self.listening = self.listening + (self.AQ3 * 2)
                self.creative = self.creative + (self.AQ3 * 1)
                self.delegation = self.delegation +(self.AQ3 *2)
                self.actions = self.actions + (self.AQ3 * 10)

            elif(self.AQ3 == 4):

                self.AQ3 = 1
                self.feedback = self.feedback + (self.AQ3 * 1)
                self.pointsother = self.pointsother + (self.AQ3 * 2)
                self.trust = self.trust + (self.AQ3 * 1)
                self.awareness = self.awareness + (self.AQ3 * 3)
                self.listening = self.listening + (self.AQ3 * 2)
                self.creative = self.creative + (self.AQ3 * 1)
                self.delegation = self.delegation +(self.AQ3 *2)
                self.actions = self.actions + (self.AQ3 * 10)
                
            elif(self.AQ3 == 3):
                self.AQ3 = 2
                self.feedback = self.feedback + (self.AQ3 * 1)
                self.pointsother = self.pointsother + (self.AQ3 * 2)
                self.trust = self.trust + (self.AQ3 * 1)
                self.awareness = self.awareness + (self.AQ3 * 3)
                self.listening = self.listening + (self.AQ3 * 2)
                self.creative = self.creative + (self.AQ3 * 1)
                self.delegation = self.delegation +(self.AQ3 *2)
                self.actions = self.actions + (self.AQ3 * 10)

            elif(self.AQ3 == 2):

                self.AQ3 = 3
                self.feedback = self.feedback + (self.AQ3 * 1)
                self.pointsother = self.pointsother + (self.AQ3 * 2)
                self.trust = self.trust + (self.AQ3 * 1)
                self.awareness = self.awareness + (self.AQ3 * 3)
                self.listening = self.listening + (self.AQ3 * 2)
                self.creative = self.creative + (self.AQ3 * 1)
                self.delegation = self.delegation +(self.AQ3 *2)
                self.actions = self.actions + (self.AQ3 * 10)

            elif(self.AQ3 == 1):

                self.AQ3 = 4
                self.feedback = self.feedback + (self.AQ3 * 1)
                self.pointsother = self.pointsother + (self.AQ3 * 2)
                self.trust = self.trust + (self.AQ3 * 1)
                self.awareness = self.awareness + (self.AQ3 * 3)
                self.listening = self.listening + (self.AQ3 * 2)
                self.creative = self.creative + (self.AQ3 * 1)
                self.delegation = self.delegation +(self.AQ3 *2)
                self.actions = self.actions + (self.AQ3 * 10)
                
            elif(self.AQ3 == 0):

                self.AQ3 = 5
                self.feedback = self.feedback + (self.AQ3 * 1)
                self.pointsother = self.pointsother + (self.AQ3 * 2)
                self.trust = self.trust + (self.AQ3 * 1)
                self.awareness = self.awareness + (self.AQ3 * 3)
                self.listening = self.listening + (self.AQ3 * 2)
                self.creative = self.creative + (self.AQ3 * 1)
                self.delegation = self.delegation +(self.AQ3 *2)
                self.actions = self.actions + (self.AQ3 * 10)

            self.RQ1 = thisdict[self.ReflectionQ1.currentText()] 

            if(self.RQ1 == 5):

                self.RQ1 = 0
                self.perspectives = self.perspectives + (self.RQ1 * 2)
                self.delegation = self.delegation + (self.RQ1 * 1)
                self.reflection = self.reflection + (self.RQ1 * 10)

            elif(self.RQ1 == 4):

                self.RQ1 = 1
                self.perspectives = self.perspectives + (self.RQ1 * 2)
                self.delegation = self.delegation + (self.RQ1 * 1)
                self.reflection = self.reflection + (self.RQ1 * 10)

            elif(self.RQ1 == 3):
                self.RQ1 = 2
                self.perspectives = self.perspectives + (self.RQ1 * 2)
                self.delegation = self.delegation + (self.RQ1 * 1)
                self.reflection = self.reflection + (self.RQ1 * 10)

            elif(self.RQ1 == 2):

                self.RQ1 = 3
                self.perspectives = self.perspectives + (self.RQ1 * 2)
                self.delegation = self.delegation + (self.RQ1 * 1)
                self.reflection = self.reflection + (self.RQ1 * 10)

            elif(self.RQ1 == 1):

                self.RQ1 = 4
                self.perspectives = self.perspectives + (self.RQ1 * 2)
                self.delegation = self.delegation + (self.RQ1 * 1)
                self.reflection = self.reflection + (self.RQ1 * 10)
                
            elif(self.RQ1 == 0):

                self.RQ1 = 5
                self.perspectives = self.perspectives + (self.RQ1 * 2)
                self.delegation = self.delegation + (self.RQ1 * 1)
                self.reflection = self.reflection + (self.RQ1 * 10)

            self.RQ2 = thisdict[self.ReflectionQ2.currentText()] 

            if(self.RQ2 == 5):

                self.RQ2 = 0
                self.pointsself = self.pointsself + (self.RQ2 * 2)
                self.perspectives = self.perspectives + (self.RQ2 * 2)
                self.reflection = self.reflection + (self.RQ2 * 10)

            elif(self.RQ2 == 4):

                self.RQ2 = 1
                self.pointsself = self.pointsself + (self.RQ2 * 2)
                self.perspectives = self.perspectives + (self.RQ2 * 2)
                self.reflection = self.reflection + (self.RQ2 * 10)

            elif(self.RQ2 == 3):
                self.RQ2 = 2
                self.pointsself = self.pointsself + (self.RQ2 * 2)
                self.perspectives = self.perspectives + (self.RQ2 * 2)
                self.reflection = self.reflection + (self.RQ2 * 10)

            elif(self.RQ2 == 2):

                self.RQ2 = 3
                self.pointsself = self.pointsself + (self.RQ2 * 2)
                self.perspectives = self.perspectives + (self.RQ2 * 2)
                self.reflection = self.reflection + (self.RQ2 * 10)

            elif(self.RQ2 == 1):

                self.RQ2 = 4
                self.pointsself = self.pointsself + (self.RQ2 * 2)
                self.perspectives = self.perspectives + (self.RQ2 * 2)
                self.reflection = self.reflection + (self.RQ2 * 10)
                
            elif(self.RQ2 == 0):

                self.RQ2 = 5
                self.pointsself = self.pointsself + (self.RQ2 * 2)
                self.perspectives = self.perspectives + (self.RQ2 * 2)
                self.reflection = self.reflection + (self.RQ2 * 10)


            self.RQ3 = thisdict[self.ReflectionQ3.currentText()] 

            if(self.RQ3 == 5):

                self.RQ3 = 0
                self.present = self.present + (self.RQ3 * 2)
                self.pointsself = self.pointsself + (self.RQ3 * 2)
                self.reflection = self.reflection + (self.RQ3 * 10)
                self.selfaware = self.selfaware + (self.RQ3 * 5)

            elif(self.RQ3 == 4):

                self.RQ3 = 1
                self.present = self.present + (self.RQ3 * 2)
                self.pointsself = self.pointsself + (self.RQ3 * 2)
                self.reflection = self.reflection + (self.RQ3 * 10)
                self.selfaware = self.selfaware + (self.RQ3 * 5)

            elif(self.RQ3 == 3):
                self.RQ3 = 2
                self.present = self.present + (self.RQ3 * 2)
                self.pointsself = self.pointsself + (self.RQ3 * 2)
                self.reflection = self.reflection + (self.RQ3 * 10)
                self.selfaware = self.selfaware + (self.RQ3 * 5)

            elif(self.RQ3 == 2):

                self.RQ3 = 3
                self.present = self.present + (self.RQ3 * 2)
                self.pointsself = self.pointsself + (self.RQ3 * 2)
                self.reflection = self.reflection + (self.RQ3 * 10)
                self.selfaware = self.selfaware + (self.RQ3 * 5)

            elif(self.RQ3 == 1):

                self.RQ3 = 4
                self.present = self.present + (self.RQ3 * 2)
                self.pointsself = self.pointsself + (self.RQ3 * 2)
                self.reflection = self.reflection + (self.RQ3 * 10)
                self.selfaware = self.selfaware + (self.RQ3 * 5)
                
            elif(self.RQ3 == 0):

                self.RQ3 = 5
                self.present = self.present + (self.RQ3 * 2)
                self.pointsself = self.pointsself + (self.RQ3 * 2)
                self.reflection = self.reflection + (self.RQ3 * 10)
                self.selfaware = self.selfaware + (self.RQ3 * 5)

            self.SQ1 = thisdict[self.SelfAwareQ1.currentText()] 
            self.present = self.present + (self.SQ1 * 3)
            self.pointsself = self.pointsself + (self.SQ1 * 2)
            self.trust = self.trust + (self.SQ1 * 2)
            self.awareness = self.awareness + (self.SQ1 * 2)
            self.listening = self.listening + (self.SQ1 * 3)
            self.reflection = self.reflection + (self.SQ1 * 2)
            self.selfaware = self.selfaware + (self.SQ1 * 10)

            self.SQ2 = thisdict[self.SelfAwareQ2.currentText()] 
            self.present = self.present + (self.SQ2 * 4)
            self.pointsself = self.pointsself + (self.SQ2 * 2)
            self.listening = self.listening + (self.SQ2 * 2)
            self.selfaware = self.selfaware + (self.SQ2 * 10)

            self.SQ3 = thisdict[self.SelfAwareQ3.currentText()] 
            self.present = self.present + (self.SQ3 * 2)
            self.pointsself = self.pointsself + (self.SQ3 * 2)
            self.pointsother = self.pointsother + (self.SQ3 * 2)
            self.perspectives = self.perspectives + (self.SQ3 * 2)
            self.listening = self.listening + (self.SQ3 * 4)
            self.delegation = self.delegation + (self.SQ3 * 5)
            self.selfaware = self.selfaware + (self.SQ3 * 10)

            self.ActionToChoice(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware)
            self.h.hide()

    def ActionToChoice(self,email,birth,edu,lead,workyears,contracting,feedback,present,pointsself,pointsother,trust,confidentiatly,awareness,perspectives,listening,creative,delegation,actions,reflection,selfaware):
        self.main = QtWidgets.QMainWindow() 
        self.ui = Ui_Status(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware) 
        self.ui.setupUi(self.main)
        self.main.show() 

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()   

    def retranslateUi(self, ActionReflectionSelfA):
        _translate = QtCore.QCoreApplication.translate
        ActionReflectionSelfA.setWindowTitle(_translate("ActionReflectionSelfA", "COTG"))
        self.label.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p align=\"center\">Please answer the following questions</p></body></html>"))
        self.label_2.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p>Me and the team are great planners, we make a plan and stick to it</p></body></html>"))
        self.ActionsQ1.setToolTip(_translate("ActionReflectionSelfA", "Please select from the following"))
        self.ActionsQ1.setItemText(0, _translate("ActionReflectionSelfA", "Never"))
        self.ActionsQ1.setItemText(1, _translate("ActionReflectionSelfA", "Very Rarely"))
        self.ActionsQ1.setItemText(2, _translate("ActionReflectionSelfA", "Rarely"))
        self.ActionsQ1.setItemText(3, _translate("ActionReflectionSelfA", "Sometimes"))
        self.ActionsQ1.setItemText(4, _translate("ActionReflectionSelfA", "Often"))
        self.ActionsQ1.setItemText(5, _translate("ActionReflectionSelfA", "Always"))
        self.ActionsQ2.setToolTip(_translate("ActionReflectionSelfA", "Please select from the following"))
        self.ActionsQ2.setItemText(0, _translate("ActionReflectionSelfA", "Never"))
        self.ActionsQ2.setItemText(1, _translate("ActionReflectionSelfA", "Very Rarely"))
        self.ActionsQ2.setItemText(2, _translate("ActionReflectionSelfA", "Rarely"))
        self.ActionsQ2.setItemText(3, _translate("ActionReflectionSelfA", "Sometimes"))
        self.ActionsQ2.setItemText(4, _translate("ActionReflectionSelfA", "Often"))
        self.ActionsQ2.setItemText(5, _translate("ActionReflectionSelfA", "Always"))
        self.label_3.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p>I\'m good at creating action plans and checking progress regulary, including with those I </p><p>work with</p></body></html>"))
        self.label_4.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p>I enjoy helping people realise that they have identified important actions they want to take</p></body></html>"))
        self.ActionsQ3.setToolTip(_translate("ActionReflectionSelfA", "Please select from the following"))
        self.ActionsQ3.setItemText(0, _translate("ActionReflectionSelfA", "Never"))
        self.ActionsQ3.setItemText(1, _translate("ActionReflectionSelfA", "Very Rarely"))
        self.ActionsQ3.setItemText(2, _translate("ActionReflectionSelfA", "Rarely"))
        self.ActionsQ3.setItemText(3, _translate("ActionReflectionSelfA", "Sometimes"))
        self.ActionsQ3.setItemText(4, _translate("ActionReflectionSelfA", "Often"))
        self.ActionsQ3.setItemText(5, _translate("ActionReflectionSelfA", "Always"))
        self.label_5.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p>I try to think of new ways of doing things</p></body></html>"))
        self.label_6.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p>I like to figure out how things work</p></body></html>"))
        self.label_7.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p>I know my own habitual patterns of thinking and I can stand apart from those habits</p></body></html>"))
        self.ReflectionQ1.setToolTip(_translate("ActionReflectionSelfA", "Please select from the following"))
        self.ReflectionQ1.setItemText(0, _translate("ActionReflectionSelfA", "Never"))
        self.ReflectionQ1.setItemText(1, _translate("ActionReflectionSelfA", "Very Rarely"))
        self.ReflectionQ1.setItemText(2, _translate("ActionReflectionSelfA", "Rarely"))
        self.ReflectionQ1.setItemText(3, _translate("ActionReflectionSelfA", "Sometimes"))
        self.ReflectionQ1.setItemText(4, _translate("ActionReflectionSelfA", "Often"))
        self.ReflectionQ1.setItemText(5, _translate("ActionReflectionSelfA", "Always"))
        self.ReflectionQ2.setToolTip(_translate("ActionReflectionSelfA", "Please select from the following"))
        self.ReflectionQ2.setItemText(0, _translate("ActionReflectionSelfA", "Never"))
        self.ReflectionQ2.setItemText(1, _translate("ActionReflectionSelfA", "Very Rarely"))
        self.ReflectionQ2.setItemText(2, _translate("ActionReflectionSelfA", "Rarely"))
        self.ReflectionQ2.setItemText(3, _translate("ActionReflectionSelfA", "Sometimes"))
        self.ReflectionQ2.setItemText(4, _translate("ActionReflectionSelfA", "Often"))
        self.ReflectionQ2.setItemText(5, _translate("ActionReflectionSelfA", "Always"))
        self.ReflectionQ3.setToolTip(_translate("ActionReflectionSelfA", "Please select from the following"))
        self.ReflectionQ3.setItemText(0, _translate("ActionReflectionSelfA", "Never"))
        self.ReflectionQ3.setItemText(1, _translate("ActionReflectionSelfA", "Very Rarely"))
        self.ReflectionQ3.setItemText(2, _translate("ActionReflectionSelfA", "Rarely"))
        self.ReflectionQ3.setItemText(3, _translate("ActionReflectionSelfA", "Sometimes"))
        self.ReflectionQ3.setItemText(4, _translate("ActionReflectionSelfA", "Often"))
        self.ReflectionQ3.setItemText(5, _translate("ActionReflectionSelfA", "Always"))
        self.label_8.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p>I am rarely aware of changes</p></body></html>"))
        self.label_9.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p>I am rarely alert to new developements</p></body></html>"))
        self.label_10.setText(_translate("ActionReflectionSelfA", "<html><head/><body><p>Our business cycle is very fast so we have a short-time horizon mentality, we are very </p><p>flexibile but lack consistent strategic thinking</p></body></html>"))
        self.SelfAwareQ1.setToolTip(_translate("ActionReflectionSelfA", "Please select from the following"))
        self.SelfAwareQ1.setItemText(0, _translate("ActionReflectionSelfA", "Never"))
        self.SelfAwareQ1.setItemText(1, _translate("ActionReflectionSelfA", "Very Rarely"))
        self.SelfAwareQ1.setItemText(2, _translate("ActionReflectionSelfA", "Rarely"))
        self.SelfAwareQ1.setItemText(3, _translate("ActionReflectionSelfA", "Sometimes"))
        self.SelfAwareQ1.setItemText(4, _translate("ActionReflectionSelfA", "Often"))
        self.SelfAwareQ1.setItemText(5, _translate("ActionReflectionSelfA", "Always"))
        self.SelfAwareQ2.setToolTip(_translate("ActionReflectionSelfA", "Please select from the following"))
        self.SelfAwareQ2.setItemText(0, _translate("ActionReflectionSelfA", "Never"))
        self.SelfAwareQ2.setItemText(1, _translate("ActionReflectionSelfA", "Very Rarely"))
        self.SelfAwareQ2.setItemText(2, _translate("ActionReflectionSelfA", "Rarely"))
        self.SelfAwareQ2.setItemText(3, _translate("ActionReflectionSelfA", "Sometimes"))
        self.SelfAwareQ2.setItemText(4, _translate("ActionReflectionSelfA", "Often"))
        self.SelfAwareQ2.setItemText(5, _translate("ActionReflectionSelfA", "Always"))
        self.SelfAwareQ3.setToolTip(_translate("ActionReflectionSelfA", "Please select from the following"))
        self.SelfAwareQ3.setItemText(0, _translate("ActionReflectionSelfA", "Never"))
        self.SelfAwareQ3.setItemText(1, _translate("ActionReflectionSelfA", "Very Rarely"))
        self.SelfAwareQ3.setItemText(2, _translate("ActionReflectionSelfA", "Rarely"))
        self.SelfAwareQ3.setItemText(3, _translate("ActionReflectionSelfA", "Sometimes"))
        self.SelfAwareQ3.setItemText(4, _translate("ActionReflectionSelfA", "Often"))
        self.SelfAwareQ3.setItemText(5, _translate("ActionReflectionSelfA", "Always"))
        self.Final.setStatusTip(_translate("ActionReflectionSelfA", "Click this to go to next stages of questions"))
        self.Final.setText(_translate("ActionReflectionSelfA", "Submit"))
        self.Back.setStatusTip(_translate("ActionReflectionSelfA", "Click this to return to previous form"))
        self.Back.setText(_translate("ActionReflectionSelfA", "Back"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ActionReflectionSelfA = QtWidgets.QDialog()
    ui = Ui_ActionReflectionSelfA()
    ui.setupUi(ActionReflectionSelfA)
    ActionReflectionSelfA.show()
    app.exec_()
