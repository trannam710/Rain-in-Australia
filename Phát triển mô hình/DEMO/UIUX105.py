from model import train_model

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QCursor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RainPredict(object):
    def setupUi(self, RainPredict):

        # Set background
        RainPredict.setObjectName("RainPredict")
        RainPredict.resize(684, 442)
        RainPredict.setAutoFillBackground(False)

        ## Loc
        # Dropbox    
        self.comboBox = QtWidgets.QComboBox(RainPredict)
        self.comboBox.setGeometry(QtCore.QRect(100, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # Text
        self.label = QtWidgets.QLabel(RainPredict)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        ## Temp
        self.groupBox = QtWidgets.QGroupBox(RainPredict)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 161, 161))
        self.groupBox.setObjectName("groupBox")
        # Min
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 51, 22))
        self.lineEdit.setObjectName("lineEdit")
        # Max
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 60, 51, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        # 9 AM
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_17.setGeometry(QtCore.QRect(100, 90, 51, 22))
        self.lineEdit_17.setObjectName("lineEdit_17")

        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(50, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        # 3 PM
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(50, 120, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")

        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_18.setGeometry(QtCore.QRect(100, 120, 51, 22))
        self.lineEdit_18.setObjectName("lineEdit_18")
        # ICON
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(0, 120, 41, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("icons/temp.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        ## WindDir
        self.groupBox_2 = QtWidgets.QGroupBox(RainPredict)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 60, 221, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        # Strongest
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(60, 30, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setAcceptDrops(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        # 9 AM
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(60, 60, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(140, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setAcceptDrops(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        # 3 PM
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(60, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(140, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setAcceptDrops(False)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        # ICON
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("icons/winddirection.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")

        ## WindSpeed
        self.groupBox_3 = QtWidgets.QGroupBox(RainPredict)
        self.groupBox_3.setGeometry(QtCore.QRect(450, 60, 201, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        # 9 AM
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(60, 60, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 60, 51, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        # 3 PM
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(60, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 90, 51, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        # Strongest
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(60, 30, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(140, 30, 51, 22))
        self.lineEdit_13.setObjectName("lineEdit_13")
        # ICON
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 31, 31))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("icons/windspeed.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")

        ## Humidity
        self.groupBox_4 = QtWidgets.QGroupBox(RainPredict)
        self.groupBox_4.setGeometry(QtCore.QRect(210, 230, 221, 131))
        self.groupBox_4.setObjectName("groupBox_4")
        # 9 AM
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(60, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 30, 51, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        # 3 PM
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(60, 60, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(140, 60, 51, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        # ICON
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(10, 90, 31, 31))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("icons/humidity.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")

        ## Pressure
        self.groupBox_5 = QtWidgets.QGroupBox(RainPredict)
        self.groupBox_5.setGeometry(QtCore.QRect(450, 230, 201, 131))
        self.groupBox_5.setObjectName("groupBox_5")
        # 9 AM
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(60, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_11.setGeometry(QtCore.QRect(140, 30, 51, 22))
        self.lineEdit_11.setObjectName("lineEdit_11")
        # 3 PM
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(60, 60, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_12.setGeometry(QtCore.QRect(140, 60, 51, 22))
        self.lineEdit_12.setObjectName("lineEdit_12")
        # ICON
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(10, 90, 31, 31))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("icons/pressure.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")

        ## Rainfall
        self.label_23 = QtWidgets.QLabel(RainPredict)
        self.label_23.setGeometry(QtCore.QRect(40, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")

        self.lineEdit_19 = QtWidgets.QLineEdit(RainPredict)
        self.lineEdit_19.setGeometry(QtCore.QRect(100, 270, 91, 22))
        self.lineEdit_19.setObjectName("lineEdit_19")

        ## Predict TOMORROW!
        self.pushButton_2 = QtWidgets.QPushButton(RainPredict)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 370, 631, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.PredictOnPressed_Tomorrow)

        self.groupBox.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.label_23.raise_()
        self.lineEdit_19.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(RainPredict)
        QtCore.QMetaObject.connectSlotsByName(RainPredict)

    def get_clear(self):
        # Get information and clear
        loc = self.comboBox.currentText()
        self.comboBox.setCurrentIndex(0)

        MinTemp = self.lineEdit.text()
        self.lineEdit.clear()

        MaxTemp = self.lineEdit_2.text()
        self.lineEdit_2.clear()

        Temp9am = self.lineEdit_17.text()
        self.lineEdit_17.clear()

        Temp3pm = self.lineEdit_18.text()
        self.lineEdit_18.clear()

        WindGustDir = self.comboBox_2.currentText()
        self.comboBox_2.setCurrentIndex(0)

        WindDir9am = self.comboBox_3.currentText()
        self.comboBox_3.setCurrentIndex(0)

        WindDir3pm = self.comboBox_4.currentText()
        self.comboBox_4.setCurrentIndex(0)

        WindGustSpeed = self.lineEdit_13.text()
        self.lineEdit_13.clear()

        WindSpeed9am = self.lineEdit_7.text()
        self.lineEdit_7.clear()

        WindSpeed3pm = self.lineEdit_8.text()
        self.lineEdit_8.clear()

        Humidity9am = self.lineEdit_9.text()
        self.lineEdit_9.clear()

        Humidity3pm = self.lineEdit_10.text()
        self.lineEdit_10.clear()

        Pressure9am = self.lineEdit_11.text()
        self.lineEdit_11.clear()

        Pressure3pm = self.lineEdit_12.text()
        self.lineEdit_12.clear()

        Rainfall = self.lineEdit_19.text()
        self.lineEdit_19.clear()

        RainToday = 'No'
        if Rainfall == '':
            RainToday = ''
        else:
            Rainfall = float(Rainfall)
            if Rainfall >= 1:
                RainToday = 'Yes'
        return loc, MinTemp, MaxTemp, Temp9am, Temp3pm, WindGustDir, WindDir9am, WindDir3pm, WindGustSpeed, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Rainfall, RainToday
 

    def retranslateUi(self, RainPredict):
        _translate = QtCore.QCoreApplication.translate
        RainPredict.setWindowTitle(_translate("RainPredict", "Rain Today and Tomorrow Prediction App"))
        self.comboBox.setItemText(0, _translate("RainPredict", "MountGinini"))
        self.comboBox.setItemText(1, _translate("RainPredict", "MountGambier"))
        self.label.setText(_translate("RainPredict", "Location"))
        self.groupBox.setTitle(_translate("RainPredict", "Temperature"))
        self.label_2.setText(_translate("RainPredict", "Min"))
        self.label_3.setText(_translate("RainPredict", "Max"))
        self.label_21.setText(_translate("RainPredict", "9 AM"))
        self.label_22.setText(_translate("RainPredict", "3 PM"))
        self.groupBox_2.setTitle(_translate("RainPredict", "Wind Direction"))
        self.label_4.setText(_translate("RainPredict", "Strongest"))
        self.label_5.setText(_translate("RainPredict", "9 AM"))
        self.comboBox_2.setItemText(1, _translate("RainPredict", "N"))
        self.comboBox_2.setItemText(2, _translate("RainPredict", "NNW"))
        self.comboBox_2.setItemText(3, _translate("RainPredict", "NW"))
        self.comboBox_2.setItemText(4, _translate("RainPredict", "WNW"))
        self.comboBox_2.setItemText(5, _translate("RainPredict", "W"))
        self.comboBox_2.setItemText(6, _translate("RainPredict", "WSW"))
        self.comboBox_2.setItemText(7, _translate("RainPredict", "WS"))
        self.comboBox_2.setItemText(8, _translate("RainPredict", "SSW"))
        self.comboBox_2.setItemText(9, _translate("RainPredict", "S"))
        self.comboBox_2.setItemText(10, _translate("RainPredict", "SSE"))
        self.comboBox_2.setItemText(11, _translate("RainPredict", "SE"))
        self.comboBox_2.setItemText(12, _translate("RainPredict", "ESE"))
        self.comboBox_2.setItemText(13, _translate("RainPredict", "E"))
        self.comboBox_2.setItemText(14, _translate("RainPredict", "ENE"))
        self.comboBox_2.setItemText(15, _translate("RainPredict", "NE"))
        self.comboBox_2.setItemText(16, _translate("RainPredict", "NNE"))
        self.comboBox_3.setItemText(1, _translate("RainPredict", "N"))
        self.comboBox_3.setItemText(2, _translate("RainPredict", "NNW"))
        self.comboBox_3.setItemText(3, _translate("RainPredict", "NW"))
        self.comboBox_3.setItemText(4, _translate("RainPredict", "WNW"))
        self.comboBox_3.setItemText(5, _translate("RainPredict", "W"))
        self.comboBox_3.setItemText(6, _translate("RainPredict", "WSW"))
        self.comboBox_3.setItemText(7, _translate("RainPredict", "WS"))
        self.comboBox_3.setItemText(8, _translate("RainPredict", "SSW"))
        self.comboBox_3.setItemText(9, _translate("RainPredict", "S"))
        self.comboBox_3.setItemText(10, _translate("RainPredict", "SSE"))
        self.comboBox_3.setItemText(11, _translate("RainPredict", "SE"))
        self.comboBox_3.setItemText(12, _translate("RainPredict", "ESE"))
        self.comboBox_3.setItemText(13, _translate("RainPredict", "E"))
        self.comboBox_3.setItemText(14, _translate("RainPredict", "ENE"))
        self.comboBox_3.setItemText(15, _translate("RainPredict", "NE"))
        self.comboBox_3.setItemText(16, _translate("RainPredict", "NNE"))
        self.label_6.setText(_translate("RainPredict", "3 PM"))
        self.comboBox_4.setItemText(1, _translate("RainPredict", "N"))
        self.comboBox_4.setItemText(2, _translate("RainPredict", "NNW"))
        self.comboBox_4.setItemText(3, _translate("RainPredict", "NW"))
        self.comboBox_4.setItemText(4, _translate("RainPredict", "WNW"))
        self.comboBox_4.setItemText(5, _translate("RainPredict", "W"))
        self.comboBox_4.setItemText(6, _translate("RainPredict", "WSW"))
        self.comboBox_4.setItemText(7, _translate("RainPredict", "WS"))
        self.comboBox_4.setItemText(8, _translate("RainPredict", "SSW"))
        self.comboBox_4.setItemText(9, _translate("RainPredict", "S"))
        self.comboBox_4.setItemText(10, _translate("RainPredict", "SSE"))
        self.comboBox_4.setItemText(11, _translate("RainPredict", "SE"))
        self.comboBox_4.setItemText(12, _translate("RainPredict", "ESE"))
        self.comboBox_4.setItemText(13, _translate("RainPredict", "E"))
        self.comboBox_4.setItemText(14, _translate("RainPredict", "ENE"))
        self.comboBox_4.setItemText(15, _translate("RainPredict", "NE"))
        self.comboBox_4.setItemText(16, _translate("RainPredict", "NNE"))
        self.groupBox_3.setTitle(_translate("RainPredict", "Wind Speed"))
        self.label_11.setText(_translate("RainPredict", "9 AM"))
        self.label_12.setText(_translate("RainPredict", "3 PM"))
        self.label_7.setText(_translate("RainPredict", "Strongest"))
        self.groupBox_4.setTitle(_translate("RainPredict", "Humidity"))
        self.label_13.setText(_translate("RainPredict", "9 AM"))
        self.label_14.setText(_translate("RainPredict", "3 PM"))
        self.groupBox_5.setTitle(_translate("RainPredict", "Pressure"))
        self.label_15.setText(_translate("RainPredict", "9 AM"))
        self.label_16.setText(_translate("RainPredict", "3 PM"))
        self.label_23.setText(_translate("RainPredict", "Rain fall"))
        self.pushButton_2.setText(_translate("RainPredict", "Predict TOMORROW!"))

    def get_feature_name(self, idx):
        if idx == 0:
            return 'MinTemp'
        if idx == 1:
            return 'MaxTemp'
        if idx == 2:
            return 'Temp9am'
        if idx == 3:
            return 'Temp3pm'
        if idx == 4:
            return 'WindGustDir'
        if idx == 5:
            return 'WindDir9am'
        if idx == 6:
            return 'WindDir3pm'
        if idx == 7:
            return 'WindGustSpeed'
        if idx == 8:
            return 'WindSpeed9am'
        if idx == 9:
            return 'WindSpeed3pm'
        if idx == 10:
            return 'Humidity9am'
        if idx == 11:
            return 'Humidity3pm'
        if idx == 12:
            return 'Pressure9am'
        if idx == 13:
            return 'Pressure3pm'
        if idx == 14:
            return 'Rainfall'
        if idx == 15:
            return 'RainToday'

    def PredictOnPressed_Tomorrow(self):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Toàn bộ thông tin trên sẽ được dùng để dự đoán, \n Bạn đã chắc chưa?")
            
            self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            self.msgReturnValue = self.msg.exec()

            if self.msgReturnValue == QMessageBox.Yes:
                loc, MinTemp, MaxTemp, Temp9am, Temp3pm, WindGustDir, WindDir9am, WindDir3pm, WindGustSpeed, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Rainfall, RainToday = self.get_clear()

                input = {
                        'MinTemp': MinTemp,
                        'MaxTemp': MaxTemp,

                        'Temp9am': Temp9am,
                        'Temp3pm': Temp3pm,

                        'WindGustDir': WindGustDir,
                        'WindDir9am': WindDir9am,
                        'WindDir3pm': WindDir3pm,
                        
                        
                        'WindGustSpeed': WindGustSpeed,
                        'WindSpeed9am': WindSpeed9am,
                        'WindSpeed3pm':WindSpeed3pm,
                        
                        'Humidity9am': Humidity9am,
                        'Humidity3pm': Humidity3pm,

                        'Pressure9am': Pressure9am,
                        'Pressure3pm': Pressure3pm,
                        
                        'Rainfall': Rainfall,

                        'RainToday': RainToday, 
                        }
                
                # Delete element in input dict if it is empty
                vars_list = [MinTemp, MaxTemp, Temp9am, Temp3pm, WindGustDir, WindDir9am, WindDir3pm, WindGustSpeed, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Rainfall, RainToday]

                # Drop items that null
                for idx, var_val in enumerate(vars_list) :
                    if var_val == '':
                        input.pop(self.get_feature_name(idx))

                
                # Change inputed items into float
                for key, item in input.items():
                    if key not in ['WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday']:
                        input[key] = float(item)

                print(input)
                
                result = train_model(loc, **input)

                if result == 0:
                    self.msg_0 = QMessageBox()
                    self.msg_0.setIcon(QMessageBox.Information)
                    self.msg_0.setText("KHÔNG MƯA BẠN ƠI, LÊU LÊU ¯\_(ツ)_/¯")
                    self.msg_0.exec_()
                else:
                    self.msg_1 = QMessageBox()
                    self.msg_1.setIcon(QMessageBox.Information)
                    self.msg_1.setText("MƯA RỒI, NHẤT BẠN NHÁ ╰(*°▽°*)╯")
                    self.msg_1.exec_()
      