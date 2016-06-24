from PyQt4.Qt import QDialog, pyqtSignal


import View_Custom_Drink_Generated

class Controller_Custom_Drink(QDialog):
    
    drink_added  = pyqtSignal(str, str, int)

    def __init__(self, size, button_no):
        super(Controller_Custom_Drink, self).__init__()
        self.ui = View_Custom_Drink_Generated.Ui_Dialog()
        self.ui.setupUi(self)
        self.button_no = button_no
        self.size = size
        self.name = "Coca Cola" # the first element in the ui Element

        if size == "Bottle":
            self.ui.drink_sel.clear()
            bottle_option = ["Coca Cola", "Diet Coke", "Pepsi", "Orange Tango"]
            #for option in bottle_option:
            self.ui.drink_sel.addItems(bottle_option)
            self.ui.size_sel.setCurrentIndex(1)
            self.ui.size_sel.setEnabled(False)
        elif size == "Can":
            self.ui.size_sel.setEnabled(False) # Drink size will be determined by the meal anyway so disabled it
        else:
            pass # should never hit this case as meal drink size is determined
        
        self.ui.drink_sel.currentIndexChanged.connect(lambda : self.handle_drink_selection(self.ui.drink_sel.currentText()))
        self.ui.size_sel.currentIndexChanged.connect(lambda  : self.handle_size_selection(self.ui.size_sel.currentText()))
        self.ui.add_to_cart_button.clicked.connect(self.handle_add_button)
        self.ui.cancel_button.clicked.connect(self.accept)
    
    def handle_drink_selection(self, drink):
        self.name = drink
    
    def handle_size_selection(self, size):
        self.size = size
        
    def handle_add_button(self):
        self.drink_added.emit(self.size, self.name, self.button_no)
        self.accept()
    