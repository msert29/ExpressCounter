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
        Dialog.resize(788, 641)
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(400, 20, 371, 501))
        self.frame_3.setStyleSheet(_fromUtf8("background:rgb(103, 255, 121);\n"
"font: 18pt \"Ubuntu\";\n"
""))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.frame_3)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 371, 501))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.veg_topping_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.veg_topping_layout.setObjectName(_fromUtf8("veg_topping_layout"))
        self.add_to_cart_button = QtGui.QPushButton(Dialog)
        self.add_to_cart_button.setGeometry(QtCore.QRect(400, 530, 371, 91))
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
        self.frame.setGeometry(QtCore.QRect(20, 20, 371, 501))
        self.frame.setStyleSheet(_fromUtf8("background:rgb(255, 211, 51);\n"
"font: 18pt \"Ubuntu\";"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 371, 501))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.meat_topping_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.meat_topping_layout.setObjectName(_fromUtf8("meat_topping_layout"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(370, 90, 371, 451))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.frame_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 351, 431))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(20, 530, 371, 91))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.add_to_cart_button.setText(_translate("Dialog", "Add to Cart", None))
        self.cancel_button.setText(_translate("Dialog", "Cancel", None))

