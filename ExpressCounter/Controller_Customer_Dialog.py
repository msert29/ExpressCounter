import View_Customer_Details_Generated
import Model_Database_Dialog
from PyQt4.Qt import QDialog, QMessageBox

class Controller_Customer_Dialog(QDialog):
    
    def __init__(self, shopping_list, total_price):
        super(Controller_Customer_Dialog, self).__init__()
        self.customer_generated_view = View_Customer_Details_Generated.Ui_Dialog()
        self.customer_generated_view.setupUi(self)
        
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
        
        
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        
        self.__n_c = New_Customer()
        self.handle_new_customer_entry()
        
        
        
    def handle_customer_search_entry(self):
        self.customer_generated_view.ex_name_edit.editingFinished.connect(lambda : self.search_by_name(self.customer_generated_view.ex_name_edit.text()))
        self.customer_generated_view.ex_addr_edit.editingFinished.connect(lambda : self.search_by_addr(self.customer_generated_view.ex_addr_edit.text()))
        self.customer_generated_view.ex_postcode_edit.editingFinished.connect(lambda : self.search_by_postcode(self.customer_generated_view.ex_postcode_edit.text()))   
        self.customer_generated_view.ex_tel_edit.editingFinished.connect(lambda : self.search_by_tel(self.customer_generated_view.ex_tel_edit.text()))
        self.customer_generated_view.ex_search_button.clicked.connect(self.search_complete)
        
    
    def search_by_name(self, name):
        print (str(name))
        
    """ 
    
    New customer entry methods
    
    """
    def handle_new_customer_entry(self):
        self.customer_generated_view.new_name_edit.editingFinished.connect(lambda : self.set_new_name(self.customer_generated_view.new_name_edit.text()))
        self.customer_generated_view.new_addr_edit.editingFinished.connect(lambda : self.set_new_addr(self.customer_generated_view.new_addr_edit.text()))
        self.customer_generated_view.new_postcode_edit.editingFinished.connect(lambda : self.set_new_postcode(self.customer_generated_view.new_postcode_edit.text()))
        self.customer_generated_view.new_tel_edit.editingFinished.connect(lambda : self.set_new_telephone(self.customer_generated_view.new_tel_edit.text()))
        self.customer_generated_view.new_add_button.clicked.connect(self.add_new_customer)
        
        
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
            self.__customerid = self.database.get_customer_id(self.__n_c.name, self.__n_c.address)
            self.database.insert_all_to_database(self.__shopping_list, self.__total_price, self.__customerid)

class New_Customer(object):
    pass