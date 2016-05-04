# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/murat/Documents/designs/pizza_toppings_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(946, 874)
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(480, 10, 451, 501))
        self.frame_3.setStyleSheet(_fromUtf8("background:rgb(103, 255, 121);\n"
"font: 18pt \"Ubuntu\";\n"
""))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.frame_3)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 451, 501))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.veg_topping_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.veg_topping_layout.setObjectName(_fromUtf8("veg_topping_layout"))
        self.verticalLayoutWidget_7.raise_()
        self.add_to_cart_button = QtGui.QPushButton(Dialog)
        self.add_to_cart_button.setGeometry(QtCore.QRect(480, 770, 451, 91))
        self.add_to_cart_button.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:rgb(39, 255, 53);\n"
"color:black;\n"
" font: 30pt \"Ubuntu\";\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"}"))
        self.add_to_cart_button.setObjectName(_fromUtf8("add_to_cart_button"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 10, 451, 501))
        self.frame.setStyleSheet(_fromUtf8("background:rgb(255, 211, 51);\n"
"font: 18pt \"Ubuntu\";"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451, 501))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.meat_topping_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.meat_topping_layout.setObjectName(_fromUtf8("meat_topping_layout"))
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(20, 770, 451, 91))
        self.cancel_button.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:rgb(255, 57, 43);\n"
"color:black;\n"
" font: 30pt \"Ubuntu\";\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"}"))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.frame_4 = QtGui.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(20, 520, 451, 241))
        self.frame_4.setStyleSheet(_fromUtf8("background:rgb(230, 230, 230);\n"
"font: 18pt \"Ubuntu\";"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayoutWidget = QtGui.QWidget(self.frame_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451, 241))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.n = QtGui.QGridLayout(self.gridLayoutWidget)
        self.n.setObjectName(_fromUtf8("n"))
        self.frame_5 = QtGui.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(480, 520, 451, 241))
        self.frame_5.setStyleSheet(_fromUtf8("background:rgb(230, 230, 230);\n"
"font: 18pt \"Ubuntu\";"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.frame_5)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 451, 241))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.no_veg_layout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.no_veg_layout.setObjectName(_fromUtf8("no_veg_layout"))
        self.frame_3.raise_()
        self.add_to_cart_button.raise_()
        self.frame.raise_()
        self.cancel_button.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.gridLayoutWidget_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.add_to_cart_button.setText(_translate("Dialog", "Add to Cart", None))
        self.cancel_button.setText(_translate("Dialog", "Cancel", None))

