    #!/usr/bin/python
# -*- coding: utf-8 -*-

"""------------------------------------------------------------------------------
FILE        : Controller_Main_Menu 
DATE        : 20-12-2015
AUTHOR      : Murat Sert
DESCRIPTION : This class is responsible for handling user Events. It initiliazes
              the View_Main_Menu class which draws the GUI elements. 
              
------------------------------------------------------------------------------"""
                                                                                

"""------------------------------------------------------------------------------
                     Development Diary
    ------------------------------------------------------------------------------
    Date             Notes
    05/01/2016       Implemented the GUI Components
    07/01/2016       Issues with importing modules
              
-------------------------------------------------------------------------------"""
import sys
from PyQt4 import QtGui
from PyQt4.Qt import QLabel, QPixmap, QObject, QEvent, QDialog, QSpinBox, \
        QPushButton, QComboBox, QCheckBox, QHBoxLayout, QGridLayout
from PyQt4.QtCore import pyqtSlot, pyqtSignal
import View_Main_Menu
import Controller_Cart_Dialog 


"""------------------------------------------------------------------------------
Function           : clickable
Description        : This function extends events on the label widget.
                     By default there are no clicked events in labels therefore
                     this method is written to return capture and report click
                     events which is then assigned to each slot
Parameters         : Murat Sert
Returns            : true on clicked event, else returns false
------------------------------------------------------------------------------"""
def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked
        
class Controller_Main_Menu(QtGui.QMainWindow):
    
    def __init__(self):
        super(Controller_Main_Menu, self).__init__()
        # Initialize the view element and draw it
        self.main_view = View_Main_Menu.Ui_MainWindow()
        self.main_view.setupUi(self)
        self.show()
        self.handle_icon_clicks()
    
    def handle_icon_clicks(self):     
        clickable(self.main_view.neworder_lbl).connect(self.on_neworder_request)
        clickable(self.main_view.search_lbl).connect(self.on_search_order_request)
        clickable(self.main_view.manager_lbl).connect(self.on_manager_mode_request)
        clickable(self.main_view.newcustomer_lbl).connect(self.on_create_new_customer_request)

    @pyqtSlot()
    def on_neworder_request(self):
        # A new order request has been received, therefore initialize
        # and execute the cart_dialog class
        self.cart_dialog = Controller_Cart_Dialog.Cart_Controller_Class()
        self.cart_dialog.exec_()
        
    @pyqtSlot()
    def on_search_order_request(self):
        print "Search order loaded"
        
    @pyqtSlot()
    def on_manager_mode_request(self):
        print "Manager mode loaded"
      
    @pyqtSlot()
    def on_create_new_customer_request(self):
        print "New customer dialog loaded"
           
        
def main():
    app = QtGui.QApplication(sys.argv)
    vmm = Controller_Main_Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
