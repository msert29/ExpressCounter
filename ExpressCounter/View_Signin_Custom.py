'''
Created on Jan 20, 2016

@author: murat
'''

import View_Signin_Generated
from PyQt4.Qt import QDialog

class View_Signin_Custom(object):
    def __init__(self):
        super(View_Signin_Custom, self).__init__()
        self.signin_ui = View_Signin_Generated.Ui_Dialog()
    
    def setup_ui(self, dialog):
        self.signin_ui.setupUi(dialog)