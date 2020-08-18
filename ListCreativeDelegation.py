# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListCreativeDelegation.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QShortcut , QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog , QAction ,QShortcut
from ActionReflectionSelfA import Ui_ActionReflectionSelfA

thisdict = {"Never":0,
            "Very Rarely":1,
            "Rarely":2,
            "Sometimes":3,
            "Often":4,
            "Always":5}


class Ui_ListCreativeDelegation(object):

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


    def setupUi(self, ListCreativeDelegation):
        ListCreativeDelegation.setObjectName("ListCreativeDelegation")
        ListCreativeDelegation.resize(822, 751)
        ListCreativeDelegation.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.GenerativeQ1 = QtWidgets.QComboBox(ListCreativeDelegation)
        self.GenerativeQ1.setGeometry(QtCore.QRect(690, 80, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GenerativeQ1.setFont(font)
        self.GenerativeQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GenerativeQ1.setMaxVisibleItems(6)
        self.GenerativeQ1.setObjectName("GenerativeQ1")
        self.GenerativeQ1.addItem("")
        self.GenerativeQ1.addItem("")
        self.GenerativeQ1.addItem("")
        self.GenerativeQ1.addItem("")
        self.GenerativeQ1.addItem("")
        self.GenerativeQ1.addItem("")
        self.label_2 = QtWidgets.QLabel(ListCreativeDelegation)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(ListCreativeDelegation)
        self.label.setGeometry(QtCore.QRect(200, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(ListCreativeDelegation)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.GenerativeQ2 = QtWidgets.QComboBox(ListCreativeDelegation)
        self.GenerativeQ2.setGeometry(QtCore.QRect(690, 140, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GenerativeQ2.setFont(font)
        self.GenerativeQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GenerativeQ2.setMaxVisibleItems(6)
        self.GenerativeQ2.setObjectName("GenerativeQ2")
        self.GenerativeQ2.addItem("")
        self.GenerativeQ2.addItem("")
        self.GenerativeQ2.addItem("")
        self.GenerativeQ2.addItem("")
        self.GenerativeQ2.addItem("")
        self.GenerativeQ2.addItem("")
        self.label_4 = QtWidgets.QLabel(ListCreativeDelegation)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.GenerativeQ3 = QtWidgets.QComboBox(ListCreativeDelegation)
        self.GenerativeQ3.setGeometry(QtCore.QRect(690, 200, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GenerativeQ3.setFont(font)
        self.GenerativeQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GenerativeQ3.setMaxVisibleItems(6)
        self.GenerativeQ3.setObjectName("GenerativeQ3")
        self.GenerativeQ3.addItem("")
        self.GenerativeQ3.addItem("")
        self.GenerativeQ3.addItem("")
        self.GenerativeQ3.addItem("")
        self.GenerativeQ3.addItem("")
        self.GenerativeQ3.addItem("")
        self.label_5 = QtWidgets.QLabel(ListCreativeDelegation)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.CreativeQ1 = QtWidgets.QComboBox(ListCreativeDelegation)
        self.CreativeQ1.setGeometry(QtCore.QRect(690, 260, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CreativeQ1.setFont(font)
        self.CreativeQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CreativeQ1.setMaxVisibleItems(6)
        self.CreativeQ1.setObjectName("CreativeQ1")
        self.CreativeQ1.addItem("")
        self.CreativeQ1.addItem("")
        self.CreativeQ1.addItem("")
        self.CreativeQ1.addItem("")
        self.CreativeQ1.addItem("")
        self.CreativeQ1.addItem("")
        self.label_6 = QtWidgets.QLabel(ListCreativeDelegation)
        self.label_6.setGeometry(QtCore.QRect(20, 320, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.CreativeQ2 = QtWidgets.QComboBox(ListCreativeDelegation)
        self.CreativeQ2.setGeometry(QtCore.QRect(690, 330, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CreativeQ2.setFont(font)
        self.CreativeQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CreativeQ2.setMaxVisibleItems(6)
        self.CreativeQ2.setObjectName("CreativeQ2")
        self.CreativeQ2.addItem("")
        self.CreativeQ2.addItem("")
        self.CreativeQ2.addItem("")
        self.CreativeQ2.addItem("")
        self.CreativeQ2.addItem("")
        self.CreativeQ2.addItem("")
        self.label_7 = QtWidgets.QLabel(ListCreativeDelegation)
        self.label_7.setGeometry(QtCore.QRect(20, 410, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.CreativeQ3_2 = QtWidgets.QComboBox(ListCreativeDelegation)
        self.CreativeQ3_2.setGeometry(QtCore.QRect(690, 410, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CreativeQ3_2.setFont(font)
        self.CreativeQ3_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CreativeQ3_2.setMaxVisibleItems(6)
        self.CreativeQ3_2.setObjectName("CreativeQ3_2")
        self.CreativeQ3_2.addItem("")
        self.CreativeQ3_2.addItem("")
        self.CreativeQ3_2.addItem("")
        self.CreativeQ3_2.addItem("")
        self.CreativeQ3_2.addItem("")
        self.CreativeQ3_2.addItem("")
        self.label_8 = QtWidgets.QLabel(ListCreativeDelegation)
        self.label_8.setGeometry(QtCore.QRect(20, 470, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.DelegationQ1 = QtWidgets.QComboBox(ListCreativeDelegation)
        self.DelegationQ1.setGeometry(QtCore.QRect(690, 480, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DelegationQ1.setFont(font)
        self.DelegationQ1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DelegationQ1.setMaxVisibleItems(6)
        self.DelegationQ1.setObjectName("DelegationQ1")
        self.DelegationQ1.addItem("")
        self.DelegationQ1.addItem("")
        self.DelegationQ1.addItem("")
        self.DelegationQ1.addItem("")
        self.DelegationQ1.addItem("")
        self.DelegationQ1.addItem("")
        self.label_9 = QtWidgets.QLabel(ListCreativeDelegation)
        self.label_9.setGeometry(QtCore.QRect(20, 560, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.DelegationQ2 = QtWidgets.QComboBox(ListCreativeDelegation)
        self.DelegationQ2.setGeometry(QtCore.QRect(690, 560, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DelegationQ2.setFont(font)
        self.DelegationQ2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DelegationQ2.setMaxVisibleItems(6)
        self.DelegationQ2.setObjectName("DelegationQ2")
        self.DelegationQ2.addItem("")
        self.DelegationQ2.addItem("")
        self.DelegationQ2.addItem("")
        self.DelegationQ2.addItem("")
        self.DelegationQ2.addItem("")
        self.DelegationQ2.addItem("")
        self.label_10 = QtWidgets.QLabel(ListCreativeDelegation)
        self.label_10.setGeometry(QtCore.QRect(20, 620, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.DelegationQ3 = QtWidgets.QComboBox(ListCreativeDelegation)
        self.DelegationQ3.setGeometry(QtCore.QRect(690, 620, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DelegationQ3.setFont(font)
        self.DelegationQ3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DelegationQ3.setMaxVisibleItems(6)
        self.DelegationQ3.setObjectName("DelegationQ3")
        self.DelegationQ3.addItem("")
        self.DelegationQ3.addItem("")
        self.DelegationQ3.addItem("")
        self.DelegationQ3.addItem("")
        self.DelegationQ3.addItem("")
        self.DelegationQ3.addItem("")
        self.Back = QtWidgets.QPushButton(ListCreativeDelegation)
        self.Back.setGeometry(QtCore.QRect(20, 690, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setAutoFillBackground(False)
        self.Back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Back.setObjectName("Back")
        self.NextQuestiion = QtWidgets.QPushButton(ListCreativeDelegation)
        self.NextQuestiion.setGeometry(QtCore.QRect(700, 690, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NextQuestiion.setFont(font)
        self.NextQuestiion.setAutoFillBackground(False)
        self.NextQuestiion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NextQuestiion.setObjectName("NextQuestiion")
        self.line = QtWidgets.QFrame(ListCreativeDelegation)
        self.line.setGeometry(QtCore.QRect(0, 110, 831, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(ListCreativeDelegation)
        self.line_2.setGeometry(QtCore.QRect(0, 180, 831, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(ListCreativeDelegation)
        self.line_3.setGeometry(QtCore.QRect(0, 230, 831, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(ListCreativeDelegation)
        self.line_4.setGeometry(QtCore.QRect(0, 290, 831, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(ListCreativeDelegation)
        self.line_5.setGeometry(QtCore.QRect(0, 380, 831, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(ListCreativeDelegation)
        self.line_6.setGeometry(QtCore.QRect(0, 440, 831, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(ListCreativeDelegation)
        self.line_7.setGeometry(QtCore.QRect(0, 530, 831, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(ListCreativeDelegation)
        self.line_8.setGeometry(QtCore.QRect(0, 590, 831, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(ListCreativeDelegation)
        self.line_9.setGeometry(QtCore.QRect(0, 660, 831, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.retranslateUi(ListCreativeDelegation)
        self.GenerativeQ1.setCurrentIndex(-1)
        self.GenerativeQ2.setCurrentIndex(-1)
        self.GenerativeQ3.setCurrentIndex(-1)
        self.CreativeQ1.setCurrentIndex(-1)
        self.CreativeQ2.setCurrentIndex(-1)
        self.CreativeQ3_2.setCurrentIndex(-1)
        self.DelegationQ1.setCurrentIndex(-1)
        self.DelegationQ2.setCurrentIndex(-1)
        self.DelegationQ3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ListCreativeDelegation)
        self.NextQuestiion.clicked.connect(self.pressed)
        self.h = ListCreativeDelegation


    def pressed(self):
        

        if(self.GenerativeQ1.currentText() == "" or self.GenerativeQ2.currentText() == "" or self.GenerativeQ3.currentText() == "" or self.CreativeQ1.currentText() == "" or self.CreativeQ2.currentText() == "" or self.CreativeQ3_2.currentText() == "" or self.DelegationQ1.currentText() == "" or self.DelegationQ2.currentText() == "" or self.DelegationQ3.currentText() == ""):

            self.messagebox("Error","Please enter all fields")

        else: 

            self.GQ1 = thisdict[self.GenerativeQ1.currentText()] 

            if(self.GQ1 == 5):

                self.GQ1 = 0
                self.contracting = self.contracting + (self.GQ1 *1)
                self.present = self.present + (self.GQ1 * 1)
                self.pointsself = self.pointsself +(self.GQ1 * 1)
                self.trust = self.trust + (self.GQ1 * 1)
                self.perspectives = self.perspectives + (self.GQ1 * 1)
                self.listening = self.listening + (self.GQ1 * 10)
                self.reflection = self.reflection + (self.GQ1 * 2)
                self.selfaware = self.selfaware + (self.GQ1 * 1)

            elif(self.GQ1 == 4):

                self.GQ1 = 1
                self.contracting = self.contracting + (self.GQ1 *1)
                self.present = self.present + (self.GQ1 * 1)
                self.pointsself = self.pointsself +(self.GQ1 * 1)
                self.trust = self.trust + (self.GQ1 * 1)
                self.perspectives = self.perspectives + (self.GQ1 * 1)
                self.listening = self.listening + (self.GQ1 * 10)
                self.reflection = self.reflection + (self.GQ1 * 2)
                self.selfaware = self.selfaware + (self.GQ1 * 1)
                
            elif(self.GQ1 == 3):
                self.GQ1 = 2
                self.contracting = self.contracting + (self.GQ1 *1)
                self.present = self.present + (self.GQ1 * 1)
                self.pointsself = self.pointsself +(self.GQ1 * 1)
                self.trust = self.trust + (self.GQ1 * 1)
                self.perspectives = self.perspectives + (self.GQ1 * 1)
                self.listening = self.listening + (self.GQ1 * 10)
                self.reflection = self.reflection + (self.GQ1 * 2)
                self.selfaware = self.selfaware + (self.GQ1 * 1)

            elif(self.GQ1 == 2):

                self.GQ1 = 3
                self.contracting = self.contracting + (self.GQ1 *1)
                self.present = self.present + (self.GQ1 * 1)
                self.pointsself = self.pointsself +(self.GQ1 * 1)
                self.trust = self.trust + (self.GQ1 * 1)
                self.perspectives = self.perspectives + (self.GQ1 * 1)
                self.listening = self.listening + (self.GQ1 * 10)
                self.reflection = self.reflection + (self.GQ1 * 2)
                self.selfaware = self.selfaware + (self.GQ1 * 1)

            elif(self.GQ1 == 1):

                self.GQ1 = 4
                self.contracting = self.contracting + (self.GQ1 *1)
                self.present = self.present + (self.GQ1 * 1)
                self.pointsself = self.pointsself +(self.GQ1 * 1)
                self.trust = self.trust + (self.GQ1 * 1)
                self.perspectives = self.perspectives + (self.GQ1 * 1)
                self.listening = self.listening + (self.GQ1 * 10)
                self.reflection = self.reflection + (self.GQ1 * 2)
                self.selfaware = self.selfaware + (self.GQ1 * 1)
                
            elif(self.GQ1 == 0):

                self.GQ1 = 5
                self.contracting = self.contracting + (self.GQ1 *1)
                self.present = self.present + (self.GQ1 * 1)
                self.pointsself = self.pointsself +(self.GQ1 * 1)
                self.trust = self.trust + (self.GQ1 * 1)
                self.perspectives = self.perspectives + (self.GQ1 * 1)
                self.listening = self.listening + (self.GQ1 * 10)
                self.reflection = self.reflection + (self.GQ1 * 2)
                self.selfaware = self.selfaware + (self.GQ1 * 1)

            self.GQ2 = thisdict[self.GenerativeQ2.currentText()] 

            if(self.GQ2 == 5):

                self.GQ2 = 0
                self.present = self.present + (self.GQ2 * 2)
                self.pointsself = self.pointsself +(self.GQ2 * 1)
                self.listening = self.listening + (self.GQ2 * 10)
                self.reflection = self.reflection + (self.GQ2 * 2)

            elif(self.GQ2 == 4):

                self.GQ2 = 1
                self.present = self.present + (self.GQ2 * 2)
                self.pointsself = self.pointsself +(self.GQ2 * 1)
                self.listening = self.listening + (self.GQ2 * 10)
                self.reflection = self.reflection + (self.GQ2 * 2)
                
            elif(self.GQ2 == 3):
                self.GQ2 = 2
                self.present = self.present + (self.GQ2 * 2)
                self.pointsself = self.pointsself +(self.GQ2 * 1)
                self.listening = self.listening + (self.GQ2 * 10)
                self.reflection = self.reflection + (self.GQ2 * 2)

            elif(self.GQ2 == 2):

                self.GQ2 = 3
                self.present = self.present + (self.GQ2 * 2)
                self.pointsself = self.pointsself +(self.GQ2 * 1)
                self.listening = self.listening + (self.GQ2 * 10)
                self.reflection = self.reflection + (self.GQ2 * 2)

            elif(self.GQ2 == 1):

                self.GQ2 = 4
                self.present = self.present + (self.GQ2 * 2)
                self.pointsself = self.pointsself +(self.GQ2 * 1)
                self.listening = self.listening + (self.GQ2 * 10)
                self.reflection = self.reflection + (self.GQ2 * 2)

            elif(self.GQ2 == 0):

                self.GQ2 = 5
                self.present = self.present + (self.GQ2 * 2)
                self.pointsself = self.pointsself +(self.GQ2 * 1)
                self.listening = self.listening + (self.GQ2 * 10)
                self.reflection = self.reflection + (self.GQ2 * 2)

            self.GQ3 = thisdict[self.GenerativeQ3.currentText()] 

            if(self.GQ3 == 5):

                self.GQ3 = 0
                self.present = self.present + (self.GQ3 * 2)
                self.pointsself = self.pointsself +(self.GQ3 * 1)
                self.trust = self.trust + (self.GQ3 * 3)
                self.listening = self.listening + (self.GQ3 * 10)

            elif(self.GQ3 == 4):

                self.GQ3 = 1
                self.present = self.present + (self.GQ3 * 2)
                self.pointsself = self.pointsself +(self.GQ3 * 1)
                self.trust = self.trust + (self.GQ3 * 3)
                self.listening = self.listening + (self.GQ3 * 10)
                
            elif(self.GQ3 == 3):
                self.GQ3 = 2
                self.present = self.present + (self.GQ3 * 2)
                self.pointsself = self.pointsself +(self.GQ3 * 1)
                self.trust = self.trust + (self.GQ3 * 3)
                self.listening = self.listening + (self.GQ3 * 10)

            elif(self.GQ3 == 2):

                self.GQ3 = 3
                self.present = self.present + (self.GQ3 * 2)
                self.pointsself = self.pointsself +(self.GQ3 * 1)
                self.trust = self.trust + (self.GQ3 * 3)
                self.listening = self.listening + (self.GQ3 * 10)

            elif(self.GQ3 == 1):

                self.GQ3 = 4
                self.present = self.present + (self.GQ3 * 2)
                self.pointsself = self.pointsself +(self.GQ3 * 1)
                self.trust = self.trust + (self.GQ3 * 3)
                self.listening = self.listening + (self.GQ3 * 10)

            elif(self.GQ3 == 0):

                self.GQ3 = 5
                self.present = self.present + (self.GQ3 * 2)
                self.pointsself = self.pointsself +(self.GQ3 * 1)
                self.trust = self.trust + (self.GQ3 * 3)
                self.listening = self.listening + (self.GQ3 * 10)

            self.CQ1 = thisdict[self.CreativeQ1.currentText()] 

            if(self.CQ1 == 5):

                self.CQ1 = 0
                self.contracting = self.contracting + (self.CQ1 * 1)
                self.trust = self.trust + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.creative = self.creative + (self.CQ1 * 10)

            elif(self.CQ1 == 4):

                self.CQ1 = 1
                self.contracting = self.contracting + (self.CQ1 * 1)
                self.trust = self.trust + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.creative = self.creative + (self.CQ1 * 10)
                
            elif(self.CQ1 == 3):
                self.CQ1 = 2
                self.contracting = self.contracting + (self.CQ1 * 1)
                self.trust = self.trust + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.creative = self.creative + (self.CQ1 * 10)

            elif(self.CQ1 == 2):

                self.CQ1 = 3
                self.contracting = self.contracting + (self.CQ1 * 1)
                self.trust = self.trust + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.creative = self.creative + (self.CQ1 * 10)

            elif(self.CQ1 == 1):

                self.CQ1 = 4
                self.contracting = self.contracting + (self.CQ1 * 1)
                self.trust = self.trust + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.creative = self.creative + (self.CQ1 * 10)

            elif(self.CQ1 == 0):

                self.CQ1 = 5
                self.contracting = self.contracting + (self.CQ1 * 1)
                self.trust = self.trust + (self.CQ1 * 2)
                self.confidentiatly = self.confidentiatly + (self.CQ1 * 1)
                self.creative = self.creative + (self.CQ1 * 10)

            self.CQ2 = thisdict[self.CreativeQ2.currentText()] 
            self.contracting = self.contracting + (self.CQ2 * 1)
            self.pointsother = self.pointsother + (self.CQ2 * 1)
            self.pointsself = self.pointsself + (self.CQ2 * 1)
            self.confidentiatly = self.confidentiatly + (self.CQ2 * 1)
            self.creative = self.creative + (self.CQ2 * 10)
                      
            self.CQ3 = thisdict[self.CreativeQ3_2.currentText()] 

            if(self.CQ3 == 5):

                self.CQ3 = 0
                self.awareness = self.awareness + (self.CQ3 * 1)
                self.creative = self.creative + (self.CQ3 * 10)

            elif(self.CQ3 == 4):

                self.CQ3 = 1
                self.awareness = self.awareness + (self.CQ3 * 1)
                self.creative = self.creative + (self.CQ3 * 10)
                
            elif(self.CQ3 == 3):
                self.CQ3 = 2
                self.awareness = self.awareness + (self.CQ3 * 1)
                self.creative = self.creative + (self.CQ3 * 10)

            elif(self.CQ3 == 2):

                self.CQ3 = 3
                self.awareness = self.awareness + (self.CQ3 * 1)
                self.creative = self.creative + (self.CQ3 * 10)

            elif(self.CQ3 == 1):

                self.CQ3 = 4
                self.awareness = self.awareness + (self.CQ3 * 1)
                self.creative = self.creative + (self.CQ3 * 10)

            elif(self.CQ3 == 0):

                self.CQ3 = 5
                self.awareness = self.awareness + (self.CQ3 * 1)
                self.creative = self.creative + (self.CQ3 * 10)

            self.DQ1 = thisdict[self.DelegationQ1.currentText()] 
            self.trust = self.trust + (self.DQ1 * 1)
            self.perspectives = self.perspectives + (self.DQ1 * 1)
            self.delegation = self.delegation + (self.DQ1 * 10)

            self.DQ2 = thisdict[self.DelegationQ2.currentText()]
            self.contracting = self.contracting + (self.DQ2 * 1)
            self.present = self.present + (self.DQ2 * 1)
            self.pointsself = self.pointsself + (self.DQ2 * 1)
            self.perspectives = self.perspectives + (self.DQ2 * 1)
            self.delegation = self.delegation + (self.DQ2 * 10)
            self.actions = self.actions + (self.DQ2 * 2)
            self.reflection = self.reflection + (self.DQ2 * 2)

            self.DQ3 = thisdict[self.DelegationQ3.currentText()]
            self.contracting = self.contracting + (self.DQ3 * 1)
            self.feedback = self.feedback + (self.DQ3 * 1)
            self.pointsself = self.pointsself + (self.DQ3 * 1)
            self.trust = self.trust + (self.DQ3 * 1)
            self.perspectives = self.perspectives + (self.DQ3 * 1)
            self.delegation = self.delegation + (self.DQ3 * 10)

            self.ListToActions(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware)
            self.h.hide()

    def ListToActions(self,email,birth,edu,lead,workyears,contracting,feedback,present,pointsself,pointsother,trust,confidentiatly,awareness,perspectives,listening,creative,delegation,actions,reflection,selfaware):
        self.main = QtWidgets.QMainWindow() 
        self.ui = Ui_ActionReflectionSelfA(self.email,self.birth,self.edu,self.lead,self.workyears,self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives,self.listening,self.creative,self.delegation,self.actions,self.reflection,self.selfaware) 
        self.ui.setupUi(self.main)
        self.main.show() 

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()   

    def retranslateUi(self, ListCreativeDelegation):
        _translate = QtCore.QCoreApplication.translate
        ListCreativeDelegation.setWindowTitle(_translate("ListCreativeDelegation", "COTG"))
        self.GenerativeQ1.setToolTip(_translate("ListCreativeDelegation", "Please select from the following"))
        self.GenerativeQ1.setItemText(0, _translate("ListCreativeDelegation", "Never"))
        self.GenerativeQ1.setItemText(1, _translate("ListCreativeDelegation", "Very Rarely"))
        self.GenerativeQ1.setItemText(2, _translate("ListCreativeDelegation", "Rarely"))
        self.GenerativeQ1.setItemText(3, _translate("ListCreativeDelegation", "Sometimes"))
        self.GenerativeQ1.setItemText(4, _translate("ListCreativeDelegation", "Often"))
        self.GenerativeQ1.setItemText(5, _translate("ListCreativeDelegation", "Always"))
        self.label_2.setText(_translate("ListCreativeDelegation", "<html><head/><body><p>I am always open to new ways of doing things</p></body></html>"))
        self.label.setText(_translate("ListCreativeDelegation", "<html><head/><body><p align=\"center\">Please answer the following questions</p></body></html>"))
        self.label_3.setText(_translate("ListCreativeDelegation", "<html><head/><body><p>I am very curious</p></body></html>"))
        self.GenerativeQ2.setToolTip(_translate("ListCreativeDelegation", "Please select from the following"))
        self.GenerativeQ2.setItemText(0, _translate("ListCreativeDelegation", "Never"))
        self.GenerativeQ2.setItemText(1, _translate("ListCreativeDelegation", "Very Rarely"))
        self.GenerativeQ2.setItemText(2, _translate("ListCreativeDelegation", "Rarely"))
        self.GenerativeQ2.setItemText(3, _translate("ListCreativeDelegation", "Sometimes"))
        self.GenerativeQ2.setItemText(4, _translate("ListCreativeDelegation", "Often"))
        self.GenerativeQ2.setItemText(5, _translate("ListCreativeDelegation", "Always"))
        self.label_4.setText(_translate("ListCreativeDelegation", "<html><head/><body><p>I listen to understand people and their ideas, not just to respond with my ideas</p></body></html>"))
        self.GenerativeQ3.setToolTip(_translate("ListCreativeDelegation", "Please select from the following"))
        self.GenerativeQ3.setItemText(0, _translate("ListCreativeDelegation", "Never"))
        self.GenerativeQ3.setItemText(1, _translate("ListCreativeDelegation", "Very Rarely"))
        self.GenerativeQ3.setItemText(2, _translate("ListCreativeDelegation", "Rarely"))
        self.GenerativeQ3.setItemText(3, _translate("ListCreativeDelegation", "Sometimes"))
        self.GenerativeQ3.setItemText(4, _translate("ListCreativeDelegation", "Often"))
        self.GenerativeQ3.setItemText(5, _translate("ListCreativeDelegation", "Always"))
        self.label_5.setText(_translate("ListCreativeDelegation", "<html><head/><body><p>I really enjoy understanding things in greater depth by asking questions</p></body></html>"))
        self.CreativeQ1.setToolTip(_translate("ListCreativeDelegation", "Please select from the following"))
        self.CreativeQ1.setItemText(0, _translate("ListCreativeDelegation", "Never"))
        self.CreativeQ1.setItemText(1, _translate("ListCreativeDelegation", "Very Rarely"))
        self.CreativeQ1.setItemText(2, _translate("ListCreativeDelegation", "Rarely"))
        self.CreativeQ1.setItemText(3, _translate("ListCreativeDelegation", "Sometimes"))
        self.CreativeQ1.setItemText(4, _translate("ListCreativeDelegation", "Often"))
        self.CreativeQ1.setItemText(5, _translate("ListCreativeDelegation", "Always"))
        self.label_6.setText(_translate("ListCreativeDelegation", "<html><head/><body><p>Sometimes I spend too much time asking questions trying to understand the details of an </p><p>issue</p></body></html>"))
        self.CreativeQ2.setToolTip(_translate("ListCreativeDelegation", "Please select from the following"))
        self.CreativeQ2.setItemText(0, _translate("ListCreativeDelegation", "Never"))
        self.CreativeQ2.setItemText(1, _translate("ListCreativeDelegation", "Very Rarely"))
        self.CreativeQ2.setItemText(2, _translate("ListCreativeDelegation", "Rarely"))
        self.CreativeQ2.setItemText(3, _translate("ListCreativeDelegation", "Sometimes"))
        self.CreativeQ2.setItemText(4, _translate("ListCreativeDelegation", "Often"))
        self.CreativeQ2.setItemText(5, _translate("ListCreativeDelegation", "Always"))
        self.label_7.setText(_translate("ListCreativeDelegation", "<html><head/><body><p>People often respond to my questions by pausing and saying \'that\'s a great questions\'</p></body></html>"))
        self.CreativeQ3_2.setToolTip(_translate("ListCreativeDelegation", "Please select from the following"))
        self.CreativeQ3_2.setItemText(0, _translate("ListCreativeDelegation", "Never"))
        self.CreativeQ3_2.setItemText(1, _translate("ListCreativeDelegation", "Very Rarely"))
        self.CreativeQ3_2.setItemText(2, _translate("ListCreativeDelegation", "Rarely"))
        self.CreativeQ3_2.setItemText(3, _translate("ListCreativeDelegation", "Sometimes"))
        self.CreativeQ3_2.setItemText(4, _translate("ListCreativeDelegation", "Often"))
        self.CreativeQ3_2.setItemText(5, _translate("ListCreativeDelegation", "Always"))
        self.label_8.setText(_translate("ListCreativeDelegation", "<html><head/><body><p>I\'m annoyed if I learn something for the first time in a meeting from a member of my </p><p>team</p></body></html>"))
        self.DelegationQ1.setToolTip(_translate("ListCreativeDelegation", "Please select from the following"))
        self.DelegationQ1.setItemText(0, _translate("ListCreativeDelegation", "Never"))
        self.DelegationQ1.setItemText(1, _translate("ListCreativeDelegation", "Very Rarely"))
        self.DelegationQ1.setItemText(2, _translate("ListCreativeDelegation", "Rarely"))
        self.DelegationQ1.setItemText(3, _translate("ListCreativeDelegation", "Sometimes"))
        self.DelegationQ1.setItemText(4, _translate("ListCreativeDelegation", "Often"))
        self.DelegationQ1.setItemText(5, _translate("ListCreativeDelegation", "Always"))
        self.label_9.setText(_translate("ListCreativeDelegation", "<html><head/><body><p>I am too busy to take time out to think strategically</p></body></html>"))
        self.DelegationQ2.setToolTip(_translate("ListCreativeDelegation", "Please select from the following"))
        self.DelegationQ2.setItemText(0, _translate("ListCreativeDelegation", "Never"))
        self.DelegationQ2.setItemText(1, _translate("ListCreativeDelegation", "Very Rarely"))
        self.DelegationQ2.setItemText(2, _translate("ListCreativeDelegation", "Rarely"))
        self.DelegationQ2.setItemText(3, _translate("ListCreativeDelegation", "Sometimes"))
        self.DelegationQ2.setItemText(4, _translate("ListCreativeDelegation", "Often"))
        self.DelegationQ2.setItemText(5, _translate("ListCreativeDelegation", "Always"))
        self.label_10.setText(_translate("ListCreativeDelegation", "<html><head/><body><p>There are no opportunities for me to delegate my work to others</p></body></html>"))
        self.DelegationQ3.setToolTip(_translate("ListCreativeDelegation", "Please select from the following"))
        self.DelegationQ3.setItemText(0, _translate("ListCreativeDelegation", "Never"))
        self.DelegationQ3.setItemText(1, _translate("ListCreativeDelegation", "Very Rarely"))
        self.DelegationQ3.setItemText(2, _translate("ListCreativeDelegation", "Rarely"))
        self.DelegationQ3.setItemText(3, _translate("ListCreativeDelegation", "Sometimes"))
        self.DelegationQ3.setItemText(4, _translate("ListCreativeDelegation", "Often"))
        self.DelegationQ3.setItemText(5, _translate("ListCreativeDelegation", "Always"))
        self.Back.setStatusTip(_translate("ListCreativeDelegation", "Click this to go back a form"))
        self.Back.setText(_translate("ListCreativeDelegation", "Back"))
        self.NextQuestiion.setStatusTip(_translate("ListCreativeDelegation", "Click this to go to next questions"))
        self.NextQuestiion.setText(_translate("ListCreativeDelegation", "Next"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListCreativeDelegation = QtWidgets.QDialog()
    ui = Ui_ListCreativeDelegation()
    ui.setupUi(ListCreativeDelegation)
    ListCreativeDelegation.show()
    app.exec_()
