# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer_mode.ui'
#
# Created: Mon Jan 25 14:43:16 2016
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
        Dialog.resize(977, 956)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 961, 821))
        self.tabWidget.setStyleSheet(_fromUtf8(" QTabBar::tab {\n"
"  background: gray;\n"
"  color: white;\n"
"  padding: 10px;\n"
"   border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: 20px;\n"
"    min-width: 13em;\n"
"    min-height:2em;\n"
"    padding: 6px;\n"
"   margin-bottom:5px;\n"
"  margin-left: 5px;\n"
" }\n"
" QTabBar::tab:selected {\n"
"  background: rgb(85, 170, 255);\n"
"  color:black;\n"
" }\n"
"\n"
""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.new_entry = QtGui.QWidget()
        self.new_entry.setObjectName(_fromUtf8("new_entry"))
        self.new_entry_frame = QtGui.QFrame(self.new_entry)
        self.new_entry_frame.setGeometry(QtCore.QRect(-1, -1, 961, 771))
        self.new_entry_frame.setStyleSheet(_fromUtf8("font:25pt \"Liberation Serif\";"))
        self.new_entry_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.new_entry_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.new_entry_frame.setObjectName(_fromUtf8("new_entry_frame"))
        self.newcustomer_label = QtGui.QLabel(self.new_entry_frame)
        self.newcustomer_label.setGeometry(QtCore.QRect(0, 0, 971, 71))
        self.newcustomer_label.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 30pt \"Ubuntu\";\n"
"background: gray;\n"
"color:black;\n"
"text-align: center;\n"
"background:rgb(77, 231, 100);\n"
"}\n"
""))
        self.newcustomer_label.setTextFormat(QtCore.Qt.AutoText)
        self.newcustomer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.newcustomer_label.setWordWrap(False)
        self.newcustomer_label.setObjectName(_fromUtf8("newcustomer_label"))
        self.formLayoutWidget = QtGui.QWidget(self.new_entry_frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 80, 921, 277))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.customer_layout = QtGui.QFormLayout(self.formLayoutWidget)
        self.customer_layout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.customer_layout.setMargin(0)
        self.customer_layout.setObjectName(_fromUtf8("customer_layout"))
        self.customernameLabel_5 = QtGui.QLabel(self.formLayoutWidget)
        self.customernameLabel_5.setObjectName(_fromUtf8("customernameLabel_5"))
        self.customer_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.customernameLabel_5)
        self.new_customer_name_entry = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_customer_name_entry.setObjectName(_fromUtf8("new_customer_name_entry"))
        self.customer_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self.new_customer_name_entry)
        self.addressLabel = QtGui.QLabel(self.formLayoutWidget)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.customer_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.new_customer_addr_entry = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_customer_addr_entry.setObjectName(_fromUtf8("new_customer_addr_entry"))
        self.customer_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.new_customer_addr_entry)
        self.postcodeLabel = QtGui.QLabel(self.formLayoutWidget)
        self.postcodeLabel.setObjectName(_fromUtf8("postcodeLabel"))
        self.customer_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.postcodeLabel)
        self.new_customer_postcode_entry = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_customer_postcode_entry.setObjectName(_fromUtf8("new_customer_postcode_entry"))
        self.customer_layout.setWidget(2, QtGui.QFormLayout.FieldRole, self.new_customer_postcode_entry)
        self.telephoneLabel = QtGui.QLabel(self.formLayoutWidget)
        self.telephoneLabel.setObjectName(_fromUtf8("telephoneLabel"))
        self.customer_layout.setWidget(3, QtGui.QFormLayout.LabelRole, self.telephoneLabel)
        self.new_customer_tel_entry = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_customer_tel_entry.setObjectName(_fromUtf8("new_customer_tel_entry"))
        self.customer_layout.setWidget(3, QtGui.QFormLayout.FieldRole, self.new_customer_tel_entry)
        self.add_customer_button = QtGui.QPushButton(self.formLayoutWidget)
        self.add_customer_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"    font: 63 25pt \"Ubuntu\";\n"
