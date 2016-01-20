'''
Created on Jan 19, 2016

@author: murat
'''

import View_Order_Display_Generated
import Model_Database_Dialog
from PyQt4.Qt import QTextEdit

class View_Order_Display_Custom(object):
    def __init__(self, parent = None):
        super(View_Order_Display_Custom, self).__init__()
        # Import the generated GUI Elements
        self.order_display_ui = View_Order_Display_Generated.Ui_Dialog()
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        
    def setupUI(self, dialog):
        self.order_display_ui.setupUi(dialog)

    def display_order(self, order):
        pound = u'\xa3'
        customer_details = QTextEdit()
        order_details    = QTextEdit()
        price_date_info  = QTextEdit()
        total_order = order
        if (len(total_order) > 0):
            customer_details.append("---------------------------------------------------------------------------------")
            customer_details.append("Name      : " + total_order[0]['customer_name'])
            customer_details.append("Address   : " + total_order[0]['customer_address'])
            customer_details.append("Postcode  : " + total_order[0]['customer_postcode'])
            customer_details.append("Telephone : " + total_order[0]['customer_tel'])
            customer_details.append("---------------------------------------------------------------------------------")
            for x in range(0, len(total_order)):
                order_details.append(total_order[x]['product_name'])
                order_details.append(" -" + total_order[x]['options'] + "\n")
            price_date_info.append("---------------------------------------------------------------------------------")
            price_date_info.append("Total: " + pound+str(float(total_order[x]['price'])) + "0")
            price_date_info.append("---------------------------------------------------------------------------------")
            price_date_info.append("Time of Order: " + total_order[x]['time'])
            price_date_info.append("---------------------------------------------------------------------------------")
            price_date_info.append("Date of Order: " + total_order[x]['date'])
            price_date_info.append("---------------------------------------------------------------------------------")
        self.order_display_ui.customer_details_layout.addWidget(customer_details)
        self.order_display_ui.order_details_layout.addWidget(order_details)
        self.order_display_ui.price_info.addWidget(price_date_info)
        f = open('order.txt', 'w')
        f.write(str(customer_details))
        f.write(str(order_details))