from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.resize(380, 485)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(380, 485))
        mainWindow.setMaximumSize(QtCore.QSize(380, 485))
        mainWindow.setBaseSize(QtCore.QSize(0, 0))
        mainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        mainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(380, 480))
        self.centralwidget.setStyleSheet("font: 15pt \"Century Gothic\";")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 381, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet("background-color: rgb(66, 66, 99);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 361, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 2, 0, 2)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.b8 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("8"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b8.sizePolicy().hasHeightForWidth())
        self.b8.setSizePolicy(sizePolicy)
        self.b8.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b8.setObjectName("b8")
        self.gridLayout.addWidget(self.b8, 4, 3, 1, 1)
        self.b1 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("1"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b1.sizePolicy().hasHeightForWidth())
        self.b1.setSizePolicy(sizePolicy)
        self.b1.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 2, 2, 1, 1)
        self.b7 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("7"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b7.sizePolicy().hasHeightForWidth())
        self.b7.setSizePolicy(sizePolicy)
        self.b7.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b7.setObjectName("b7")
        self.gridLayout.addWidget(self.b7, 4, 2, 1, 1)
        self.b5 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("5"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b5.sizePolicy().hasHeightForWidth())
        self.b5.setSizePolicy(sizePolicy)
        self.b5.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b5.setObjectName("b5")
        self.gridLayout.addWidget(self.b5, 3, 3, 1, 1)
        self.btnLimp = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("Lm"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnLimp.sizePolicy().hasHeightForWidth())
        self.btnLimp.setSizePolicy(sizePolicy)
        self.btnLimp.setStyleSheet("QPushButton{\n"
"     \n"
"    background-color: rgb(47, 47, 70);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:  rgb(47, 47, 70);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.btnLimp.setObjectName("btnLimp")
        self.gridLayout.addWidget(self.btnLimp, 1, 2, 1, 2)
        self.btnDivi = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("/"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnDivi.sizePolicy().hasHeightForWidth())
        self.btnDivi.setSizePolicy(sizePolicy)
        self.btnDivi.setStyleSheet("QPushButton{\n"
"     \n"
"    background-color: rgb(255, 194, 250);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:  rgb(255, 194, 250);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.btnDivi.setObjectName("btnDivi")
        self.gridLayout.addWidget(self.btnDivi, 4, 5, 1, 1)
        self.b3 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("3"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b3.sizePolicy().hasHeightForWidth())
        self.b3.setSizePolicy(sizePolicy)
        self.b3.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b3.setObjectName("b3")
        self.gridLayout.addWidget(self.b3, 2, 4, 1, 1)
        self.b2 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("2"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b2.sizePolicy().hasHeightForWidth())
        self.b2.setSizePolicy(sizePolicy)
        self.b2.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 2, 3, 1, 1)
        self.b6 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.Apertar("6"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b6.sizePolicy().hasHeightForWidth())
        self.b6.setSizePolicy(sizePolicy)
        self.b6.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b6.setObjectName("b6")
        self.gridLayout.addWidget(self.b6, 3, 4, 1, 1)
        self.btnMenos = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("-"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnMenos.sizePolicy().hasHeightForWidth())
        self.btnMenos.setSizePolicy(sizePolicy)
        self.btnMenos.setStyleSheet("QPushButton{\n"
"     \n"
"    background-color: rgb(255, 194, 250);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:  rgb(255, 194, 250);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.btnMenos.setObjectName("btnMenos")
        self.gridLayout.addWidget(self.btnMenos, 2, 5, 1, 1)
        self.btnApag = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.apagar())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnApag.sizePolicy().hasHeightForWidth())
        self.btnApag.setSizePolicy(sizePolicy)
        self.btnApag.setStyleSheet("QPushButton{\n"
"     \n"
"    background-color: rgb(47, 47, 70);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:  rgb(47, 47, 70);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.btnApag.setObjectName("btnApag")
        self.gridLayout.addWidget(self.btnApag, 1, 4, 1, 1)
        self.b4 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda:self.Apertar("4"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b4.sizePolicy().hasHeightForWidth())
        self.b4.setSizePolicy(sizePolicy)
        self.b4.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b4.setObjectName("b4")
        self.gridLayout.addWidget(self.b4, 3, 2, 1, 1)
        self.btnPonto = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.ponto())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnPonto.sizePolicy().hasHeightForWidth())
        self.btnPonto.setSizePolicy(sizePolicy)
        self.btnPonto.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.btnPonto.setObjectName("btnPonto")
        self.gridLayout.addWidget(self.btnPonto, 5, 4, 1, 1)
        self.b0 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.Apertar("0"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b0.sizePolicy().hasHeightForWidth())
        self.b0.setSizePolicy(sizePolicy)
        self.b0.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b0.setObjectName("b0")
        self.gridLayout.addWidget(self.b0, 5, 2, 1, 2)
        self.b9 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.Apertar("9"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.b9.sizePolicy().hasHeightForWidth())
        self.b9.setSizePolicy(sizePolicy)
        self.b9.setStyleSheet("QPushButton{\n"
"     background-color: rgb(172, 172, 172);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:rgb(172, 172, 172);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.b9.setObjectName("b9")
        self.gridLayout.addWidget(self.b9, 4, 4, 1, 1)
        self.btnIgual = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.igual())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnIgual.sizePolicy().hasHeightForWidth())
        self.btnIgual.setSizePolicy(sizePolicy)
        self.btnIgual.setStyleSheet("QPushButton{\n"
"     \n"
"    background-color: rgb(255, 194, 250);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:  rgb(255, 194, 250);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.btnIgual.setObjectName("btnIgual")
        self.gridLayout.addWidget(self.btnIgual, 5, 5, 1, 1)
        self.btnMult = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.Apertar("*"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnMult.sizePolicy().hasHeightForWidth())
        self.btnMult.setSizePolicy(sizePolicy)
        self.btnMult.setStyleSheet("QPushButton{\n"
"     \n"
"    background-color: rgb(255, 194, 250);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:  rgb(255, 194, 250);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.btnMult.setObjectName("btnMult")
        self.gridLayout.addWidget(self.btnMult, 3, 5, 1, 1)
        self.btnMais = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.Apertar("+"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnMais.sizePolicy().hasHeightForWidth())
        self.btnMais.setSizePolicy(sizePolicy)
        self.btnMais.setStyleSheet("QPushButton{\n"
"     \n"
"    background-color: rgb(255, 194, 250);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:  rgb(255, 194, 250);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.btnMais.setObjectName("btnMais")
        self.gridLayout.addWidget(self.btnMais, 1, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 4)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Calculadora"))
        self.b8.setText(_translate("mainWindow", "8"))
        self.b1.setText(_translate("mainWindow", "1"))
        self.b7.setText(_translate("mainWindow", "7"))
        self.b5.setText(_translate("mainWindow", "5"))
        self.btnLimp.setText(_translate("mainWindow", "Limpar"))
        self.btnDivi.setText(_translate("mainWindow", "/"))
        self.b3.setText(_translate("mainWindow", "3"))
        self.b2.setText(_translate("mainWindow", "2"))
        self.b6.setText(_translate("mainWindow", "6"))
        self.btnMenos.setText(_translate("mainWindow", "-"))
        self.btnApag.setText(_translate("mainWindow", "Apagar"))
        self.b4.setText(_translate("mainWindow", "4"))
        self.btnPonto.setText(_translate("mainWindow", "."))
        self.b0.setText(_translate("mainWindow", "0"))
        self.b9.setText(_translate("mainWindow", "9"))
        self.btnIgual.setText(_translate("mainWindow", "="))
        self.btnMult.setText(_translate("mainWindow", "x"))
        self.btnMais.setText(_translate("mainWindow", "+"))
        self.label.setText(_translate("mainWindow", ""))

    def ponto(self):
        tela = self.label.text()
        if "." in tela:
            pass
        else:
            self.label.setText(f'{tela}.')

    def apagar(self):
        tela = self.label.text()
        tela = tela[:-1]
        self.label.setText(tela)


    def Apertar(self, click):
        if click == "Lm":
                self.label.setText("")
        else:
                if self.label.text() == "0":
                        self.label.setText("")
                self.label.setText(f'{self.label.text()}{click}')

    def igual(self):
        tela = self.label.text()
        try:
            resp = eval(tela) #eval interpreta a string criada como um cálculo
            self.label.setText(str(resp))
        except:
            self.label.setText("Erro :/")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec())
