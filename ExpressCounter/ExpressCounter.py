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
from PyQt4.Qt import QLabel, QPixmap, QObject, QEvent, QDialog, QSpinBox, QPushButton, QComboBox, QCheckBox, QHBoxLayout, QGridLayout
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from cart import Ui_Dialog


def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked





        
class Express_Counter(QtGui.QMainWindow):
    
    ""
    
    def __init__(self):
        super(Express_Counter, self).__init__()
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
        self.dial = Ui_Dialog()
        
        self.show()
        clickable(neworder_lbl).connect(self.on_pushButton_clicked)
  
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.dial.exec_()
        
          
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Express_Counter()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