"}\n"
"QPushButton::hover {\n"
"background: rgb(20, 255, 67);\n"
"color:black;\n"
"} "))
        self.add_customer_button.setObjectName(_fromUtf8("add_customer_button"))
        self.customer_layout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.add_customer_button)
        self.tabWidget.addTab(self.new_entry, _fromUtf8(""))
        self.customer = QtGui.QWidget()
        self.customer.setObjectName(_fromUtf8("customer"))
        self.new_entry_frame_2 = QtGui.QFrame(self.customer)
        self.new_entry_frame_2.setGeometry(QtCore.QRect(0, 0, 961, 751))
        self.new_entry_frame_2.setStyleSheet(_fromUtf8("font:25pt \"Liberation Serif\";"))
        self.new_entry_frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.new_entry_frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.new_entry_frame_2.setObjectName(_fromUtf8("new_entry_frame_2"))
        self.newcustomer_label_2 = QtGui.QLabel(self.new_entry_frame_2)
        self.newcustomer_label_2.setGeometry(QtCore.QRect(0, 0, 971, 81))
        self.newcustomer_label_2.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 30pt \"Ubuntu\";\n"
"background: gray;\n"
"color:black;\n"
"text-align: center;\n"
"background:rgb(255, 170, 0);\n"
"}\n"
""))
        self.newcustomer_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.newcustomer_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.newcustomer_label_2.setWordWrap(False)
        self.newcustomer_label_2.setObjectName(_fromUtf8("newcustomer_label_2"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.new_entry_frame_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 92, 931, 277))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.customer_layout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.customer_layout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.customer_layout_2.setMargin(0)
        self.customer_layout_2.setObjectName(_fromUtf8("customer_layout_2"))
        self.customernameLabel_6 = QtGui.QLabel(self.formLayoutWidget_2)
        self.customernameLabel_6.setObjectName(_fromUtf8("customernameLabel_6"))
        self.customer_layout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.customernameLabel_6)
        self.name_search = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.name_search.setObjectName(_fromUtf8("name_search"))
        self.customer_layout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.name_search)
        self.addressLabel_2 = QtGui.QLabel(self.formLayoutWidget_2)
        self.addressLabel_2.setObjectName(_fromUtf8("addressLabel_2"))
        self.customer_layout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.addressLabel_2)
        self.add_search = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.add_search.setObjectName(_fromUtf8("add_search"))
        self.customer_layout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.add_search)
        self.postcodeLabel_2 = QtGui.QLabel(self.formLayoutWidget_2)
        self.postcodeLabel_2.setObjectName(_fromUtf8("postcodeLabel_2"))
        self.customer_layout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.postcodeLabel_2)
        self.postcode_search = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.postcode_search.setObjectName(_fromUtf8("postcode_search"))
        self.customer_layout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.postcode_search)
        self.telephoneLabel_2 = QtGui.QLabel(self.formLayoutWidget_2)
        self.telephoneLabel_2.setObjectName(_fromUtf8("telephoneLabel_2"))
        self.customer_layout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.telephoneLabel_2)
        self.tel_search = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.tel_search.setObjectName(_fromUtf8("tel_search"))
        self.customer_layout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.tel_search)
        self.existing_customer_search_button = QtGui.QPushButton(self.formLayoutWidget_2)
        self.existing_customer_search_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"    font: 63 25pt \"Ubuntu\";\n"
"}\n"
"QPushButton::hover {\n"
"background:rgb(255, 170, 0);\n"
"color:black;\n"
"} "))
        self.existing_customer_search_button.setObjectName(_fromUtf8("existing_customer_search_button"))
        self.customer_layout_2.setWidget(4, QtGui.QFormLayout.SpanningRole, self.existing_customer_search_button)
        self.formLayoutWidget_3 = QtGui.QWidget(self.new_entry_frame_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 470, 931, 281))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.customer_layout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.customer_layout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.customer_layout_3.setMargin(0)
        self.customer_layout_3.setObjectName(_fromUtf8("customer_layout_3"))
        self.customernameLabel_7 = QtGui.QLabel(self.formLayoutWidget_3)
        self.customernameLabel_7.setObjectName(_fromUtf8("customernameLabel_7"))
        self.customer_layout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.customernameLabel_7)
        self.addressLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.addressLabel_3.setObjectName(_fromUtf8("addressLabel_3"))
        self.customer_layout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.addressLabel_3)
        self.new_addr_entry = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.new_addr_entry.setObjectName(_fromUtf8("new_addr_entry"))
        self.customer_layout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.new_addr_entry)
        self.postcodeLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.postcodeLabel_3.setObjectName(_fromUtf8("postcodeLabel_3"))
        self.customer_layout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.postcodeLabel_3)
        self.new_postcode_entry = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.new_postcode_entry.setObjectName(_fromUtf8("new_postcode_entry"))
        self.customer_layout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.new_postcode_entry)
        self.telephoneLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.telephoneLabel_3.setObjectName(_fromUtf8("telephoneLabel_3"))
        self.customer_layout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.telephoneLabel_3)
        self.new_tel_entry = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.new_tel_entry.setObjectName(_fromUtf8("new_tel_entry"))
        self.customer_layout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.new_tel_entry)
        self.existing_customer_update_button = QtGui.QPushButton(self.formLayoutWidget_3)
        self.existing_customer_update_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"    font: 63 25pt \"Ubuntu\";\n"
