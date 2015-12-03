# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cart.ui'
#
# Created: Wed Dec  2 09:09:15 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QDialog

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

class Ui_Dialog(QDialog):
    def __init__(self, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1626, 967)
        Dialog.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(85, 170, 255);\n"
"  color:black;\n"
" }\n"
"QListWidget {\n"
" background:rgb(253, 252, 255);\n"
"}\n"
"QDialog {\n"
"background-color:rgb(253, 252, 255);\n"
"}"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 70, 1011, 881))
        self.tabWidget.setStyleSheet(_fromUtf8(" QTabBar::tab {\n"
"  background: gray;\n"
"  color: white;\n"
"  padding: 10px;\n"
"   border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: 20px;\n"
"    min-width: 10em;\n"
"    min-height:2em;\n"
"    padding: 6px;\n"
"   margin-bottom:5px;\n"
" }\n"
" QTabBar::tab:selected {\n"
"  background: rgb(85, 170, 255);\n"
"  color:black;\n"
" }\n"
"\n"
""))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.kebab_tab = QtGui.QWidget()
        self.kebab_tab.setObjectName(_fromUtf8("kebab_tab"))
        self.tabWidget.addTab(self.kebab_tab, _fromUtf8(""))
        self.pizza_tab = QtGui.QWidget()
        self.pizza_tab.setObjectName(_fromUtf8("pizza_tab"))
        self.tabWidget.addTab(self.pizza_tab, _fromUtf8(""))
        self.burger_tab = QtGui.QWidget()
        self.burger_tab.setObjectName(_fromUtf8("burger_tab"))
        self.tabWidget.addTab(self.burger_tab, _fromUtf8(""))
        self.other_tab = QtGui.QWidget()
        self.other_tab.setObjectName(_fromUtf8("other_tab"))
        self.tabWidget.addTab(self.other_tab, _fromUtf8(""))
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(1060, 900, 161, 51))
        self.cancel_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: red;\n"
"color:black;\n"
"} "))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(1230, 900, 161, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: rgb(20, 255, 67);\n"
"color:black;\n"
"} "))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.cart_view = QtGui.QListWidget(Dialog)
        self.cart_view.setGeometry(QtCore.QRect(1060, 140, 331, 701))
        self.cart_view.setStyleSheet(_fromUtf8("background:rgb(240, 240, 240)"))
        self.cart_view.setObjectName(_fromUtf8("cart_view"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1060, 70, 331, 61))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.cart_total = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.cart_total.setMargin(0)
        self.cart_total.setObjectName(_fromUtf8("cart_total"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"color:white;\n"
"text-align: center;\n"
"border-radius: 10px 20px;\n"
"}\n"
"QLabel:hover {\n"
"background:rgb(85, 170, 255);\n"
"color:black;\n"
"}"))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.cart_total.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1060, 850, 331, 41))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.price_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.price_layout.setMargin(0)
        self.price_layout.setObjectName(_fromUtf8("price_layout"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.kebab_tab), _translate("Dialog", "Kebabs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pizza_tab), _translate("Dialog", "Pizzas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.burger_tab), _translate("Dialog", "Burgers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.other_tab), _translate("Dialog", "Others", None))
        self.cancel_button.setText(_translate("Dialog", "Cancel", None))
        self.pushButton_2.setText(_translate("Dialog", "Confirm", None))
        self.label.setText(_translate("Dialog", "Order Summary", None))

