import View_Custom_Pizza_Generated
from PyQt4.Qt import QDialog, pyqtSlot, QMessageBox, pyqtSignal, Qt

class Controller_Custom_Pizza(QDialog):
    
    pizza_added  = pyqtSignal(str, str, str, str, int)

    def __init__(self, size, button_no):
        super(Controller_Custom_Pizza, self).__init__()
        self.ui = View_Custom_Pizza_Generated.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.button_no = button_no
        # if meal specifies 9 inch or 12 inch then disable it
        if size == "12":
            self.ui.size_sel.setCurrentIndex(1)
            self.ui.size_sel.setEnabled(False)
            self.pizza_size = size # 12 passed by initializer
        elif size == "9":
            self.ui.size_sel.setCurrentIndex(0)
            self.ui.size_sel.setEnabled(False)
            self.pizza_size = size # 9 passed by initializer
        else:
            # Default size and pizza
            self.pizza_size = "9"
        
        self.pizza_name = "Margarita"
        
        self.extra_toppings = [] # Dynamic list which shall store extra topping requests
        self.no_toppings    = [] # Dynamic list which shall store unwanted toppings
        

        
        self.handle_pizza_size_name()
        self.handle_topping_clicks()
        self.handle_no_topping_clicks()

        self.ui.cancel_button.clicked.connect(self.accept)
        self.ui.add_to_cart_button.clicked.connect(self.handle_add_request)

       
        
    def handle_pizza_size_name(self):
        self.ui.size_sel.currentIndexChanged.connect(lambda : self.handle_combo_assg("Size", self.ui.size_sel.currentText()))
        self.ui.pizza_sel.currentIndexChanged.connect(lambda : self.handle_combo_assg("Pizza", self.ui.pizza_sel.currentText()))
        
        
        
    pyqtSlot(str, str)
    def handle_combo_assg(self, combo_type, selection):
        if (combo_type == "Size"):
            self.pizza_size = selection
        elif (combo_type == "Pizza"):
            self.pizza_name = selection
        else:
            QMessageBox.critical(None, "Invalid Combobox Specifier", "Invalid Combobox selection please contact developer!")   
            
            
    def handle_topping_clicks(self):
        self.ui.pineapple_sel.stateChanged.connect(lambda : self.add_topping(self.ui.pineapple_sel.checkState(), "Pineapple"))
        self.ui.tomato_sel.stateChanged.connect(lambda : self.add_topping(self.ui.tomato_sel.checkState(), "Fresh Tomato"))
        self.ui.onion_sel.stateChanged.connect(lambda : self.add_topping(self.ui.onion_sel.checkState(), "Onion"))
        self.ui.olives_sel.stateChanged.connect(lambda : self.add_topping(self.ui.olives_sel.checkState(), "Olive"))
        self.ui.pepper_sel.stateChanged.connect(lambda : self.add_topping(self.ui.pepper_sel.checkState(), "Green Pepper"))
        self.ui.sweetcorn_sel.stateChanged.connect(lambda : self.add_topping(self.ui.sweetcorn_sel.checkState(), "Sweetcorn"))
        self.ui.jalapeno_sel.stateChanged.connect(lambda : self.add_topping(self.ui.jalapeno_sel.checkState(), "Jalapeno"))
        self.ui.mushroom_sel.stateChanged.connect(lambda : self.add_topping(self.ui.mushroom_sel.checkState(), "Mushroom"))
        self.ui.cheese_sel.stateChanged.connect(lambda : self.add_topping(self.ui.cheese_sel.checkState(), "Extra Cheese"))
        self.ui.beef_sel.stateChanged.connect(lambda : self.add_topping(self.ui.beef_sel.checkState(), "Spicy Beef"))
        self.ui.peperoni_sel.stateChanged.connect(lambda : self.add_topping(self.ui.peperoni_sel.checkState(), "Peperoni"))
        self.ui.ham_sel.stateChanged.connect(lambda : self.add_topping(self.ui.ham_sel.checkState(), "Ham"))
        self.ui.chicken_sel.stateChanged.connect(lambda : self.add_topping(self.ui.chicken_sel.checkState(), "Chicken"))
        self.ui.prawn_sel.stateChanged.connect(lambda : self.add_topping(self.ui.prawn_sel.checkState(), "Prawn"))
        self.ui.tuna_sel.stateChanged.connect(lambda : self.add_topping(self.ui.tuna_sel.checkState(), "Tuna"))
        
        
    def handle_no_topping_clicks(self):
        self.ui.no_pineapple_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_pineapple_sel.checkState(), "No Pineapple"))
        self.ui.no_tomato_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_tomato_sel.checkState(), "No Fresh Tomato"))
        self.ui.no_onion_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_onion_sel.checkState(), "No Onion"))
        self.ui.no_olive_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_olive_sel.checkState(), "No Olive"))
        self.ui.no_pepper_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_pepper_sel.checkState(), "No Green Pepper"))
        self.ui.no_sweetcorn_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_sweetcorn_sel.checkState(), "No Sweetcorn"))
        self.ui.no_jalapeno_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_jalapeno_sel.checkState(), "No Jalapeno"))
        self.ui.no_mushroom_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_mushroom_sel.checkState(), "No Mushroom"))
        self.ui.no_cheese_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_cheese_sel.checkState(), "No Extra Cheese"))
        self.ui.no_beef_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_beef_sel.checkState(), "No Spicy Beef"))
        self.ui.no_peperoni_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_peperoni_sel.checkState(), "No Peperoni"))
        self.ui.no_ham_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_ham_sel.checkState(), "No Ham"))
        self.ui.no_chicken_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_chicken_sel.checkState(), "No Chicken"))
        self.ui.no_prawn_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_prawn_sel.checkState(), "No Prawn"))
        self.ui.no_tuna_sel.stateChanged.connect(lambda : self.add_no_topping(self.ui.no_tuna_sel.checkState(), "No Tuna"))
        
    pyqtSlot(int, str)
    def add_topping(self, state, topping):
        if (state == Qt.Checked):
            self.extra_toppings.append(topping)
        elif (state == Qt.Unchecked):
            self.extra_toppings.remove(topping)
        else:
            pass
            
    pyqtSlot(int, str)
    def add_no_topping(self, state, topping):
        if (state == Qt.Checked):
            self.no_toppings.append(topping)
        elif (state == Qt.Unchecked):
            self.no_toppings.remove(topping)
        else:
            pass 
            
    def concat_extra_topping(self):
        topping = " ".join(self.extra_toppings)
        return topping
    
    def concat_no_topping(self):
        no_topping = " ".join(self.no_toppings)
        return no_topping
            
    def handle_add_request(self):
        if len (self.extra_toppings) > 0: 
            extra_topping = self.concat_extra_topping()
        if len(self.no_toppings) > 0:
            no_extra_topping = self.concat_no_topping()
        if len (self.extra_toppings) > 0 and len(self.no_toppings) > 0:
            self.pizza_added.emit(self.pizza_size, self.pizza_name, extra_topping, no_extra_topping, self.button_no)
        elif len (self.extra_toppings) > 0:
            self.pizza_added.emit(self.pizza_size, self.pizza_name, extra_topping, "None", self.button_no)
        elif len (self.no_toppings) > 0:
            self.pizza_added.emit(self.pizza_size, self.pizza_name, "None", no_extra_topping, self.button_no)
        else:
            self.pizza_added.emit(self.pizza_size, self.pizza_name, "None", "None", self.button_no)
            
        self.accept()
        