"}\n"
"QPushButton::hover {\n"
"background:rgb(77, 231, 100);\n"
"color:black;\n"
"} "))
        self.existing_customer_update_button.setObjectName(_fromUtf8("existing_customer_update_button"))
        self.customer_layout_3.setWidget(4, QtGui.QFormLayout.SpanningRole, self.existing_customer_update_button)
        self.new_name_entry = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.new_name_entry.setObjectName(_fromUtf8("new_name_entry"))
        self.customer_layout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.new_name_entry)
        self.newcustomer_label_3 = QtGui.QLabel(self.new_entry_frame_2)
        self.newcustomer_label_3.setGeometry(QtCore.QRect(0, 380, 961, 81))
        self.newcustomer_label_3.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 30pt \"Ubuntu\";\n"
"background: gray;\n"
"color:black;\n"
"text-align: center;\n"
"background:rgb(77, 231, 100);\n"
"}\n"
""))
        self.newcustomer_label_3.setTextFormat(QtCore.Qt.AutoText)
        self.newcustomer_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.newcustomer_label_3.setWordWrap(False)
        self.newcustomer_label_3.setObjectName(_fromUtf8("newcustomer_label_3"))
        self.tabWidget.addTab(self.customer, _fromUtf8(""))
        self.delete_tab = QtGui.QWidget()
        self.delete_tab.setObjectName(_fromUtf8("delete_tab"))
        self.new_entry_frame_3 = QtGui.QFrame(self.delete_tab)
        self.new_entry_frame_3.setGeometry(QtCore.QRect(0, 0, 961, 771))
        self.new_entry_frame_3.setStyleSheet(_fromUtf8("font:25pt \"Liberation Serif\";"))
        self.new_entry_frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.new_entry_frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.new_entry_frame_3.setObjectName(_fromUtf8("new_entry_frame_3"))
        self.newcustomer_label_4 = QtGui.QLabel(self.new_entry_frame_3)
        self.newcustomer_label_4.setGeometry(QtCore.QRect(0, 0, 971, 71))
        self.newcustomer_label_4.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 30pt \"Ubuntu\";\n"
"background: gray;\n"
"color:black;\n"
"text-align: center;\n"
"background:rgb(255, 85, 0);\n"
"}\n"
""))
        self.newcustomer_label_4.setTextFormat(QtCore.Qt.AutoText)
        self.newcustomer_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.newcustomer_label_4.setWordWrap(False)
        self.newcustomer_label_4.setObjectName(_fromUtf8("newcustomer_label_4"))
        self.formLayoutWidget_4 = QtGui.QWidget(self.new_entry_frame_3)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(20, 80, 921, 277))
        self.formLayoutWidget_4.setObjectName(_fromUtf8("formLayoutWidget_4"))
        self.customer_layout_4 = QtGui.QFormLayout(self.formLayoutWidget_4)
        self.customer_layout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.customer_layout_4.setMargin(0)
        self.customer_layout_4.setObjectName(_fromUtf8("customer_layout_4"))
        self.customernameLabel_8 = QtGui.QLabel(self.formLayoutWidget_4)
        self.customernameLabel_8.setObjectName(_fromUtf8("customernameLabel_8"))
        self.customer_layout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.customernameLabel_8)
        self.new_name_edit_4 = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.new_name_edit_4.setObjectName(_fromUtf8("new_name_edit_4"))
        self.customer_layout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.new_name_edit_4)
        self.addressLabel_4 = QtGui.QLabel(self.formLayoutWidget_4)
        self.addressLabel_4.setObjectName(_fromUtf8("addressLabel_4"))
        self.customer_layout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.addressLabel_4)
        self.new_addr_edit_4 = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.new_addr_edit_4.setObjectName(_fromUtf8("new_addr_edit_4"))
        self.customer_layout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.new_addr_edit_4)
        self.postcodeLabel_4 = QtGui.QLabel(self.formLayoutWidget_4)
        self.postcodeLabel_4.setObjectName(_fromUtf8("postcodeLabel_4"))
        self.customer_layout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.postcodeLabel_4)
        self.new_postcode_edit_4 = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.new_postcode_edit_4.setObjectName(_fromUtf8("new_postcode_edit_4"))
        self.customer_layout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.new_postcode_edit_4)
        self.telephoneLabel_4 = QtGui.QLabel(self.formLayoutWidget_4)
        self.telephoneLabel_4.setObjectName(_fromUtf8("telephoneLabel_4"))
        self.customer_layout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.telephoneLabel_4)
        self.new_tel_edit_4 = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.new_tel_edit_4.setObjectName(_fromUtf8("new_tel_edit_4"))
        self.customer_layout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.new_tel_edit_4)
        self.delete_customer_search_button = QtGui.QPushButton(self.formLayoutWidget_4)
        self.delete_customer_search_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"    font: 63 25pt \"Ubuntu\";\n"
