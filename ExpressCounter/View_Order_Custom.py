'''
Created on Jan 17, 2016

@author: murat
'''
import View_Order_Generated
from PyQt4.Qt import \
    QTableWidgetItem, QPushButton, QButtonGroup
import Model_Database_Dialog


class View_Order_Custom(object):
    def __init__(self, parent = None):
        super(View_Order_Custom, self).__init__()
        # Import the generated GUI Elements
        self.order_ui = View_Order_Generated.Ui_Dialog()
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        self.__view_button_group = QButtonGroup()
    def setupUI(self, dialog):
        self.order_ui.setupUi(dialog)
        
    def echo_order(self, order):
        self.__order = order
        pound = u'\xa3'
       
        self.order_ui.table_search_result.setRowCount(len(order))
        for x in range(0, len(order)):
           
            self.order_ui.table_search_result.setItem(x,0, QTableWidgetItem(order[x]['id']))
            self.order_ui.table_search_result.setItem(x,1, QTableWidgetItem(order[x]['customer_name']))
            self.order_ui.table_search_result.setItem(x,2, QTableWidgetItem(order[x]['customer_address']))
            self.order_ui.table_search_result.setItem(x,3, QTableWidgetItem(order[x]['customer_postcode']))
            self.order_ui.table_search_result.setItem(x,4, QTableWidgetItem(order[x]['customer_tel']))
            self.order_ui.table_search_result.setItem(x,5, QTableWidgetItem(pound + order[x]['price']))
            self.order_ui.table_search_result.setItem(x,6, QTableWidgetItem(order[x]['date']))
            self.order_ui.table_search_result.setItem(x,7, QTableWidgetItem(order[x]['time']))
            xbutton = QPushButton("View")
            self.__view_button_group.addButton(xbutton, x)
            self.order_ui.table_search_result.setCellWidget(x, 8, xbutton)
            
            """ Because of pyqt signal slot mechanism limitation, we have to install the click event
            for the pushbutton in the view. This is a bad practice but unfortunately as events cannot be 
            installed in for loops we have no other option but to install it here. """
            #self.display_button_array[x].clicked.connect(lambda: self.display_order(order[x]['id']))
       
            
            
    def display_order(self, button_id):
        order_id = self.__order[button_id]['id']
        total_order = self.database.search_order_by_id_for_display(order_id)
        if (len(total_order) > 0):
            print ("------------------------------")
            print total_order[0]['customer_name']
            print total_order[0]['customer_address']
            print total_order[0]['customer_postcode']
            print total_order[0]['customer_tel']
            for x in range(0, len(total_order)):
                print ("------------------------------")
                print total_order[x]['product_name']
                print total_order[x]['options']
            print ("------------------------------")
            print total_order[x]['time']
            print total_order[x]['date']
            print ("------------------------------")
            print total_order[x]['price']
            print ("------------------------------")
                
    def get_button_group(self):
        return self.__view_button_group
   