'''
Created on Jan 20, 2016

@author: murat
'''
import Model_Database_Dialog
import View_Signin_Custom
import Controller_Manager_Dialog
from PyQt4.Qt import QDialog, QLineEdit, QMessageBox

class Controller_Signin_Dialog(QDialog):

    def __init__(self):
        super(Controller_Signin_Dialog, self).__init__()
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        self.manager_signin_ui = View_Signin_Custom.View_Signin_Custom()
        self.manager_signin_ui.setup_ui(self)
        # dont echo password on screen
        self.manager_signin_ui.signin_ui.password.setEchoMode(QLineEdit.Password)
        self.__account = Account()
        self.handle_signin_input()
        self.setWindowTitle("Sign In")
        
    def handle_signin_input(self):
        self.manager_signin_ui.signin_ui.account_name.editingFinished.connect(\
                        lambda : self.set_account_name(self.manager_signin_ui.signin_ui.account_name.text()))
        self.manager_signin_ui.signin_ui.password.editingFinished.connect(\
                        lambda : self.set_password(self.manager_signin_ui.signin_ui.password.text()))
        self.manager_signin_ui.signin_ui.close_button.clicked.connect(self.close)
        self.manager_signin_ui.signin_ui.login_button.clicked.connect(self.sign_in)
    def set_account_name(self, account_name):
        if (account_name == ""):
            QMessageBox.critical(None, "Account Name empty!", "Please enter your account name!")
        else:
            self.__account.name = account_name
                
    def set_password(self, password):
        if (password == ""):
            QMessageBox.critical(None, "Password empty!", "Please enter your Password!")
        else:
            self.__account.password = password

    def sign_in(self):
        sign_details = self.database.check_manager_details(self.__account.name, self.__account.password)
        if sign_details:
            self.close()
            self.manager_mode = Controller_Manager_Dialog.Controller_Manager_Dialog()
            self.manager_mode.exec_()
        else:
            QMessageBox.critical(None, "Access Denied!", "Your Account Name or Password is invalid!")
class Account(object):
    pass