"}\n"
"QPushButton::hover {\n"
"background:rgb(255, 85, 0);\n"
"color:black;\n"
"} "))
        self.delete_customer_search_button.setObjectName(_fromUtf8("delete_customer_search_button"))
        self.customer_layout_4.setWidget(4, QtGui.QFormLayout.SpanningRole, self.delete_customer_search_button)
        self.delete_table_search = QtGui.QTableWidget(self.new_entry_frame_3)
        self.delete_table_search.setGeometry(QtCore.QRect(20, 370, 921, 371))
        self.delete_table_search.setStyleSheet(_fromUtf8("font: 16pt \"Liberation Serif\";"))
        self.delete_table_search.setObjectName(_fromUtf8("delete_table_search"))
        self.delete_table_search.setColumnCount(6)
        self.delete_table_search.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.delete_table_search.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.delete_table_search.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.delete_table_search.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.delete_table_search.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.delete_table_search.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.delete_table_search.setHorizontalHeaderItem(5, item)
        self.delete_table_search.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.delete_tab, _fromUtf8(""))
        self.exit_button = QtGui.QPushButton(Dialog)
        self.exit_button.setGeometry(QtCore.QRect(10, 860, 961, 81))
        self.exit_button.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: rgb(255, 0, 4);\n"
"    font: 75 20pt \"Ubuntu\";\n"
"color:white;\n"
"border:none;\n"
"}\n"
""))
        self.exit_button.setObjectName(_fromUtf8("exit_button"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.newcustomer_label.setText(_translate("Dialog", "New Customer Entry", None))
        self.customernameLabel_5.setText(_translate("Dialog", "Name", None))
        self.addressLabel.setText(_translate("Dialog", "Address", None))
        self.postcodeLabel.setText(_translate("Dialog", "Postcode", None))
        self.telephoneLabel.setText(_translate("Dialog", "Telephone", None))
        self.add_customer_button.setText(_translate("Dialog", "Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_entry), _translate("Dialog", "New Entry", None))
        self.newcustomer_label_2.setText(_translate("Dialog", "Update Customer Entry", None))
        self.customernameLabel_6.setText(_translate("Dialog", "Name", None))
        self.addressLabel_2.setText(_translate("Dialog", "Address", None))
        self.postcodeLabel_2.setText(_translate("Dialog", "Postcode", None))
        self.telephoneLabel_2.setText(_translate("Dialog", "Telephone", None))
        self.existing_customer_search_button.setText(_translate("Dialog", "Search", None))
        self.customernameLabel_7.setText(_translate("Dialog", "Name", None))
        self.addressLabel_3.setText(_translate("Dialog", "Address", None))
        self.postcodeLabel_3.setText(_translate("Dialog", "Postcode", None))
        self.telephoneLabel_3.setText(_translate("Dialog", "Telephone", None))
        self.existing_customer_update_button.setText(_translate("Dialog", "Update", None))
        self.newcustomer_label_3.setText(_translate("Dialog", "New Customer Details", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customer), _translate("Dialog", "Update", None))
        self.newcustomer_label_4.setText(_translate("Dialog", "Delete an Existig Customer", None))
        self.customernameLabel_8.setText(_translate("Dialog", "Name", None))
        self.addressLabel_4.setText(_translate("Dialog", "Address", None))
        self.postcodeLabel_4.setText(_translate("Dialog", "Postcode", None))
        self.telephoneLabel_4.setText(_translate("Dialog", "Telephone", None))
        self.delete_customer_search_button.setText(_translate("Dialog", "Search", None))
        item = self.delete_table_search.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID", None))
        item = self.delete_table_search.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name", None))
        item = self.delete_table_search.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Address", None))
        item = self.delete_table_search.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Postcode", None))
        item = self.delete_table_search.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Number", None))
        item = self.delete_table_search.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.delete_tab), _translate("Dialog", "Delete", None))
        self.exit_button.setText(_translate("Dialog", "Exit", None))

