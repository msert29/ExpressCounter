# -*- coding: utf-8 -*-
import View_Customer_Details_Custom
import Model_Database_Dialog
from PyQt4.Qt import QDialog, QMessageBox, QDate, QTime
import subprocess

class Controller_Customer_Dialog(QDialog):
    
    def __init__(self, parent_widget, shopping_list, total_price):
        super(Controller_Customer_Dialog, self).__init__(parent=parent_widget)
        
        self.customer_view_custom = View_Customer_Details_Custom.View_Customer_Details_Custom()
        self.customer_view_custom.setupUi(self)
        
        # To be used to print pound sign
        self.__pound = u'\xa3' 
        
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
        
        caller_id = self.read_caller_id()
        if (caller_id != False):
            self.customer_view_custom.customer_generated_view.ex_tel_edit.setText(caller_id)
            self.__search_tel = caller_id
            self.__number = caller_id
            self.search_complete()
        
    def read_caller_id(self):
        try:
            file = open('number.txt', 'r')    
            caller_id = file.read()
            return caller_id
        except IOError:
            QMessageBox.critical(None, "Caller ID detection failed", "Caller ID Detection failed, please check USB Modem is connected. Consult Manufacturer!")
            return False
    
    
    def handle_cart_cancel_confirm_buttons(self):
        self.customer_view_custom.customer_generated_view.confirm_button.clicked.connect(self.cart_confirmed)
        self.customer_view_custom.customer_generated_view.cancel_button.clicked.connect(self.operation_cancel)
        
    def cart_confirmed(self):
        if self.__customerid:
            # Insert all to details into database and which also returns order id which will be printed as well
            order_id = self.database.insert_all_to_database(self.__shopping_list, self.__total_price, self.__customerid)
            self.file_i_o(self.__shopping_list, self.__total_price, self.__customerid, order_id)
            QMessageBox.information(None, "Order received!", "Order is correctly inserted into the database")
            self.close()
            self.parent().close()
        else:
            QMessageBox.critical(None, "No customer selected or added!", "Please either add a new customer or search for a customer and make a selection!")
    def operation_cancel(self):
        self.close()
        #self.parent().close()
        
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
            self.customer_view_custom.customer_generated_view.ex_tel_edit.setText("")
            self.customer_view_custom.customer_generated_view.new_tel_edit.setText(self.__number)
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
            else:
                QMessageBox.information(None, "Customer successfully inserted!", "Customer has been inserted, please confirm to complete order!")

    def file_i_o(self, order, price, customer, order_id):
        product_len = len(order)
        f = open('order.txt', 'w')
        # truncate it before writing it to clear previous orders
        f.truncate()
        self.echo_header(f)
        self.echo_order_id(f, order_id)
        for x in range(0, product_len):
            if (order[x].type == "Kebab"):
                self.echo_kebab(f, order[x])
            elif (order[x].type == "Pizza"):
                self.echo_pizza(f, order[x])
            elif (order[x].type == "Burger"):
                self.echo_burger(f, order[x])
            elif (order[x].type == "Other") or (order[x].type == "Drink"):
                self.echo_other(f, order[x])
            else:
                QMessageBox.critical(None, "Unkown product type", "An unkown product type ha been passed to file write")
        f.write("___________________________")
        f.write("\nTotal Price:       " + self.__pound.encode('utf8') + str(price) + "0")
        f.write("\n___________________________")
        self.echo_customer(f, customer)
        f.write("\n___________________________")
        f.close()
        # Start the bash script in order to print it
        subprocess.Popen(['sh', 'printer.sh'])
        del order[:]
        
    def echo_kebab(self, f, order):
        f.write(order.size + " " + order.name)
        f.write("\n-" + str(order.kebab_type))
        f.write("\n-" + str(order.salad))
        f.write("\n-" + str(order.sauce))
        f.write("\n \t \t   " + self.__pound.encode('utf8') + str(float(order.price)) + "0")
        f.write("\n")
        return
    
    def echo_pizza(self, f, order):
        f.write(order.size + " " + order.name)
        try:
            f.write("\n-Extra: " + str(order.toppings))
        except AttributeError:
            pass
        f.write("\n \t \t   " + self.__pound.encode('utf8') + str(float(order.price)) + "0")
        f.write("\n")
        return
    
    def echo_burger(self, f, order):
        f.write(order.name +" "+order.cheese)
        f.write("\n-" + str(order.salad))
        f.write("\n-" + str(order.sauce))
        f.write("\n\t \t   " + self.__pound.encode('utf8') + str(float(order.price)) + "0")
        f.write("\n")
        return
    
    def echo_other(self, f, order):
        if order.type == "Drink":
            f.write(order.size + " of " + order.name)
            f.write("\n \t \t   " + self.__pound.encode('utf8') + str(float(order.price)) + "0")
            f.write("\n")
        else:
            f.write(order.name)
            f.write("\n \t \t   " + self.__pound.encode('utf8') + str(float(order.price)) + "0")
            f.write("\n")
        
    def echo_header(self, f):
        header_file = open('order_header.txt', 'r')
        header_data = header_file.read()
        f.write(header_data)
        return 
    def echo_customer(self, f, customer_id):
        customer = self.database.get_customer_details(customer_id)
        f.write("\nCustomer")
        f.write("\nName:      " + str(customer['name']))
        f.write("\nAddress:   " + str(customer['address']))
        f.write("\nPostcode:  " + str(customer['postcode']))
        f.write("\nTelephone: " + str(customer['telephone']))
        return 
    def echo_order_id(self, f, order_id):
        date = QDate.currentDate().toString("yyyy-MM-dd")
        time = QTime.currentTime().toString("hh:mm:ss")
        
        f.write("   Order ID :  " + str(order_id))
        f.write("\n   Date     :  " + date)
        f.write("\n   Time     :  " + time)
        f.write("\n___________________________\n\n")
class New_Customer(object):
    pass