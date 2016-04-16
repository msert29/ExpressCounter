# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/murat/Documents/designs/product_addon_widget.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(1288, 763)
        Dialog.setStyleSheet(_fromUtf8("QCheckBox {\n"
"    font: 18pt \"Ubuntu\";\n"
"   color:black;\n"
"}\n"
"\n"
"QWidget{\n"
"background:white;\n"
"}"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.frame_4 = QtGui.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(20, 10, 411, 101))
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
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(20, 630, 621, 121))
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
        self.frame_5 = QtGui.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(860, 10, 411, 101))
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
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(440, 10, 411, 101))
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
        self.add_to_cart_button = QtGui.QPushButton(Dialog)
        self.add_to_cart_button.setGeometry(QtCore.QRect(650, 630, 621, 121))
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
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 120, 1251, 211))
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
        self.fried_special_sel = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.fried_special_sel.setObjectName(_fromUtf8("fried_special_sel"))
        self.verticalLayout.addWidget(self.fried_special_sel)
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
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 340, 1251, 81))
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
        self.chilli_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.chilli_sel.setObjectName(_fromUtf8("chilli_sel"))
        self.sauce_selection_layout.addWidget(self.chilli_sel)
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
        self.frame_6 = QtGui.QFrame(Dialog)
        self.frame_6.setGeometry(QtCore.QRect(20, 530, 1251, 91))
        self.frame_6.setStyleSheet(_fromUtf8("background:rgb(168, 168, 168);"))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.frame_6)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 1231, 71))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.no_salad_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_4)
        self.no_salad_sel.setObjectName(_fromUtf8("no_salad_sel"))
        self.horizontalLayout_3.addWidget(self.no_salad_sel)
        self.no_sauce_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_4)
        self.no_sauce_sel.setObjectName(_fromUtf8("no_sauce_sel"))
        self.horizontalLayout_3.addWidget(self.no_sauce_sel)
        self.frame_7 = QtGui.QFrame(Dialog)
        self.frame_7.setGeometry(QtCore.QRect(20, 430, 1251, 91))
        self.frame_7.setStyleSheet(_fromUtf8("background:rgb(168, 168, 168);"))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.frame_7)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 1231, 71))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.no_lettuce_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_5)
        self.no_lettuce_sel.setObjectName(_fromUtf8("no_lettuce_sel"))
        self.horizontalLayout_5.addWidget(self.no_lettuce_sel)
        self.no_onion_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_5)
        self.no_onion_sel.setObjectName(_fromUtf8("no_onion_sel"))
        self.horizontalLayout_5.addWidget(self.no_onion_sel)
        self.no_cab_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_5)
        self.no_cab_sel.setObjectName(_fromUtf8("no_cab_sel"))
        self.horizontalLayout_5.addWidget(self.no_cab_sel)
        self.no_tomato_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_5)
        self.no_tomato_sel.setObjectName(_fromUtf8("no_tomato_sel"))
        self.horizontalLayout_5.addWidget(self.no_tomato_sel)
        self.no_cucumber_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_5)
        self.no_cucumber_sel.setObjectName(_fromUtf8("no_cucumber_sel"))
        self.horizontalLayout_5.addWidget(self.no_cucumber_sel)
        self.no_pick_sel = QtGui.QCheckBox(self.horizontalLayoutWidget_5)
        self.no_pick_sel.setObjectName(_fromUtf8("no_pick_sel"))
        self.horizontalLayout_5.addWidget(self.no_pick_sel)
        self.buttonBox.raise_()
        self.frame_4.raise_()
        self.cancel_button.raise_()
        self.frame_5.raise_()
        self.frame_3.raise_()
        self.add_to_cart_button.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_6.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.frame_7.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.size_sel.setItemText(0, _translate("Dialog", "Small", None))
        self.size_sel.setItemText(1, _translate("Dialog", "Large", None))
        self.cancel_button.setText(_translate("Dialog", "Cancel", None))
        self.cheese_sel.setItemText(0, _translate("Dialog", "No Cheese", None))
        self.cheese_sel.setItemText(1, _translate("Dialog", "Cheese", None))
        self.type_sel.setItemText(0, _translate("Dialog", "Pitta", None))
        self.type_sel.setItemText(1, _translate("Dialog", "Wrap", None))
        self.add_to_cart_button.setText(_translate("Dialog", "Add To Cart", None))
        self.all_salad_sel.setText(_translate("Dialog", "All Salad", None))
        self.lorw_sel.setText(_translate("Dialog", "L/O/R/W", None))
        self.fried_special_sel.setText(_translate("Dialog", "Fried Specials", None))
        self.lettuce_sel.setText(_translate("Dialog", "Lettuce", None))
        self.w_cabbage_sel.setText(_translate("Dialog", "W Cabbage", None))
        self.r_cabbage_sel.setText(_translate("Dialog", "R Cabbage", None))
        self.onion_sel.setText(_translate("Dialog", "Onion", None))
        self.tomato_sel.setText(_translate("Dialog", "Tomato", None))
        self.cucumber_sel.setText(_translate("Dialog", "Cucumber", None))
        self.pickle_sel.setText(_translate("Dialog", "Pickle", None))
        self.chilli_sel.setText(_translate("Dialog", "Chilli Sauce", None))
        self.mayo_sel.setText(_translate("Dialog", "Mayonaise", None))
        self.gm_sel.setText(_translate("Dialog", "Garlic Mayo", None))
        self.ketchup_sel.setText(_translate("Dialog", "Kethcup", None))
        self.bbq_sel.setText(_translate("Dialog", "BBQ", None))
        self.relish_sel.setText(_translate("Dialog", "Relish", None))
        self.sweet_chill_sel.setText(_translate("Dialog", "Sweet Chilli", None))
        self.no_salad_sel.setText(_translate("Dialog", "No Salad", None))
        self.no_sauce_sel.setText(_translate("Dialog", "No Sauce", None))
        self.no_lettuce_sel.setText(_translate("Dialog", "No Lettuce", None))
        self.no_onion_sel.setText(_translate("Dialog", "No Onion", None))
        self.no_cab_sel.setText(_translate("Dialog", "No Cabbage", None))
        self.no_tomato_sel.setText(_translate("Dialog", "No Tomato", None))
        self.no_cucumber_sel.setText(_translate("Dialog", "No Cucumber", None))
        self.no_pick_sel.setText(_translate("Dialog", "No Pickles", None))

