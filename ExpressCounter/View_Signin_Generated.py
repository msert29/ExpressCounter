# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager_log_in.ui'
#
# Created: Wed Jan 20 14:59:46 2016
#      by: PyQt4 UI code generator 4.10.4
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
        Dialog.resize(511, 332)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 511, 331))
        self.frame.setStyleSheet(_fromUtf8("border:1px solid black;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.login_button = QtGui.QPushButton(self.frame)
        self.login_button.setGeometry(QtCore.QRect(10, 190, 481, 61))
        self.login_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"font: 63 18pt \"Ubuntu\";\n"
"}\n"
"QPushButton::hover {\n"
"background:rgb(43, 255, 50);\n"
"color:black;\n"
"\n"
"} \n"
"\n"
""))
        self.login_button.setCheckable(False)
        self.login_button.setDefault(False)
        self.login_button.setFlat(False)
        self.login_button.setObjectName(_fromUtf8("login_button"))
        self.close_button = QtGui.QPushButton(self.frame)
        self.close_button.setGeometry(QtCore.QRect(10, 260, 481, 61))
        self.close_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"font: 63 18pt \"Ubuntu\";\n"
"}\n"
"QPushButton::hover {\n"
"background:red;\n"
"color:black;\n"
"} \n"
""))
        self.close_button.setCheckable(False)
        self.close_button.setDefault(False)
        self.close_button.setFlat(False)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.account_name = QtGui.QLineEdit(self.frame)
        self.account_name.setGeometry(QtCore.QRect(150, 84, 341, 41))
        self.account_name.setObjectName(_fromUtf8("account_name"))
        self.password = QtGui.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(150, 134, 341, 41))
        self.password.setObjectName(_fromUtf8("password"))
        self.customernameLabel_2 = QtGui.QLabel(self.frame)
        self.customernameLabel_2.setGeometry(QtCore.QRect(10, 90, 141, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.customernameLabel_2.setFont(font)
        self.customernameLabel_2.setStyleSheet(_fromUtf8("border:none;"))
        self.customernameLabel_2.setObjectName(_fromUtf8("customernameLabel_2"))
        self.customernameLabel_3 = QtGui.QLabel(self.frame)
        self.customernameLabel_3.setGeometry(QtCore.QRect(10, 130, 131, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.customernameLabel_3.setFont(font)
        self.customernameLabel_3.setStyleSheet(_fromUtf8("border:none;"))
        self.customernameLabel_3.setObjectName(_fromUtf8("customernameLabel_3"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 511, 59))
        self.label_3.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"color:white;\n"
"text-align: center;\n"
"background:rgb(85, 170, 255);\n"
"color:black;\n"
"}"))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.login_button.setText(_translate("Dialog", "Log In", None))
        self.close_button.setText(_translate("Dialog", "Close", None))
        self.customernameLabel_2.setText(_translate("Dialog", "Account Name", None))
        self.customernameLabel_3.setText(_translate("Dialog", "Password", None))
        self.label_3.setText(_translate("Dialog", "Manager Sign In", None))

