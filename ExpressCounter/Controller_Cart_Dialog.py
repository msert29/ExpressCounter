"""------------------------------------------------------------------------------
FILE        : Controller_Cart_Dialog 
DATE        : 10-12-2015
AUTHOR      : Murat Sert
DESCRIPTION : This class is instanced upon new order click event by the user.
              It initializes the View_Cart_Dialog class to display the cart dialog
              UI. The main purpose of this class is to handle user Events.
              The class is instanced directly by the Controller_Main_Menu class upon 
              new order request.
              
------------------------------------------------------------------------------"""
import Model_Database_Dialog                                                                           

"""------------------------------------------------------------------------------
                     Development Diary
    ------------------------------------------------------------------------------
    Date             Notes
    11/12/2015       Fix the issue with
    10/12/2015       Class created, issues importing the view class unable to 
                     resolve
              
-------------------------------------------------------------------------------"""

import View_Cart_Dialog 
from PyQt4.QtCore import Qt 
from PyQt4.Qt import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox,\
    QComboBox, QPushButton

class Cart_Controller_Class(QDialog):
    def __init__(self):
        super(Cart_Controller_Class, self).__init__()
        self.cart_view_init = View_Cart_Dialog.Ui_Dialog()
        self.cart_view_init.setupUi(self)
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        
        kebabs_list  = self.database.get_kebabs()
        salad_list   = self.database.get_custom_salads()
        sauce_list   = self.database.get_custom_sauces()
        
        self.pizzas_list  = self.database.get_pizzas()
        self.burgers_list = self.database.get_pizzas()
        self.others_list  = self.database.get_others()
        
        self.cart_view_init.display_kebabs(kebabs_list)
        self.cart_view_init.display_salad_options(salad_list)
        self.cart_view_init.display_sauce_options(sauce_list)

                
