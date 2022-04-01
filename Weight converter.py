from PyQt5 import QtCore, QtGui, QtWidgets

#constants for converting
kgtolb = 2.205
kgtog = 1000
kgtomg= 1000000
kgtooz = 35.274
lbtog = 453.592
lbtomg = 453592
lbtot = 2204.62
lbtooz = 16
gtooz = 28.3495
mgtot = 1000000000
mgtooz = 28349.5
ttooz = 35274

def measure(frm, to):
    if frm == "kg" and to == "kg":
        return 1
    elif frm == "kg" and to == "lb":
        return kgtolb
    elif frm == "kg" and to == "g":
        return kgtog
    elif frm == "kg" and to == "t":
        return 1/kgtog
    elif frm == "kg" and to == "oz":
        return kgtooz
    elif frm == "kg" and to == "mg":
        return kgtomg
    
    
    elif frm == "lb" and to == "lb":
        return 1
    elif frm == "lb" and to == "kg":
        return 1/kgtolb
    elif frm == "lb" and to == "g":
        return lbtog
    elif frm == "lb" and to == "mg":
        return lbtomg
    elif frm == "lb" and to == "t":
        return 1/lbtot
    elif frm == "lb" and to == "oz":
        return lbtooz

    elif frm == "g" and to == "lb":
        return 1/lbtog
    elif frm == "g" and to == "kg":
        return 1/kgtog
    elif frm == "g" and to == "g":
        return 1
    elif frm == "g" and to == "mg":
        return kgtog
    elif frm == "g" and to == "t":
        return 1/kgtomg
    elif frm == "g" and to == "oz":
        return 1/gtooz
    
    elif frm == "mg" and to == "lb":
        return 1/lbtomg
    elif frm == "mg" and to == "kg":
        return 1/kgtomg
    elif frm == "mg" and to == "g":
        return 1/kgtog
    elif frm == "mg" and to == "mg":
        return 1
    elif frm == "mg" and to == "t":
        return 1/mgtot
    elif frm == "mg" and to == "oz":
        return 1/mgtooz
    
    elif frm == "t" and to == "lb":
        return lbtot
    elif frm == "t" and to == "kg":
        return kgtog
    elif frm == "t" and to == "g":
        return kgtomg
    elif frm == "t" and to == "mg":
        return mgtot
    elif frm == "t" and to == "t":
        return 1
    elif frm == "t" and to == "oz":
        return ttooz
    
    elif frm == "oz" and to == "lb":
        return 1/lbtooz
    elif frm == "oz" and to == "kg":
        return 1/kgtooz
    elif frm == "oz" and to == "g":
        return gtooz
    elif frm == "oz" and to == "mg":
        return mgtooz
    elif frm == "oz" and to == "t":
        return 1/ttooz
    elif frm == "oz" and to == "oz":
        return 1


def conversion( frm,  to,  weight):
    return (weight*measure(frm, to))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SP weight converter")
        MainWindow.resize(766, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 180, 181, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.inputweight = QtWidgets.QComboBox(self.centralwidget)
        self.inputweight.setGeometry(QtCore.QRect(150, 210, 181, 24))
        self.inputweight.setObjectName("inputweight")
        self.inputweight.addItem("")
        self.inputweight.addItem("")
        self.inputweight.addItem("")
        self.inputweight.addItem("")
        self.inputweight.addItem("")
        self.inputweight.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 50, 861, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(220, 10, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setWordWrap(True)
        self.Title.setObjectName("Title")
        self.Input = QtWidgets.QLabel(self.centralwidget)
        self.Input.setGeometry(QtCore.QRect(90, 180, 58, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Input.setFont(font)
        self.Input.setAlignment(QtCore.Qt.AlignCenter)
        self.Input.setObjectName("Input")
        self.equal = QtWidgets.QLabel(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(340, 170, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.equal.setFont(font)
        self.equal.setAlignment(QtCore.Qt.AlignCenter)
        self.equal.setObjectName("equal")
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(420, 180, 181, 21))
        self.output.setText("New Weight")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        self.outputweight = QtWidgets.QComboBox(self.centralwidget)
        self.outputweight.setGeometry(QtCore.QRect(420, 210, 181, 24))
        self.outputweight.setObjectName("outputweight")
        self.outputweight.addItem("")
        self.outputweight.addItem("")
        self.outputweight.addItem("")
        self.outputweight.addItem("")
        self.outputweight.addItem("")
        self.outputweight.addItem("")
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(300, 250, 161, 24))
        self.Button.setObjectName("Button")
        self.Button.clicked.connect(self.clicked)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Sp weight converter", "Sp weight converter"))
        self.inputweight.setItemText(0, _translate("MainWindow", "kg"))
        self.inputweight.setItemText(1, _translate("MainWindow", "lb"))
        self.inputweight.setItemText(2, _translate("MainWindow", "g"))
        self.inputweight.setItemText(3, _translate("MainWindow", "mg"))
        self.inputweight.setItemText(4, _translate("MainWindow", "t"))
        self.inputweight.setItemText(5, _translate("MainWindow", "oz"))
        self.Title.setText(_translate("MainWindow", "Weight Converter"))
        self.Input.setText(_translate("MainWindow", "Input"))
        self.equal.setText(_translate("MainWindow", "="))
        self.outputweight.setItemText(0, _translate("MainWindow", "kg"))
        self.outputweight.setItemText(1, _translate("MainWindow", "lb"))
        self.outputweight.setItemText(2, _translate("MainWindow", "g"))
        self.outputweight.setItemText(3, _translate("MainWindow", "mg"))
        self.outputweight.setItemText(4, _translate("MainWindow", "t"))
        self.outputweight.setItemText(5, _translate("MainWindow", "oz"))
        self.Button.setText(_translate("MainWindow", "Enter"))
        
    
    asfa = str(conversion("lb","kg", 10))
    
    def clicked(self):
        input1 = self.inputweight.currentText()
        output1 = self.outputweight.currentText()
        input12 = self.lineEdit.text()
        inputvalue = self.Input.text()
        converts = str(conversion(input1,output1,int(input12)))
        self.output.setText(converts)
    

    
        
    
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
