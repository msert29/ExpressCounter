# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_Cart_resolution.ui'
#
# Created: Sat Jan 23 14:52:59 2016
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
        Dialog.resize(1280, 950)
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
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 841, 901))
        self.tabWidget.setStyleSheet(_fromUtf8(" QTabBar::tab {\n"
"  background: gray;\n"
"  color: white;\n"
"  padding: 10px;\n"
"   border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: 15px;\n"
"    min-width: 8em;\n"
"    min-height:3em;\n"
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
        self.kebabs_frame = QtGui.QFrame(self.kebab_tab)
        self.kebabs_frame.setGeometry(QtCore.QRect(10, 10, 811, 671))
        self.kebabs_frame.setStyleSheet(_fromUtf8("QFrame {\n"
" border:none;\n"
"}\n"
"QGroupBox {\n"
"border: 1px solid rgb(150, 150, 150);\n"
"background-color:rgb(253, 253, 253);\n"
"border-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-top-right-radius: 9px;\n"
"max-width:950px;\n"
"max-height:170px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 63 17pt \"Ubuntu\";\n"
"    color:black;\n"
"    margin-bottom:0px;\n"
"}\n"

"QPushButton {\n"
"background: rgb(252, 83, 86);\n"
"color:black;\n"
"border-radius:0px;\n"
"border: 1px solid rgb(150, 150, 150);\n"
"font: 63 10pt \"Ubuntu\";\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"min-width:370px;\n"
"max-height:700px;\n"
"padding-left:0px;\n"
"margin-top:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 0, 0);\n"
"  color:black;\n"
" }\n"
"\n"
"QComboBox {\n"
"min-width:92px;\n"
"min-height:38;\n"
"margin-bottom:5px;\n"
"}"))
        self.kebabs_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.kebabs_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.kebabs_frame.setObjectName(_fromUtf8("kebabs_frame"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.kebabs_frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 811, 671))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.kebabs_layout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.kebabs_layout.setMargin(0)
        self.kebabs_layout.setObjectName(_fromUtf8("kebabs_layout"))
        self.custom_Frame = QtGui.QFrame(self.kebab_tab)
        self.custom_Frame.setGeometry(QtCore.QRect(10, 690, 811, 61))
        self.custom_Frame.setStyleSheet(_fromUtf8("background:orange;\n"
"QCheckBox{\n"
"color:black;\n"
"}\n"
""))
        self.custom_Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.custom_Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.custom_Frame.setObjectName(_fromUtf8("custom_Frame"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.custom_Frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 811, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.custom_salads_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.custom_salads_layout.setMargin(0)
        self.custom_salads_layout.setObjectName(_fromUtf8("custom_salads_layout"))
        self.custom_Frame_2 = QtGui.QFrame(self.kebab_tab)
        self.custom_Frame_2.setGeometry(QtCore.QRect(10, 760, 811, 61))
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
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.custom_sauces_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.custom_sauces_layout.setMargin(0)
        self.custom_sauces_layout.setObjectName(_fromUtf8("custom_sauces_layout"))
        self.tabWidget.addTab(self.kebab_tab, _fromUtf8(""))
        self.pizza_tab = QtGui.QWidget()
        self.pizza_tab.setObjectName(_fromUtf8("pizza_tab"))
        self.frame_4 = QtGui.QFrame(self.pizza_tab)
        self.frame_4.setGeometry(QtCore.QRect(10, 730, 821, 91))
        self.frame_4.setStyleSheet(_fromUtf8("background:rgb(255, 147, 85);\n"
"color:black;"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.frame_4)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 821, 91))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pizza_frame = QtGui.QFrame(self.pizza_tab)
        self.pizza_frame.setGeometry(QtCore.QRect(10, 10, 821, 711))
        self.pizza_frame.setStyleSheet(_fromUtf8("QFrame {\n"
"border:none;\n}"
"QGroupBox {\n"
"border: 1px solid rgb(150, 150, 150);\n"
"background-color:rgb(253, 253, 253);\n"
"border-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"max-width:950px;\n"
"max-height:170px;\n"
"}\n"
"\n"
"QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"color:black;\n"
"}\n"
"QPushButton {\n"
"background: rgb(252, 83, 86);\n"
"color:black;\n"
"border-radius:0px;\n"
"border: 1px solid rgb(150, 150, 150);\n"
"font: 63 15pt \"Ubuntu\";\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"margin-top: 0px;\n"
"max-width:344px;\n"
"max-height:40px;\n"
"padding-left:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 0, 0);\n"
"  color:black;\n"
" }\n"
"\n"
"QCheckBox{\n"
"max-width:150px;\n"
"min-height:50;\n"
"font: 63 15pt \"Ubuntu\";\n"
"}"
"QComboBox {\n"
"max-width:150px;\n"
"min-height:50;\n"
"}"))
        self.pizza_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pizza_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.pizza_frame.setObjectName(_fromUtf8("pizza_frame"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.pizza_frame)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 821, 711))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.pizzas_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.pizzas_layout.setMargin(0)
        self.pizzas_layout.setObjectName(_fromUtf8("pizzas_layout"))
        self.tabWidget.addTab(self.pizza_tab, _fromUtf8(""))
        self.burger_tab = QtGui.QWidget()
        self.burger_tab.setObjectName(_fromUtf8("burger_tab"))
        self.frame_7 = QtGui.QFrame(self.burger_tab)
        self.frame_7.setGeometry(QtCore.QRect(10, 690, 811, 61))
        self.frame_7.setStyleSheet(_fromUtf8("background:orange;\n"
"QCheckBox{\n"
"color:black;\n"
"}\n"
""))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.frame_7)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.burger_custom_sauce_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.burger_custom_sauce_layout.setMargin(0)
        self.burger_custom_sauce_layout.setObjectName(_fromUtf8("burger_custom_sauce_layout"))
        self.frame_8 = QtGui.QFrame(self.burger_tab)
        self.frame_8.setGeometry(QtCore.QRect(10, 760, 811, 61))
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
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.burger_custom_salad_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.burger_custom_salad_layout.setMargin(0)
        self.burger_custom_salad_layout.setObjectName(_fromUtf8("burger_custom_salad_layout"))
        self.burgers_frame = QtGui.QFrame(self.burger_tab)
        self.burgers_frame.setGeometry(QtCore.QRect(10, 10, 811, 671))
        self.burgers_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.burgers_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.burgers_frame.setObjectName(_fromUtf8("burgers_frame"))
        self.burgers_frame.setStyleSheet(_fromUtf8("QFrame {\n"
"border:none;\n}"
"QGroupBox {\n"
"border: 1px solid rgb(150, 150, 150);\n"
"background-color:rgb(253, 253, 253);\n"
"border-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"max-width:950px;\n"
"max-height:170px;\n"
"}\n"
"\n"
"QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"color:black;\n"
"}\n"
"QPushButton {\n"
"background: rgb(252, 83, 86);\n"
"color:black;\n"
"border-radius:0px;\n"
"border: 1px solid rgb(150, 150, 150);\n"
"font: 63 15pt \"Ubuntu\";\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"margin-top: 0px;\n"
"min-width:370px;\n"
"max-height:40px;\n"
"padding-left:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 0, 0);\n"
"  color:black;\n"
" }\n"
"\n"
"QCheckBox{\n"
"max-width:150px;\n"
"min-height:50;\n"
"font: 63 15pt \"Ubuntu\";\n"
"}"
"QComboBox {\n"
"max-width:150px;\n"
"min-height:50;\n"
"}"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.burgers_frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 811, 671))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.burgers_layout_2 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.burgers_layout_2.setMargin(0)
        self.burgers_layout_2.setObjectName(_fromUtf8("burgers_layout_2"))
        self.tabWidget.addTab(self.burger_tab, _fromUtf8(""))
        self.other_tab = QtGui.QWidget()
        self.other_tab.setObjectName(_fromUtf8("other_tab"))
        self.others_frame = QtGui.QFrame(self.other_tab)
        self.others_frame.setGeometry(QtCore.QRect(10, 10, 811, 801))
        self.others_frame.setStyleSheet(_fromUtf8("QFrame {\n"
"border:none;\n"
"}"))
        self.others_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.others_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.others_frame.setObjectName(_fromUtf8("others_frame"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.others_frame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 811, 801))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.others_layout = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.others_layout.setMargin(0)
        self.others_layout.setObjectName(_fromUtf8("others_layout"))
        self.tabWidget.addTab(self.other_tab, _fromUtf8(""))
        self.drinks_tab = QtGui.QWidget()
        self.drinks_tab.setObjectName(_fromUtf8("drinks_tab"))
        self.tabWidget.addTab(self.drinks_tab, _fromUtf8(""))
        self.cart_view = QtGui.QListWidget(Dialog)
        self.cart_view.setGeometry(QtCore.QRect(880, 100, 391, 721))
        self.cart_view.setStyleSheet(_fromUtf8("background:rgb(240, 240, 240);\n"
"margin-top:5px;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border:1px solid rgb(195, 195, 195)"))
        self.cart_view.setObjectName(_fromUtf8("cart_view"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(880, 30, 391, 61))
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
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(880, 880, 191, 51))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"background: rgb(171, 171, 171);\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: rgb(255, 0, 4);\n"
"color:white;\n"
"}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 880, 191, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"background: rgb(171, 171, 171);\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: rgb(37, 216, 67);\n"
"color:white;\n"
"}"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(880, 830, 391, 41))

        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 211, 41))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_2.setStyleSheet(_fromUtf8("font: 20pt \"Liberation Serif\";"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 0, 181, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.total_price_display = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.total_price_display.setMargin(0)
        self.total_price_display.setObjectName(_fromUtf8("total_price_display"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.kebab_tab), _translate("Dialog", "Kebabs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pizza_tab), _translate("Dialog", "Pizzas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.burger_tab), _translate("Dialog", "Burgers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.other_tab), _translate("Dialog", "Others", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drinks_tab), _translate("Dialog", "Drinks", None))
        self.label.setText(_translate("Dialog", "Order Summary", None))
        self.pushButton.setText(_translate("Dialog", "Cancel", None))
        self.pushButton_2.setText(_translate("Dialog", "Confirm", None))
        self.label_2.setText(_translate("Dialog", "Total Price:  ", None))

