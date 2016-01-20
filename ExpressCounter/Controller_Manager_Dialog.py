'''
Created on Jan 20, 2016

@author: murat
'''
from PyQt4.Qt import QDialog, QDate, QMessageBox
import View_Manager_Custom
import Model_Database_Dialog
class Controller_Manager_Dialog(QDialog):

    def __init__(self):
        super(Controller_Manager_Dialog, self).__init__()
        self.custom_ui = View_Manager_Custom.View_Manager_Custom()
        self.custom_ui.setup_ui(self)
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        self.custom_ui.generated_ui.date_selection.clearMaximumDate()
        current_date = QDate.currentDate()
        self.custom_ui.generated_ui.date_selection.setDate(current_date)
        self.__date = current_date.toString("yyyy-MM-dd")
        self.handle_manager_mode_requests()
        self.custom_ui.generated_ui.total_order.setReadOnly(True)
        self.custom_ui.generated_ui.total_income.setReadOnly(True)
    def handle_manager_mode_requests(self):
        self.custom_ui.generated_ui.date_selection.dateChanged[QDate].connect(self.set_date)
        self.custom_ui.generated_ui.arrange.clicked.connect(lambda : self.order(self.__date))
        self.custom_ui.generated_ui.signout_button.clicked.connect(self.close)
    
    def set_date(self, date):
        self.__date = date.toString("yyyy-MM-dd")
        
    def order(self, date):
        order = self.database.search_order_by_date(self.__date)
        if (len(order) > 0):
            self.custom_ui.echo_order(order)
        else:
            QMessageBox.critical(None, "No Results Returned!", "No Matching Results returned, please choose a different date!")