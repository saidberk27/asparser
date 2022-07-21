# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dortluyap.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import functions as fonksiyon
import yukleniyor as yukleniyorPencere




class Ui_DortluYap(object):
    def yukleniyorAc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = yukleniyorPencere.Ui_YukleniyorPencere()
        self.ui.setupUi(self.window)
        self.window.show()

    def yukleniyorKapa(self):
        self.window.hide()

    def setupUi(self, DortluYap):
        DortluYap.setObjectName("DortluYap")
        DortluYap.resize(681, 444)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DortluYap.sizePolicy().hasHeightForWidth())
        DortluYap.setSizePolicy(sizePolicy)
        DortluYap.setMinimumSize(QtCore.QSize(681, 444))
        DortluYap.setMaximumSize(QtCore.QSize(681, 444))
        self.centralwidget = QtWidgets.QWidget(DortluYap)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 602, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.yatayBoslukText = QtWidgets.QLabel(self.gridLayoutWidget)
        self.yatayBoslukText.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.yatayBoslukText.setFont(font)
        self.yatayBoslukText.setAlignment(QtCore.Qt.AlignCenter)
        self.yatayBoslukText.setObjectName("yatayBoslukText")
        self.gridLayout.addWidget(self.yatayBoslukText, 1, 0, 1, 1)
        self.dikeyBoslukText = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dikeyBoslukText.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dikeyBoslukText.setFont(font)
        self.dikeyBoslukText.setAlignment(QtCore.Qt.AlignCenter)
        self.dikeyBoslukText.setObjectName("dikeyBoslukText")
        self.gridLayout.addWidget(self.dikeyBoslukText, 0, 0, 1, 1)
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
        self.yatayBoslukLine.setAlignment(QtCore.Qt.AlignCenter)
        self.yatayBoslukLine.setObjectName("yatayBoslukLine")
        self.gridLayout.addWidget(self.yatayBoslukLine, 1, 1, 1, 1)
        self.dikeyBosukLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dikeyBosukLine.sizePolicy().hasHeightForWidth())
        self.dikeyBosukLine.setSizePolicy(sizePolicy)
        self.dikeyBosukLine.setMinimumSize(QtCore.QSize(400, 100))
        self.dikeyBosukLine.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dikeyBosukLine.setFont(font)
        self.dikeyBosukLine.setAlignment(QtCore.Qt.AlignCenter)
        self.dikeyBosukLine.setObjectName("dikeyBosukLine")
        self.gridLayout.addWidget(self.dikeyBosukLine, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        DortluYap.setCentralWidget(self.centralwidget)

        self.retranslateUi(DortluYap)
        QtCore.QMetaObject.connectSlotsByName(DortluYap)

    def retranslateUi(self, DortluYap):
        _translate = QtCore.QCoreApplication.translate
        DortluYap.setWindowTitle(_translate("DortluYap", "Dörtlü Yap"))
        self.yatayBoslukText.setText(_translate("DortluYap", "YATAY BOSLUK:"))
        self.dikeyBoslukText.setText(_translate("DortluYap", "DIKEY BOSLUK:"))
        self.yatayBoslukLine.setPlaceholderText(_translate("DortluYap", "LUTFEN SADECE RAKAM OLARAK GIRINIZ"))
        self.dikeyBosukLine.setPlaceholderText(_translate("DortluYap", "LUTFEN SADECE RAKAM OLARAK GIRINIZ"))
        self.pushButton.setText(_translate("DortluYap", "DÖRTLÜ YAP"))

        self.pushButton.clicked.connect(self.tiklandi)

    def tiklandi(self):
        self.yukleniyorAc()
        yatayBoslukInput = int(self.yatayBoslukLine.text())
        dikeyBoslukInput = int(self.dikeyBosukLine.text())

        fonksiyon.dortluYap(dikeyBoslukInput,yatayBoslukInput)
        self.yukleniyorKapa()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DortluYap = QtWidgets.QMainWindow()
    ui = Ui_DortluYap()
    ui.setupUi(DortluYap)
    DortluYap.show()
    sys.exit(app.exec_())
