
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import functions as fonksiyon
import yukleniyor as yukleniyorPencere
import dortluyap as dortluyap
import ikiliyap as ikiliyap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 975)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(630, 975))
        MainWindow.setMaximumSize(QtCore.QSize(630, 975))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);border:0;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 621, 930))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.ulke_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ulke_label.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ulke_label.setFont(font)
        self.ulke_label.setStyleSheet("color: rgb(4, 155, 224);")
        self.ulke_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ulke_label.setObjectName("ulke_label")
        self.gridLayout.addWidget(self.ulke_label, 1, 0, 1, 1)
        self.sa_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sa_line.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sa_line.setFont(font)
        self.sa_line.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.sa_line.setAlignment(QtCore.Qt.AlignCenter)
        self.sa_line.setObjectName("sa_line")
        self.gridLayout.addWidget(self.sa_line, 13, 2, 1, 1)
        self.parti_eleman_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.parti_eleman_label.setFont(font)
        self.parti_eleman_label.setStyleSheet("color: rgb(4, 155, 224);")
        self.parti_eleman_label.setAlignment(QtCore.Qt.AlignCenter)
        self.parti_eleman_label.setObjectName("parti_eleman_label")
        self.gridLayout.addWidget(self.parti_eleman_label, 11, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
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
        self.gridLayout.addWidget(self.pushButton, 14, 2, 1, 1)
        self.lot_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lot_label.setFont(font)
        self.lot_label.setStyleSheet("color: rgb(4, 155, 224);")
        self.lot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lot_label.setObjectName("lot_label")
        self.gridLayout.addWidget(self.lot_label, 9, 0, 1, 1)
        self.sinif_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sinif_label.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sinif_label.setFont(font)
        self.sinif_label.setStyleSheet("color: rgb(4, 155, 224);")
        self.sinif_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sinif_label.setObjectName("sinif_label")
        self.gridLayout.addWidget(self.sinif_label, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 12, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 16, 2, 1, 1)
        self.logo = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(240, 100))
        self.logo.setMaximumSize(QtCore.QSize(240, 100))
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setAcceptDrops(False)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setStyleSheet("color: rgb(4, 155, 224);")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 14, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.size_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.size_line.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.size_line.setFont(font)
        self.size_line.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.size_line.setText("")
        self.size_line.setAlignment(QtCore.Qt.AlignCenter)
        self.size_line.setObjectName("size_line")
        self.gridLayout.addWidget(self.size_line, 7, 2, 1, 1)
        self.parti_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.parti_line.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parti_line.setFont(font)
        self.parti_line.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.parti_line.setText("")
        self.parti_line.setAlignment(QtCore.Qt.AlignCenter)
        self.parti_line.setObjectName("parti_line")
        self.gridLayout.addWidget(self.parti_line, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 16, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 1)
        self.size_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.size_label.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.size_label.setFont(font)
        self.size_label.setStyleSheet("color: rgb(4, 155, 224);")
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setObjectName("size_label")
        self.gridLayout.addWidget(self.size_label, 7, 0, 1, 1)
        self.sa_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sa_label.setFont(font)
        self.sa_label.setStyleSheet("color: rgb(4, 155, 224);")
        self.sa_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sa_label.setObjectName("sa_label")
        self.gridLayout.addWidget(self.sa_label, 13, 0, 1, 1)
        self.ulke_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ulke_line.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ulke_line.setFont(font)
        self.ulke_line.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.ulke_line.setText("")
        self.ulke_line.setAlignment(QtCore.Qt.AlignCenter)
        self.ulke_line.setObjectName("ulke_line")
        self.gridLayout.addWidget(self.ulke_line, 1, 2, 1, 1)
        self.parti_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parti_label.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parti_label.setFont(font)
        self.parti_label.setStyleSheet("color: rgb(4, 155, 224);")
        self.parti_label.setAlignment(QtCore.Qt.AlignCenter)
        self.parti_label.setObjectName("parti_label")
        self.gridLayout.addWidget(self.parti_label, 3, 0, 1, 1)
        self.lot_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lot_line.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lot_line.setFont(font)
        self.lot_line.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.lot_line.setAlignment(QtCore.Qt.AlignCenter)
        self.lot_line.setObjectName("lot_line")
        self.gridLayout.addWidget(self.lot_line, 9, 2, 1, 1)
        self.parti_eleman_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.parti_eleman_line.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parti_eleman_line.setFont(font)
        self.parti_eleman_line.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.parti_eleman_line.setAlignment(QtCore.Qt.AlignCenter)
        self.parti_eleman_line.setObjectName("parti_eleman_line")
        self.gridLayout.addWidget(self.parti_eleman_line, 11, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 10, 0, 1, 1)
        self.sinif_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sinif_line.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sinif_line.setFont(font)
        self.sinif_line.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.sinif_line.setText("")
        self.sinif_line.setAlignment(QtCore.Qt.AlignCenter)
        self.sinif_line.setObjectName("sinif_line")
        self.gridLayout.addWidget(self.sinif_line, 5, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 14, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 630, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_lot = QtWidgets.QMenu(self.menuBar)
        self.menu_lot.setObjectName("menu_lot")
        self.menu_coklu = QtWidgets.QMenu(self.menuBar)
        self.menu_coklu.setObjectName("menu_coklu")
        MainWindow.setMenuBar(self.menuBar)
        self.menu_ikili = QtWidgets.QAction(MainWindow)
        self.menu_ikili.setObjectName("menu_ikili")
        self.menu_dortlu = QtWidgets.QAction(MainWindow)
        self.menu_dortlu.setObjectName("menu_dortlu")
        self.menu_altili = QtWidgets.QAction(MainWindow)
        self.menu_altili.setObjectName("menu_altili")
        self.menu_sekizli = QtWidgets.QAction(MainWindow)
        self.menu_sekizli.setObjectName("menu_sekizli")
        self.menu_coklu.addAction(self.menu_ikili)
        self.menu_coklu.addSeparator()
        self.menu_coklu.addAction(self.menu_dortlu)
        self.menu_coklu.addSeparator()
        self.menu_coklu.addAction(self.menu_altili)
        self.menu_coklu.addSeparator()
        self.menu_coklu.addAction(self.menu_sekizli)
        self.menuBar.addAction(self.menu_lot.menuAction())
        self.menuBar.addAction(self.menu_coklu.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pixmap = QPixmap('logo.jpg')
        self.menu_dortlu.triggered.connect(self.dortluMenuAc)
        self.menu_ikili.triggered.connect(self.ikiliMenuAc)
        self.menu_lot.triggered.connect(self.lotMenuAc)
        self.pushButton.clicked.connect(self.tiklandi)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ASPARSER"))
        self.ulke_label.setText(_translate("MainWindow", "ÜLKE KODU:"))
        self.sa_line.setPlaceholderText(_translate("MainWindow", "S/A"))
        self.parti_eleman_label.setText(_translate("MainWindow", "PARTI ELEMAN SAYISI:"))
        self.pushButton.setText(_translate("MainWindow", "Belge Oluştur"))
        self.lot_label.setText(_translate("MainWindow", "LOT NUMARASI:"))
        self.sinif_label.setText(_translate("MainWindow", "SINIF NUMARASI:"))
        self.label_3.setText(_translate("MainWindow", "ASPAR ENERJI ICIN GELISTIRILMISTIR."))
        self.logo.setText(_translate("MainWindow", "Logo"))
        self.checkBox.setText(_translate("MainWindow", "SAMPLE MOD"))
        self.size_line.setPlaceholderText(_translate("MainWindow", "8,9,10,11,12"))
        self.parti_line.setPlaceholderText(_translate("MainWindow", "1,2,3 ... 999"))
        self.label_2.setText(_translate("MainWindow", "C.SAİD BERK © TARAFINDAN"))
        self.size_label.setText(_translate("MainWindow", "SIZE:"))
        self.sa_label.setText(_translate("MainWindow", "STANDART/ARC"))
        self.ulke_line.setPlaceholderText(_translate("MainWindow", "TR,UK,GE ..."))
        self.parti_label.setText(_translate("MainWindow", "PARTİ NUMARASI:"))
        self.parti_eleman_line.setPlaceholderText(_translate("MainWindow", "1,2,3 ... 999"))
        self.sinif_line.setPlaceholderText(_translate("MainWindow", "00,0,4"))
        self.menu_lot.setTitle(_translate("MainWindow", "Lot Numarası Oluştur"))
        self.menu_coklu.setTitle(_translate("MainWindow", "Çoklu Belge Oluştur"))
        self.menu_ikili.setText(_translate("MainWindow", "İkili Belge Oluştur"))
        self.menu_dortlu.setText(_translate("MainWindow", "Dörtlü Belge Oluştur"))
        self.menu_altili.setText(_translate("MainWindow", "Altılı Belge Oluştur"))
        self.menu_sekizli.setText(_translate("MainWindow", "Sekizli Belge Oluştur"))

        self.logo.setPixmap(self.pixmap)

    def lotMenuAc(self):
        print("lot")

    def dortluMenuAc(self):
        print("Dortlu Menu Tiklandi")
        self.window = QtWidgets.QMainWindow()
        self.ui = dortluyap.Ui_DortluYap()
        self.ui.setupUi(self.window)
        self.window.show()

    def ikiliMenuAc(self):
        sizeInput = self.size_line.text()

        print("İkili Menu Tiklandi")
        self.window = QtWidgets.QMainWindow()
        self.ui = ikiliyap.Ui_IkiliYap(sizeInput)
        self.ui.setupUi(self.window)
        self.window.show()

    def tiklandi(self):
        self.yukleniyorAc()
        print("Tiklandi")

        ulkeInput = self.ulke_line.text()
        partiInput = self.parti_line.text()
        sinifInput = self.sinif_line.text()
        sizeInput = self.size_line.text()
        lotInput = self.lot_line.text()
        partiElemanInput = int(self.parti_eleman_line.text())
        saInput = self.sa_line.text()  # sa = Standart/Arc

        isSample = False
        if (self.checkBox.isChecked()):
            isSample = True

        fonksiyon.seriNoOlustur(ulkeInput, partiInput, sinifInput, partiElemanInput, sizeInput, saInput)
        fonksiyon.qrCodeOlustur(sinifInput, saInput, isSample)
        fonksiyon.qrCodeEkle(saInput)
        fonksiyon.yaziResimBirlesme(sinifInput, sizeInput, lotInput, saInput)

        if(self.checkBox.isChecked()):
            fonksiyon.sampleMod()

        self.yukleniyorKapa()

    def yukleniyorAc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = yukleniyorPencere.Ui_YukleniyorPencere()
        self.ui.setupUi(self.window)
        self.window.show()

    def yukleniyorKapa(self):
        self.window.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
