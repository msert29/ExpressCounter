#!/usr/bin/python
# -*- coding: utf-8 -*-

"""------------------------------------------------------------------------------
FILE        : Controller_Main_Menu 
DATE        : 09-12-2015
AUTHOR      : Murat Sert
DESCRIPTION : This class is responsible for handling user Events. It initiliazes
              the View_Main_Menu_Generated class which draws the GUI elements. The view 
              also creates four icons which allows the user to navigate to 
              different dialogs such as new order dialog, search order dialog, 
              manager mode dialog and add new customer dialog. THis is the homepage
              equvilant of the program.
              
------------------------------------------------------------------------------"""
                                                                                

"""------------------------------------------------------------------------------
                     Development Diary
    ------------------------------------------------------------------------------
    Date             Notes
    12/12/2015       Installed click events for Label objects allow user to call 
                     different dialogs.
    10/12/2015       Imported View class which draws the main background and icons
    09/12/2015       Creation of the class
              
-------------------------------------------------------------------------------"""
import sys
import sip
sip.setapi('QString', 2)
from PyQt4 import QtGui
from PyQt4.Qt import QObject, QEvent
from PyQt4.QtCore import pyqtSlot, pyqtSignal


import View_Main_Menu_Custom
import Controller_Cart_Dialog 
import Model_Database_Dialog


class Controller_Main_Menu(QtGui.QMainWindow):
    
    def __init__(self):
        super(Controller_Main_Menu, self).__init__()
        # Establish a connection during startup
        self.establish_database = Model_Database_Dialog.Model_Database_Dialog()
        self.establish_database.establish_connection()
        # Initialize the view element and draw it
        self.main_view_custom = View_Main_Menu_Custom.View_Main_Menu_Custom()
        self.main_view_custom.setupUi(self)
        self.show()
        self.handle_icon_clicks()

    
    """------------------------------------------------------------------------------
    Function           : clickable
    Description        : This function extends events on the label widget.
                         By default there are no clicked events in labels therefore
                         this method is written to return capture and report click
                         events which is then assigned to each slot
    Parameters         : Widget (corresponding label in this case)
    Returns            : true on clicked event, else returns false
    ------------------------------------------------------------------------------"""
    def install_click_event(self, widget):
        class Filter(QObject):
            clicked = pyqtSignal()
            def eventFilter(self, obj, event):
                if obj == widget:
                    if event.type() == QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            return True
                
                return False
        
        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked


    """------------------------------------------------------------------------------
    Function           : clickable
    Description        : This function passes the labels created in View_Main_Menu_Generated file
                         to the install_click_event defined above.
                         It install click events on the given labels and then once they
                         are clicked, it connects to the slots defined inside .connect()
                         statement. 
    Parameters         : None
    Returns            : Void
    ------------------------------------------------------------------------------"""
    def handle_icon_clicks(self):
        """ Pass the labels created in View class to install_click_event function
            for it to install click events on label objects.
            If any of the icons are clicked, it would connect to the slots defined below
            and execute the corresponding dialog.                                    """
        self.install_click_event(self.main_view_custom.neworder_lbl).connect(self.on_neworder_request)
        self.install_click_event(self.main_view_custom.search_lbl).connect(self.on_search_order_request)
        self.install_click_event(self.main_view_custom.manager_lbl).connect(self.on_manager_mode_request)
        self.install_click_event(self.main_view_custom.newcustomer_lbl).connect(self.on_create_new_customer_request)

    @pyqtSlot()
    def on_neworder_request(self):
        # A new order request has been received, therefore initialize
        # and execute the cart_dialog class
        self.cart_dialog = Controller_Cart_Dialog.Cart_Controller_Class()
        self.cart_dialog.exec_()
        
    @pyqtSlot()
    def on_search_order_request(self):
        print ("Search order loaded")
        
    @pyqtSlot()
    def on_manager_mode_request(self):
        print ("Manager mode loaded")
      
    @pyqtSlot()
    def on_create_new_customer_request(self):
        print ("New customer dialog loaded")
        
    
        
def main():
    app = QtGui.QApplication(sys.argv)
    vmm = Controller_Main_Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
