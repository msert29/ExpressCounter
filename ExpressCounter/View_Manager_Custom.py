'''
Created on Jan 20, 2016

@author: murat
'''

import View_Manager_Generated
from PyQt4.Qt import QTableWidgetItem

class View_Manager_Custom(object):


    def __init__(self):
       super(View_Manager_Custom, self).__init__()
       self.generated_ui = View_Manager_Generated.Ui_Dialog()
       
    def setup_ui(self, dialog):
        self.generated_ui.setupUi(dialog)
    
    
    def echo_order(self, order):
        pound = u'\xa3'
        self.generated_ui.table_search_result.setRowCount(len(order))
        for x in range(0, len(order)):
            self.generated_ui.table_search_result.setItem(x,0, QTableWidgetItem(order[x]['id']))
            self.generated_ui.table_search_result.setItem(x,1, QTableWidgetItem(order[x]['customer_name']))
            self.generated_ui.table_search_result.setItem(x,2, QTableWidgetItem(order[x]['customer_address']))
            self.generated_ui.table_search_result.setItem(x,3, QTableWidgetItem(order[x]['customer_postcode']))
            self.generated_ui.table_search_result.setItem(x,4, QTableWidgetItem(order[x]['customer_tel']))
            self.generated_ui.table_search_result.setItem(x,5, QTableWidgetItem(pound + str(float(order[x]['price'])) + "0"))
            self.generated_ui.table_search_result.setItem(x,6, QTableWidgetItem(order[x]['date']))
            self.generated_ui.table_search_result.setItem(x,7, QTableWidgetItem(order[x]['time']))
            self.generated_ui.total_order.setText(str(order[x]['order_count']))
            self.generated_ui.total_income.setText(str(order[x]['price_count']) + "0")
        self.generated_ui.table_search_result.horizontalHeader().setStretchLastSection(True)
        self.generated_ui.table_search_result.verticalHeader().setStretchLastSection(True)