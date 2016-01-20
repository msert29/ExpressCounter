# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order_display.ui'
#
# Created: Tue Jan 19 23:33:40 2016
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
        Dialog.resize(468, 948)
        self.print_button = QtGui.QPushButton(Dialog)
        self.print_button.setGeometry(QtCore.QRect(240, 880, 221, 61))
        self.print_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: rgb(69, 209, 0);\n"
"color:black;\n"
"} "))
        self.print_button.setObjectName(_fromUtf8("print_button"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 451, 861))
        self.frame_2.setStyleSheet(_fromUtf8("background:rgb(240, 240, 240);\n"
"font: 16pt \"Ubuntu\";\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 451, 59))
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
        self.searc_results_frame = QtGui.QFrame(self.frame_2)
        self.searc_results_frame.setGeometry(QtCore.QRect(0, 60, 451, 801))
        self.searc_results_frame.setStyleSheet(_fromUtf8("border:1px solid rgb(93, 93, 93);\n"
"font: 63 14pt \"Ubuntu\";\n"
"text-align:center;\n"
"border:0px;"))
        self.searc_results_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.searc_results_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.searc_results_frame.setObjectName(_fromUtf8("searc_results_frame"))
        self.verticalLayoutWidget = QtGui.QWidget(self.searc_results_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451, 131))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.customer_details_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.customer_details_layout.setMargin(0)
        self.customer_details_layout.setObjectName(_fromUtf8("customer_details_layout"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.searc_results_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 130, 451, 511))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.order_details_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.order_details_layout.setMargin(0)
        self.order_details_layout.setObjectName(_fromUtf8("order_details_layout"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.searc_results_frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 640, 451, 161))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.price_info = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.price_info.setMargin(0)
        self.price_info.setObjectName(_fromUtf8("price_info"))
        self.close_button = QtGui.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(10, 880, 221, 61))
        self.close_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: red;\n"
"color:black;\n"
"} "))
        self.close_button.setObjectName(_fromUtf8("close_button"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.print_button.setText(_translate("Dialog", "Print Order", None))
        self.label_3.setText(_translate("Dialog", "Order Search", None))
        self.close_button.setText(_translate("Dialog", "Close", None))

