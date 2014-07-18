from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import sys
import source 

def main():
    app = QApplication(sys.argv)
    win = source.test()
    win.show()
    sys.exit(app.exec_())



main()
