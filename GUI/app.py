from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.initUI()

    def initUI():
        label = QtWidgets.QLabel(win)
