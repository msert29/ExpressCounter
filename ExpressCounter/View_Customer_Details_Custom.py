'''
Created on Dec 31, 2015

@author: murat
'''
import View_Customer_Details_Generated
import Model_Database_Dialog
from PyQt4.Qt import QObject, QListWidget, QListWidgetItem

class View_Customer_Details_Custom(QObject):


    def __init__(self):
        super(View_Customer_Details_Custom, self).__init__()
        self.customer_generated_view = View_Customer_Details_Generated.Ui_Dialog()
    
    def setupUi(self, dialog):
        self.customer_generated_view.setupUi(dialog)
        self.customer_id_result = []
        self.search_results = QListWidget()
        self.customer_generated_view.search_results_layout.addWidget(self.search_results)
        
    """ 
    This function will receive a dictionary of the search 
    results. It will organise it to a string and display it
    appropriatly"""
    def display_existing_customer_results(self, search_result):
        if (len (search_result) == 1):
            id       = search_result[0]['id']
            name     = search_result[0]['name']
            address  = search_result[0]['address']
            postcode = search_result[0]['postcode']
            number   = search_result[0]['number'] 
            customer_info = " Name: " + str(name) + " Address: " + str(address) + " Postcode: " + str(postcode) + " Number: " + str(number)
            customer_info = QListWidgetItem(customer_info)
            self.search_results.addItem(customer_info)
            self.customer_id_result.append(id)
        elif (len (search_result) > 1):
            for x in range (0, len(search_result)):
                id       = search_result[x]['id']
                name     = search_result[x]['name']
                address  = search_result[x]['address']
                postcode = search_result[x]['postcode']
                number   = search_result[x]['number'] 
                customer_info = " Name: " + str(name) + " Address: " + str(address) + " Postcode: " + str(postcode) + " Number: " + str(number)
                customer_info = QListWidgetItem(customer_info)
                self.search_results.addItem(customer_info)
                self.customer_id_result.append(id)
        else:
            print "SHould never hit this case"