# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer_details.ui'
#
# Created: Sun Dec 27 18:34:51 2015
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
        Dialog.resize(471, 948)
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(10, 880, 221, 61))
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
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 320, 451, 551))
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
        self.formLayoutWidget_3 = QtGui.QWidget(self.frame_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 431, 221))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.customer_layout_2 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.customer_layout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.customer_layout_2.setMargin(0)
        self.customer_layout_2.setObjectName(_fromUtf8("customer_layout_2"))
        self.customernameLabel_2 = QtGui.QLabel(self.formLayoutWidget_3)
        self.customernameLabel_2.setObjectName(_fromUtf8("customernameLabel_2"))
        self.customer_layout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.customernameLabel_2)
        self.ex_name_edit = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.ex_name_edit.setObjectName(_fromUtf8("ex_name_edit"))
        self.customer_layout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.ex_name_edit)
        self.addressLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.addressLabel_3.setObjectName(_fromUtf8("addressLabel_3"))
        self.customer_layout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.addressLabel_3)
        self.ex_addr_edit = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.ex_addr_edit.setObjectName(_fromUtf8("ex_addr_edit"))
        self.customer_layout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.ex_addr_edit)
        self.postcodeLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.postcodeLabel_3.setObjectName(_fromUtf8("postcodeLabel_3"))
        self.customer_layout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.postcodeLabel_3)
        self.ex_postcode_edit = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.ex_postcode_edit.setObjectName(_fromUtf8("ex_postcode_edit"))
        self.customer_layout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.ex_postcode_edit)
        self.telephoneLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.telephoneLabel_3.setObjectName(_fromUtf8("telephoneLabel_3"))
        self.customer_layout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.telephoneLabel_3)
        self.ex_tel_edit = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.ex_tel_edit.setObjectName(_fromUtf8("ex_tel_edit"))
        self.customer_layout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.ex_tel_edit)
        self.ex_search_button = QtGui.QPushButton(self.formLayoutWidget_3)
        self.ex_search_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background:rgb(255, 170, 0);\n"
"color:black;\n"
"} \n"
""))
        self.ex_search_button.setCheckable(False)
        self.ex_search_button.setDefault(False)
        self.ex_search_button.setFlat(False)
        self.ex_search_button.setObjectName(_fromUtf8("ex_search_button"))
        self.customer_layout_2.setWidget(4, QtGui.QFormLayout.SpanningRole, self.ex_search_button)
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 451, 59))
        self.label_3.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"color:white;\n"
"text-align: center;\n"
"background:rgb(255, 170, 0);\n"
"color:black;\n"
"}"))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.searc_results_frame = QtGui.QFrame(self.frame_2)
        self.searc_results_frame.setGeometry(QtCore.QRect(10, 340, 431, 201))
        self.searc_results_frame.setStyleSheet(_fromUtf8("border:1px solid rgb(93, 93, 93);"))
        self.searc_results_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.searc_results_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.searc_results_frame.setObjectName(_fromUtf8("searc_results_frame"))
        self.verticalLayoutWidget = QtGui.QWidget(self.searc_results_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 201))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.search_results_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.search_results_layout.setMargin(0)
        self.search_results_layout.setObjectName(_fromUtf8("search_results_layout"))
        self.results_label = QtGui.QLabel(self.frame_2)
        self.results_label.setGeometry(QtCore.QRect(10, 290, 431, 41))
        self.results_label.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"text-align: center;\n"
