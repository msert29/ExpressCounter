# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_cart.ui'
#
# Created: Fri Dec 11 11:22:44 2015
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
        Dialog.resize(1920, 1080)
        
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
"}\n"
"\n"
"QFormLayout#customer_layout {\n"
"background-color : red;\n"
"}\n"
"QLineEdit {\n"
"min-height:30px;\n"
"text-align: center;\n"
"}\n"
"\n"
"\n"
""))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 70, 1011, 941))
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
        self.gridLayoutWidget_2 = QtGui.QWidget(self.kebab_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 991, 761))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.kebabs_layout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.kebabs_layout.setMargin(0)
        self.kebabs_layout.setObjectName(_fromUtf8("kebabs_layout"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.kebab_tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 780, 481, 80))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.custom_salad_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.custom_salad_layout.setMargin(0)
        self.custom_salad_layout.setObjectName(_fromUtf8("custom_salad_layout"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.kebab_tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(500, 780, 501, 80))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.custom_sauce_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.custom_sauce_layout.setMargin(0)
        self.custom_sauce_layout.setObjectName(_fromUtf8("custom_sauce_layout"))
        self.tabWidget.addTab(self.kebab_tab, _fromUtf8(""))
        self.pizza_tab = QtGui.QWidget()
        self.pizza_tab.setObjectName(_fromUtf8("pizza_tab"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.pizza_tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 981, 761))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.pizzas_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.pizzas_layout.setMargin(0)
        self.pizzas_layout.setObjectName(_fromUtf8("pizzas_layout"))
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.pizza_tab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 780, 981, 80))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.custom_topping_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.custom_topping_layout.setMargin(0)
        self.custom_topping_layout.setObjectName(_fromUtf8("custom_topping_layout"))
        self.tabWidget.addTab(self.pizza_tab, _fromUtf8(""))
        self.burger_tab = QtGui.QWidget()
        self.burger_tab.setObjectName(_fromUtf8("burger_tab"))
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.burger_tab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(500, 780, 501, 80))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.burger_sauce_layout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.burger_sauce_layout_2.setMargin(0)
        self.burger_sauce_layout_2.setObjectName(_fromUtf8("burger_sauce_layout_2"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.burger_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 991, 761))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.burgers_layout_2 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.burgers_layout_2.setMargin(0)
        self.burgers_layout_2.setObjectName(_fromUtf8("burgers_layout_2"))
        self.verticalLayoutWidget_8 = QtGui.QWidget(self.burger_tab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 780, 481, 80))
        self.verticalLayoutWidget_8.setObjectName(_fromUtf8("verticalLayoutWidget_8"))
        self.burger_salad_layout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_8)
        self.burger_salad_layout_2.setMargin(0)
        self.burger_salad_layout_2.setObjectName(_fromUtf8("burger_salad_layout_2"))
        self.tabWidget.addTab(self.burger_tab, _fromUtf8(""))
        self.other_tab = QtGui.QWidget()
        self.other_tab.setObjectName(_fromUtf8("other_tab"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.other_tab)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 981, 851))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.others_layout = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.others_layout.setMargin(0)
        self.others_layout.setObjectName(_fromUtf8("others_layout"))
        self.tabWidget.addTab(self.other_tab, _fromUtf8(""))
        self.cart_view = QtGui.QListWidget(Dialog)
        self.cart_view.setGeometry(QtCore.QRect(1060, 130, 371, 831))
        self.cart_view.setStyleSheet(_fromUtf8("background:rgb(240, 240, 240);\n"
""))
        self.cart_view.setObjectName(_fromUtf8("cart_view"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1060, 70, 371, 61))
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
"\n"
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
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(1450, 70, 461, 401))
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
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 70, 441, 311))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.customer_layout = QtGui.QFormLayout(self.formLayoutWidget)
        self.customer_layout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.customer_layout.setMargin(0)
        self.customer_layout.setObjectName(_fromUtf8("customer_layout"))
        self.customernameLabel = QtGui.QLabel(self.formLayoutWidget)
        self.customernameLabel.setObjectName(_fromUtf8("customernameLabel"))
        self.customer_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.customernameLabel)
        self.nameLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.customer_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameLineEdit)
        self.addressLabel = QtGui.QLabel(self.formLayoutWidget)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.customer_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.customeraddressLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.customeraddressLineEdit.setObjectName(_fromUtf8("customeraddressLineEdit"))
        self.customer_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.customeraddressLineEdit)
        self.postcodeLabel = QtGui.QLabel(self.formLayoutWidget)
        self.postcodeLabel.setObjectName(_fromUtf8("postcodeLabel"))
        self.customer_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.postcodeLabel)
        self.postcodeLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.postcodeLineEdit.setObjectName(_fromUtf8("postcodeLineEdit"))
        self.customer_layout.setWidget(2, QtGui.QFormLayout.FieldRole, self.postcodeLineEdit)
        self.telephoneLabel = QtGui.QLabel(self.formLayoutWidget)
        self.telephoneLabel.setObjectName(_fromUtf8("telephoneLabel"))
        self.customer_layout.setWidget(3, QtGui.QFormLayout.LabelRole, self.telephoneLabel)
        self.telephoneLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.telephoneLineEdit.setObjectName(_fromUtf8("telephoneLineEdit"))
        self.customer_layout.setWidget(3, QtGui.QFormLayout.FieldRole, self.telephoneLineEdit)
        self.dateOfOrderLabel = QtGui.QLabel(self.formLayoutWidget)
        self.dateOfOrderLabel.setObjectName(_fromUtf8("dateOfOrderLabel"))
        self.customer_layout.setWidget(4, QtGui.QFormLayout.LabelRole, self.dateOfOrderLabel)
        self.dateOfOrderDateEdit = QtGui.QDateEdit(self.formLayoutWidget)
        self.dateOfOrderDateEdit.setEnabled(False)
        self.dateOfOrderDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 3, 1), QtCore.QTime(0, 0, 0)))
        self.dateOfOrderDateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateOfOrderDateEdit.setCalendarPopup(True)
        self.dateOfOrderDateEdit.setObjectName(_fromUtf8("dateOfOrderDateEdit"))
        self.customer_layout.setWidget(4, QtGui.QFormLayout.FieldRole, self.dateOfOrderDateEdit)
        self.timeOfOrderLabel = QtGui.QLabel(self.formLayoutWidget)
        self.timeOfOrderLabel.setObjectName(_fromUtf8("timeOfOrderLabel"))
        self.customer_layout.setWidget(5, QtGui.QFormLayout.LabelRole, self.timeOfOrderLabel)
        self.timeOfOrderTimeEdit = QtGui.QTimeEdit(self.formLayoutWidget)
        self.timeOfOrderTimeEdit.setEnabled(False)
        self.timeOfOrderTimeEdit.setObjectName(_fromUtf8("timeOfOrderTimeEdit"))
        self.customer_layout.setWidget(5, QtGui.QFormLayout.FieldRole, self.timeOfOrderTimeEdit)
        self.existing_customer_confirm_button_2 = QtGui.QPushButton(self.formLayoutWidget)
        self.existing_customer_confirm_button_2.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: rgb(20, 255, 67);\n"
