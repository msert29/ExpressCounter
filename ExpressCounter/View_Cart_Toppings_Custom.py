'''
Created on Apr 10, 2016

@author: murat
'''
import View_Cart_Toppings_Generated
from PyQt4.Qt import QObject, QCheckBox

class View_Cart_Toppings_Custom(QObject):

    def __init__(self):
        super(View_Cart_Toppings_Custom, self).__init__()
        # Import the generated GUI Elements
        self.generated_cart_toppings_ui = View_Cart_Toppings_Generated.Ui_Dialog()

        
    def setupUI(self, dialog):
        self.generated_cart_toppings_ui.setupUi(dialog)
        
        
    def display_custom_pizza_toppings(self, toppings_list):
        topping_length = len(toppings_list)
        # Layout variables to display data
       
        self.__toppings = [None] * topping_length
        for x in range(0, topping_length):
            if x <= 4:
                self.__toppings[x] = QCheckBox(toppings_list[x]['name'])
                self.generated_cart_toppings_ui.meat_topping_layout.addWidget(self.__toppings[x])
            else:
                self.__toppings[x] = QCheckBox(toppings_list[x]['name'])
                self.generated_cart_toppings_ui.veg_topping_layout.addWidget(self.__toppings[x])


    def get_toppings(self):
        return self.__toppings