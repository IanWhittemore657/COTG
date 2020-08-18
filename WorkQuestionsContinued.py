# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkQuestionsContinued.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QShortcut , QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog , QAction ,QShortcut
import pymysql
from ContractFeed import Ui_ContractFeedPresent

#f = open("Main.txt","r")  #this is used to open up the file where the database settings are kept

#dbname = str(f.readline())
#dbname =  dbname.replace('\n','' )
#userDB = str(f.readline())
#userDB =  userDB.replace('\n','' )
#passDB =  str(f.readline())                     
#passDB =  passDB.replace('\n','' )
#address = str(f.readline())
#address = address.replace('\n','' )


thisdict = {"Never":0,
            "Very Rarely":1,
            "Rarely":2,
            "Sometimes":3,
            "Often":4,
            "Always":5}

class Ui_WorkQCont(object):

    def __init__(self,email,birth,edu,lead,workyears,WorkQ1,WorkQ2,WorkQ3,WorkQ4,WorkQ5,WorkQ6,WorkQ7,WorkQ8,WorkQ9):

        self.email = email
        self.birth = birth
        self.edu = edu            
        self.lead = lead
        self.workyears = workyears
        self.WorkQ1 = WorkQ1
        self.WorkQ2 = WorkQ2 
        self.WorkQ3 = WorkQ3 
        self.WorkQ4 = WorkQ4
        self.WorkQ5 = WorkQ5
        self.WorkQ6 = WorkQ6
        self.WorkQ7 = WorkQ7
        self.WorkQ8 = WorkQ8
        self.WorkQ9 = WorkQ9

    def setupUi(self, WorkQCont):
        WorkQCont.setObjectName("WorkQCont")
        WorkQCont.resize(829, 785)
        WorkQCont.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.label = QtWidgets.QLabel(WorkQCont)
        self.label.setGeometry(QtCore.QRect(170, 10, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.NextForm2 = QtWidgets.QPushButton(WorkQCont)
        self.NextForm2.setGeometry(QtCore.QRect(710, 740, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NextForm2.setFont(font)
        self.NextForm2.setAutoFillBackground(False)
        self.NextForm2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NextForm2.setObjectName("NextForm2")
        self.Back = QtWidgets.QPushButton(WorkQCont)
        self.Back.setGeometry(QtCore.QRect(10, 740, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setAutoFillBackground(False)
        self.Back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Back.setObjectName("Back")
        self.label_10 = QtWidgets.QLabel(WorkQCont)
        self.label_10.setGeometry(QtCore.QRect(10, 200, 611, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(WorkQCont)
        self.label_11.setGeometry(QtCore.QRect(10, 260, 611, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(WorkQCont)
        self.label_12.setGeometry(QtCore.QRect(10, 320, 611, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(WorkQCont)
        self.label_13.setGeometry(QtCore.QRect(10, 380, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(WorkQCont)
        self.label_14.setGeometry(QtCore.QRect(10, 440, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(WorkQCont)
        self.label_15.setGeometry(QtCore.QRect(10, 530, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(WorkQCont)
        self.label_16.setGeometry(QtCore.QRect(10, 590, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(WorkQCont)
        self.label_17.setGeometry(QtCore.QRect(10, 680, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(WorkQCont)
        self.label_18.setGeometry(QtCore.QRect(10, 80, 611, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(WorkQCont)
        self.label_19.setGeometry(QtCore.QRect(10, 140, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.WorkQ10 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ10.setGeometry(QtCore.QRect(670, 80, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ10.setFont(font)
        self.WorkQ10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ10.setMaxVisibleItems(6)
        self.WorkQ10.setObjectName("WorkQ10")
        self.WorkQ10.addItem("")
        self.WorkQ10.addItem("")
        self.WorkQ10.addItem("")
        self.WorkQ10.addItem("")
        self.WorkQ10.addItem("")
        self.WorkQ10.addItem("")
        self.WorkQ11 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ11.setGeometry(QtCore.QRect(670, 140, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ11.setFont(font)
        self.WorkQ11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ11.setMaxVisibleItems(6)
        self.WorkQ11.setObjectName("WorkQ11")
        self.WorkQ11.addItem("")
        self.WorkQ11.addItem("")
        self.WorkQ11.addItem("")
        self.WorkQ11.addItem("")
        self.WorkQ11.addItem("")
        self.WorkQ11.addItem("")
        self.WorkQ12 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ12.setGeometry(QtCore.QRect(670, 200, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ12.setFont(font)
        self.WorkQ12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ12.setMaxVisibleItems(6)
        self.WorkQ12.setObjectName("WorkQ12")
        self.WorkQ12.addItem("")
        self.WorkQ12.addItem("")
        self.WorkQ12.addItem("")
        self.WorkQ12.addItem("")
        self.WorkQ12.addItem("")
        self.WorkQ12.addItem("")
        self.WorkQ13 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ13.setGeometry(QtCore.QRect(670, 260, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ13.setFont(font)
        self.WorkQ13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ13.setMaxVisibleItems(6)
        self.WorkQ13.setObjectName("WorkQ13")
        self.WorkQ13.addItem("")
        self.WorkQ13.addItem("")
        self.WorkQ13.addItem("")
        self.WorkQ13.addItem("")
        self.WorkQ13.addItem("")
        self.WorkQ13.addItem("")
        self.WorkQ14 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ14.setGeometry(QtCore.QRect(670, 320, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ14.setFont(font)
        self.WorkQ14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ14.setMaxVisibleItems(6)
        self.WorkQ14.setObjectName("WorkQ14")
        self.WorkQ14.addItem("")
        self.WorkQ14.addItem("")
        self.WorkQ14.addItem("")
        self.WorkQ14.addItem("")
        self.WorkQ14.addItem("")
        self.WorkQ14.addItem("")
        self.WorkQ15 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ15.setGeometry(QtCore.QRect(670, 380, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ15.setFont(font)
        self.WorkQ15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ15.setMaxVisibleItems(6)
        self.WorkQ15.setObjectName("WorkQ15")
        self.WorkQ15.addItem("")
        self.WorkQ15.addItem("")
        self.WorkQ15.addItem("")
        self.WorkQ15.addItem("")
        self.WorkQ15.addItem("")
        self.WorkQ15.addItem("")
        self.WorkQ16 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ16.setGeometry(QtCore.QRect(670, 450, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ16.setFont(font)
        self.WorkQ16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ16.setMaxVisibleItems(6)
        self.WorkQ16.setObjectName("WorkQ16")
        self.WorkQ16.addItem("")
        self.WorkQ16.addItem("")
        self.WorkQ16.addItem("")
        self.WorkQ16.addItem("")
        self.WorkQ16.addItem("")
        self.WorkQ16.addItem("")
        self.WorkQ17 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ17.setGeometry(QtCore.QRect(670, 530, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ17.setFont(font)
        self.WorkQ17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ17.setMaxVisibleItems(6)
        self.WorkQ17.setObjectName("WorkQ17")
        self.WorkQ17.addItem("")
        self.WorkQ17.addItem("")
        self.WorkQ17.addItem("")
        self.WorkQ17.addItem("")
        self.WorkQ17.addItem("")
        self.WorkQ17.addItem("")
        self.WorkQ18 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ18.setGeometry(QtCore.QRect(670, 600, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ18.setFont(font)
        self.WorkQ18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ18.setMaxVisibleItems(6)
        self.WorkQ18.setObjectName("WorkQ18")
        self.WorkQ18.addItem("")
        self.WorkQ18.addItem("")
        self.WorkQ18.addItem("")
        self.WorkQ18.addItem("")
        self.WorkQ18.addItem("")
        self.WorkQ18.addItem("")
        self.WorkQ19 = QtWidgets.QComboBox(WorkQCont)
        self.WorkQ19.setGeometry(QtCore.QRect(670, 680, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WorkQ19.setFont(font)
        self.WorkQ19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WorkQ19.setMaxVisibleItems(6)
        self.WorkQ19.setObjectName("WorkQ19")
        self.WorkQ19.addItem("")
        self.WorkQ19.addItem("")
        self.WorkQ19.addItem("")
        self.WorkQ19.addItem("")
        self.WorkQ19.addItem("")
        self.WorkQ19.addItem("")
        self.line = QtWidgets.QFrame(WorkQCont)
        self.line.setGeometry(QtCore.QRect(0, 110, 831, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(WorkQCont)
        self.line_2.setGeometry(QtCore.QRect(0, 170, 831, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(WorkQCont)
        self.line_3.setGeometry(QtCore.QRect(0, 230, 831, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(WorkQCont)
        self.line_4.setGeometry(QtCore.QRect(0, 290, 831, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(WorkQCont)
        self.line_5.setGeometry(QtCore.QRect(0, 350, 831, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(WorkQCont)
        self.line_6.setGeometry(QtCore.QRect(0, 410, 831, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(WorkQCont)
        self.line_7.setGeometry(QtCore.QRect(0, 500, 831, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(WorkQCont)
        self.line_8.setGeometry(QtCore.QRect(-10, 560, 831, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(WorkQCont)
        self.line_9.setGeometry(QtCore.QRect(0, 650, 831, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(WorkQCont)
        self.line_10.setGeometry(QtCore.QRect(0, 710, 831, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")

        self.retranslateUi(WorkQCont)
        self.WorkQ10.setCurrentIndex(-1)
        self.WorkQ11.setCurrentIndex(-1)
        self.WorkQ12.setCurrentIndex(-1)
        self.WorkQ13.setCurrentIndex(-1)
        self.WorkQ14.setCurrentIndex(-1)
        self.WorkQ15.setCurrentIndex(-1)
        self.WorkQ16.setCurrentIndex(-1)
        self.WorkQ17.setCurrentIndex(-1)
        self.WorkQ18.setCurrentIndex(-1)
        self.WorkQ19.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(WorkQCont)
        self.NextForm2.clicked.connect(self.pressed)
        
        self.h =WorkQCont

    def pressed(self):
        if(self.WorkQ10.currentText() == "" or self.WorkQ11.currentText() == "" or self.WorkQ12.currentText() == "" or self.WorkQ13.currentText() == "" or self.WorkQ14.currentText() == "" or self.WorkQ15.currentText() == "" or self.WorkQ16.currentText() == "" or self.WorkQ17.currentText() == "" or self.WorkQ18.currentText() == "" or self.WorkQ19.currentText() == ""):

            self.messagebox("Error","Please enter all fields")

        else: 

            self.Q1 = thisdict[self.WorkQ1]
            self.Q2 = thisdict[self.WorkQ2] 
            self.Q3 = thisdict[self.WorkQ3] 
       
            self.Q4 = thisdict[self.WorkQ4]
            if(self.Q4 == 5):
                self.Q4 = 0 
            elif(self.Q4 == 4):
                self.Q4 = 1 
            elif(self.Q4 == 3):
                self.Q4 = 2 
            elif(self.Q4 == 2):
                self.Q4 = 3
            elif(self.Q4 == 1):
                self.Q4 = 4
            elif(self.Q4 == 0):
                self.Q4 = 5 
         

            self.Q5 = thisdict[self.WorkQ5]
            if(self.Q5 == 5):
                self.Q5 = 0 
            elif(self.Q5 == 4):
                self.Q5 = 1 
            elif(self.Q5 == 3):
                self.Q5 = 2 
            elif(self.Q5 == 2):
                self.Q5 = 3
            elif(self.Q5 == 1):
                self.Q5 = 4
            elif(self.Q5 == 0):
                self.Q5 = 5 
   

            self.Q6 = thisdict[self.WorkQ6]
            if(self.Q6 == 5):
                self.Q6 = 0 
            elif(self.Q6 == 4):
                self.Q6 = 1 
            elif(self.Q6 == 3):
                self.Q6 = 2 
            elif(self.Q6 == 2):
                self.Q6 = 3
            elif(self.Q6 == 1):
                self.Q6 = 4
            elif(self.Q6 == 0):
                self.Q6 = 5 

            self.Q7 = thisdict[self.WorkQ7] 

            self.Q8 = thisdict[self.WorkQ8]
            if(self.Q8 == 5):
                self.Q8 = 0 
            elif(self.Q8 == 4):
                self.Q8 = 1 
            elif(self.Q8 == 3):
                self.Q8 = 2 
            elif(self.Q8 == 2):
                self.Q8 = 3 
            elif(self.Q8 == 1):
                self.Q8 = 4
            elif(self.Q8 == 0):
                self.Q8 = 5 

            self.Q9 = thisdict[self.WorkQ9]

            self.totalToQ9 = self.Q1 + self.Q2 + self.Q3 + self.Q4 + self.Q5 + self.Q6 + self.Q7 + self.Q8 + self.Q9

           

            self.Q10 = thisdict[self.WorkQ10.currentText()] 
            self.Q11 = thisdict[self.WorkQ11.currentText()] 
            self.Q12 = thisdict[self.WorkQ12.currentText()] 
            self.Q13 = thisdict[self.WorkQ13.currentText()] 
            self.Q14 = thisdict[self.WorkQ14.currentText()] 
            self.Q15 = thisdict[self.WorkQ15.currentText()] 

            self.Q16 = thisdict[self.WorkQ16.currentText()]
            if(self.Q16 == 5):
                self.Q16 = 0 
            elif(self.Q16 == 4):
                self.Q16 = 1 
            elif(self.Q16 == 3):
                self.Q16 = 2 
            elif(self.Q16 == 2):
                self.Q16 = 3
            elif(self.Q16 == 1):
                self.Q16 = 4
            elif(self.Q16 == 0):
                self.Q16 = 5 
         
            self.Q17 = thisdict[self.WorkQ17.currentText()]

            self.Q18 = thisdict[self.WorkQ18.currentText()]
            if(self.Q18 == 5):
                self.Q18 = 0 
            elif(self.Q18 == 4):
                self.Q18 = 1 
            elif(self.Q18 == 3):
                self.Q18 = 2 
            elif(self.Q18 == 2):
                self.Q18 = 3
            elif(self.Q18 == 1):
                self.Q18 = 4
            elif(self.Q18 == 0):
                self.Q18 = 5 
   

            self.Q19 = thisdict[self.WorkQ19.currentText()]
            if(self.Q19 == 5):
                self.Q19 = 0 
            elif(self.Q19 == 4):
                self.Q19 = 1 
            elif(self.Q19 == 3):
                self.Q19 = 2 
            elif(self.Q19 == 2):
                self.Q19 = 3
            elif(self.Q19 == 1):
                self.Q19 = 4
            elif(self.Q19 == 0):
                self.Q19 = 5
      

            self.Q10ToQ19 = self.Q10 + self.Q11 + self.Q12 + self.Q13 + self.Q14 + self.Q15 + self.Q16 + self.Q17 + self.Q19
            
           

            self.totalsum = self.totalToQ9 + self.Q10ToQ19

            

            self.WorkQ10 = self.WorkQ10.currentText() 
            self.WorkQ11 = self.WorkQ11.currentText() 
            self.WorkQ12 = self.WorkQ12.currentText() 
            self.WorkQ13 = self.WorkQ13.currentText() 
            self.WorkQ14 = self.WorkQ14.currentText() 
            self.WorkQ15 = self.WorkQ15.currentText() 
            self.WorkQ16 = self.WorkQ16.currentText() 
            self.WorkQ17 = self.WorkQ17.currentText() 
            self.WorkQ18 = self.WorkQ18.currentText() 
            self.WorkQ19 = self.WorkQ19.currentText() 
            

            self.toxicity = ""
            if(self.totalsum < 23):
                self.toxicity = "Low"
            elif(self.totalsum >= 24 and self.totalsum < 47):
                self.toxicity = "Medium"
            elif(self.totalsum >= 48 and self.totalsum <71):
                self.toxicity = "High"
            elif(self.totalsum >= 72):
                self.toxicity = "Very High"

            #try:

            #    conn = pymysql.connect(host = self.address,		
            #                    user = self.userDB,		
            #                    passwd = self.passDB ,		
            #                    db = self.dbname)			

            #    myCursor = conn.cursor()		
            #    query =("INSERT INTO workquestions(Work_Q1,Work_Q2,Work_Q3,Work_Q4,Work_Q5,Work_Q6,Work_Q7,Work_Q8,Work_Q9,Work_Q10,Work_Q11,Work_Q12,Work_Q13,Work_Q14,Work_Q15,Work_Q16,Work_Q17,Work_Q18,Work_Q19,Total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")		#SQL to add
            #    data = myCursor.execute(query,(self.WorkQ1,self.WorkQ2,self.WorkQ3,self.WorkQ4,self.WorkQ5,self.WorkQ6,self.WorkQ7,self.WorkQ8,self.WorkQ9,self.WorkQ10,self.WorkQ11,self.WorkQ12,self.WorkQ13,self.WorkQ14,self.WorkQ15,self.WorkQ16,self.WorkQ17,self.WorkQ18,self.WorkQ19,self.totalsum))		#values to add into DB,%s
                
            #    conn.commit()
            self.WorkToContractFeed(self.email,self.birth,self.edu,self.lead,self.workyears)
            self.h.hide()

           #     conn.close()
           # except:

            self.messagebox("Error","The work rating is : " + self.toxicity ); #the try catch statment will display this if DB cannot connect
                
    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()   

    def WorkToContractFeed(self,email,birth,edu,lead,workyears):
        self.main = QtWidgets.QMainWindow() 
        self.ui = Ui_ContractFeedPresent(self.email,self.birth,self.edu,self.lead,self.workyears) 
        self.ui.setupUi(self.main)
        self.main.show()        
            


    def retranslateUi(self, WorkQCont):
        _translate = QtCore.QCoreApplication.translate
        WorkQCont.setWindowTitle(_translate("WorkQCont", "COTG"))
        self.label.setText(_translate("WorkQCont", "Working in an organisation continued questions"))
        self.NextForm2.setStatusTip(_translate("WorkQCont", "Click this to go to next stages of questions"))
        self.NextForm2.setText(_translate("WorkQCont", "Next"))
        self.Back.setStatusTip(_translate("WorkQCont", "Click this to return to previous form"))
        self.Back.setText(_translate("WorkQCont", "Back"))
        self.label_10.setText(_translate("WorkQCont", "The organisation has a tendency to micro-manage"))
        self.label_11.setText(_translate("WorkQCont", "Because of self-promotion some leaders achieve and then maintain their position"))
        self.label_12.setText(_translate("WorkQCont", "Vital information is restricted and people who need to know, are left out"))
        self.label_13.setText(_translate("WorkQCont", "A lot of time is spent presenting upwards so that people present themselves as superior"))
        self.label_14.setText(_translate("WorkQCont", "<html><head/><body><p>The team proactively identifies what could go wrong or should be changed; We openly</p><p>discuss mistakes and lessons learnt</p></body></html>"))
        self.label_15.setText(_translate("WorkQCont", "In our organisation we do not really have the time to coach the people we work with "))
        self.label_16.setText(_translate("WorkQCont", "<html><head/><body><p>We have a culture of checking what is being overlooked, or ignored, so we are not</p><p>blindsided by radical changes in context</p></body></html>"))
        self.label_17.setText(_translate("WorkQCont", "I spend time teaching and coaching"))
        self.label_18.setText(_translate("WorkQCont", "The organisation does keep track of all mistakes"))
        self.label_19.setText(_translate("WorkQCont", "Some leaders\' competency is far below the level needed to adequately lead our business"))
        self.WorkQ10.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ10.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ10.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ10.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ10.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ10.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ10.setItemText(5, _translate("WorkQCont", "Always"))
        self.WorkQ11.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ11.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ11.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ11.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ11.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ11.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ11.setItemText(5, _translate("WorkQCont", "Always"))
        self.WorkQ12.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ12.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ12.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ12.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ12.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ12.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ12.setItemText(5, _translate("WorkQCont", "Always"))
        self.WorkQ13.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ13.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ13.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ13.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ13.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ13.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ13.setItemText(5, _translate("WorkQCont", "Always"))
        self.WorkQ14.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ14.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ14.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ14.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ14.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ14.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ14.setItemText(5, _translate("WorkQCont", "Always"))
        self.WorkQ15.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ15.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ15.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ15.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ15.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ15.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ15.setItemText(5, _translate("WorkQCont", "Always"))
        self.WorkQ16.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ16.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ16.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ16.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ16.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ16.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ16.setItemText(5, _translate("WorkQCont", "Always"))
        self.WorkQ17.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ17.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ17.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ17.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ17.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ17.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ17.setItemText(5, _translate("WorkQCont", "Always"))
        self.WorkQ18.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ18.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ18.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ18.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ18.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ18.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ18.setItemText(5, _translate("WorkQCont", "Always"))
        self.WorkQ19.setToolTip(_translate("WorkQCont", "Please select from the following"))
        self.WorkQ19.setItemText(0, _translate("WorkQCont", "Never"))
        self.WorkQ19.setItemText(1, _translate("WorkQCont", "Very Rarely"))
        self.WorkQ19.setItemText(2, _translate("WorkQCont", "Rarely"))
        self.WorkQ19.setItemText(3, _translate("WorkQCont", "Sometimes"))
        self.WorkQ19.setItemText(4, _translate("WorkQCont", "Often"))
        self.WorkQ19.setItemText(5, _translate("WorkQCont", "Always"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WorkQCont = QtWidgets.QDialog()
    ui = Ui_WorkQCont()
    ui.setupUi(WorkQCont)
    WorkQCont.show()
    app.exec_()
