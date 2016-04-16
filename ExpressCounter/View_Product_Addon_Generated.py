# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/murat/Documents/designs/product_addon.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1284, 581)
        Form.setStyleSheet(_fromUtf8("QCheckBox {\n"
"    font: 18pt \"Ubuntu\";\n"
"   color:black;\n"
"}\n"
"\n"
"QWidget{\n"
"background:white;\n"
"}\n"
""))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 140, 1251, 201))
        self.frame.setStyleSheet(_fromUtf8("background:rgb(111, 255, 152);\n"
"color:black;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1231, 191))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.all_salad_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.all_salad_sel.setObjectName(_fromUtf8("all_salad_sel"))
        self.verticalLayout.addWidget(self.all_salad_sel)
        self.lorw_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.lorw_sel.setObjectName(_fromUtf8("lorw_sel"))
        self.verticalLayout.addWidget(self.lorw_sel)
        self.checkBox = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lettuce_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.lettuce_sel.setObjectName(_fromUtf8("lettuce_sel"))
        self.verticalLayout_2.addWidget(self.lettuce_sel)
        self.w_cabbage_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.w_cabbage_sel.setObjectName(_fromUtf8("w_cabbage_sel"))
        self.verticalLayout_2.addWidget(self.w_cabbage_sel)
        self.r_cabbage_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.r_cabbage_sel.setObjectName(_fromUtf8("r_cabbage_sel"))
        self.verticalLayout_2.addWidget(self.r_cabbage_sel)
        self.onion_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.onion_sel.setObjectName(_fromUtf8("onion_sel"))
        self.verticalLayout_2.addWidget(self.onion_sel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tomato_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.tomato_sel.setObjectName(_fromUtf8("tomato_sel"))
        self.verticalLayout_3.addWidget(self.tomato_sel)
        self.cucumber_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.cucumber_sel.setObjectName(_fromUtf8("cucumber_sel"))
        self.verticalLayout_3.addWidget(self.cucumber_sel)
        self.pickle_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.pickle_sel.setObjectName(_fromUtf8("pickle_sel"))
        self.verticalLayout_3.addWidget(self.pickle_sel)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(20, 350, 1251, 81))
        self.frame_2.setStyleSheet(_fromUtf8("background:rgb(255, 123, 46);\n"
"color:black;"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1251, 81))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.sauce_selection_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.sauce_selection_layout.setObjectName(_fromUtf8("sauce_selection_layout"))
        self.chilli_sauce_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.chilli_sauce_sel.setObjectName(_fromUtf8("chilli_sauce_sel"))
        self.sauce_selection_layout.addWidget(self.chilli_sauce_sel)
        self.mayo_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.mayo_sel.setObjectName(_fromUtf8("mayo_sel"))
        self.sauce_selection_layout.addWidget(self.mayo_sel)
        self.gm_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.gm_sel.setObjectName(_fromUtf8("gm_sel"))
        self.sauce_selection_layout.addWidget(self.gm_sel)
        self.ketchup_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.ketchup_sel.setObjectName(_fromUtf8("ketchup_sel"))
        self.sauce_selection_layout.addWidget(self.ketchup_sel)
        self.bbq_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.bbq_sel.setObjectName(_fromUtf8("bbq_sel"))
        self.sauce_selection_layout.addWidget(self.bbq_sel)
        self.relish_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.relish_sel.setObjectName(_fromUtf8("relish_sel"))
        self.sauce_selection_layout.addWidget(self.relish_sel)
        self.sweet_chill_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.sweet_chill_sel.setObjectName(_fromUtf8("sweet_chill_sel"))
        self.sauce_selection_layout.addWidget(self.sweet_chill_sel)
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(440, 30, 411, 101))
        self.frame_3.setStyleSheet(_fromUtf8("background:rgb(253, 255, 90);"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.type_sel = QtGui.QComboBox(self.frame_3)
        self.type_sel.setGeometry(QtCore.QRect(10, 20, 391, 61))
        self.type_sel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.type_sel.setStyleSheet(_fromUtf8("font: 45pt \"Ubuntu\";\n"
"color:black;\n"
"background:white;\n"
""))
        self.type_sel.setObjectName(_fromUtf8("type_sel"))
        self.type_sel.addItem(_fromUtf8(""))
        self.type_sel.addItem(_fromUtf8(""))
        self.frame_4 = QtGui.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(20, 30, 411, 101))
        self.frame_4.setStyleSheet(_fromUtf8("background:rgb(65, 221, 255)"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.size_sel = QtGui.QComboBox(self.frame_4)
        self.size_sel.setGeometry(QtCore.QRect(10, 20, 381, 61))
        self.size_sel.setStyleSheet(_fromUtf8("font: 45pt \"Ubuntu\";\n"
"background:white;\n"
"color:black;"))
        self.size_sel.setObjectName(_fromUtf8("size_sel"))
        self.size_sel.addItem(_fromUtf8(""))
        self.size_sel.addItem(_fromUtf8(""))
        self.add_to_cart_button = QtGui.QPushButton(Form)
        self.add_to_cart_button.setGeometry(QtCore.QRect(650, 450, 621, 121))
        self.add_to_cart_button.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:rgb(39, 255, 53);\n"
"color:black;\n"
" font: 30pt \"Ubuntu\";\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"}"))
        self.add_to_cart_button.setObjectName(_fromUtf8("add_to_cart_button"))
        self.cancel_button = QtGui.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(20, 450, 621, 121))
        self.cancel_button.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:rgb(255, 57, 43);\n"
"color:black;\n"
" font: 30pt \"Ubuntu\";\n"
" padding: 10px;\n"
" border-radius:5px 20px;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"}"))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.frame_5 = QtGui.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(860, 30, 411, 101))
        self.frame_5.setStyleSheet(_fromUtf8("background:rgb(143, 139, 255);"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.cheese_sel = QtGui.QComboBox(self.frame_5)
        self.cheese_sel.setGeometry(QtCore.QRect(10, 20, 391, 61))
        self.cheese_sel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cheese_sel.setStyleSheet(_fromUtf8("font: 45pt \"Ubuntu\";\n"
"color:black;\n"
"background:white;\n"
""))
        self.cheese_sel.setObjectName(_fromUtf8("cheese_sel"))
        self.cheese_sel.addItem(_fromUtf8(""))
        self.cheese_sel.addItem(_fromUtf8(""))
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.add_to_cart_button.raise_()
        self.cancel_button.raise_()
        self.type_sel.raise_()
        self.frame_5.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.all_salad_sel.setText(_translate("Form", "All Salad", None))
        self.lorw_sel.setText(_translate("Form", "L/O/R/W", None))
        self.checkBox.setText(_translate("Form", "Fried Specials", None))
        self.lettuce_sel.setText(_translate("Form", "Luttuce", None))
        self.w_cabbage_sel.setText(_translate("Form", "W Cabbage", None))
        self.r_cabbage_sel.setText(_translate("Form", "R Cabbage", None))
        self.onion_sel.setText(_translate("Form", "Onion", None))
        self.tomato_sel.setText(_translate("Form", "Tomato", None))
        self.cucumber_sel.setText(_translate("Form", "Cucumber", None))
        self.pickle_sel.setText(_translate("Form", "Pickle", None))
        self.chilli_sauce_sel.setText(_translate("Form", "Chilli Sauce", None))
        self.mayo_sel.setText(_translate("Form", "Mayonaise", None))
        self.gm_sel.setText(_translate("Form", "Garlic Mayo", None))
        self.ketchup_sel.setText(_translate("Form", "Kethcup", None))
        self.bbq_sel.setText(_translate("Form", "BBQ", None))
        self.relish_sel.setText(_translate("Form", "Relish", None))
        self.sweet_chill_sel.setText(_translate("Form", "Sweet Chilli", None))
        self.type_sel.setItemText(0, _translate("Form", "Pitta", None))
        self.type_sel.setItemText(1, _translate("Form", "Wrap", None))
        self.size_sel.setItemText(0, _translate("Form", "Small", None))
        self.size_sel.setItemText(1, _translate("Form", "Large", None))
        self.add_to_cart_button.setText(_translate("Form", "Add To Cart", None))
        self.cancel_button.setText(_translate("Form", "Cancel", None))
        self.cheese_sel.setItemText(0, _translate("Form", "No Cheese", None))
        self.cheese_sel.setItemText(1, _translate("Form", "Cheese", None))

