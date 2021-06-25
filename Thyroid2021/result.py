# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Thyroid2019\result.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SVM import SVM
from NB import NB
from DT import DT
from NN import NN
from KNN import KNN
from Graphs import graph


class Result(object):

    r1 = 0.0;  
    r2 = 0.0;
    r3 = 0.0;
    r4 = 0.0;
    r5 = 0.0;




    def calc(self):
        r=SVM()
        r=r.accuracy()
        self.svm.setText(str(r) + " %")
        self.progressBar.setProperty("value", 20)
        Result.r1=r
        r=NB()
        r=r.accuracy()
        self.nn.setText(str(r) + " %")
        self.progressBar.setProperty("value", 40)
        Result.r2=r
        r=KNN()
        r=r.accuracy()
        self.knn.setText(str(r) + " %")
        self.progressBar.setProperty("value", 60)
        Result.r3=r
        r=DT()
        
        r=r.accuracy()
        self.knn_2.setText(str(r) + " %")
        self.progressBar.setProperty("value", 80)
        Result.r4=r
        r=NN()
        r=r.accuracy()
        self.knn_3.setText(str(r) + " %")
        self.progressBar.setProperty("value", 100)
        Result.r5=r
        


        
    
    def performance(self):
        l=[Result.r1,Result.r2,Result.r3,Result.r4,Result.r5]
        print("results=",l)
        graph.view(l)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(475, 634)
        Dialog.setStyleSheet("background-color: rgb(164, 185, 255);")
        Dialog.setSizeGripEnabled(False) 
        Dialog.setModal(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 301, 51))
        self.label.setStyleSheet("font: 18pt \"FangSong\";\n"
"")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 540, 430, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 131, 41))
        self.label_2.setStyleSheet("font: 16pt \"Levenim MT\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 151, 41))
        self.label_3.setStyleSheet("font: 16pt \"Levenim MT\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 130, 41))
        self.label_4.setStyleSheet("font: 16pt \"Levenim MT\";")
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(50, 210, 371, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(50, 260, 370, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(50, 310, 370, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.svm = QtWidgets.QLabel(Dialog)
        self.svm.setGeometry(QtCore.QRect(230, 180, 191, 30))
        self.svm.setStyleSheet("font: 12pt \"Levenim MT\";")
        self.svm.setObjectName("svm")
        self.nn = QtWidgets.QLabel(Dialog)
        self.nn.setGeometry(QtCore.QRect(230, 230, 191, 30))
        self.nn.setStyleSheet("font: 12pt \"Levenim MT\";")
        self.nn.setObjectName("nn")
        self.knn = QtWidgets.QLabel(Dialog)
        self.knn.setGeometry(QtCore.QRect(230, 280, 191, 30))
        self.knn.setStyleSheet("font: 12pt \"Levenim MT\";")
        self.knn.setObjectName("knn")
        self.Button1 = QtWidgets.QPushButton(Dialog)
        self.Button1.setGeometry(QtCore.QRect(20, 490, 190, 30))
        self.Button1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Levenim MT\";")
        self.Button1.setObjectName("Button1")
                ######################3
        self.Button1.clicked.connect(self.calc)
        #################

        self.Button2 = QtWidgets.QPushButton(Dialog)
        self.Button2.setGeometry(QtCore.QRect(150, 580, 190, 30))
        self.Button2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Levenim MT\";")
        self.Button2.setObjectName("Button2")
                ######################3
        self.Button2.clicked.connect(self.performance)
        #################

        self.knn_2 = QtWidgets.QLabel(Dialog)
        self.knn_2.setGeometry(QtCore.QRect(230, 330, 191, 30))
        self.knn_2.setStyleSheet("font: 12pt \"Levenim MT\";")
        self.knn_2.setObjectName("knn_2")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(50, 360, 370, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 320, 130, 40))
        self.label_5.setStyleSheet("font: 16pt \"Levenim MT\";")
        self.label_5.setObjectName("label_5")
        self.knn_3 = QtWidgets.QLabel(Dialog)
        self.knn_3.setGeometry(QtCore.QRect(230, 380, 191, 30))
        self.knn_3.setStyleSheet("font: 12pt \"Levenim MT\";")
        self.knn_3.setObjectName("knn_3")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(50, 410, 370, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 370, 130, 40))
        self.label_6.setStyleSheet("font: 16pt \"Levenim MT\";")
        self.label_6.setObjectName("label_6")
        self.knn_4 = QtWidgets.QLabel(Dialog)
        self.knn_4.setGeometry(QtCore.QRect(230, 140, 191, 30))
        self.knn_4.setStyleSheet("font: 12pt \"Levenim MT\";")
        self.knn_4.setObjectName("knn_4")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(50, 170, 370, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 140, 170, 30))
        self.label_7.setStyleSheet("font: 16pt \"Levenim MT\";")
        self.label_7.setObjectName("label_7")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(50, 130, 370, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Classifications</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "SVM"))
        self.label_3.setText(_translate("Dialog", "Naive Bayes"))
        self.label_4.setText(_translate("Dialog", "KNN"))
        self.svm.setText(_translate("Dialog", "Non"))
        self.nn.setText(_translate("Dialog", "Non"))
        self.knn.setText(_translate("Dialog", "Non"))
        self.Button1.setText(_translate("Dialog", "Calculation"))
        self.Button2.setText(_translate("Dialog", "View Graph"))
        self.knn_2.setText(_translate("Dialog", "Non"))
        self.label_5.setText(_translate("Dialog", "DT"))
        self.knn_3.setText(_translate("Dialog", "Non"))
        self.label_6.setText(_translate("Dialog", "NN"))
        self.knn_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#f8f8f8;\">Accuracy</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#f7f2fc;\">Algorithm</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Result()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
