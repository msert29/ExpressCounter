'''
Created on Jan 24, 2016

@author: murat
'''

import Model_Database_Dialog
import View_Customer_Mode_Custom
from PyQt4.Qt import QDialog, QMessageBox

from Controller_Customer_Dialog import New_Customer


class Controller_Customer_Mode_Dialog(QDialog):

    def __init__(self):
        super(Controller_Customer_Mode_Dialog, self).__init__()
        self.customer_ui = View_Customer_Mode_Custom.View_Customer_Mode_Custom()
        self.customer_ui.setup_ui(self)
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        self.setWindowTitle("Customer Dialog")
        
        
        # Empty structs which will be used to depending on the operation
        self.__ex_customer = Existing_Customer()
        self.__new_customer = New_Customer()
        self.__update_customer = New_Customer()
        
        # a bool which determines if user has searched for a customer
        self.__searched = False
        self.handle_new_customer_entry()
        self.handle_update_customer_entry()
        self.handle_existing_customer_new_details()
        self.handle_customer_delete()
    """ --------------------------------------------------------------------------------------------------------------
     New customer entry related section 
    --------------------------------------------------------------------------------------------------------------"""
    
    def handle_new_customer_entry(self):
        # Must contain a space in order for isspace() method to correctly calculate if string is empty or not
        
        self.__new_customer.name = " "
        self.__new_customer.address = " "
        self.__new_customer.postcode = " "
        self.__new_customer.telephone = " "
        
        
        self.customer_ui.generated_ui.new_customer_name_entry.editingFinished.connect(\
            lambda : self.set_new_customer_name(self.customer_ui.generated_ui.new_customer_name_entry.text()))
        
        self.customer_ui.generated_ui.new_customer_addr_entry.editingFinished.connect(\
            lambda : self.set_new_customer_addr(self.customer_ui.generated_ui.new_customer_addr_entry.text()))
        
        self.customer_ui.generated_ui.new_customer_postcode_entry.editingFinished.connect(\
            lambda : self.set_new_customer_postcode(self.customer_ui.generated_ui.new_customer_postcode_entry.text()))
        
        self.customer_ui.generated_ui.new_customer_tel_entry.editingFinished.connect(\
            lambda : self.set_new_customer_tel(self.customer_ui.generated_ui.new_customer_tel_entry.text()))
        
        self.customer_ui.generated_ui.add_customer_button.clicked.connect(\
                self.check_new_customer)
        
        # when the exit button is clicked, then close the dialog
        self.customer_ui.generated_ui.exit_button.clicked.connect(self.close)
    # We will be setting the variable once they are set 
    def set_new_customer_name(self, new_name):
        if (new_name.isspace()) or (new_name == ""):
            # Set to emptry string because in the check function we will check if empty and error it
            self.__new_customer.name = " "
            QMessageBox.critical(None, "No Name specified!", "Please specify a name!")
        else:
            self.__new_customer.name = new_name
            
    def set_new_customer_addr(self, new_addr):
        if (new_addr.isspace()) or (new_addr == ""):
            # Set to emptry string because in the check function we will check if empty and error it
            self.__new_customer.address = " "
            QMessageBox.critical(None, "No Address specified!", "Please specify an Address!")
        else:
            self.__new_customer.address = new_addr
            
    def set_new_customer_postcode(self, new_postcode):
        if (new_postcode.isspace()) or (new_postcode == ""):
            # Set to emptry string because in the check function we will check if empty and error it
            self.__new_customer.postcode = " "
            QMessageBox.critical(None, "No Postcode specified!", "Please specify a Postcode!")
        else:
            self.__new_customer.postcode = new_postcode
    def set_new_customer_tel(self, new_tel):
        if (new_tel.isspace()) or (new_tel == ""):
            # Set to emptry string because in the check function we will check if empty and error it
            self.__new_customer.telephone = " "
            QMessageBox.critical(None, "No Tel specified!", "Please specify a Telephone number!")
        else:
            self.__new_customer.telephone = new_tel
            
    
    def check_new_customer(self):
        if (self.__new_customer.name.isspace()):
            QMessageBox.critical(None, "No Name specified!", "Please specify a name!")
        elif (self.__new_customer.address.isspace()):
            QMessageBox.critical(None, "No Address specified!", "Please specify an Address!")
        elif (self.__new_customer.postcode.isspace()):
            QMessageBox.critical(None, "No Postcode specified!", "Please specify a Postcode!")
        elif (self.__new_customer.telephone.isspace()):
            QMessageBox.critical(None, "No Tel specified!", "Please specify a Telephone number!")
        else:
            self.database.insert_new_customer(self.__new_customer)    
            
            
    """ --------------------------------------------------------------------------------------------------------------
     Existing customer search related section 
    --------------------------------------------------------------------------------------------------------------"""
    def handle_update_customer_entry(self):
        self.__ex_customer.name = " "
        self.__ex_customer.address = " "
        self.__ex_customer.postcode = " "
        self.__ex_customer.telephone = " "
        self.customer_ui.generated_ui.name_search.editingFinished.connect(lambda : self.set_search_name(self.customer_ui.generated_ui.name_search.text()))
        self.customer_ui.generated_ui.add_search.editingFinished.connect( lambda : self.set_search_addr(self.customer_ui.generated_ui.add_search.text()))
        self.customer_ui.generated_ui.postcode_search.editingFinished.connect(lambda : self.set_search_postcode(self.customer_ui.generated_ui.postcode_search.text()))
        self.customer_ui.generated_ui.tel_search.editingFinished.connect(lambda : self.set_search_tel(self.customer_ui.generated_ui.tel_search.text()))
        self.customer_ui.generated_ui.existing_customer_search_button.clicked.connect(self.search_existing_customer)
        
        
        
    def set_search_name(self, search_name):
        if (search_name.isspace()) or (search_name == ""):
            # set it to empty string else during search the last inputted valid value get stored
            self.__ex_customer.name = " "
        else:
            self.__ex_customer.name = search_name
    def set_search_addr(self, search_addr):
        if (search_addr.isspace()) or (search_addr == ""):
            # set it to empty string else during search the last inputted valid value get stored
            self.__ex_customer.address = " "
        else:
            self.__ex_customer.address = search_addr
    def set_search_postcode(self, search_postcode):
        if (search_postcode.isspace()) or (search_postcode == ""):
            # set it to empty string else during search the last inputted valid value get stored
            self.__ex_customer.postcode = " "
        else:
            self.__ex_customer.postcode = search_postcode
    def set_search_tel(self, search_tel):
        if (search_tel.isspace()) or (search_tel == ""):
            # set it to empty string else during search the last inputted valid value get stored
            self.__ex_customer.telephone = " "
        else:
            self.__ex_customer.telephone = search_tel
            
    def search_existing_customer(self):
        if not (self.__ex_customer.name.isspace()) and not (self.__ex_customer.address.isspace()) and not (self.__ex_customer.postcode.isspace()) \
        and not (self.__ex_customer.telephone.isspace()):
            self.__result = self.database.search_existing_customer(self.__ex_customer.name, self.__ex_customer.address, 
                                                   self.__ex_customer.postcode, self.__ex_customer.telephone)
        elif not(self.__ex_customer.name.isspace()):
            self.__result = self.database.search_existing_customer("name", self.__ex_customer.name)
        elif not (self.__ex_customer.address.isspace()):
            self.__result = self.database.search_existing_customer("address", self.__ex_customer.address)
        elif not (self.__ex_customer.postcode.isspace()):
            self.__result = self.database.search_existing_customer("postcode", self.__ex_customer.postcode)
        elif not (self.__ex_customer.telephone.isspace()):
            self.__result = self.database.search_existing_customer("tel", self.__ex_customer.telephone)
        else:
            QMessageBox.critical(None, "No Results", "Please refine your search as there are no results returned")
        
        try:
            if (len(self.__result) > 0):
                self.customer_ui.echo_search_results(self.__result[0])
                # used internally while updating customer details
                self.__update_customer.id   = self.__result[0]['id']
                self.initiliaze_update_fields()
                self.__searched = True
            else:
                QMessageBox.critical(None, "No Results", "No results have been returned, please modify your search!")
        except AttributeError:
            #self.__result will not be set if we enter the else clause which will be triggered if user doesnt input values for search customer field
            pass
            
    def handle_existing_customer_new_details(self):
        self.__update_customer.name = self.customer_ui.generated_ui.new_name_entry.text()
        self.__update_customer.address =  self.customer_ui.generated_ui.new_addr_entry.text()
        self.__update_customer.postcode = self.customer_ui.generated_ui.new_postcode_entry.text()
        self.__update_customer.telephone = self.customer_ui.generated_ui.new_tel_entry.text()
        
        
        self.customer_ui.generated_ui.new_name_entry.editingFinished.connect(lambda : self.update_name_entry(self.customer_ui.generated_ui.new_name_entry.text()))
        self.customer_ui.generated_ui.new_addr_entry.editingFinished.connect(lambda : self.update_addr_entry(self.customer_ui.generated_ui.new_addr_entry.text()))
        self.customer_ui.generated_ui.new_postcode_entry.editingFinished.connect(lambda : self.update_postcode_entry(self.customer_ui.generated_ui.new_postcode_entry.text()))
        self.customer_ui.generated_ui.new_tel_entry.editingFinished.connect(lambda : self.update_tel_entry(self.customer_ui.generated_ui.new_tel_entry.text()))
        self.customer_ui.generated_ui.existing_customer_update_button.clicked.connect(self.update_customer_details)

    # initialize update customer fields with the data returned
    def initiliaze_update_fields(self):
        self.__name_set     = True 
        self.__addr_set     = True 
        self.__postcode_set = True 
        self.__tel_set      = True 
        self.__update_customer.name = self.customer_ui.generated_ui.new_name_entry.text()
        self.__update_customer.address =  self.customer_ui.generated_ui.new_addr_entry.text()
        self.__update_customer.postcode = self.customer_ui.generated_ui.new_postcode_entry.text()
        self.__update_customer.telephone = self.customer_ui.generated_ui.new_tel_entry.text()
        
        
    def update_name_entry(self, new_name):
        if (new_name.isspace()) or (new_name == ""):
            # check if the echoed result empty
            if (self.customer_ui.generated_ui.new_name_entry.text().isspace()) or (self.customer_ui.generated_ui.new_name_entry.text() == ""):
                QMessageBox.critical(None, "No Name specified!", "Please specify a name!")
                self.__name_set = False
            else:
                self.__update_customer.name = self.customer_ui.generated_ui.new_name_entry.text()
                self.__name_set = True
        else:
            self.__update_customer.name = new_name
            self.__name_set = True
    
    def update_addr_entry(self, new_addr):
        if (new_addr.isspace()) or (new_addr == ""):
            # check if the echoed result empty
            if (self.customer_ui.generated_ui.new_addr_entry.text().isspace()) or (self.customer_ui.generated_ui.new_addr_entry.text() == ""):
                QMessageBox.critical(None, "No Address specified!", "Please specify an Address!")
                self.__addr_set = False
            else:
                self.__update_customer.address =  self.customer_ui.generated_ui.new_addr_entry.text()
                self.__addr_set = True
        else:
            self.__update_customer.address = new_addr
            self.__addr_set = True
            
    def update_postcode_entry(self, new_postcode):
        if (new_postcode.isspace()) or (new_postcode == ""):
            # check if the echoed result empty
            if (self.customer_ui.generated_ui.new_postcode_entry.text().isspace()) or (self.customer_ui.generated_ui.new_postcode_entry.text() == ""):
                QMessageBox.critical(None, "No Postcode specified!", "Please specify a Postcode!")
                self.__postcode_set = False
            else:
                self.__update_customer.postcode = self.customer_ui.generated_ui.new_postcode_entry.text()
                self.__postcode_set = True
        else:
            self.__update_customer.postcode = new_postcode  
            self.__postcode_set = True
    
    def update_tel_entry(self, new_tel):
        if (new_tel.isspace()) or (new_tel == ""):
            # check if the echoed result empty
            if (self.customer_ui.generated_ui.new_tel_entry.text().isspace()) or (self.customer_ui.generated_ui.new_tel_entry.text() == ""):
                QMessageBox.critical(None, "No Telephone specified!", "Please specify a Telephone number!")
                self.__tel_set = False
            else:
                self.__update_customer.telephone = self.customer_ui.generated_ui.new_tel_entry.text()
                self.__tel_set = True
        else:
            self.__update_customer.telephone = new_tel
            self.__tel_set = True
    
    def update_customer_details(self):
        if (self.__searched) and (self.__name_set) and (self.__addr_set) and (self.__postcode_set) and (self.__tel_set):
            self.database.update_customer_details(self.__update_customer.id, self.__update_customer.name, self.__update_customer.address, \
                    self.__update_customer.postcode, self.__update_customer.telephone)
            print self.__update_customer.name
            print self.__update_customer.address
            print self.__update_customer.postcode
            print self.__update_customer.telephone
        else:
            QMessageBox.critical(None, "Fields blank", "1) Please search for a customer 2) All fields must be filled in!")
   
   
    """ --------------------------------------------------------------------------------------------------------------
     Delete customer related section 
    --------------------------------------------------------------------------------------------------------------"""
    
    def initiliaze_delete_custommer(self):
        self.__customer_delete = New_Customer()
        self.__customer_delete.name = " "
        self.__customer_delete.address = " "
        self.__customer_delete.postcode = " "
        self.__customer_delete.telephone = " "
        self.__del_name_set = False
        self.__del_addr_set = False
        self.__del_postcode_set = False
        self.__del_tel_set = False
    def handle_customer_delete(self):
        self.initiliaze_delete_custommer()
        self.customer_ui.generated_ui.new_name_edit_4.editingFinished.connect(lambda : self.set_name_search(self.customer_ui.generated_ui.new_name_edit_4.text()))
        self.customer_ui.generated_ui.new_addr_edit_4.editingFinished.connect(lambda : self.set_addr_search(self.customer_ui.generated_ui.new_addr_edit_4.text()))
        self.customer_ui.generated_ui.new_postcode_edit_4.editingFinished.connect(lambda : self.set_postcode_search(self.customer_ui.generated_ui.new_postcode_edit_4.text()))
        self.customer_ui.generated_ui.new_tel_edit_4.editingFinished.connect(lambda : self.set_tel_search(self.customer_ui.generated_ui.new_tel_edit_4.text()))
        self.customer_ui.generated_ui.delete_customer_search_button.clicked.connect(self.search_for_deleting)
    
    
    def set_name_search(self, delete_name):
        self.__customer_delete.name = delete_name
        if (delete_name.isspace()) or (delete_name == ""):
            self.__del_name_set = False
        else:
            self.__del_name_set = True
    def set_addr_search(self, delete_addr):
        self.__customer_delete.address = delete_addr
        if (delete_addr.isspace()) or (delete_addr == ""):
            self.__del_addr_set = False
        else:
            self.__del_addr_set = True
    def set_postcode_search(self, delete_postcode):
        self.__customer_delete.postcode = delete_postcode
        if (delete_postcode.isspace()) or (delete_postcode == ""):
            self.__del_postcode_set = False
        else:
            self.__del_postcode_set = True
    def set_tel_search(self, delete_tel):
        self.__customer_delete.telephone = delete_tel
        if (delete_tel.isspace()) or (delete_tel == ""):
            self.__del_tel_set = False
        else:
            self.__del_tel_set = True
        
    def search_for_deleting(self):
        if (self.__del_name_set) and (self.__del_addr_set) and (self.__del_postcode_set) and (self.__del_tel_set):
            self.__result = self.database.search_existing_customer(self.__ex_customer.name, self.__ex_customer.address, \
                                self.__ex_customer.postcode, self.__ex_customer.telephone)
        elif (self.__del_name_set):
            self.__result = self.database.search_existing_customer("name", self.__customer_delete.name)
        elif (self.__del_addr_set):
            self.__result = self.database.search_existing_customer("address", self.__customer_delete.address)
        elif (self.__del_postcode_set):
            self.__result = self.database.search_existing_customer("postcode", self.__customer_delete.postcode)
        elif (self.__del_tel_set):
            self.__result = self.database.search_existing_customer("tel", self.__customer_delete.telephone)
        else:
            QMessageBox.critical(None, "No Results", "Please refine your search as there are no results returned")
        
        try:
            if (len(self.__result) > 0):
                self.customer_ui.echo_delete_results(self.__result)
                self.handle_delete_request()
                # used internally while updating customer details
            else:
                self.customer_ui.delete_table_search.clear()
                QMessageBox.critical(None, "No Results", "No results have been returned, please modify your search!")
        except AttributeError:
            #self.__result will not be set if we enter the else clause which will be triggered if user doesnt input values for search customer field
            pass
        
    def handle_delete_request(self):
        del_button = self.customer_ui.get_delete_buttons()
        del_button.buttonClicked[int].connect(self.delete_customer_event)
    
    def delete_customer_event(self, number):
        customer_id = self.customer_ui.calculate_id(number)
        result = self.database.delete_customer(customer_id)
        if result:
            QMessageBox.information(None, "Deleted Customer!!", "The customer entry has been removed from the database")

        
class New_Customer(object):
    pass        

class Existing_Customer(object):
    pass
