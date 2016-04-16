'''
Created on Apr 11, 2016

@author: murat
'''
import View_Cart_Addon_Custom
import Model_Database_Dialog
from PyQt4.Qt import QDialog, pyqtSlot, QMessageBox, pyqtSignal
from PyQt4.QtCore import Qt

class Controller_Cart_Addon(QDialog):
    
    # burger 7 args, "Burger", name, cheese_selection, price, salad, sauce, id
    # kebab 8 args    "Kebab", size, name, type, price, salad, sauce, id
    
    burger_added = pyqtSignal(str, str, str, float, str, str, str)
    kebab_added  = pyqtSignal(str, str, str, str, float, str, str, str)
    
    def __init__(self, product_type, product_name, size, price, product_id):
        super(Controller_Cart_Addon, self).__init__()
        self.ui = View_Cart_Addon_Custom.View_Cart_Addon_Custom()
        self.ui.setupUi(self)
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        #combobox selection variables
        #these might be set but we will assign default values in case the user doesn't make another selection
        self.size_selection = "Small"
        self.type = "Pitta"
        self.cheese = "No Cheese"
        
        self.salad_array = []
        self.sauce_array = []
        self.cheese_sel = "No Cheese"
        
        
        self.product_type = product_type
        
        # Wrap/Pitta choices are not valid for burgers
        if self.product_type == "Burger":
            self.ui.generated_ui.type_sel.setEnabled(False)
            self.ui.generated_ui.size_sel.setEnabled(False)
        
        
        # assign price and name for product and calculate price acordingly 
        self.product_name = product_name
        self.product_price        = price
        self.product_size         = size
        self.product_id           = product_id
        
        self.handle_buttons()
        self.handle_salad_checkbox_events()
        self.handle_sauce_checkboxes_events()
        self.handle_combobox_list_events()
        
        
    def handle_buttons(self):
        self.ui.generated_ui.cancel_button.clicked.connect(self.accept)
        self.ui.generated_ui.add_to_cart_button.clicked.connect(self.handle_add_request)
            
            
    def handle_salad_checkbox_events(self):
        self.ui.generated_ui.all_salad_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.all_salad_sel.checkState(), "All Salad"))
        self.ui.generated_ui.lorw_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.lorw_sel.checkState(), "L/O/R/W"))
        self.ui.generated_ui.fried_special_sel.stateChanged.connect(lambda : \
                                        self.handle_salad(self.ui.generated_ui.fried_special_sel.checkState(), "Fried Specials"))
        self.ui.generated_ui.lettuce_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.lettuce_sel.checkState(), "Lettuce"))
        self.ui.generated_ui.w_cabbage_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.w_cabbage_sel.checkState(), "White Cabbage"))
        self.ui.generated_ui.r_cabbage_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.r_cabbage_sel.checkState(), "Red Cabbage"))
        self.ui.generated_ui.onion_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.onion_sel.checkState(), "Onion"))
        self.ui.generated_ui.tomato_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.tomato_sel.checkState(), "Tomato"))
        self.ui.generated_ui.cucumber_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.cucumber_sel.checkState(), "Cucumber"))
        self.ui.generated_ui.pickle_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.pickle_sel.checkState(), "Pickle"))
        
        # No Salad section
        self.ui.generated_ui.no_salad_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.no_salad_sel.checkState(), "No Salad"))
        self.ui.generated_ui.no_lettuce_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.no_lettuce_sel.checkState(), "No Lettuce"))
        self.ui.generated_ui.no_onion_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.no_onion_sel.checkState(), "No Onion"))
        self.ui.generated_ui.no_cab_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.no_cab_sel.checkState(), "No Cabbage"))
        self.ui.generated_ui.no_tomato_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.no_tomato_sel.checkState(), "No Tomato"))
        self.ui.generated_ui.no_cucumber_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.no_cucumber_sel.checkState(), "No Cucumber"))
        self.ui.generated_ui.no_pick_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.generated_ui.no_pick_sel.checkState(), "No Pickle"))
        
    def handle_sauce_checkboxes_events(self):
        self.ui.generated_ui.chilli_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.generated_ui.chilli_sel.checkState(), "Chilli Sauce"))
        self.ui.generated_ui.mayo_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.generated_ui.mayo_sel.checkState(), "Mayonaise"))
        self.ui.generated_ui.gm_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.generated_ui.gm_sel.checkState(), "Garlic Mayo"))
        self.ui.generated_ui.ketchup_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.generated_ui.ketchup_sel.checkState(), "Ketchup"))
        self.ui.generated_ui.bbq_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.generated_ui.bbq_sel.checkState(), "BBQ"))
        self.ui.generated_ui.relish_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.generated_ui.relish_sel.checkState(), "Relish"))
        self.ui.generated_ui.sweet_chill_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.generated_ui.sweet_chill_sel.checkState(), "Sweet Chilli"))
        self.ui.generated_ui.no_sauce_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.generated_ui.no_sauce_sel.checkState(), "No Sauce"))

    def handle_combobox_list_events(self):
        self.ui.generated_ui.type_sel.currentIndexChanged.connect(lambda : self.handle_combo_assg("Type", self.ui.generated_ui.type_sel.currentText()))
        self.ui.generated_ui.size_sel.currentIndexChanged.connect(lambda : self.handle_combo_assg("Size", self.ui.generated_ui.size_sel.currentText()))
        self.ui.generated_ui.cheese_sel.currentIndexChanged.connect(lambda : self.handle_combo_assg("Cheese", self.ui.generated_ui.cheese_sel.currentText()))

    
    pyqtSlot(int, str)
    def handle_salad(self, state, salad):
        if (state == Qt.Checked):
            self.salad_array.append(salad)
        elif (state == Qt.Unchecked):
            self.salad_array.remove(salad)
                
    pyqtSlot(int, str)
    def handle_sauce(self, state, sauce):
        if (state == Qt.Checked):
            self.sauce_array.append(sauce)
        elif (state == Qt.Unchecked):
            self.sauce_array.remove(sauce)
    
    pyqtSlot(str, str)
    def handle_combo_assg(self, combo_type, selection):
        if (combo_type == "Type"):
            self.type = selection
        elif (combo_type == "Size"):
            self.size_selection = selection
        elif (combo_type == "Cheese"):
            self.cheese = selection
        else:
            QMessageBox.critical(None, "Invalid Combobox Specifier", "Invalid Combobox selection please contact developer!")   


    def handle_add_request(self):
        salad = self.concat_salad()
        sauce = self.concat_sauce()
        if salad == "" or sauce == "":
            QMessageBox.critical(None, "Select Salad/Sauce", "Please make a salad/sauce selection in order to proceed")
            print self.salad_array + self.sauce_array
        else:
            price = self.calculate_price(self.product_name, self.size_selection, self.product_type)
            
            if self.product_type == "Kebab":
                self.kebab_added.emit("Kebab", self.product_size, self.product_name, self.type, price, salad, sauce, self.product_id)
            else:
                self.burger_added.emit("Burger", self.product_name, self.cheese, price, salad, sauce, self.product_id)
            
            self.accept()
    
    def concat_salad(self):
        salad = " ".join(self.salad_array)
        return salad
    
    def concat_sauce(self):
        sauce = " ".join(self.sauce_array)
        return sauce
    
    def calculate_price(self, name, size, product_type):
        # cheese, small/large and fried specials will affect price
        price = self.database.get_price(name, size)
        if self.cheese == "Cheese":
            if product_type == "Kebab":
                price = float(price) + 1.00
            elif product_type == "Burger":
                price = float(price) + 0.20
            else:
                QMessageBox.critical(None, "Invalid Product Specifier", "Invalid product specifier!")

        if self.salad_array.count("Fried Specials") > 0:
            price = float(price) + 1.00
                
        return float(price)
    
    def print_it(self):
        print self.salad_array