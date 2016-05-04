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
            if x <= 5:
                self.__toppings[x] = QCheckBox(toppings_list[x]['name'])
                self.generated_cart_toppings_ui.meat_topping_layout.addWidget(self.__toppings[x])
            else:
                self.__toppings[x] = QCheckBox(toppings_list[x]['name'])
                self.generated_cart_toppings_ui.veg_topping_layout.addWidget(self.__toppings[x])


    def get_toppings(self):
        return self.__toppings
    
    def display_custom_pizza_toppings_no(self, toppings_list):
        topping_length = len(toppings_list)
        # Layout variables to display data
        placeholder = 0
        pc = 0 
        self.__no_toppings = [None] * topping_length
        for x in range(0, topping_length):
            if x <= 5:
                self.__no_toppings[x] = QCheckBox("No " + toppings_list[x]['name'])
                
                if (x == 0) or (x == 1):
                    self.generated_cart_toppings_ui.n.addWidget(self.__no_toppings[x], 0, pc)
                elif (x == 2) or (x==3):
                    self.generated_cart_toppings_ui.n.addWidget(self.__no_toppings[x], 1, pc)
                else:
                    self.generated_cart_toppings_ui.n.addWidget(self.__no_toppings[x], 2, pc)                     
                if (pc == 1):
                    pc = 0
                else:
                    pc = 1
            else:
                for i in range(6, topping_length):
                    self.__no_toppings[i] = QCheckBox("No " + toppings_list[i]['name'])
                    if (i == 0) or (i == 1):
                        self.generated_cart_toppings_ui.no_veg_layout.addWidget(self.__no_toppings[i], 0, placeholder)
                    elif (i==2) or (i == 3):
                        self.generated_cart_toppings_ui.no_veg_layout.addWidget(self.__no_toppings[i], 1, placeholder)
                    elif (i==4) or (i == 5):
                        self.generated_cart_toppings_ui.no_veg_layout.addWidget(self.__no_toppings[i], 2, placeholder)
                    elif (i==6) or (i == 7):
                        self.generated_cart_toppings_ui.no_veg_layout.addWidget(self.__no_toppings[i], 3, placeholder)
                    elif (i==8) or (i == 9):
                        self.generated_cart_toppings_ui.no_veg_layout.addWidget(self.__no_toppings[i], 4, placeholder)
                    elif (i==10) or (i == 11):
                        self.generated_cart_toppings_ui.no_veg_layout.addWidget(self.__no_toppings[i], 5, placeholder)
                    else:
                        self.generated_cart_toppings_ui.no_veg_layout.addWidget(self.__no_toppings[i], 6, placeholder)

                    # Increment the place holder
                    if (placeholder == 1):
                        placeholder = 0
                    else:
                        placeholder = 1

    def get_no_toppings(self):
        return self.__no_toppings