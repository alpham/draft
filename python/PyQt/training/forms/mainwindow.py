# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Apr 16 16:14:57 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(898, 569)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.account_id_label = QtGui.QLabel(self.centralwidget)
        self.account_id_label.setObjectName(_fromUtf8("account_id_label"))
        self.horizontalLayout.addWidget(self.account_id_label)
        self.account_id_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.account_id_lineEdit.setObjectName(_fromUtf8("account_id_lineEdit"))
        self.horizontalLayout.addWidget(self.account_id_lineEdit)
        self.go_pushButton = QtGui.QPushButton(self.centralwidget)
        self.go_pushButton.setObjectName(_fromUtf8("go_pushButton"))
        self.horizontalLayout.addWidget(self.go_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.posts_listWidget = QtGui.QListWidget(self.centralwidget)
        self.posts_listWidget.setObjectName(_fromUtf8("posts_listWidget"))
        self.horizontalLayout_2.addWidget(self.posts_listWidget)
        self.friends_listWidget = QtGui.QListWidget(self.centralwidget)
        self.friends_listWidget.setObjectName(_fromUtf8("friends_listWidget"))
        self.horizontalLayout_2.addWidget(self.friends_listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.num_of_friends_label = QtGui.QLabel(self.centralwidget)
        self.num_of_friends_label.setObjectName(_fromUtf8("num_of_friends_label"))
        self.horizontalLayout_3.addWidget(self.num_of_friends_label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.friends_count_label = QtGui.QLabel(self.centralwidget)
        self.friends_count_label.setObjectName(_fromUtf8("friends_count_label"))
        self.horizontalLayout_3.addWidget(self.friends_count_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.most_used_words_label = QtGui.QLabel(self.centralwidget)
        self.most_used_words_label.setObjectName(_fromUtf8("most_used_words_label"))
        self.horizontalLayout_4.addWidget(self.most_used_words_label)
        self.most_used_words_listWidget = QtGui.QListWidget(self.centralwidget)
        self.most_used_words_listWidget.setObjectName(_fromUtf8("most_used_words_listWidget"))
        self.horizontalLayout_4.addWidget(self.most_used_words_listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        MainWindow.setMenuBar(self.menubar)
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.menu_File.addAction(self.action_Quit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.account_id_label.setBuddy(self.account_id_lineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.account_id_label.setText(_translate("MainWindow", "&Account ID : ", None))
        self.go_pushButton.setText(_translate("MainWindow", "&Go!", None))
        self.num_of_friends_label.setText(_translate("MainWindow", "Num of friends", None))
        self.friends_count_label.setText(_translate("MainWindow", "0 friends", None))
        self.most_used_words_label.setText(_translate("MainWindow", "Most used words (top 10)", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))

