from UIUX105 import Ui_RainPredict

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class demo(qtw.QWidget, Ui_RainPredict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
    


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    widget = demo()
    widget.show()

    app.exec_()
