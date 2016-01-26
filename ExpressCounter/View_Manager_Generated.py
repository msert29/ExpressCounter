# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager_mode.ui'
#
# Created: Tue Jan 26 15:49:00 2016
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
        Dialog.resize(994, 950)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 961, 841))
        self.tabWidget.setStyleSheet(_fromUtf8(" QTabBar::tab {\n"
"  background: gray;\n"
"  color: white;\n"
"  padding: 10px;\n"
"   border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: 20px;\n"
"    min-width: 19.9em;\n"
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
        self.sales_tab = QtGui.QWidget()
        self.sales_tab.setObjectName(_fromUtf8("sales_tab"))
        self.table_search_result = QtGui.QTableWidget(self.sales_tab)
        self.table_search_result.setEnabled(True)
        self.table_search_result.setGeometry(QtCore.QRect(0, 60, 951, 571))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.table_search_result.setFont(font)
        self.table_search_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_search_result.setStyleSheet(_fromUtf8("font: 80 14pt \"Liberation Serif\";"))
        self.table_search_result.setShowGrid(True)
        self.table_search_result.setWordWrap(True)
        self.table_search_result.setCornerButtonEnabled(True)
        self.table_search_result.setColumnCount(8)
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
        self.table_search_result.horizontalHeader().setVisible(True)
        self.table_search_result.horizontalHeader().setCascadingSectionResizes(False)
        self.table_search_result.horizontalHeader().setDefaultSectionSize(105)
        self.table_search_result.horizontalHeader().setMinimumSectionSize(89)
        self.table_search_result.verticalHeader().setVisible(False)
        self.label = QtGui.QLabel(self.sales_tab)
        self.label.setGeometry(QtCore.QRect(10, 720, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("font: 18pt \"Liberation Serif\";\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.arrange = QtGui.QPushButton(self.sales_tab)
        self.arrange.setGeometry(QtCore.QRect(770, 720, 171, 41))
        self.arrange.setStyleSheet(_fromUtf8("font: 63 16pt \"Ubuntu\";\n"
""))
        self.arrange.setObjectName(_fromUtf8("arrange"))
        self.date_selection = QtGui.QDateEdit(self.sales_tab)
        self.date_selection.setGeometry(QtCore.QRect(170, 720, 581, 41))
        self.date_selection.setDate(QtCore.QDate(2016, 1, 20))
        self.date_selection.setMaximumDate(QtCore.QDate(2020, 12, 31))
        self.date_selection.setCurrentSection(QtGui.QDateTimeEdit.YearSection)
        self.date_selection.setCalendarPopup(True)
        self.date_selection.setObjectName(_fromUtf8("date_selection"))
        self.frame = QtGui.QFrame(self.sales_tab)
        self.frame.setGeometry(QtCore.QRect(-10, 630, 961, 80))
        self.frame.setStyleSheet(_fromUtf8("background:rgb(240, 240, 240);\n"
"font: 18pt \"Liberation Serif\";\n"
"\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.total_order = QtGui.QLineEdit(self.frame)
        self.total_order.setGeometry(QtCore.QRect(140, 20, 291, 35))
        self.total_order.setStyleSheet(_fromUtf8("background:white;"))
        self.total_order.setObjectName(_fromUtf8("total_order"))
        self.customernameLabel = QtGui.QLabel(self.frame)
        self.customernameLabel.setGeometry(QtCore.QRect(21, 20, 111, 35))
        self.customernameLabel.setObjectName(_fromUtf8("customernameLabel"))
        self.total_income = QtGui.QLineEdit(self.frame)
        self.total_income.setGeometry(QtCore.QRect(618, 20, 291, 35))
        self.total_income.setStyleSheet(_fromUtf8("background:white;"))
        self.total_income.setObjectName(_fromUtf8("total_income"))
        self.customernameLabel_2 = QtGui.QLabel(self.frame)
        self.customernameLabel_2.setGeometry(QtCore.QRect(460, 20, 151, 35))
        self.customernameLabel_2.setObjectName(_fromUtf8("customernameLabel_2"))
        self.label_4 = QtGui.QLabel(self.sales_tab)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 961, 59))
        self.label_4.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"color:white;\n"
"text-align: center;\n"
"background:rgb(85, 255, 0);\n"
"color:black;\n"
"}"))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.sales_tab, _fromUtf8(""))
        self.order_tab = QtGui.QWidget()
        self.order_tab.setObjectName(_fromUtf8("order_tab"))
        self.frame_2 = QtGui.QFrame(self.order_tab)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 941, 691))
        self.frame_2.setStyleSheet(_fromUtf8("border:1px solid black;\n"
"background : white;"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.delete_calendar = QtGui.QCalendarWidget(self.frame_2)
        self.delete_calendar.setGeometry(QtCore.QRect(20, 10, 911, 591))
        self.delete_calendar.setStyleSheet(_fromUtf8("border:none;\n"
"background:rgb(0, 170, 255);\n"
"color:black;"))
        self.delete_calendar.setObjectName(_fromUtf8("delete_calendar"))
        self.delete_date_button = QtGui.QPushButton(self.frame_2)
        self.delete_date_button.setGeometry(QtCore.QRect(20, 610, 451, 71))
        self.delete_date_button.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: rgb(255, 85, 0);\n"
"    font: 75 18pt \"Ubuntu\";\n"
"color:white;\n"
"border:none;\n"
"}"))
        self.delete_date_button.setObjectName(_fromUtf8("delete_date_button"))
        self.delete_all_orders_button = QtGui.QPushButton(self.frame_2)
        self.delete_all_orders_button.setGeometry(QtCore.QRect(480, 610, 451, 71))
        self.delete_all_orders_button.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: rgb(255, 0, 4);\n"
"    font: 75 18pt \"Ubuntu\";\n"
"color:white;\n"
"border:none;\n"
"}"))
        self.delete_all_orders_button.setObjectName(_fromUtf8("delete_all_orders_button"))
        self.label_3 = QtGui.QLabel(self.order_tab)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 991, 59))
        self.label_3.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"color:white;\n"
"text-align: center;\n"
"background:rgb(255, 85, 0);\n"
"color:black;\n"
"}"))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.order_tab, _fromUtf8(""))
        self.signout_button = QtGui.QPushButton(Dialog)
        self.signout_button.setGeometry(QtCore.QRect(10, 860, 961, 71))
        self.signout_button.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: rgb(255, 0, 4);\n"
"    font: 75 18pt \"Ubuntu\";\n"
"color:white;\n"
"border:none;\n"
"}"))
        self.signout_button.setObjectName(_fromUtf8("signout_button"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
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
        self.label.setText(_translate("Dialog", "Date of Order", None))
        self.arrange.setText(_translate("Dialog", "Arrange", None))
        self.date_selection.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd", None))
        self.customernameLabel.setText(_translate("Dialog", "Total Order", None))
        self.customernameLabel_2.setText(_translate("Dialog", "Total Income £", None))
        self.label_4.setText(_translate("Dialog", "View Sales", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sales_tab), _translate("Dialog", "Sales", None))
        self.delete_date_button.setText(_translate("Dialog", " Delete Specified Date ", None))
        self.delete_all_orders_button.setText(_translate("Dialog", "Delete All Orders", None))
        self.label_3.setText(_translate("Dialog", "Delete Orders", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.order_tab), _translate("Dialog", "Orders", None))
        self.signout_button.setText(_translate("Dialog", "Sign Out", None))

