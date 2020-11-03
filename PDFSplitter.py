# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HP\PycharmProjects\StoryTeller\Gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox

from PyPDF2 import PdfFileReader,PdfFileWriter



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 250)
        MainWindow.setWindowTitle("PDF Splitter")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setWindowIcon(QtGui.QIcon("library.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.browseBtn.setGeometry(QtCore.QRect(520, 30, 75, 31))
        self.browseBtn.setObjectName("browseBtn")

        self.browse2Btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse2Btn.setGeometry(QtCore.QRect(520, 100, 75, 31))
        self.browse2Btn.setObjectName("browseBtn")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(530, 170, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(20)

        self.splitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.splitBtn.setGeometry(QtCore.QRect(260, 200, 75, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitBtn.sizePolicy().hasHeightForWidth())
        self.splitBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.splitBtn.setFont(font)
        self.splitBtn.setObjectName("splitBtn")
        self.splitpath = QtWidgets.QLineEdit(self.centralwidget)
        self.splitpath.setGeometry(QtCore.QRect(10, 100, 491, 31))
        self.splitpath.setObjectName("splitpath")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 161, 16))
        self.label_2.setWhatsThis("")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 175, 161, 16))
        self.label_3.setObjectName("label_3")
        self.filepath = QtWidgets.QLineEdit(self.centralwidget)
        self.filepath.setGeometry(QtCore.QRect(10, 30, 491, 31))
        self.filepath.setReadOnly(True)
        self.filepath.setObjectName("filepath")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.browseBtn.clicked.connect(self.browse)
        self.browse2Btn.clicked.connect(self.browse2)
        self.splitBtn.clicked.connect(self.split)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.browseBtn.setText(_translate("MainWindow", "Browse"))
        self.browse2Btn.setText(_translate("MainWindow", "Browse"))
        self.splitBtn.setText(_translate("MainWindow", "Split"))
        self.label.setText(_translate("MainWindow", "Path of file:"))
        self.label_2.setText(_translate("MainWindow", "Path of splitted files:"))
        self.label_3.setText(_translate("MainWindow", "Number of Parts:"))

        global fileName
        fileName = ""
        global folderName
        folderName = ""

    def browse(self):
        global fileName
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select PDF File", "",
                                                            "PDF Files (*.pdf);;All Files (*)")
        self.filepath.setText(fileName)

    def browse2(self):
        global folderName
        folderName = QtWidgets.QFileDialog.getExistingDirectory()
        self.splitpath.setText(folderName)

    def split(self):
        global splitName
        global fileName
        splitName = self.splitpath.text()
        parts = self.spinBox.value()

        if not fileName == "" and not splitName == "":
            file = open(fileName, 'rb')
            read = PdfFileReader(file)
            writer = PdfFileWriter()
            p = int(read.getNumPages() / parts)
            r = read.getNumPages() % parts

            for j in range(1, parts + 1):
                if j == parts:
                    for i in range((j - 1) * p, j * p + r):
                        writer.addPage(read.getPage(i))
                else:
                    for i in range((j - 1) * p, j * p):
                        writer.addPage(read.getPage(i))

                split = open(splitName + '/part' + str(j) + '.pdf', 'wb')
                writer.write(split)
                file.close()
                split.close()
                writer = PdfFileWriter()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("The PDF have been splitted successfully   ")
            msg.setInformativeText("Do you want to exit?")
            msg.setWindowTitle("Split!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()

        elif fileName == "":
            msgbrs = QMessageBox()
            msgbrs.setIcon(QMessageBox.Warning)
            msgbrs.setText("Please select a file  ")
            msgbrs.exec_()

        elif splitName == "":
            msgspt = QMessageBox()
            msgspt.setIcon(QMessageBox.Warning)
            msgspt.setText("Please insert a directory  ")
            msgspt.exec_()
        else:
            pass



    def msgbtn(self, i):
        print('Button is' + i.text())
        if i.text() == '&Yes':
            sys.exit()
        else:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

