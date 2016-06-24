

from PyQt4.Qt import QDialog, pyqtSlot, QMessageBox, pyqtSignal
from PyQt4.QtCore import Qt


import View_Custom_Kebab_Generated

class Controller_Custom_Kebab(QDialog):
    
    kebab_added  = pyqtSignal(str, str, str, str, str, int)

    def __init__(self, kebab_size, kebab_name, button_no):
        super(Controller_Custom_Kebab, self).__init__()
        self.ui = View_Custom_Kebab_Generated.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.button_no = button_no # some meals contain two components of the same type so we need to disable the clicked button
        
        self.type = "Pitta"
    
        self.kebab_name = "Doner"
        self.salad_array = []
        self.sauce_array = []
        self.cheese_sel = "No Cheese"
    
        self.handle_buttons()
        self.handle_salad_checkbox_events()
        self.handle_sauce_checkboxes_events()
        self.handle_combobox_list_events()
        
        if kebab_name == "House Special":
            self.ui.kebab_sel.setCurrentIndex(7)
            self.ui.kebab_sel.setEnabled(False)
            self.kebab_name = "House Special"
        if kebab_size == "Small":
            self.ui.size_sel.setEnabled(False)
            self.size_selection = kebab_size
        elif kebab_size == "Large":
            self.ui.size_sel.setEnabled(False)
            self.size_selection = kebab_size
        else:
            self.size_selection = "Small"
            pass
            
    def handle_buttons(self):
        self.ui.cancel_button.clicked.connect(self.accept)
        self.ui.add_to_cart_button.clicked.connect(self.handle_add_request)
            
            
    def handle_salad_checkbox_events(self):
        self.ui.all_salad_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.all_salad_sel.checkState(), "All Salad"))
        self.ui.lorw_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.lorw_sel.checkState(), "L/O/R/W"))
        self.ui.fried_special_sel.stateChanged.connect(lambda : \
                                        self.handle_salad(self.ui.fried_special_sel.checkState(), "Fried Specials"))
        self.ui.lettuce_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.lettuce_sel.checkState(), "Lettuce"))
        self.ui.w_cabbage_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.w_cabbage_sel.checkState(), "White Cabbage"))
        self.ui.r_cabbage_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.r_cabbage_sel.checkState(), "Red Cabbage"))
        self.ui.onion_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.onion_sel.checkState(), "Onion"))
        self.ui.tomato_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.tomato_sel.checkState(), "Tomato"))
        self.ui.cucumber_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.cucumber_sel.checkState(), "Cucumber"))
        self.ui.pickle_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.pickle_sel.checkState(), "Pickle"))
        
        # No Salad section
        self.ui.no_salad_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.no_salad_sel.checkState(), "No Salad"))
        self.ui.no_lettuce_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.no_lettuce_sel.checkState(), "No Lettuce"))
        self.ui.no_onion_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.no_onion_sel.checkState(), "No Onion"))
        self.ui.no_cab_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.no_cab_sel.checkState(), "No Cabbage"))
        self.ui.no_tomato_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.no_tomato_sel.checkState(), "No Tomato"))
        self.ui.no_cucumber_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.no_cucumber_sel.checkState(), "No Cucumber"))
        self.ui.no_pick_sel.stateChanged.connect(lambda : self.handle_salad(self.ui.no_pick_sel.checkState(), "No Pickle"))
        
    def handle_sauce_checkboxes_events(self):
        self.ui.chilli_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.chilli_sel.checkState(), "Chilli Sauce"))
        self.ui.mayo_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.mayo_sel.checkState(), "Mayonaise"))
        self.ui.gm_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.gm_sel.checkState(), "Garlic Mayo"))
        self.ui.ketchup_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.ketchup_sel.checkState(), "Ketchup"))
        self.ui.bbq_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.bbq_sel.checkState(), "BBQ"))
        self.ui.relish_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.relish_sel.checkState(), "Relish"))
        self.ui.sweet_chill_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.sweet_chill_sel.checkState(), "Sweet Chilli"))
        self.ui.no_sauce_sel.stateChanged.connect(lambda : self.handle_sauce(self.ui.no_sauce_sel.checkState(), "No Sauce"))

    def handle_combobox_list_events(self):
        self.ui.type_sel.currentIndexChanged.connect(lambda : self.handle_combo_assg("Type", self.ui.type_sel.currentText()))
        self.ui.size_sel.currentIndexChanged.connect(lambda : self.handle_combo_assg("Size", self.ui.size_sel.currentText()))
        self.ui.kebab_sel.currentIndexChanged.connect(lambda : self.handle_combo_assg("Kebab", self.ui.kebab_sel.currentText()))
    
    pyqtSlot(int, str)
    def handle_salad(self, state, salad):
        if (state == Qt.Checked):
            self.salad_array.append(salad)
        elif (state == Qt.Unchecked):
            self.salad_array.remove(salad)
        else:
            pass
                
    pyqtSlot(int, str)
    def handle_sauce(self, state, sauce):
        if (state == Qt.Checked):
            self.sauce_array.append(sauce)
        elif (state == Qt.Unchecked):
            self.sauce_array.remove(sauce)
        else:
            pass
    
    pyqtSlot(str, str)
    def handle_combo_assg(self, combo_type, selection):
        if (combo_type == "Type"):
            self.type = selection
        elif (combo_type == "Size"):
            self.size_selection = selection
        elif (combo_type == "Kebab"):
            self.kebab_name = selection
        else:
            QMessageBox.critical(None, "Invalid Combobox Specifier", "Invalid Combobox selection please contact developer!")   
    
    
    def handle_add_request(self):
        salad = self.concat_salad()
        sauce = self.concat_sauce()
        if salad == "" or sauce == "":
            QMessageBox.critical(None, "Select Salad/Sauce", "Please make a salad/sauce selection in order to proceed")
            #print self.salad_array + self.sauce_array
        else:
            self.kebab_added.emit(self.size_selection, self.type, self.kebab_name, salad, sauce, self.button_no)
            self.accept()
    
    def concat_salad(self):
        salad = " ".join(self.salad_array)
        return salad
    
    def concat_sauce(self):
        sauce = " ".join(self.sauce_array)
        return sauce
    
    
        