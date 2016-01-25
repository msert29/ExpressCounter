'''
Created on Jan 24, 2016

@author: murat
'''

import View_Customer_Mode_Generated
from PyQt4.Qt import QTableWidgetItem, QPushButton
from PyQt4.QtGui import QButtonGroup

class View_Customer_Mode_Custom(object):

    def __init__(self):
        super(View_Customer_Mode_Custom, self).__init__()
        self.generated_ui = View_Customer_Mode_Generated.Ui_Dialog()
        self.__delete_button_group = QButtonGroup()
        self.__reuslt = 0
    def setup_ui(self, dialog):
        self.generated_ui.setupUi(dialog)
        
    def echo_search_results(self, result):
        self.generated_ui.new_name_entry.setText(result['name'])
        self.generated_ui.new_addr_entry.setText(result['address'])
        self.generated_ui.new_postcode_entry.setText(result['postcode'])
        self.generated_ui.new_tel_entry.setText(result['number'])
    
    def echo_delete_results(self, result):
        # self.__result is used to calculate the id
        self.__result = result
        self.generated_ui.delete_table_search.setRowCount(len(result))
        for x in range(0, len(result)):
            self.generated_ui.delete_table_search.setItem(x,0, QTableWidgetItem(result[x]['id']))
            self.generated_ui.delete_table_search.setItem(x,1, QTableWidgetItem(result[x]['name']))
            self.generated_ui.delete_table_search.setItem(x,2, QTableWidgetItem(result[x]['address']))
            self.generated_ui.delete_table_search.setItem(x,3, QTableWidgetItem(result[x]['postcode']))
            self.generated_ui.delete_table_search.setItem(x,4, QTableWidgetItem(result[x]['number']))
            delete_button = QPushButton("Delete")
            self.__delete_button_group.addButton(delete_button, x)
            self.generated_ui.delete_table_search.setCellWidget(x, 5, delete_button)
        
        self.generated_ui.delete_table_search.horizontalHeader().setVisible(True)
        self.generated_ui.delete_table_search.horizontalHeader().setStretchLastSection(True)

    def get_delete_buttons(self):
        return self.__delete_button_group
    
    def calculate_id(self, button_id):
        return str(self.__result[button_id]['id'])