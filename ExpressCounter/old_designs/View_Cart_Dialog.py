# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_cart.ui'
#
# Created: Sat Dec 12 07:47:35 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt 
from PyQt4.Qt import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox,\
    QComboBox, QPushButton, QCheckBox
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
"  margin-left: 5px;\n"
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
        self.frame_3 = QtGui.QFrame(self.kebab_tab)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 989, 759))
        self.frame_3.setStyleSheet(_fromUtf8("QFrame {\n"
" border:none;\n"
"}\n"
"QGroupBox {\n"
"border: 1px solid rgb(150, 150, 150);\n"
"background-color:rgb(253, 253, 253);\n"
"border-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-top-right-radius: 9px;\n"
"min-width:460px;\n"
"min-height:170px;\n"
"max-width:460px;\n"
"max-height:170px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 63 20pt \"Ubuntu\";\n"
"   color:black;\n"
"}\n"
"QPushButton {\n"
"background: rgb(252, 83, 86);\n"
"color:black;\n"
"border-radius:0px;\n"
"border: 1px solid rgb(150, 150, 150);\n"
"min-width:430px;\n"
"min-height:40px;\n"
"padding-left:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 0, 0);\n"
"  color:black;\n"
" }\n"
"\n"
"QComboBox {\n"
"min-width:215;\n"
"min-height:55;\n"
"}"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.frame_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 971, 731))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.kebabs_layout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.kebabs_layout.setMargin(0)
        self.kebabs_layout.setObjectName(_fromUtf8("kebabs_layout"))
        self.custom_Frame = QtGui.QFrame(self.kebab_tab)
        self.custom_Frame.setGeometry(QtCore.QRect(20, 750, 981, 55))
        self.custom_Frame.setStyleSheet(_fromUtf8("background:orange;\n"
"QCheckBox{\n"
"color:black;\n"
"}\n"
""))
        self.custom_Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.custom_Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.custom_Frame.setObjectName(_fromUtf8("custom_Frame"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.custom_Frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 981, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.custom_salads_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.custom_salads_layout.setMargin(0)
        self.custom_salads_layout.setObjectName(_fromUtf8("custom_salads_layout"))
        self.custom_Frame_2 = QtGui.QFrame(self.kebab_tab)
        self.custom_Frame_2.setGeometry(QtCore.QRect(20, 810, 981, 55))
        self.custom_Frame_2.setStyleSheet(_fromUtf8("background:rgb(92, 255, 165);\n"
"QCheckBox{\n"
"background:orange;\n"
"color:black;\n"
"}\n"
""))
        self.custom_Frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.custom_Frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.custom_Frame_2.setObjectName(_fromUtf8("custom_Frame_2"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.custom_Frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.custom_sauces_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.custom_sauces_layout.setMargin(0)
        self.custom_sauces_layout.setObjectName(_fromUtf8("custom_sauces_layout"))
        self.tabWidget.addTab(self.kebab_tab, _fromUtf8(""))
        self.pizza_tab = QtGui.QWidget()
        self.pizza_tab.setObjectName(_fromUtf8("pizza_tab"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.pizza_tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 981, 761))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.pizzas_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.pizzas_layout.setMargin(0)
        self.pizzas_layout.setObjectName(_fromUtf8("pizzas_layout"))
        self.frame_4 = QtGui.QFrame(self.pizza_tab)
        self.frame_4.setGeometry(QtCore.QRect(10, 780, 981, 80))
        self.frame_4.setStyleSheet(_fromUtf8("background:rgb(255, 147, 85);\n"
"color:black;"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.frame_4)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 981, 80))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget.addTab(self.pizza_tab, _fromUtf8(""))
        self.burger_tab = QtGui.QWidget()
        self.burger_tab.setObjectName(_fromUtf8("burger_tab"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.burger_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 991, 731))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.burgers_layout_2 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.burgers_layout_2.setMargin(0)
        self.burgers_layout_2.setObjectName(_fromUtf8("burgers_layout_2"))
        self.frame_7 = QtGui.QFrame(self.burger_tab)
        self.frame_7.setGeometry(QtCore.QRect(10, 750, 991, 55))
        self.frame_7.setStyleSheet(_fromUtf8("background:orange;\n"
"QCheckBox{\n"
"color:black;\n"
"}\n"
""))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.frame_7)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 991, 51))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.burger_custom_sauce_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.burger_custom_sauce_layout.setMargin(0)
        self.burger_custom_sauce_layout.setObjectName(_fromUtf8("burger_custom_sauce_layout"))
        self.frame_8 = QtGui.QFrame(self.burger_tab)
        self.frame_8.setGeometry(QtCore.QRect(10, 810, 991, 55))
        self.frame_8.setStyleSheet(_fromUtf8("background:rgb(92, 255, 165);\n"
"QCheckBox{\n"
"background:orange;\n"
"color:black;\n"
"}\n"
""))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.horizontalLayoutWidget_8 = QtGui.QWidget(self.frame_8)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 991, 51))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.burger_custom_salad_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.burger_custom_salad_layout.setMargin(0)
        self.burger_custom_salad_layout.setObjectName(_fromUtf8("burger_custom_salad_layout"))
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
        self.existing_customer_confirm_button_3.setCheckable(False)
        self.existing_customer_confirm_button_3.setDefault(False)
        self.existing_customer_confirm_button_3.setFlat(False)
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
        self.tabWidget.setCurrentIndex(2)
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



    """------------------------------------------------------------------------------
    Function           : display_kebabs
    Description        : This function retrieves a list of kebab options from the 
                         Controller_Cart_Dialog class. It then iterates through 
                         all of the options, creates a salad and sauce combobox
                         selection for each item and an add button for the item
                         to be added to the cart.
    Parameters         : kebabs_list (This parameter is fetched by Controller_Cart_Dialog
                         class which accesses the DatabaseConnection class -> get_kebabs()
                         method which iterates through the Items table in the database selecting
                         items with type = 'kebab' only. The list is then passed to this method
                         which is directly called in Controller_Cart_Dialog
    Returns            : Void
    ------------------------------------------------------------------------------"""
    def display_kebabs(self, kebabs_list):
        length = len(kebabs_list)
        place_holder = 0 #holds the position of widget
        for i in range(length):
            salad_options = ['All', 'L/O/R/W', 'No Salad', 'Custom Salad']
            sauce_options = ['Chilli Sauce', 'Garlic Mayo', 'Mayo', 'BBQ', 'No Sauce', 'Custom Sauce']
            salad_box     = QComboBox()
            sauce_box     = QComboBox()
            salad_box.addItems(salad_options)
            sauce_box.addItems(sauce_options)
            
            add_button = QPushButton("Add")
            widget_holder = QGroupBox()
            core = QVBoxLayout()
            top_layout = QVBoxLayout()
            bottom_layout = QHBoxLayout()
            add_button_holder = QVBoxLayout()
            add_button_holder.addWidget(add_button)
            name = QLabel(kebabs_list[i]['name'])
            name.setAlignment(Qt.AlignCenter)
            add_button_holder.setAlignment(Qt.AlignCenter)
            top_layout.addWidget(name)
            bottom_layout.addWidget(salad_box)
            bottom_layout.addWidget(sauce_box)
            core.addLayout(top_layout)
            core.addLayout(bottom_layout)
            core.addLayout(add_button_holder)
            
            widget_holder.setLayout(core)
            # Check for row
            if (i == 2) or (i == 3):
                self.kebabs_layout.addWidget(widget_holder, 1, place_holder)
            elif (i == 4) or (i == 5):
                self.kebabs_layout.addWidget(widget_holder, 2, place_holder)
            elif (i == 6) or (i == 7):
                self.kebabs_layout.addWidget(widget_holder, 3, place_holder)
            else:
                self.kebabs_layout.addWidget(widget_holder, 0, place_holder)
            # Increment the place holder
            if (place_holder == 1):
                place_holder = 0
            else:
                place_holder = 1
                
    
    """------------------------------------------------------------------------------
    Function           : display_salads_options
    Description        : This function retrieves a list of custom salad variables from
                         the Controller_Cart_Dialog class. It then creates 
                         dynamic variables to store each check box thus allowing user
                         to select specific salad options. 
                         This function is called directly by the Controller_Cart_Dialog.
    Parameters         : salad_list (A list of salad options available fetched by 
                         databaseConnection class, get_custom_salads method, which is 
                         retrieved by Controller_Cart_Dialog and passed to this function.
    Returns            : Void
    ------------------------------------------------------------------------------"""
    def display_salad_options(self, salad_list):
        tmp_holder = QHBoxLayout()
        tmp_group = QGroupBox()
        salads_length = len(salad_list)
        salads_var = [None] * salads_length
        for x in range(0, salads_length):
            salads_var[x] = salad_list[x]
            tmp_holder.addWidget(QCheckBox(salads_var[x]))
        tmp_group.setLayout(tmp_holder)
        self.custom_salads_layout.addWidget(tmp_group)
        
    """------------------------------------------------------------------------------
    Function           : display_sauce_options
    Description        :This function retrieves a list of custom salad variables from
                        the Controller_Cart_Dialog class. It then creates 
                        dynamic variables to store each check box thus allowing user
                        to select specific sauce options. 
                        This function is called directly by the Controller_Cart_Dialog.
    Parameters         : sauce_list (A list of sauce options available fetched by 
                         databaseConnection class, get_custom_salads method, which is 
                         retrieved by Controller_Cart_Dialog and passed to this function.
    Returns            : Void
    ------------------------------------------------------------------------------"""
    def display_sauce_options(self, sauce_list):
        tmp_holder = QHBoxLayout()
        tmp_group = QGroupBox()
        sauces_length = len(sauce_list)
        sauces_var = [None] * sauces_length
        for x in range(0, sauces_length):
            sauces_var[x] = sauce_list[x]
            tmp_holder.addWidget(QCheckBox(sauces_var[x]))
        tmp_group.setLayout(tmp_holder)
        self.custom_sauces_layout.addWidget(tmp_group)