"color:black;\n"
"} "))
        self.existing_customer_confirm_button_2.setObjectName(_fromUtf8("existing_customer_confirm_button_2"))
        self.customer_layout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.existing_customer_confirm_button_2)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 461, 59))
        self.label_4.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"color:white;\n"
"text-align: center;\n"
"}\n"
"QLabel:hover {\n"
"background:rgb(77, 231, 100);\n"
"color:black;\n"
"}"))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tota_price_layout_frame = QtGui.QFrame(Dialog)
        self.tota_price_layout_frame.setGeometry(QtCore.QRect(1060, 960, 371, 51))
        self.tota_price_layout_frame.setStyleSheet(_fromUtf8("background:rgb(240, 240, 240);"))
        self.tota_price_layout_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tota_price_layout_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.tota_price_layout_frame.setObjectName(_fromUtf8("tota_price_layout_frame"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tota_price_layout_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 371, 51))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.price_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.price_layout.setMargin(0)
        self.price_layout.setObjectName(_fromUtf8("price_layout"))
        self.existing_customer_cancel_button = QtGui.QPushButton(Dialog)
        self.existing_customer_cancel_button.setGeometry(QtCore.QRect(1450, 950, 221, 61))
        self.existing_customer_cancel_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: red;\n"
"color:black;\n"
"} "))
        self.existing_customer_cancel_button.setObjectName(_fromUtf8("existing_customer_cancel_button"))
        self.existing_customer_confirm_button = QtGui.QPushButton(Dialog)
        self.existing_customer_confirm_button.setGeometry(QtCore.QRect(1680, 950, 221, 61))
        self.existing_customer_confirm_button.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: rgb(20, 255, 67);\n"
