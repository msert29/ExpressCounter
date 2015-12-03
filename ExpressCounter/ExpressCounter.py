    #!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar and a central widget. 

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

import sys
from PyQt4 import QtGui
from core import Ui_MainWindow
from PyQt4.Qt import QLabel, QPixmap, QObject, QEvent, QDialog, QSpinBox, QPushButton, QComboBox, QCheckBox, QHBoxLayout, QGridLayout
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from cart import Ui_Dialog


class PenPropertiesDlg(QDialog):
    def __init__(self, parent=None):
        super(PenPropertiesDlg, self).__init__(parent)
        
        widthLabel = QLabel("&Width:")
        self.widthSpinBox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        #self.widthSpinBox.setAlignment(Qt.AlignRight)
        self.widthSpinBox.setRange(0, 24)
        self.bevelledCheckBox = QCheckBox("&Bevelled edges")
        styleLabel = QLabel("&Style:")
        self.styleComboBox = QComboBox()
        
        styleLabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(["Solid", "Dashed", "Dotted",
                             "DashDotted", "DashDotDotted"])
        okButton = QPushButton("&OK")
        cancelButton = QPushButton("Cancel")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(self.bevelledCheckBox, 0, 2)
        layout.addWidget(styleLabel, 1, 0)
        layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)


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

        
        
class Example(QtGui.QMainWindow):
    
    ""
    
    def __init__(self):
        super(Example, self).__init__()
        self.background = Ui_MainWindow()
        self.background.setupUi(self)
        self.initUI()

        
    def initUI(self):               
        pixmap_image = QtGui.QPixmap('images/order.png')
        manager_icon = QPixmap('images/root.png')
        search_icon = QPixmap('images/search.png')
        manager_lbl = QLabel("Manager Log in")
        manager_lbl.setPixmap(manager_icon)
        search_lbl = QLabel("Search")
        search_lbl.setPixmap(search_icon)
        lbl = QLabel("Place an order")
        lbl.setPixmap(pixmap_image)
        
        self.background.new_order_layout.addWidget(lbl)
        self.background.m.addWidget(manager_lbl)
        self.background.search_order_layout.addWidget(search_lbl)
        self.dial = Ui_Dialog()
        
        self.show()
        clickable(lbl).connect(self.on_pushButton_clicked)
  
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.dial.exec_()
        
          
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
