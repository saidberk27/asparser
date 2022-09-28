# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ikiliyap.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import functions as fonksiyon
import yukleniyor as yukleniyorPencere


class Ui_IkiliYap(object):
    def __init__(self, sizeData):
        self.sizeData = sizeData
        print(sizeData)

    def yukleniyorAc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = yukleniyorPencere.Ui_YukleniyorPencere()
        self.ui.setupUi(self.window)
        self.window.show()

    def yukleniyorKapa(self):
        self.window.hide()

    def setupUi(self, IkiliYap):
        IkiliYap.setObjectName("IkiliYap")
        IkiliYap.resize(681, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IkiliYap.sizePolicy().hasHeightForWidth())
        IkiliYap.setSizePolicy(sizePolicy)
        IkiliYap.setMinimumSize(QtCore.QSize(681, 400))
        IkiliYap.setMaximumSize(QtCore.QSize(681, 400))
        IkiliYap.setStyleSheet("background-color: rgb(255, 255, 255);border:0;")
        self.centralwidget = QtWidgets.QWidget(IkiliYap)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 602, 408))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.yatayBoslukText = QtWidgets.QLabel(self.gridLayoutWidget)
        self.yatayBoslukText.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.yatayBoslukText.setFont(font)
        self.yatayBoslukText.setStyleSheet("color: rgb(4, 155, 224);")
        self.yatayBoslukText.setAlignment(QtCore.Qt.AlignCenter)
        self.yatayBoslukText.setObjectName("yatayBoslukText")
        self.gridLayout.addWidget(self.yatayBoslukText, 0, 0, 1, 1)
        self.yatayBoslukLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yatayBoslukLine.sizePolicy().hasHeightForWidth())
        self.yatayBoslukLine.setSizePolicy(sizePolicy)
        self.yatayBoslukLine.setMinimumSize(QtCore.QSize(400, 100))
        self.yatayBoslukLine.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yatayBoslukLine.setFont(font)
        self.yatayBoslukLine.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.yatayBoslukLine.setAlignment(QtCore.Qt.AlignCenter)
        self.yatayBoslukLine.setObjectName("yatayBoslukLine")
        self.gridLayout.addWidget(self.yatayBoslukLine, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 200))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"color: rgb(4, 155, 224);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid;\n"
"border-color:#049BE0;\n"
"border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(4, 155, 224);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(62, 198, 247);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(4, 155, 224);")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        IkiliYap.setCentralWidget(self.centralwidget)

        self.retranslateUi(IkiliYap)
        QtCore.QMetaObject.connectSlotsByName(IkiliYap)

        self.pushButton.clicked.connect(self.tiklandi)

    def tiklandi(self):
        self.yukleniyorAc()
        yatayBoslukInput = int(self.yatayBoslukLine.text())

        if(self.checkBox.isChecked()):
            fonksiyon.ikiliYap(yatayBoslukInput, self.sizeData,isSample=True)
        else:
            fonksiyon.ikiliYap(yatayBoslukInput, self.sizeData,isSample=False)

        self.yukleniyorKapa()

    def retranslateUi(self, IkiliYap):
        _translate = QtCore.QCoreApplication.translate
        IkiliYap.setWindowTitle(_translate("IkiliYap", "İKİLİ YAP"))
        self.yatayBoslukText.setText(_translate("IkiliYap", "YATAY BOSLUK:"))
        self.yatayBoslukLine.setPlaceholderText(_translate("IkiliYap", "LUTFEN SADECE RAKAM OLARAK GIRINIZ"))
        self.pushButton.setText(_translate("IkiliYap", "İKİLİ YAP"))
        self.checkBox.setText(_translate("IkiliYap", "SAMPLE MOD"))
