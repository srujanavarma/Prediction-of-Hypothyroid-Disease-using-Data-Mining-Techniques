 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Thyroid2019\admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from feature import featureselection
from result import Result

class AdminHome(object):

    def browsefile(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File",
                                                                "E://",
                                                                "*.csv")
            print(fileName)
            self.file.setText(fileName)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)
    
    def featurecalc(self):
        featureselection.calc(self.file.text())

    def classificationqt(self):
            self.su = QtWidgets.QDialog()
            self.sui = Result()
            self.sui.setupUi(self.su)
            self.su.show()

    	        


    def setupUi(self, box):
        box.setObjectName("box")
        box.resize(694, 559)
        box.setStyleSheet("background-color: rgb(117, 141, 179);")
        self.centralwidget = QtWidgets.QWidget(box)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 701, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.label = QtWidgets.QLabel(self.Home)
        self.label.setGeometry(QtCore.QRect(70, 30, 551, 71))
        self.label.setStyleSheet("font: 95 16pt \"Modern\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Home)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 291, 41))
        self.label_2.setStyleSheet("font: 14pt \"FangSong\";\n"
"color: rgb(226, 226, 226);")
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.Home, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 551, 71))
        self.label_3.setStyleSheet("font: 95 16pt \"Modern\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setObjectName("label_3")
        self.file = QtWidgets.QLineEdit(self.tab_2)
        self.file.setGeometry(QtCore.QRect(150, 210, 330, 30))
        self.file.setObjectName("file")

        self.browse = QtWidgets.QToolButton(self.tab_2)
        self.browse.setGeometry(QtCore.QRect(490, 210, 40, 30))
        self.browse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse.setObjectName("browse")
                ######################3
        self.browse.clicked.connect(self.browsefile)
        #################

        self.feature = QtWidgets.QPushButton(self.tab_2)
        self.feature.setGeometry(QtCore.QRect(150, 260, 380, 30))
        self.feature.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.feature.setObjectName("feature")
        ######################3
        self.feature.clicked.connect(self.featurecalc)
        #################

        self.algo = QtWidgets.QPushButton(self.tab_2)
        self.algo.setGeometry(QtCore.QRect(150, 300, 380, 30))
        self.algo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.algo.setObjectName("algo")
            ######################3
        self.algo.clicked.connect(self.classificationqt)
        #################

        self.tabWidget.addTab(self.tab_2, "")
        box.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(box)
        self.statusbar.setObjectName("statusbar")
        box.setStatusBar(self.statusbar)

        self.retranslateUi(box)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(box)

    def retranslateUi(self, box):
        _translate = QtCore.QCoreApplication.translate
        box.setWindowTitle(_translate("box", "MainWindow"))
        self.label.setText(_translate("box", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Prediction of hypothyroid Disease Using Data Mining Techniques</span></p></body></html>"))
        self.label_2.setText(_translate("box", "Welcome Admin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("box", "Home"))
        self.label_3.setText(_translate("box", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Prediction of hypothyroid Disease Using Data Mining Techniques</span></p></body></html>"))
        self.browse.setText(_translate("box", "..."))
        self.feature.setText(_translate("box", "Feature Selection"))
        self.algo.setText(_translate("box", "Classifications"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("box", "Classification"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    box = QtWidgets.QMainWindow()
    ui = AdminHome()
    ui.setupUi(box)
    box.show()
    sys.exit(app.exec_())
