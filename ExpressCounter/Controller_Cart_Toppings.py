'''
Created on Apr 10, 2016

@author: murat
'''
import View_Cart_Toppings_Custom
import Controller_Cart_Dialog
from PyQt4.Qt import QDialog, Qt, QMessageBox, pyqtSlot, pyqtSignal

class Controller_Cart_Toppings(QDialog):
    custom_pizza_inserted = pyqtSignal(str, str, str, float, str, str)
    no_custom_toppings    = pyqtSignal(str, str, str, unicode, str)
    
    def __init__(self, extra_checkbox, toppings_list, pizza_size, pizza_name, pizza_id):
        super(Controller_Cart_Toppings, self).__init__()
        self.ui = View_Cart_Toppings_Custom.View_Cart_Toppings_Custom()
        self.ui.setupUI(self)
        self.main_cart = Controller_Cart_Dialog.Cart_Controller_Class()
        # a dynamic array to hold topping options
        self.__custom_topping_list = []
        self.pizza = []
        self.ui.generated_cart_toppings_ui.cancel_button.clicked.connect(lambda :self.close_request(extra_checkbox))
        self.display_toppings(toppings_list)
        self.ui.generated_cart_toppings_ui.add_to_cart_button.clicked.connect(lambda : self.handle_add_request(pizza_size, pizza_name, pizza_id))
        self.__extra_checkbox = extra_checkbox
        
        
    def close_request(self, extra_checkbox):
        for x in range(0, len(extra_checkbox)):
            if (extra_checkbox[x].checkState() == Qt.Checked):
                extra_checkbox[x].setCheckState(Qt.Unchecked)
        self.accept()
        
    def display_toppings(self, toppings_list):
        self.ui.display_custom_pizza_toppings(toppings_list)
        self.handle_custom_topping_selection(toppings_list)
    
    
    """-----------------------------------------------------------------------------
    Function    : handle_custom_topping_selection
    Description : This method is called in the Pizza section above which handles
                  user click events on custom toppings checkboxes.
                  
    Parameters  : topping_list (A list of toppings retreived from the database)
    returns     : Void
    ------------------------------------------------------------------------------"""    
    def handle_custom_topping_selection(self, topping_list):
        toppings = self.ui.get_toppings()
        toppings[0].stateChanged.connect(lambda : self.set_topping(toppings[0].checkState(), topping_list[0]['name']))
        toppings[1].stateChanged.connect(lambda : self.set_topping(toppings[1].checkState(), topping_list[1]['name']))
        toppings[2].stateChanged.connect(lambda : self.set_topping(toppings[2].checkState(), topping_list[2]['name']))
        toppings[3].stateChanged.connect(lambda : self.set_topping(toppings[3].checkState(), topping_list[3]['name']))
        toppings[4].stateChanged.connect(lambda : self.set_topping(toppings[4].checkState(), topping_list[4]['name']))
        toppings[5].stateChanged.connect(lambda : self.set_topping(toppings[5].checkState(), topping_list[5]['name']))
        toppings[6].stateChanged.connect(lambda : self.set_topping(toppings[6].checkState(), topping_list[6]['name']))
        toppings[7].stateChanged.connect(lambda : self.set_topping(toppings[7].checkState(), topping_list[7]['name']))
        toppings[8].stateChanged.connect(lambda : self.set_topping(toppings[8].checkState(), topping_list[8]['name']))
        toppings[9].stateChanged.connect(lambda : self.set_topping(toppings[9].checkState(), topping_list[9]['name']))
        toppings[10].stateChanged.connect(lambda : self.set_topping(toppings[10].checkState(), topping_list[10]['name']))
        toppings[11].stateChanged.connect(lambda : self.set_topping(toppings[11].checkState(), topping_list[11]['name']))
        toppings[12].stateChanged.connect(lambda : self.set_topping(toppings[12].checkState(), topping_list[12]['name']))
        toppings[13].stateChanged.connect(lambda : self.set_topping(toppings[13].checkState(), topping_list[13]['name']))
    
    @pyqtSlot(int, str)
    def set_topping(self, state, selected_topping):
        if state == Qt.Checked:
            self.__custom_topping_list.append(selected_topping)
        elif state == Qt.Unchecked:
            #print ("Removed" + selected_topping)
            rowNo = self.__custom_topping_list.index(selected_topping)
            self.__custom_topping_list.pop(rowNo)
            # Clear concatenated list as well as we pass the value of this to shopping list
            self.__cat_toppings = ""
        else:
            QMessageBox.critical(None, "Invalid topping checkbox state!", "The topping checkbox is in an unkown state")
            
    def clear_selected_checkboxes(self):
        for x in range(0, len(self.ui.toppings)):
            if (self.ui.toppings[x].checkState() == Qt.Checked):
                self.ui.toppings[x].toggle()
               
            
    @pyqtSlot(str, str)
    def handle_add_request(self, size, name, pizza_id):
        price = self.main_cart.database.get_price(name, size)
        #check if any toppings requested and update the price accordingly
        if (len(self.__custom_topping_list) > 0):
            topping_price = self.calculate_topping_price(size)
            price = float(price) + topping_price
            # concatenate the toppings into one string 
            self.__cat_toppings = " ".join(self.__custom_topping_list)
            
            # Now send it to the shopping list
            self.custom_pizza_inserted.emit("Pizza", size, name, price, self.__cat_toppings, pizza_id)
        else:
            self.no_custom_toppings.emit("Pizza", size, name, price, pizza_id)
        
        self.close_request(self.__extra_checkbox)
        

        
    """
    A list of custom toppings requested by the user therefore calculate the price of the toppings requested.
    """
    def calculate_topping_price(self, size):
        if (size == '9'):
            plus = (len(self.__custom_topping_list) * 0.90)
            return float(plus)
        elif (size == '12'):
            plus = (len(self.__custom_topping_list) * 1)
            return float(plus)
        else:
            QMessageBox.critical(None, "Price Error", "Pizza Custom topping price update error! unkown size!: " + str(size))

               