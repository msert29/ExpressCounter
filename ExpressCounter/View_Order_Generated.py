# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order_search.ui'
#
# Created: Mon Jan 25 20:48:19 2016
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
        Dialog.resize(998, 948)
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(10, 880, 971, 61))
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
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 971, 861))
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
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 951, 261))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.customer_layout_2 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.customer_layout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.customer_layout_2.setMargin(0)
        self.customer_layout_2.setObjectName(_fromUtf8("customer_layout_2"))
        self.customernameLabel_2 = QtGui.QLabel(self.formLayoutWidget_3)
        self.customernameLabel_2.setObjectName(_fromUtf8("customernameLabel_2"))
        self.customer_layout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.customernameLabel_2)
        self.order_search_box = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.order_search_box.setStyleSheet(_fromUtf8("background:white;"))
        self.order_search_box.setObjectName(_fromUtf8("order_search_box"))
        self.customer_layout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.order_search_box)
        self.addressLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.addressLabel_3.setObjectName(_fromUtf8("addressLabel_3"))
        self.customer_layout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.addressLabel_3)
        self.name_search_box = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.name_search_box.setStyleSheet(_fromUtf8("background:white;"))
        self.name_search_box.setObjectName(_fromUtf8("name_search_box"))
        self.customer_layout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.name_search_box)
        self.postcodeLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.postcodeLabel_3.setObjectName(_fromUtf8("postcodeLabel_3"))
        self.customer_layout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.postcodeLabel_3)
        self.address_search_box = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.address_search_box.setStyleSheet(_fromUtf8("background:white;"))
        self.address_search_box.setObjectName(_fromUtf8("address_search_box"))
        self.customer_layout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.address_search_box)
        self.telephoneLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.telephoneLabel_3.setObjectName(_fromUtf8("telephoneLabel_3"))
        self.customer_layout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.telephoneLabel_3)
        self.postcode_search_box = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.postcode_search_box.setStyleSheet(_fromUtf8("background:white;"))
        self.postcode_search_box.setObjectName(_fromUtf8("postcode_search_box"))
        self.customer_layout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.postcode_search_box)
        self.telephoneLabel_4 = QtGui.QLabel(self.formLayoutWidget_3)
        self.telephoneLabel_4.setObjectName(_fromUtf8("telephoneLabel_4"))
        self.customer_layout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.telephoneLabel_4)
        self.tel_search_box = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.tel_search_box.setStyleSheet(_fromUtf8("background:white;"))
        self.tel_search_box.setObjectName(_fromUtf8("tel_search_box"))
        self.customer_layout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.tel_search_box)
        self.search_button = QtGui.QPushButton(self.formLayoutWidget_3)
        self.search_button.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.search_button.setCheckable(False)
        self.search_button.setDefault(False)
        self.search_button.setFlat(False)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.customer_layout_2.setWidget(5, QtGui.QFormLayout.SpanningRole, self.search_button)
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 971, 59))
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
        self.searc_results_frame.setGeometry(QtCore.QRect(10, 390, 951, 461))
        self.searc_results_frame.setStyleSheet(_fromUtf8("border:1px solid rgb(93, 93, 93);"))
        self.searc_results_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.searc_results_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.searc_results_frame.setObjectName(_fromUtf8("searc_results_frame"))
        self.verticalLayoutWidget = QtGui.QWidget(self.searc_results_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 951, 461))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.search_results_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.search_results_layout.setMargin(0)
        self.search_results_layout.setObjectName(_fromUtf8("search_results_layout"))
        self.table_search_result = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.table_search_result.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.table_search_result.setFont(font)
        self.table_search_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_search_result.setStyleSheet(_fromUtf8(""))
        self.table_search_result.setShowGrid(True)
        self.table_search_result.setWordWrap(True)
        self.table_search_result.setCornerButtonEnabled(True)
        self.table_search_result.setColumnCount(9)
        self.table_search_result.setObjectName(_fromUtf8("table_search_result"))
        self.table_search_result.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_search_result.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_search_result.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_search_result.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_search_result.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_search_result.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_search_result.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table_search_result.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table_search_result.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.table_search_result.setHorizontalHeaderItem(8, item)
        self.table_search_result.horizontalHeader().setVisible(True)
        self.table_search_result.horizontalHeader().setCascadingSectionResizes(False)
        self.table_search_result.horizontalHeader().setDefaultSectionSize(105)
        self.table_search_result.horizontalHeader().setMinimumSectionSize(89)
        self.table_search_result.verticalHeader().setVisible(False)
        self.search_results_layout.addWidget(self.table_search_result)
        self.results_label = QtGui.QLabel(self.frame_2)
        self.results_label.setGeometry(QtCore.QRect(10, 340, 951, 41))
        self.results_label.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"text-align: center;\n"
"background:rgb(255, 255, 0);\n"
"color:black;\n"
"}"))
        self.results_label.setAlignment(QtCore.Qt.AlignCenter)
        self.results_label.setObjectName(_fromUtf8("results_label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.cancel_button.setText(_translate("Dialog", "Close", None))
        self.customernameLabel_2.setText(_translate("Dialog", "Order ID", None))
        self.addressLabel_3.setText(_translate("Dialog", "Name", None))
        self.postcodeLabel_3.setText(_translate("Dialog", "Address", None))
        self.telephoneLabel_3.setText(_translate("Dialog", "Postcode", None))
        self.telephoneLabel_4.setText(_translate("Dialog", "Telephone", None))
        self.search_button.setText(_translate("Dialog", "Search", None))
        self.label_3.setText(_translate("Dialog", "Order Search", None))
        item = self.table_search_result.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID", None))
        item = self.table_search_result.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name", None))
        item = self.table_search_result.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Address", None))
        item = self.table_search_result.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Postcode", None))
        item = self.table_search_result.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Telephone", None))
        item = self.table_search_result.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Price", None))
        item = self.table_search_result.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Date", None))
        item = self.table_search_result.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Time", None))
        item = self.table_search_result.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Display", None))
        self.results_label.setText(_translate("Dialog", "Results", None))

