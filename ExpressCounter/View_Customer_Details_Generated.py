# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/murat/Documents/designs/new_customer_dialog.ui'
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
        Dialog.resize(1294, 806)
        self.new_frame = QtGui.QFrame(Dialog)
        self.new_frame.setGeometry(QtCore.QRect(27, 90, 511, 701))
        self.new_frame.setStyleSheet(_fromUtf8(""))
        self.new_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.new_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.new_frame.setObjectName(_fromUtf8("new_frame"))
        self.frame = QtGui.QFrame(self.new_frame)
        self.frame.setGeometry(QtCore.QRect(10, 10, 491, 681))
        self.frame.setStyleSheet(_fromUtf8("QLabel{\n"
"    font: 18pt \"Ubuntu\";\n"
"   margin:5px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"font: 18pt \"Ubuntu\";\n"
"margin:5px;\n"
"min-height:50px;\n"
"}\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayoutWidget = QtGui.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 5, 471, 346))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.new_name_edit = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_name_edit.setObjectName(_fromUtf8("new_name_edit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.new_name_edit)
        self.new_house_no_edit = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_house_no_edit.setObjectName(_fromUtf8("new_house_no_edit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.new_house_no_edit)
        self.new_addr_edit = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_addr_edit.setObjectName(_fromUtf8("new_addr_edit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.new_addr_edit)
        self.new_postcode_edit = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_postcode_edit.setObjectName(_fromUtf8("new_postcode_edit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.new_postcode_edit)
        self.new_tel_edit = QtGui.QLineEdit(self.formLayoutWidget)
        self.new_tel_edit.setObjectName(_fromUtf8("new_tel_edit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.new_tel_edit)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.new_frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 360, 471, 321))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.auto_fill_button = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.auto_fill_button.setStyleSheet(_fromUtf8("min-height:80px;\n"
"background:rgb(0, 170, 255);\n"
"color:black;\n"
"font: 18pt \"Ubuntu\";"))
        self.auto_fill_button.setObjectName(_fromUtf8("auto_fill_button"))
        self.verticalLayout_3.addWidget(self.auto_fill_button)
        self.new_add_button = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.new_add_button.setStyleSheet(_fromUtf8("min-height:80px;\n"
"background:rgb(0, 255, 127);\n"
"color:black;\n"
"font: 18pt \"Ubuntu\";"))
        self.new_add_button.setObjectName(_fromUtf8("new_add_button"))
        self.verticalLayout_3.addWidget(self.new_add_button)
        self.new_cancel_button = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.new_cancel_button.setStyleSheet(_fromUtf8("min-height:80px;\n"
"background:rgb(255, 0, 0);\n"
"color:black;\n"
"font: 18pt \"Ubuntu\";"))
        self.new_cancel_button.setObjectName(_fromUtf8("new_cancel_button"))
        self.verticalLayout_3.addWidget(self.new_cancel_button)
        self.existing_frame = QtGui.QFrame(Dialog)
        self.existing_frame.setGeometry(QtCore.QRect(540, 90, 741, 701))
        self.existing_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.existing_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.existing_frame.setObjectName(_fromUtf8("existing_frame"))
        self.frame_2 = QtGui.QFrame(self.existing_frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 721, 361))
        self.frame_2.setStyleSheet(_fromUtf8("QLabel{\n"
"    font: 18pt \"Ubuntu\";\n"
"   margin:5px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"font: 18pt \"Ubuntu\";\n"
"margin:3px;\n"
"min-height:50px;\n"
"}"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.frame_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 5, 701, 271))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
        self.ex_name_edit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.ex_name_edit.setObjectName(_fromUtf8("ex_name_edit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.ex_name_edit)
        self.ex_addr_edit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.ex_addr_edit.setObjectName(_fromUtf8("ex_addr_edit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.ex_addr_edit)
        self.ex_postcode_edit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.ex_postcode_edit.setObjectName(_fromUtf8("ex_postcode_edit"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.ex_postcode_edit)
        self.ex_tel_edit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.ex_tel_edit.setObjectName(_fromUtf8("ex_tel_edit"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.ex_tel_edit)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 280, 701, 71))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ex_search_button = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.ex_search_button.setStyleSheet(_fromUtf8("min-height:60px;\n"
"background:rgb(0, 255, 127);\n"
"color:black;\n"
"font: 18pt \"Ubuntu\";"))
        self.ex_search_button.setObjectName(_fromUtf8("ex_search_button"))
        self.horizontalLayout_2.addWidget(self.ex_search_button)
        self.cancel_button = QtGui.QPushButton(self.existing_frame)
        self.cancel_button.setGeometry(QtCore.QRect(10, 610, 351, 81))
        self.cancel_button.setStyleSheet(_fromUtf8("min-height:50px;\n"
"background:rgb(255, 0, 0);\n"
"color:black;\n"
"font: 18pt \"Ubuntu\";"))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.confirm_button = QtGui.QPushButton(self.existing_frame)
        self.confirm_button.setGeometry(QtCore.QRect(370, 610, 361, 81))
        self.confirm_button.setStyleSheet(_fromUtf8("min-height:50px;\n"
"background:rgb(0, 255, 0);\n"
"color:black;\n"
"font: 18pt \"Ubuntu\";"))
        self.confirm_button.setObjectName(_fromUtf8("confirm_button"))
        self.frame_3 = QtGui.QFrame(self.existing_frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 380, 721, 221))
        self.frame_3.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu\";"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.frame_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(-10, 0, 741, 221))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.search_results_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.search_results_layout.setObjectName(_fromUtf8("search_results_layout"))
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.cancel_button.raise_()
        self.confirm_button.raise_()
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(28, 10, 511, 80))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 28pt \"Ubuntu\";\n"
"background: rgb(85, 255, 0);\n"
"color:black;\n"
"text-align: center;\n"
"max-height:80px;\n"
"}"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(540, 10, 739, 78))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 63 28pt \"Ubuntu\";\n"
"background: rgb(255, 85, 0);\n"
"color:black;\n"
"text-align: center;\n"
"max-height:100px;\n"
"}"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Name", None))
        self.label_4.setText(_translate("Dialog", "House Number", None))
        self.label_5.setText(_translate("Dialog", "Street Name", None))
        self.label_6.setText(_translate("Dialog", "Postcode", None))
        self.label_7.setText(_translate("Dialog", "Telephone", None))
        self.auto_fill_button.setText(_translate("Dialog", "Auto Fill", None))
        self.new_add_button.setText(_translate("Dialog", "Add", None))
        self.new_cancel_button.setText(_translate("Dialog", "Cancel", None))
        self.label_8.setText(_translate("Dialog", "Name", None))
        self.label_9.setText(_translate("Dialog", "Address", None))
        self.label_10.setText(_translate("Dialog", "Postcode", None))
        self.label_11.setText(_translate("Dialog", "Telephone", None))
        self.ex_search_button.setText(_translate("Dialog", "Search", None))
        self.cancel_button.setText(_translate("Dialog", "Cancel", None))
        self.confirm_button.setText(_translate("Dialog", "Confirm", None))
        self.label_2.setText(_translate("Dialog", "New Customer Entry", None))
        self.label.setText(_translate("Dialog", "Existing Customer Search", None))

