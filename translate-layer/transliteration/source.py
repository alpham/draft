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
        self.buck2uni_ = {"2": u"\u0621", # hamza-on-the-line
            "|": u"\u0622", # madda
            ">": u"\u0623", # hamza-on-'alif
            "&": u"\u0624", # hamza-on-waaw
            "<": u"\u0625", # hamza-under-'alif
            
            "e": u"\u0625", # hamza-under-'alif

            "}": u"\u0626", # hamza-on-yaa'
            "a": u"\u0627", # bare 'alif
            "b": u"\u0628", # baa'
            "p": u"\u0629", # taa' marbuuTa
            "t": u"\u062A", # taa'
            "v": u"\u062B", # thaa'
            "j": u"\u062C", # jiim
            "7": u"\u062D", # Haa'
            "x": u"\u062E", # khaa'
            "d": u"\u062F", # daal
            "*": u"\u0630", # dhaal
            "r": u"\u0631", # raa'
            "z": u"\u0632", # zaay
            "s": u"\u0633", # siin
            "4": u"\u0634", # shiin
            "S": u"\u0635", # Saad
            "D": u"\u0636", # Daad
            # "t": u"\u0637", # Taa'
            "6": u"\u0637", # Taa'
            "Z": u"\u0638", # Zaa' (DHaa')
            "3": u"\u0639", # cayn
            "g": u"\u063A", # ghayn
            # "_": u"\u0640", # taTwiil
            "f": u"\u0641", # faa'
            "q": u"\u0642", # qaaf
            "k": u"\u0643", # kaaf
            "l": u"\u0644", # laam
            "m": u"\u0645", # miim
            "n": u"\u0646", # nuun
            "h": u"\u0647", # haa'
            "w": u"\u0648", # waaw
            "o": u"\u0648", # waaw

            # "3": u"\xd8",   # 3een

            "Y": u"\u0649", # 'alif maqSuura
            "y": u"\u064A", # yaa'
            # "F": u"\u064B", # fatHatayn
            # "N": u"\u064C", # Dammatayn
            # "K": u"\u064D", # kasratayn
            # "a": u"\u064E", # fatHa
            # "u": u"\u064F", # Damma
            # "i": u"\u0650", # kasra
            # "~": u"\u0651", # shaddah
            # "o": u"\u0652", # sukuun
            "`": u"\u0670", # dagger 'alif
            "{": u"\u0671", # waSla
            " ": u"\u00A0"
        }

    def setupConnections(self):
        QObject.connect(self.ui.retrieve, SIGNAL('clicked()'), self.retrieve_function)

    def retrieve_function(self):
        string = str(self.ui.word.text())
        l = list(string)
        res = ""
        for letter in l:
            res = res + self.buck2uni_[letter];
        self.ui.root.setText(QString(res))
        
