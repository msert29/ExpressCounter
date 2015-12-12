# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core.ui'
#
# Created: Sat Dec 12 14:37:07 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QPixmap, QLabel

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
        MainWindow.resize(1280, 950)
        MainWindow.setStyleSheet(_fromUtf8("background:white;\n"
"\n"
"QHBoxLayout::hover {\n"
"    background-color:blue;\n"
"}\n"
"\n"
"QFrame, QLabel, QToolTip {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    background-color: rgb(28, 233, 255);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 130, 391, 331))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.new_order_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.new_order_layout.setMargin(0)
        self.new_order_layout.setObjectName(_fromUtf8("new_order_layout"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(590, 130, 391, 331))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.search_order_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.search_order_layout.setMargin(0)
        self.search_order_layout.setObjectName(_fromUtf8("search_order_layout"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(590, 480, 391, 331))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.newcustomer_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.newcustomer_layout.setMargin(0)
        self.newcustomer_layout.setObjectName(_fromUtf8("newcustomer_layout"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(170, 480, 389, 329))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.manager_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.manager_layout.setMargin(0)
        self.manager_layout.setObjectName(_fromUtf8("manager_layout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.draw_icons()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

    
    def draw_icons(self):     
        neworder_icon = QtGui.QPixmap('images/icn-phone2.png')
        manager_icon = QPixmap('images/admin-icon.png')
        search_icon = QPixmap('images/search-icon.png')
        newcustomer_icon = QPixmap('images/newcustomer-icon.png')
        
        self.neworder_lbl = QLabel("Place an order")
        self.manager_lbl = QLabel("Manager Log in")
        self.search_lbl = QLabel("Search")
        self.newcustomer_lbl = QLabel("New Customer Entry")
        
        self.manager_lbl.setPixmap(manager_icon)
        self.search_lbl.setPixmap(search_icon)
        self.neworder_lbl.setPixmap(neworder_icon)
        self.newcustomer_lbl.setPixmap(newcustomer_icon)
        
        self.new_order_layout.addWidget(self.neworder_lbl)
        self.manager_layout.addWidget(self.manager_lbl)
        self.search_order_layout.addWidget(self.search_lbl)
        self.newcustomer_layout.addWidget(self.newcustomer_lbl)