"background:rgb(255, 255, 0);\n"
"color:black;\n"
"}"))
        self.results_label.setObjectName(_fromUtf8("results_label"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 451, 301))
        self.frame.setStyleSheet(_fromUtf8("background:rgb(240, 240, 240);\n"
"font: 16pt \"Ubuntu\";\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayoutWidget = QtGui.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 70, 431, 221))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.customer_layout = QtGui.QFormLayout(self.formLayoutWidget)
        self.customer_layout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.customer_layout.setMargin(0)
        self.customer_layout.setObjectName(_fromUtf8("customer_layout"))
        self.customernameLabel = QtGui.QLabel(self.formLayoutWidget)
        self.customernameLabel.setObjectName(_fromUtf8("customernameLabel"))
        self.customer_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.customernameLabel)
        self.addressLabel = QtGui.QLabel(self.formLayoutWidget)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.customer_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.new_addr_edit = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_addr_edit.setObjectName(_fromUtf8("new_addr_edit"))
        self.customer_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.new_addr_edit)
        self.postcodeLabel = QtGui.QLabel(self.formLayoutWidget)
        self.postcodeLabel.setObjectName(_fromUtf8("postcodeLabel"))
        self.customer_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.postcodeLabel)
        self.new_postcode_edit = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_postcode_edit.setObjectName(_fromUtf8("new_postcode_edit"))
        self.customer_layout.setWidget(2, QtGui.QFormLayout.FieldRole, self.new_postcode_edit)
        self.telephoneLabel = QtGui.QLabel(self.formLayoutWidget)
        self.telephoneLabel.setObjectName(_fromUtf8("telephoneLabel"))
        self.customer_layout.setWidget(3, QtGui.QFormLayout.LabelRole, self.telephoneLabel)
        self.new_tel_edit = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_tel_edit.setObjectName(_fromUtf8("new_tel_edit"))
        self.customer_layout.setWidget(3, QtGui.QFormLayout.FieldRole, self.new_tel_edit)
        self.new_add_button = QtGui.QPushButton(self.formLayoutWidget)
        self.new_add_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: rgb(20, 255, 67);\n"
"color:black;\n"
"} "))
        self.new_add_button.setObjectName(_fromUtf8("new_add_button"))
        self.customer_layout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.new_add_button)
        self.new_name_edit = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_name_edit.setObjectName(_fromUtf8("new_name_edit"))
        self.customer_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self.new_name_edit)
        self.newcustomer_label = QtGui.QLabel(self.frame)
        self.newcustomer_label.setGeometry(QtCore.QRect(0, 0, 461, 59))
        self.newcustomer_label.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"color:white;\n"
"text-align: center;\n"
"}\n"
"QLabel {\n"
"background:rgb(77, 231, 100);\n"
"color:black;\n"
"}"))
        self.newcustomer_label.setTextFormat(QtCore.Qt.AutoText)
        self.newcustomer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.newcustomer_label.setWordWrap(False)
        self.newcustomer_label.setObjectName(_fromUtf8("newcustomer_label"))
        self.confirm_button = QtGui.QPushButton(Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(240, 880, 221, 61))
        self.confirm_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: rgb(20, 255, 67);\n"
"color:black;\n"
"} "))
        self.confirm_button.setObjectName(_fromUtf8("confirm_button"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.cancel_button.setText(_translate("Dialog", "Cancel", None))
        self.customernameLabel_2.setText(_translate("Dialog", "Name", None))
        self.addressLabel_3.setText(_translate("Dialog", "Address", None))
        self.postcodeLabel_3.setText(_translate("Dialog", "Postcode", None))
        self.telephoneLabel_3.setText(_translate("Dialog", "Telephone", None))
        self.ex_search_button.setText(_translate("Dialog", "Search", None))
        self.label_3.setText(_translate("Dialog", "Existing Customer Search", None))
        self.results_label.setText(_translate("Dialog", "                             Results", None))
        self.customernameLabel.setText(_translate("Dialog", "Name", None))
        self.addressLabel.setText(_translate("Dialog", "Address", None))
        self.postcodeLabel.setText(_translate("Dialog", "Postcode", None))
        self.telephoneLabel.setText(_translate("Dialog", "Telephone", None))
        self.new_add_button.setText(_translate("Dialog", "Add", None))
        self.newcustomer_label.setText(_translate("Dialog", "New customer Entry", None))
        self.confirm_button.setText(_translate("Dialog", "Confirm", None))

