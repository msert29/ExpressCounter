# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/murat/Documents/designs/cart_widget.ui'
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

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(1280, 950)
        self.cart_view = QtGui.QListWidget(Widget)
        self.cart_view.setGeometry(QtCore.QRect(880, 90, 391, 721))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cart_view.setFont(font)
        self.cart_view.setStyleSheet(_fromUtf8(""))
        self.cart_view.setObjectName(_fromUtf8("cart_view"))
        self.tabWidget = QtGui.QTabWidget(Widget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 841, 921))
        self.tabWidget.setStyleSheet(_fromUtf8("QTabBar::tab {\n"
"background: gray;\n"
" color: white;\n"
" padding: 10px;\n"
"  border-style: outset;\n"
"   border-width: 2px;\n"
"   border-radius: 5px;\n"
"  border-color: beige;\n"
"  font: 15px;\n"
"  min-width: 7em;\n"
"  min-height:3em;\n"
" padding: 6px;\n"
" margin-bottom:5px;\n"
" margin-left: 5px;\n"
"}\n"
"QTabBar::tab:selected {\n"
" background: rgb(85, 170, 255);\n"
" color:black;\n"
"}"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.kebab_tab = QtGui.QWidget()
        self.kebab_tab.setObjectName(_fromUtf8("kebab_tab"))
        self.kebabs_frame = QtGui.QFrame(self.kebab_tab)
        self.kebabs_frame.setGeometry(QtCore.QRect(10, 10, 811, 821))
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
"font: 63 30pt \"Ubuntu\";\n"
"color:black;\n"
"margin-bottom:0px;\n"
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
"min-width:370px;\n"
"min-height:70;\n"
"padding-left:0px;\n"
"margin-top:5px;\n"
"}\n"
"QPushButton:hover {\n"
" background: rgb(255, 0, 0);\n"
" color:black;\n"
"}\n"
"QComboBox {\n"
"min-width:92px;\n"
"min-height:38;\n"
"margin-bottom:5px;\n"
"}"))
        self.kebabs_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.kebabs_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.kebabs_frame.setObjectName(_fromUtf8("kebabs_frame"))
        self.gridLayoutWidget = QtGui.QWidget(self.kebabs_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 821))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.kebabs_layout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.kebabs_layout.setObjectName(_fromUtf8("kebabs_layout"))
        self.tabWidget.addTab(self.kebab_tab, _fromUtf8(""))
        self.pizza_tab = QtGui.QWidget()
        self.pizza_tab.setObjectName(_fromUtf8("pizza_tab"))
        self.frame_2 = QtGui.QFrame(self.pizza_tab)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 801, 821))
        self.frame_2.setStyleSheet(_fromUtf8("QFrame {\n"
"border:none;\n"
"}\n"
"QGroupBox{\n"
"border: 1px solid rgb(150, 150, 150);\n"
"background-color:rgb(253, 253, 253);\n"
"border-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"max-width:950px;\n"
"max-height:185px;\n"
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
"}\n"
"\n"
"QCheckBox{\n"
"max-width:150px;\n"
"min-height:50;\n"
"font: 63 25pt \"Ubuntu\";\n"
"}\n"
"QComboBox {\n"
"max-width:150px;\n"
"min-height:50;\n"
"font: 63 30pt \"Ubuntu\";\n"
"}"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 821))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.pizzas_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.pizzas_layout.setObjectName(_fromUtf8("pizzas_layout"))
        self.tabWidget.addTab(self.pizza_tab, _fromUtf8(""))
        self.burger_tab = QtGui.QWidget()
        self.burger_tab.setObjectName(_fromUtf8("burger_tab"))
        self.burger_frame = QtGui.QFrame(self.burger_tab)
        self.burger_frame.setGeometry(QtCore.QRect(10, 10, 811, 821))
        self.burger_frame.setStyleSheet(_fromUtf8("QFrame {\n"
"border:none;\n"
"}\n"
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
"QLabel {\n"
"font: 63 30pt \"Ubuntu\";\n"
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
"min-height:70;\n"
"padding-left:0px;\n"
"}\n"
"QPushButton:hover {\n"
"  background: rgb(255, 0, 0);\n"
"  color:black;\n"
" }\n"
"QCheckBox{\n"
"max-width:150px;\n"
"min-height:50;\n"
"font: 63 15pt \"Ubuntu\";\n"
"}\n"
"QComboBox {\n"
"max-width:150px;\n"
"min-height:50;\n"
"}"))
        self.burger_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.burger_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.burger_frame.setObjectName(_fromUtf8("burger_frame"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.burger_frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 811, 821))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.burgers_layout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.burgers_layout_2.setObjectName(_fromUtf8("burgers_layout_2"))
        self.tabWidget.addTab(self.burger_tab, _fromUtf8(""))
        self.other_tab = QtGui.QWidget()
        self.other_tab.setObjectName(_fromUtf8("other_tab"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.other_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 811, 821))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.others_layout = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.others_layout.setObjectName(_fromUtf8("others_layout"))
        self.tabWidget.addTab(self.other_tab, _fromUtf8(""))
        self.drink_tab = QtGui.QWidget()
        self.drink_tab.setObjectName(_fromUtf8("drink_tab"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.drink_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 811, 821))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.drinks_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.drinks_layout.setObjectName(_fromUtf8("drinks_layout"))
        self.tabWidget.addTab(self.drink_tab, _fromUtf8(""))
        self.deal_tab = QtGui.QWidget()
        self.deal_tab.setObjectName(_fromUtf8("deal_tab"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.deal_tab)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 801, 811))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.deals_layout = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.deals_layout.setObjectName(_fromUtf8("deals_layout"))
        self.tabWidget.addTab(self.deal_tab, _fromUtf8(""))
        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(880, 10, 391, 71))
        self.label.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 20pt \"Ubuntu\";\n"
"background: gray;\n"
"color:white;\n"
"text-align: center;\n"
"}\n"
"QLabel:hover {\n"
"background:rgb(85, 170, 255);\n"
"color:black;\n"
"}"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 880, 191, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"background: rgb(171, 171, 171);\n"
"color:black;\n"
"}\n"
"QPushButton::hover{\n"
"background: rgb(37, 216, 67);\n"
"color:white;\n"
"}"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.frame = QtGui.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(880, 820, 391, 51))
        self.frame.setStyleSheet(_fromUtf8("border:1px solid rgb(181, 181, 181);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet(_fromUtf8("border: none;\n"
"font: 20pt Liberation Serif;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.total_price_display = QtGui.QHBoxLayout()
        self.total_price_display.setObjectName(_fromUtf8("total_price_display"))
        self.horizontalLayout.addLayout(self.total_price_display)
        self.pushButton = QtGui.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(880, 880, 191, 51))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"background: rgb(171, 171, 171);\n"
"color:black;\n"
"}\n"
"QPushButton::hover{\n"
"background: rgb(255, 0, 4);\n"
"color:white;\n"
"}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Widget)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.kebab_tab), _translate("Widget", "Kebabs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pizza_tab), _translate("Widget", "Pizzas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.burger_tab), _translate("Widget", "Burgers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.other_tab), _translate("Widget", "Others", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drink_tab), _translate("Widget", "Drinks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.deal_tab), _translate("Widget", "Deals", None))
        self.label.setText(_translate("Widget", "Order Summary", None))
        self.pushButton_2.setText(_translate("Widget", "Confirm", None))
        self.label_2.setText(_translate("Widget", "Total Price  £", None))
        self.pushButton.setText(_translate("Widget", "Cancel", None))

