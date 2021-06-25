# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Thyroid2019\home.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from adminloginaction import AdminLoginCheck
from AdminHome import AdminHome
from userhome import UserHome
from signup import Signup
from userloginaction import UserLoginCheck

class Home(object):
    def userlogin(self):
        try:
            print("ulogin")
            uid = self.uid.text()
            upwd = self.upwd.text()
            self.uid.setText("")
            self.upwd.setText("")
            ul = UserLoginCheck()
            res = ul.datacheck(uid, upwd)
            if res:
                self.showAlertBox("Alert", "Fill the Fields")
            elif UserLoginCheck.logincheck(uid, upwd):
                self.u6 = QtWidgets.QDialog()
                self.ui6 = UserHome()
                self.ui6.setupUi(self.u6)
                self.u6.show()
           
                

            else:
                self.showAlertBox("Login Alert", "Login Fail")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


    def signup(self):
    
        try:
            print("signup")
            rname = self.rname.text()
            remail = self.remail.text()
            rph = self.rph.text()
            rpwd = self.rpwd.text()

            Signup.store(remail,rname,rph,rpwd)

            self.remail.setText("")
            self.rpwd.setText("")
            self.rph.setText("")
            self.rname.setText("")
            self.showAlertBox("Registration", "Registration Success")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    

    def adminlogin(self):
        print("adminlogin")
        auidvar = self.aid.text()
        apwdvar = self.apwd.text()
        self.aid.setText("")
        self.apwd.setText("")
        al = AdminLoginCheck()
        res = al.datacheck(auidvar, apwdvar)
        if res:
            self.showAlertBox("Alert", "Fill the Fields")
        elif AdminLoginCheck.logincheck(auidvar, apwdvar):
            self.u = QtWidgets.QMainWindow()
            self.ui = AdminHome()
            self.ui.setupUi(self.u)
            self.u.show()
            

        else:
            self.showAlertBox("Login Alert", "Login Fail")        
            
    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 585)
        Dialog.setStyleSheet("background-color: rgb(183,163,210);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 721, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(40, 30, 641, 331))
        self.tableView.setStyleSheet("border-image: url(thyroid.jpg);")
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(270, 110, 191, 61))
        self.label.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.label.setObjectName("label")
        self.aid = QtWidgets.QLineEdit(self.tab_2)
        self.aid.setGeometry(QtCore.QRect(220, 180, 290, 40))
        self.aid.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.aid.setText("")
        self.aid.setObjectName("aid")
        self.apwd = QtWidgets.QLineEdit(self.tab_2)
        self.apwd.setGeometry(QtCore.QRect(220, 230, 290, 40))
        self.apwd.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.apwd.setText("")
        self.apwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.apwd.setObjectName("apwd")
        self.alogin = QtWidgets.QPushButton(self.tab_2)
        self.alogin.setGeometry(QtCore.QRect(220, 280, 120, 40))
        self.alogin.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.alogin.setObjectName("alogin")
        self.alogin.clicked.connect(self.adminlogin)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.ulogin = QtWidgets.QPushButton(self.tab_3)
        self.ulogin.setGeometry(QtCore.QRect(220, 280, 120, 40))
        self.ulogin.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.ulogin.setObjectName("ulogin")
        self.ulogin.clicked.connect(self.userlogin)


       



        self.uid = QtWidgets.QLineEdit(self.tab_3)
        self.uid.setGeometry(QtCore.QRect(220, 180, 290, 40))
        self.uid.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.uid.setText("")

        self.uid.setObjectName("uid")
        self.upwd = QtWidgets.QLineEdit(self.tab_3)
        self.upwd.setGeometry(QtCore.QRect(220, 230, 290, 40))
        self.upwd.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.upwd.setText("")
        self.upwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.upwd.setObjectName("upwd")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(270, 110, 191, 61))
        self.label_3.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_4 = QtWidgets.QLabel(self.tab_7)
        self.label_4.setGeometry(QtCore.QRect(260, 110, 221, 61))
        self.label_4.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.label_4.setObjectName("label_4")
        self.ulogin_2 = QtWidgets.QPushButton(self.tab_7)
        self.ulogin_2.setGeometry(QtCore.QRect(220, 380, 120, 40))
        self.ulogin_2.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.ulogin_2.setObjectName("ulogin_2")

        
        self.ulogin_2.clicked.connect(self.signup)

        self.remail = QtWidgets.QLineEdit(self.tab_7)
        self.remail.setGeometry(QtCore.QRect(220, 280, 290, 40))
        self.remail.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.remail.setText("")
        self.remail.setObjectName("remail")
        self.rpwd = QtWidgets.QLineEdit(self.tab_7)
        self.rpwd.setGeometry(QtCore.QRect(220, 330, 290, 40))
        self.rpwd.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.rpwd.setText("")
        self.rpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rpwd.setObjectName("rpwd")
        self.rname = QtWidgets.QLineEdit(self.tab_7)
        self.rname.setGeometry(QtCore.QRect(220, 180, 290, 40))
        self.rname.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.rname.setText("")
        self.rname.setObjectName("rname")
        self.rph = QtWidgets.QLineEdit(self.tab_7)
        self.rph.setGeometry(QtCore.QRect(220, 230, 290, 40))
        self.rph.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.rph.setText("")
        self.rph.setObjectName("rph")
        self.tabWidget.addTab(self.tab_7, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Admin Login</span></p></body></html>"))
        self.aid.setPlaceholderText(_translate("Dialog", "Enter Login ID"))
        self.apwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.alogin.setText(_translate("Dialog", "Login"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Admin"))
        self.ulogin.setText(_translate("Dialog", "Login"))
        self.uid.setPlaceholderText(_translate("Dialog", "Enter Email ID"))
        self.upwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">User Login</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "User"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">User Registration</span></p></body></html>"))
        self.ulogin_2.setText(_translate("Dialog", "Register"))
        self.remail.setPlaceholderText(_translate("Dialog", "Enter Email ID"))
        self.rpwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.rname.setPlaceholderText(_translate("Dialog", "Enter Name"))
        self.rph.setPlaceholderText(_translate("Dialog", "Enter Contact"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog", "User Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
