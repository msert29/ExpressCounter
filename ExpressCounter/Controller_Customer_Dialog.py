import View_Customer_Details_Custom
import Model_Database_Dialog
from PyQt4.Qt import QDialog, QMessageBox, QListWidgetItem

class Controller_Customer_Dialog(QDialog):
    
    def __init__(self, shopping_list, total_price):
        super(Controller_Customer_Dialog, self).__init__()
        
        self.customer_view_custom = View_Customer_Details_Custom.View_Customer_Details_Custom()
        self.customer_view_custom.setupUi(self)
        
        # Cart data from Controller cart dialog
        self.__shopping_list = shopping_list
        self.__total_price = total_price
        
        # Will hold the returned value of the new customer
        self.__customerid = ""
        
        # String variable declartion which will hold the value 
        # of given respective names
        # they are used in selection statement below to report 
        # errors if they aren't set
        self.__new_name= ""
        self.__new_addr = ""
        self.__new_postcode = ""
        self.__new_tel = ""
        
        self.__result = ""
        
        # variables which will be populated as user fills input to search
        self.__search_name = ""
        self.__search_addr = ""
        self.__search_postcode = ""
        self.__search_tel = ""
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        
        self.__n_c = New_Customer()
        self.handle_new_customer_entry()
        
        self.handle_cart_cancel_confirm_buttons()
        self.handle_customer_search_entry()
        self.handle_existing_customer_selection()
    def handle_cart_cancel_confirm_buttons(self):
        self.customer_view_custom.customer_generated_view.confirm_button.clicked.connect(self.cart_confirmed)
        self.customer_view_custom.customer_generated_view.cancel_button.clicked.connect(self.operation_cancel)
        
    def cart_confirmed(self):
        if self.__customerid:
            self.database.insert_all_to_database(self.__shopping_list, self.__total_price, self.__customerid)
            QMessageBox.critical(None, "Order received!", "Order is correctly inserted into the database")
            self.close()
        else:
            QMessageBox.critical(None, "No customer selected or added!", "Please either add a new customer or search for a customer and make a selection!")
    def operation_cancel(self):
        self.close()
        
    def handle_customer_search_entry(self):
        self.customer_view_custom.customer_generated_view.ex_name_edit.editingFinished.connect(lambda : self.search_by_name(self.customer_view_custom.customer_generated_view.ex_name_edit.text()))
        self.customer_view_custom.customer_generated_view.ex_addr_edit.editingFinished.connect(lambda : self.search_by_addr(self.customer_view_custom.customer_generated_view.ex_addr_edit.text()))
        self.customer_view_custom.customer_generated_view.ex_postcode_edit.editingFinished.connect(lambda : self.search_by_postcode(self.customer_view_custom.customer_generated_view.ex_postcode_edit.text()))   
        self.customer_view_custom.customer_generated_view.ex_tel_edit.editingFinished.connect(lambda : self.search_by_tel(self.customer_view_custom.customer_generated_view.ex_tel_edit.text()))
        self.customer_view_custom.customer_generated_view.ex_search_button.clicked.connect(self.search_complete)
        
    
    def search_by_name(self, name):
        self.__search_name = name
        
    def search_by_addr(self, addr):
        self.__search_addr = addr
       
    def search_by_postcode(self, postcode):
        self.__search_postcode = postcode
        
    def search_by_tel(self, tel):
        self.__search_tel = tel
        
        
    
    def search_complete(self):
        # check which search strings are inputted and search accordingly to it
        if (self.__search_name) and (self.__search_addr) and (self.__search_postcode) and (self.__search_tel):
            self.__result = self.database.search_existing_customer(self.__search_name, self.__search_addr, 
                                                   self.__search_postcode, self.__search_tel)
        elif (self.__search_name):
            self.__result = self.database.search_existing_customer("name", self.__search_name)
        elif (self.__search_addr):
            self.__result = self.database.search_existing_customer("address", self.__search_addr)
        elif (self.__search_postcode):
            self.__result = self.database.search_existing_customer("postcode", self.__search_postcode)
        elif (self.__search_tel):
            self.__result = self.database.search_existing_customer("tel", self.__search_tel)
        else:
            print ("Neither condition met")
            
            
        # check for matching results
        if (len (self.__result) > 0):
            self.customer_view_custom.display_existing_customer_results(self.__result)
        else:
            QMessageBox.critical(None, "NO results found", "The specified user doesnt exist!")
        
        
        
    """ 
    Handle existing customer search listwidget clicks
    """
    
    def handle_existing_customer_selection(self):
        self.customer_view_custom.search_results.itemClicked.connect(lambda : self.assign_id(self.customer_view_custom.search_results.currentRow()))
        
    def assign_id(self, row):
        self.__customerid = self.customer_view_custom.customer_id_result[row]
    
    """ 
    
    New customer entry methods
    
    """
    def handle_new_customer_entry(self):
        self.customer_view_custom.customer_generated_view.new_name_edit.editingFinished.connect(lambda : self.set_new_name(self.customer_view_custom.customer_generated_view.new_name_edit.text()))
        self.customer_view_custom.customer_generated_view.new_addr_edit.editingFinished.connect(lambda : self.set_new_addr(self.customer_view_custom.customer_generated_view.new_addr_edit.text()))
        self.customer_view_custom.customer_generated_view.new_postcode_edit.editingFinished.connect(lambda : self.set_new_postcode(self.customer_view_custom.customer_generated_view.new_postcode_edit.text()))
        self.customer_view_custom.customer_generated_view.new_tel_edit.editingFinished.connect(lambda : self.set_new_telephone(self.customer_view_custom.customer_generated_view.new_tel_edit.text()))
        self.customer_view_custom.customer_generated_view.new_add_button.clicked.connect(self.add_new_customer)
        
        
    def set_new_name(self, name):
        self.__new_name = name
        self.__n_c.name = name
    def set_new_addr(self, address):
        self.__new_addr = address
        self.__n_c.address = address
    def set_new_postcode(self, postcode):
        self.__new_postcode = postcode
        self.__n_c.postcode = postcode
    def set_new_telephone(self, tel_no):
        self.__new_tel = tel_no
        self.__n_c.telephone = tel_no
    def add_new_customer(self):
        if not self.__new_name:
            QMessageBox.critical(None, "No name assigned!", "Please insert a value for the name field")
        elif not self.__new_addr:
            QMessageBox.critical(None, "No address assigned!", "Please insert a value for the address field")
        elif not self.__new_postcode:
            QMessageBox.critical(None, "No postcode assigned!", "Please insert a value for the postcode field")
        elif not self.__new_tel:
            QMessageBox.critical(None, "No telephone number assigned!", "Please insert a value for the telephone number field")
        else:
            self.database.insert_new_customer(self.__n_c)
            # we need to get the id of the last customer we inserted into the cart 
            self.__customerid = self.database.get_customer_id(self.__n_c.name, self.__n_c.address, 
                                                              self.__n_c.postcode, self.__n_c.telephone)
            if not (self.__customerid):
                QMessageBox.critical(None, "Customer id failed", "Customer id retreive operation failed!")
                

class New_Customer(object):
    pass