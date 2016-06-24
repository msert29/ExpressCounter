from PyQt4.Qt import QDialog, pyqtSignal

import View_Garlic_Bread_Generated
class Controller_GB_Custom(QDialog):
    gb_confirmed = pyqtSignal(str, str, str, int)
    
    def __init__(self):
        super(Controller_GB_Custom, self).__init__()
        self.ui = View_Garlic_Bread_Generated.Ui_GarlicBreadSelection()
        self.ui.setupUi(self)
        
        #assign default value to sauce
        self.name = "Garlic Bread"
        self.option = "No Cheese"
        
        self.ui.cheese_sel.currentIndexChanged.connect(lambda : self.assign_cheese(self.ui.cheese_sel.currentText()))
        self.ui.cancel_button.clicked.connect(self.accept)
        self.ui.add_to_cart_button.clicked.connect(self.confirmed)
        
    def assign_cheese(self, option):
        self.option = option
        print self.option
    
    def confirmed(self):
        # as garlic bread is stored under "Garlic Bread", is no cheese is selected we need to send Garlic bread only
        if self.option == "No Cheese":
            self.name = "Garlic Bread"
        else:
            self.name = "Garlic Bread Cheese"
            print self.name
        self.gb_confirmed.emit("Other", self.name, "Standard", 0)
        self.accept()