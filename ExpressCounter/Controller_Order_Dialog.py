'''
Created on Jan 17, 2016

@author: murat
'''

import View_Order_Custom
import Model_Database_Dialog
import Controller_Order_View_Dialog

from PyQt4.Qt import QDialog, QMessageBox

class Controller_Order_Dialog(QDialog):
    def __init__(self):
        super(Controller_Order_Dialog, self).__init__()
        self.database   = Model_Database_Dialog.Model_Database_Dialog()
        self.order_view = View_Order_Custom.View_Order_Custom()
        self.order_view.setupUI(self)
        
        self.handle_order_search_operations()
        
        
        
        
    def handle_order_search_operations(self):
        self.__order_id = 0
        self.__name     = ""
        self.__address  = ""
        self.__postcode = ""
        self.__tel      = ""
        self.handle_order_id()
        self.handle_name()
        self.handle_address()
        self.handle_postcode()
        self.handle_tel()
        self.handle_order_operations()
        self.handle_order_view_click()
    def handle_order_id(self):
        self.order_view.order_ui.order_search_box.editingFinished.connect(\
                        lambda : self.set_order_id(self.order_view.order_ui.order_search_box.text()))
        
    
    def set_order_id(self, order_id):
        if (order_id == "0") or (not order_id.isdigit()):
            QMessageBox.critical(None, "Please input a number", "Please input a number or enter a number greater than zero")
        else:
            self.__order_id = order_id
    
    
    def handle_name(self):
        self.order_view.order_ui.name_search_box.editingFinished.connect(\
                        lambda : self.set_name(self.order_view.order_ui.name_search_box.text()))
        
        
    def set_name(self, name):
        self.__name = name
    
    def handle_address(self):
        self.order_view.order_ui.address_search_box.editingFinished.connect(\
                        lambda : self.set_address(self.order_view.order_ui.address_search_box.text()))
    
    def set_address(self, address):
        self.__address = address

    
    def handle_postcode(self):
        self.order_view.order_ui.postcode_search_box.editingFinished.connect(\
                        lambda : self.set_postcode(self.order_view.order_ui.postcode_search_box.text()))
    
    def set_postcode(self, postcode):
        self.__address = postcode
        
        
    def handle_tel(self):
        self.order_view.order_ui.tel_search_box.editingFinished.connect(\
                        lambda : self.set_tel(self.order_view.order_ui.tel_search_box.text()))
    
    def set_tel(self, tel):
        self.__address = tel
        
    
    def handle_order_view_click(self):
        button_group = self.order_view.get_button_group()
        button_group.buttonClicked[int].connect(self.initialize_display)
    
    def initialize_display(self, number):
        order_id = self.order_view.calculate_id(number)
        self.order_view_dialog = Controller_Order_View_Dialog.Controller_Order_View_Dialog(order_id)
        self.order_view_dialog.exec_()
    
    def handle_order_operations(self):
        self.order_view.order_ui.search_button.clicked.connect(self.handle_order_search_req)
        self.order_view.order_ui.cancel_button.clicked.connect(self.close)
        
    
    def handle_order_search_req(self):
        if (self.__order_id) and (self.__name) and (self.__address) and (self.__postcode) and (self.__tel):
            print ("All")
        elif (self.__order_id != 0):
            order = self.database.search_order_by_id(self.__order_id)
            try:
                if (len(order) > 0 ):
                    self.order_view.echo_order(order)
            except TypeError:
                QMessageBox.critical(None, "No Results found!", "Please input a valid order number!")
        elif (self.__name):
            if (self.__name.isdigit()) or (self.__name == ""):
                QMessageBox.critical(None, "Not a valid name!", "Please input a valid name!")
            else:
                order = self.database.search_order_by_name(self.__name)
                if (len(order) > 0 ):
                    self.order_view.echo_order(order)
                else:
                    QMessageBox.critical(None, "No Results found!", "Please input a valid name!")
        elif (self.__address):
            print self.__address
        elif (self.__postcode):
            print self.__postcode
        elif (self.__tel):
            print self.__tel
        else:
            print "Else"
            
            
