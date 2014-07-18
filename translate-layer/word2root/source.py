from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from nltk.stem.isri import *
import test_ui


class test(QMainWindow,test_ui.Ui_MainWindow):
    def __init__(self,parent=None):
        self.ui = test_ui.Ui_MainWindow()
        QMainWindow.__init__(self,parent)
        self.ui.setupUi(self)
        self.setupConnections()

    def setupConnections(self):
        QObject.connect(self.ui.retrieve, SIGNAL('clicked()'), self.retrieve_function)

    def retrieve_function(self):
        word = self.ui.word.text()
        stemmer = ISRIStemmer()
        stemmed = stemmer.stem(unicode(word))
        self.ui.root.setText(stemmed)
