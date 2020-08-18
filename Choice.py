# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Choice.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QLineEdit, QFormLayout, QVBoxLayout, QDialogButtonBox , QFileDialog
import pymysql
from collections import Counter 

#f = open("Main.txt","r")  #this is used to open up the file where the database settings are kept

#dbname = str(f.readline())
#dbname =  dbname.replace('\n','' )
#userDB = str(f.readline())
#userDB =  userB.replace('\n','' )
#passDB =  str(f.readline())                     
#passDB =  passDB.replace('\n','' )
#address = str(f.readline())D
#address = address.replace('\n','' )

class Ui_Status(object):

    def __init__(self,email,birth,edu,lead,workyears,contracting,feedback,present,pointsself,pointsother,trust,confidentiatly,awareness,perspectives,listening,creative,delegation,actions,reflection,selfaware):

        self.email = email
        self.birth = birth
        self.edu = edu             
        self.lead = lead
        self.workyears = workyears


        self.contracting = contracting
        self.feedback = feedback
        self.present= present
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


    def setupUi(self, Status):
        Status.setObjectName("Status")
        Status.resize(564, 353)
        Status.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.label = QtWidgets.QLabel(Status)
        self.label.setGeometry(QtCore.QRect(150, 20, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.TopL = QtWidgets.QLabel(Status)
        self.TopL.setGeometry(QtCore.QRect(150, 190, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TopL.setFont(font)
        self.TopL.setObjectName("TopL")
        self.SecondL = QtWidgets.QLabel(Status)
        self.SecondL.setGeometry(QtCore.QRect(150, 220, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SecondL.setFont(font)
        self.SecondL.setObjectName("SecondL")
        self.ThirdL = QtWidgets.QLabel(Status)
        self.ThirdL.setGeometry(QtCore.QRect(150, 250, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ThirdL.setFont(font)
        self.ThirdL.setObjectName("ThirdL")
        self.Fourth = QtWidgets.QLabel(Status)
        self.Fourth.setGeometry(QtCore.QRect(150, 280, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Fourth.setFont(font)
        self.Fourth.setObjectName("Fourth")
        self.FiveL = QtWidgets.QLabel(Status)
        self.FiveL.setGeometry(QtCore.QRect(150, 310, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FiveL.setFont(font)
        self.FiveL.setObjectName("FiveL")

        self.retranslateUi(Status)
        QtCore.QMetaObject.connectSlotsByName(Status)
        self.insert()

    def insert(self):

        self.total = self.contracting + self.feedback + self.present + self.pointsself + self.pointsother + self.trust + self.confidentiatly + self.awareness + self.perspectives + self.listening + self.creative + self.delegation + self.actions + self.reflection + self.selfaware


        ContractingPercentage = (self.contracting / 375) * 100
        FeedbackPercentage = (self.feedback / 365) * 100
        PresentPercentage = (self.present / 385) * 100
        pointsselfPercentage = (self.pointsself / 315) * 100
        pointsotherPercentage = (self.pointsother / 295) * 100
        trustPercentage = (self.trust / 510) * 100
        confidentiatlyPercentage = (self.confidentiatly / 210) * 100
        AwarePercentage = (self.awareness / 390) * 100
        perspectivesPercentage = (self.perspectives / 405) * 100
        listeningPercentage = (self.listening / 425) * 100
        creativePercentage = (self.creative / 435) * 100
        delegationPercentage = (self.delegation / 285) * 100
        actionsPercentage = (self.actions / 280) * 100
        reflectionPercentage = (self.reflection / 240) * 100
        selfawarePercentage = (self.selfaware / 365) * 100


        my_dict = {"Contracting":ContractingPercentage,"Giving Feedback":FeedbackPercentage,
                    "Being Present":PresentPercentage,"Pause Points-Self":pointsselfPercentage,
                    "Pause Points-Other":pointsotherPercentage,"Building Trust and Rapport":trustPercentage,
                    "Confidentiality":confidentiatlyPercentage,"Creating Awareness":AwarePercentage,
                    "Changing Perspectives":perspectivesPercentage,"Generative Listening":listeningPercentage,
                    "Creative Questions":creativePercentage,"Delegation":delegationPercentage,
                    "Creating Actions":actionsPercentage,"Reflection":reflectionPercentage,
                    "Self Awareness":selfawarePercentage}

        k = Counter(my_dict)

        high = k.most_common(5)


        print("Top 5")
        print("Name : Value")
        top5 =[]
        for i in high:
            print(i[0]," : ",i[1],"\n")
            top5 += [i[0]]

            
        print(top5)
        Top = top5[0]
        Second = top5[1]
        Third = top5[2]
        Fourths = top5[3]
        Fifth = top5[4]


        self.TopL.setText("<html><head/><body><p align=\"center\">" + Top + "</p><p align=\"center\"></body></html>")
        self.SecondL.setText("<html><head/><body><p align=\"center\">" + Second + "</p><p align=\"center\"></body></html>")
        self.ThirdL.setText("<html><head/><body><p align=\"center\">" + Third + "</p><p align=\"center\"></body></html>")
        self.Fourth.setText("<html><head/><body><p align=\"center\">" + Fourths + "</p><p align=\"center\"></body></html>")
        self.FiveL.setText("<html><head/><body><p align=\"center\">" + Fifth + "</p><p align=\"center\"></body></html>")

        #try:

        #        conn = pymysql.connect(host = address,		
        #                        user = userDB,		
        #                        passwd = passDB,		
        #                        db = dbname)			
           
        #        myCursor = conn.cursor()		
        #        query =("INSERT INTO demographic(Email_Address,Country_Of_Birth,Education,Team_Lead,Years_In_Work) VALUES (%s,%s,%s,%s,%s)")		#SQL to add
        #        data = myCursor.execute(query,(self.email,self.birth,self.edu,self.lead,self.workyears))		#values to add into DB,%s
                
          
        #        questionquery =("INSERT INTO questions(Contracting,Giving_Feedback,Being_Present,Pause_Points_Self,Pause_Points_Other,Building_Trust_&_Rapport,Confidentiality,Creating_Awareness,Changing_Perspectives,Generative_Listening,Creative_Questions,Delegation,Creating_Actions,Reflection,Self_Awareness,Total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,$s)")		#SQL to add
        #        dataQuestions = myCursor.execute(questionquery,(self.contracting,self.feedback,self.present,self.pointsself,self.pointsother,self.trust,self.confidentiatly,self.awareness,self.perspectives, self.listening, self.creative,self.delegation,self.actions,self.reflection,self.selfaware,self.total))		#values to add into DB,%s


        #        conn.commit()
        #        conn.close()

        #except:
        #    self.messagebox("Error","Please check the Database connection"); #the try catch statment will display this if DB cannot connect

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)                          
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_() 

    def retranslateUi(self, Status):
        _translate = QtCore.QCoreApplication.translate
        Status.setWindowTitle(_translate("Status", "COTG"))
        self.label.setText(_translate("Status", "<html><head/><body><p align=\"center\">Thank you for your time</p><p align=\"center\"><br/></p><p align=\"center\">You should take :</p></body></html>"))
        self.TopL.setText(_translate("Status", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SecondL.setText(_translate("Status", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ThirdL.setText(_translate("Status", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Fourth.setText(_translate("Status", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.FiveL.setText(_translate("Status", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Status = QtWidgets.QDialog()
    ui = Ui_Status()
    ui.setupUi(Status)
    Status.show()
    app.exec_()
