'''
Created on Apr 11, 2016

@author: murat
'''
import View_Cart_Addon_Generated
from PyQt4.Qt import QObject

class View_Cart_Addon_Custom(QObject):
    def __init__(self):
        super(View_Cart_Addon_Custom, self).__init__()
        self.generated_ui = View_Cart_Addon_Generated.Ui_Dialog()
    
    def setupUi(self, dialog):
        self.generated_ui.setupUi(dialog)
        
        