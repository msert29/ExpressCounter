import View_Main_Menu_Generated

import sys
import os 
from PyQt4 import QtGui
from PyQt4.Qt import QPixmap, QLabel



"""------------------------------------------------------------------------------
FILE        : View_Main_Menu_Custom
DATE        : 13-12-2015
AUTHOR      : Murat Sert
DESCRIPTION : This class is responsible for populating the generated UI fields
              by the Qt Creator. Decision of the addition of the 'Custom' 
              component to the MVC architecture has just been made as a result of
              constantly updated UI Designs. After each update, the generated code
              gets updated as well thus clearing any code written by the developer.
              Instead I have taken another approach of adding in a Custom View architecture.
              With this architecture, Any generated files are untouched and instead of
              directly appending code to these generate classes, we instance them
              in the custom class and populate the views via custom component.
            
             The controller constructs will be connected to these classes directly,
             rather than the View_Main_Menu_Generated.
------------------------------------------------------------------------------"""
                                                                                

"""------------------------------------------------------------------------------
                     Development Diary
    ------------------------------------------------------------------------------
    Date             Notes
    13/12/2015       Creation of the class and successfully instanced from 
                     Controller_Main_Menu class.

              
-------------------------------------------------------------------------------"""


class View_Main_Menu_Custom(object):


    def __init__(self):
        super(View_Main_Menu_Custom, self).__init__()
        self.generated_main_menu_ui = View_Main_Menu_Generated.Ui_MainWindow()

    def setupUi(self, MainWindow):
        self.generated_main_menu_ui.setupUi(MainWindow)
        self.draw_icons()
        
    
    """------------------------------------------------------------------------------
    Function    :   draw_icons
    Description :   This function draws in the icons of the main menu.
                    The getcwd method from OS package is used to access the working
                    directory and then enter into the images folder to retreive the 
                    images. It is then called by the setupUI Method.
    Parameters  : 
    Returns     :   Void
    ------------------------------------------------------------------------------"""
    def draw_icons(self):     
        neworder_icon = QtGui.QPixmap(os.getcwd() + '/images/old-tel.png')
        manager_icon = QPixmap(os.getcwd() + '/images/admin-icon.png')
        search_icon = QPixmap(os.getcwd() +'/images/search-icon.png')
        newcustomer_icon = QPixmap(os.getcwd() +'/images/newcustomer-icon.png')
        
        self.neworder_lbl = QLabel("Place an order")
        self.manager_lbl = QLabel("Manager Log in")
        self.search_lbl = QLabel("Search")
        self.newcustomer_lbl = QLabel("New Customer Entry")
        
        self.manager_lbl.setPixmap(manager_icon)
        self.search_lbl.setPixmap(search_icon)
        self.neworder_lbl.setPixmap(neworder_icon)
        self.newcustomer_lbl.setPixmap(newcustomer_icon)
        
        self.generated_main_menu_ui.new_order_layout.addWidget(self.neworder_lbl)
        self.generated_main_menu_ui.manager_layout.addWidget(self.manager_lbl)
        self.generated_main_menu_ui.search_order_layout.addWidget(self.search_lbl)
        self.generated_main_menu_ui.newcustomer_layout.addWidget(self.newcustomer_lbl)