    #!/usr/bin/python
# -*- coding: utf-8 -*-

"""------------------------------------------------------------------------------
FILE        : View_Main_Menu 
DATE        : 20-12-2015
AUTHOR      : Murat Sert
DESCRIPTION : This class is responsible for displaying GUI components. It calls a 
              list of other GUI Classes which construct the core elements.
              
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
from core import Ui_MainWindow
from PyQt4.Qt import QLabel, QPixmap, QObject, QEvent, QDialog, QSpinBox, \
        QPushButton, QComboBox, QCheckBox, QHBoxLayout, QGridLayout
from PyQt4.QtCore import pyqtSlot, pyqtSignal
import View_Cart_Dialog



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
        
class View_Main_Menu(QtGui.QMainWindow):
    
    ""
    
    def __init__(self):
        super(View_Main_Menu, self).__init__()
        self.background = Ui_MainWindow()
        self.background.setupUi(self)
        self.initUI()

    
    def initUI(self):     
                  
        neworder_icon = QtGui.QPixmap('images/icn-phone2.png')
        manager_icon = QPixmap('images/admin-icon.png')
        search_icon = QPixmap('images/search-icon.png')
        newcustomer_icon = QPixmap('images/newcustomer-icon.png')
        
        neworder_lbl = QLabel("Place an order")
        manager_lbl = QLabel("Manager Log in")
        search_lbl = QLabel("Search")
        newcustomer_lbl = QLabel("New Customer Entry")
        
        manager_lbl.setPixmap(manager_icon)
        search_lbl.setPixmap(search_icon)
        neworder_lbl.setPixmap(neworder_icon)
        newcustomer_lbl.setPixmap(newcustomer_icon)
        
        self.background.new_order_layout.addWidget(neworder_lbl)
        self.background.manager_layout.addWidget(manager_lbl)
        self.background.search_order_layout.addWidget(search_lbl)
        self.background.newcustomer_layout.addWidget(newcustomer_lbl)
        self.cart_dialog = View_Cart_Dialog.Ui_Dialog()
        
        self.show()
        clickable(neworder_lbl).connect(self.on_neworder_clicked)
  
        
    @pyqtSlot()
    def on_neworder_clicked(self):
        self.cart_dialog.exec_()
        
          
        
def main():
    app = QtGui.QApplication(sys.argv)
    vmm = View_Main_Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
