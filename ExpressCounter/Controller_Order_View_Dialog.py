'''
Created on Jan 19, 2016

@author: murat
'''

import View_Order_Display_Custom
import Model_Database_Dialog
from PyQt4.Qt import QDialog, QMessageBox
import subprocess
class Controller_Order_View_Dialog(QDialog):
    def __init__(self, order_id):
        super(Controller_Order_View_Dialog, self).__init__()
        self.database   = Model_Database_Dialog.Model_Database_Dialog()
        self.display_order = View_Order_Display_Custom.View_Order_Display_Custom()
        self.display_order.setupUI(self)
        self.__order_id = order_id
        self.__total_order = self.get_order()
        self.display_order.display_order(self.__total_order)
       
        self.handle_view_order_operations()
        
    #Retrieves the total order info using the order_id passed from Controller_View_Order
    def get_order(self):
        total_order = self.database.search_order_by_id_for_display(self.__order_id)
        return total_order
    
    def handle_view_order_operations(self):
        self.display_order.order_display_ui.close_button.clicked.connect(self.close)
        self.display_order.order_display_ui.print_button.clicked.connect(self.view_file_i_o)
        
    def view_file_i_o(self):
        self.__pound = u'\xa3'
        order = self.__total_order 
        f = open('order.txt', 'w')
        self.echo_header(f)
        self.echo_order_id(f, order[0]['id'])
        for x in range(0, (len(order))):
            if (order[x]['product_type'] == "Kebab"):
                self.echo_kebab(f, order[x])
            elif (order[x]['product_type'] == "Pizza"):
                self.echo_pizza(f, order[x])
            elif (order[x]['product_type'] == "Burger"):
                self.echo_burger(f, order[x])
            elif (order[x]['product_type'] == "Other"):
                self.echo_other(f, order[x])
            else:
                QMessageBox.critical(None, "Unkown product type", "An unkown product type ha been passed to file write")
        f.write("___________________________")
        f.write("\nTotal Price:       " + self.__pound.encode('utf8') + str(order[0]['price']) + "0")
        f.write("\n___________________________")
        self.echo_customer(f, order[0])
        f.write("\n___________________________")
        f.close()
        # Start the bash script in order to print it
        subprocess.Popen(['sh', 'printer.sh'])
        
    def echo_kebab(self, f, order):
        f.write(order['product_name'])
        f.write("\n-" + order['options'])
        f.write("\n")
        return
    
    def echo_pizza(self, f, order):
        f.write(order['product_name'])
        try:
            f.write("\n-Extra: " + order['options'])
        except AttributeError:
            pass
        f.write("\n")
        return
    
    def echo_burger(self, f, order):
        f.write(order['product_name'])
        f.write("\n-" + order['options'])
        f.write("\n")
        return
    
    def echo_other(self, f, order):
        f.write(order['product_name'])
        f.write("\n")
        return
        
    def echo_header(self, f):
        header_file = open('order_header.txt', 'r')
        header_data = header_file.read()
        f.write(header_data)
        return 
    def echo_customer(self, f, order):
        f.write("\nCustomer")
        f.write("\nName:      " + str(order['customer_name']))
        f.write("\nAddress:   " + str(order['customer_address']))
        f.write("\nPostcode:  " + str(order['customer_postcode']))
        f.write("\nTelephone: " + str(order['customer_tel']))
        return 
    def echo_order_id(self, f, order_id):
        f.write("   Order ID:" + str(order_id))
        f.write("\n___________________________\n\n")
class New_Customer(object):
    pass