#!/bin/python


from PyQt4.QtGui import QApplication
from source.MainWindow import *
import sys

def main():
	app = QApplication(sys.argv)
	mainwindow = MainWindow()

	mainwindow.show()
	sys.exit(app.exec_())

if __name__ == "__main__" :
	main()
