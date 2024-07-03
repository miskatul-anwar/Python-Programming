from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os


def clicked():
    os.system("google-chrome-stable")


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(200, 200, 300, 300)
    window.setWindowTitle("Coding")
    label = QtWidgets.QLabel(window)
    label.setText("hi there")
    label.move(50, 50)
    button1 = QtWidgets.QPushButton(window)
    button1.setText("Codeforces")
    button1.clicked.connect(clicked)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
