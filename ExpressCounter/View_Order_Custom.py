'''
Created on Jan 17, 2016

@author: murat
'''
import View_Order_Generated
from PyQt4.Qt import \
    QTableWidgetItem, QPushButton, QButtonGroup, QTextDocument, QTextEdit
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
            self.order_ui.table_search_result.setItem(x,5, QTableWidgetItem(pound + str(float(order[x]['price'])) + "0"))
            self.order_ui.table_search_result.setItem(x,6, QTableWidgetItem(order[x]['date']))
            self.order_ui.table_search_result.setItem(x,7, QTableWidgetItem(order[x]['time']))
            xbutton = QPushButton("View")
            self.__view_button_group.addButton(xbutton, x)
            self.order_ui.table_search_result.setCellWidget(x, 8, xbutton)
                
    def get_button_group(self):
        return self.__view_button_group
    
    """ This method receives the id of the button clicked. As the results are displayed in a table,
    and the unique order id corresponds with different buttons, it returns this unique order id which
    is then used to print the order contents in Controller_Order_View_Dialog Dialog """
    def calculate_id(self, button_id):
        return str(self.__order[button_id]['id'])