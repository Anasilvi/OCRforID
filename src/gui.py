# Form implementation generated from reading ui file 'Proyecto2.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 613)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setVisible(False)
        self.frame_2.setGeometry(QtCore.QRect(0, 10, 1001, 591))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 30, 490, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(10, 20, 471, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(350, 512, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 30, 490, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 471, 481))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.formLayout.setContentsMargins(15, 45, 15, 0)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 510, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")


        #Creating home page
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(40, 60, 901, 431))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 160, 180, 180))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(((os.path.dirname(os.path.realpath(__file__))+"\\resources\\OCRicon.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.getfile)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 160, 180, 180))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(((os.path.dirname(os.path.realpath(__file__))+"\\resources\\SearchIcon.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 160, 180, 180))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(((os.path.dirname(os.path.realpath(__file__))+"\\resources\\helpIcon.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_5.setObjectName("pushButton_5")
        #Labels
        self.labelH = QtWidgets.QLabel(self.frame_3)
        self.labelH.setGeometry(QtCore.QRect(6, -1, 891, 121))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.labelH.setFont(font)
        self.labelH.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.labelH.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelH.setObjectName("labelH")
        self.labelH_2 = QtWidgets.QLabel(self.frame_3)
        self.labelH_2.setGeometry(QtCore.QRect(70, 360, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelH_2.setFont(font)
        self.labelH_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelH_2.setObjectName("labelH_2")
        self.labelH_3 = QtWidgets.QLabel(self.frame_3)
        self.labelH_3.setGeometry(QtCore.QRect(360, 360, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelH_3.setFont(font)
        self.labelH_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelH_3.setObjectName("labelH_3")
        self.labelH_4 = QtWidgets.QLabel(self.frame_3)
        self.labelH_4.setGeometry(QtCore.QRect(680, 360, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelH_4.setFont(font)
        self.labelH_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelH_4.setObjectName("labelH_4")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtGui.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSearch_info = QtGui.QAction(MainWindow)
        self.actionSearch_info.setObjectName("actionSearch_info")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ID Reader"))
        self.groupBox.setTitle(_translate("MainWindow", "Image"))
        self.pushButton.setText(_translate("MainWindow", "Process Image"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Data extracted"))
        self.label.setText(_translate("MainWindow", "ID Number:"))
        self.label_2.setText(_translate("MainWindow", "Names:"))
        self.label_3.setText(_translate("MainWindow", "Family Names:"))
        self.label_4.setText(_translate("MainWindow", "Gender:"))
        self.label_5.setText(_translate("MainWindow", "Nationality:"))
        self.label_6.setText(_translate("MainWindow", "Date of Birth:"))
        self.pushButton_2.setText(_translate("MainWindow", "Save Data"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open image"))
        self.actionSearch_info.setText(_translate("MainWindow", "Search info"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.labelH.setText(_translate("MainWindow", "ID Reader"))
        self.labelH_2.setText(_translate("MainWindow", "Process an image"))
        self.labelH_3.setText(_translate("MainWindow", "Search person"))
        self.labelH_4.setText(_translate("MainWindow", "Help"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open image"))
        self.actionSearch_info.setText(_translate("MainWindow", "Search info"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


    #Function to open a file
    def getfile(self):
        fDialog = QtWidgets.QFileDialog()
        file_filter = 'Image File (*.jpg *.jpeg *.png)'
        fname = fDialog.getOpenFileName(caption='Select a data file',
            filter=file_filter,)
        self.frame_3.setVisible(False)
        self.img_label = QtWidgets.QLabel(self.frame)
        pixmap = QtGui.QPixmap(fname[0])
        pixmap = pixmap.scaled(480, 480, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.img_label.setPixmap(pixmap)
        self.img_label.setScaledContents(True)
        self.img_label.resize(pixmap.width(),pixmap.height())
        self.frame_2.setVisible(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())