"color:black;\n"
"} "))
        self.existing_customer_confirm_button.setObjectName(_fromUtf8("existing_customer_confirm_button"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(1450, 490, 461, 451))
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
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 441, 231))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.customer_layout_2 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.customer_layout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.customer_layout_2.setMargin(0)
        self.customer_layout_2.setObjectName(_fromUtf8("customer_layout_2"))
        self.customernameLabel_2 = QtGui.QLabel(self.formLayoutWidget_3)
        self.customernameLabel_2.setObjectName(_fromUtf8("customernameLabel_2"))
        self.customer_layout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.customernameLabel_2)
        self.nameLineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.nameLineEdit_3.setObjectName(_fromUtf8("nameLineEdit_3"))
        self.customer_layout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameLineEdit_3)
        self.addressLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.addressLabel_3.setObjectName(_fromUtf8("addressLabel_3"))
        self.customer_layout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.addressLabel_3)
        self.customeraddressLineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.customeraddressLineEdit_2.setObjectName(_fromUtf8("customeraddressLineEdit_2"))
        self.customer_layout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.customeraddressLineEdit_2)
        self.postcodeLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.postcodeLabel_3.setObjectName(_fromUtf8("postcodeLabel_3"))
        self.customer_layout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.postcodeLabel_3)
        self.postcodeLineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.postcodeLineEdit_3.setObjectName(_fromUtf8("postcodeLineEdit_3"))
        self.customer_layout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.postcodeLineEdit_3)
        self.telephoneLabel_3 = QtGui.QLabel(self.formLayoutWidget_3)
        self.telephoneLabel_3.setObjectName(_fromUtf8("telephoneLabel_3"))
        self.customer_layout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.telephoneLabel_3)
        self.telephoneLineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.telephoneLineEdit_3.setObjectName(_fromUtf8("telephoneLineEdit_3"))
        self.customer_layout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.telephoneLineEdit_3)
        self.existing_customer_confirm_button_3 = QtGui.QPushButton(self.formLayoutWidget_3)
        self.existing_customer_confirm_button_3.setStyleSheet(_fromUtf8("QPushButton {\n"
" background: gray;\n"
" color:white;\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton::hover {\n"
"background: rgb(85, 170, 255);\n"
"color:black;\n"
"} "))
        self.existing_customer_confirm_button_3.setObjectName(_fromUtf8("existing_customer_confirm_button_3"))
        self.customer_layout_2.setWidget(4, QtGui.QFormLayout.SpanningRole, self.existing_customer_confirm_button_3)
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 461, 59))
        self.label_3.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"color:white;\n"
"text-align: center;\n"
"\n"
"}\n"
"QLabel:hover {\n"
"background:rgb(85, 170, 255);\n"
"color:black;\n"
"}"))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayoutWidget = QtGui.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 310, 441, 131))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.search_results_grid_layout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.search_results_grid_layout.setMargin(0)
        self.search_results_grid_layout.setObjectName(_fromUtf8("search_results_grid_layout"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.kebab_tab), _translate("Dialog", "Kebabs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pizza_tab), _translate("Dialog", "Pizzas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.burger_tab), _translate("Dialog", "Burgers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.other_tab), _translate("Dialog", "Others", None))
        self.label.setText(_translate("Dialog", "Order Summary", None))
        self.customernameLabel.setText(_translate("Dialog", "Name", None))
        self.addressLabel.setText(_translate("Dialog", "Address", None))
        self.postcodeLabel.setText(_translate("Dialog", "Postcode", None))
        self.telephoneLabel.setText(_translate("Dialog", "Telephone", None))
        self.dateOfOrderLabel.setText(_translate("Dialog", "Date of Order", None))
        self.timeOfOrderLabel.setText(_translate("Dialog", "Time of Order", None))
        self.existing_customer_confirm_button_2.setText(_translate("Dialog", "Add", None))
        self.label_4.setText(_translate("Dialog", "New customer Entry", None))
        self.existing_customer_cancel_button.setText(_translate("Dialog", "Cancel", None))
        self.existing_customer_confirm_button.setText(_translate("Dialog", "Confirm", None))
        self.customernameLabel_2.setText(_translate("Dialog", "Name", None))
        self.addressLabel_3.setText(_translate("Dialog", "Address", None))
        self.postcodeLabel_3.setText(_translate("Dialog", "Postcode", None))
        self.telephoneLabel_3.setText(_translate("Dialog", "Telephone", None))
        self.existing_customer_confirm_button_3.setText(_translate("Dialog", "Search", None))
        self.label_3.setText(_translate("Dialog", "Existing Customer Search", None))

