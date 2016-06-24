import View_Cart_Generated
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt , pyqtSlot, pyqtSignal
from PyQt4.Qt import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox,\
    QComboBox, QPushButton, QCheckBox, QObject, QEvent, QListWidget, QListWidgetItem,\
    QStandardItemModel, QStandardItem, QLineEdit
from PyQt4.QtGui import QButtonGroup



    
"""------------------------------------------------------------------------------
FILE        : View_Cart_Custom
DATE        : 13-12-2015
AUTHOR      : Murat Sert
DESCRIPTION : This class is responsible for populating the generated UI fields
              by the Qt Creator. Decision of the addition of the 'Custom' 
              component to the MVC architecture has just been made as a result of
              constantly updated UI Designs. After each update, the generated code
              gets updated as well thus clearing any code written by the developer.
              Instead I have taken another approach of adding in a Custom View architecture.
              With this architecture, Any generated files are untouched and instead of
              directly appending code to these generate classes, we instance them
              in the custom class and populate the views via custom component.
            
             The controller constructs will be connected to these classes directly,
             rather than the View_Cart_Generated.
------------------------------------------------------------------------------"""
                                                                                

"""------------------------------------------------------------------------------
                     Development Diary
    ------------------------------------------------------------------------------
    Date             Notes
    13/12/2015       Creation of the class and successfully instanced from 
                     Controller_Cart_Dialog class.

              
-------------------------------------------------------------------------------"""

class View_Cart_Custom(QObject):
    def __init__(self):
        super(View_Cart_Custom, self).__init__()
        # Import the generated GUI Elements
        self.generated_cart_ui = View_Cart_Generated.Ui_widget()
        pound = u'\xa3'
        self.__total_price_display = QLineEdit(pound + "00.00")
        self.burger_add_button_group = QButtonGroup()
        self.drinks_add_button_group = QButtonGroup()
        
    def setupUI(self, dialog):
        self.generated_cart_ui.setupUi(dialog)
        self.generated_cart_ui.total_price_display.addWidget(self.__total_price_display)
        
    def get_total_price(self):
        return self.__total_price_display
    """------------------------------------------------------------------------------
    Function           : display_kebabs
    Description        : This function retrieves a list of kebab options from the 
                         Controller_Cart_Dialog class. It then iterates through 
                         all of the options, creates a salad and sauce combobox
                         selection for each item and an add button for the item
                         to be added to the cart.
    Parameters         : kebabs_list (This parameter is fetched by Controller_Cart_Dialog
                         class which accesses the DatabaseConnection class -> get_kebabs()
                         method which iterates through the Items table in the database selecting
                         items with type = 'kebab' only. The list is then passed to this method
                         which is directly called in Controller_Cart_Dialog
    Returns            : Void
    ------------------------------------------------------------------------------"""
    def display_kebabs(self, kebabs_list):
        kebabs_length = len(kebabs_list)
        #holds the position of widget
        place_holder = 0 
        self.select_button_group = QButtonGroup()
        for i in range(kebabs_length):
            Select_Button = QPushButton("Select")
            self.select_button_group.addButton(Select_Button, i)
            
            # Need a groupbox which will hold a bundle of QLabel, QComboBox and QPushbutton
            kebab_group_box = QGroupBox()
             
            # Need a layout which will hold nested layouts 
            core = QVBoxLayout()
            top_layout = QVBoxLayout()
            add_button_holder = QVBoxLayout()
            add_button_holder.addWidget(Select_Button)
            name = QLabel(kebabs_list[i]['name'])
            name.setAlignment(Qt.AlignCenter)
            add_button_holder.setAlignment(Qt.AlignCenter)
            top_layout.addWidget(name)
            core.addLayout(top_layout)
            core.addLayout(add_button_holder)
            
            kebab_group_box.setLayout(core)
            
            # Check for row
            if (i == 2) or (i == 3):
                self.generated_cart_ui.kebabs_layout.addWidget(kebab_group_box, 1, place_holder)
            elif (i == 4) or (i == 5):
                self.generated_cart_ui.kebabs_layout.addWidget(kebab_group_box, 2, place_holder)
            elif (i == 6) or (i == 7):
                self.generated_cart_ui.kebabs_layout.addWidget(kebab_group_box, 3, place_holder)
            elif (i == 8) or (i == 9):
                self.generated_cart_ui.kebabs_layout.addWidget(kebab_group_box, 4, place_holder)
            elif (i == 10) or (i == 11):
                self.generated_cart_ui.kebabs_layout.addWidget(kebab_group_box, 5, place_holder)
            elif (i == 11) or (i == 12):  
                self.generated_cart_ui.kebabs_layout.addWidget(kebab_group_box, 6, place_holder)
            elif (i == 13) or (i == 14):  
                self.generated_cart_ui.kebabs_layout.addWidget(kebab_group_box, 7, place_holder)    
            else:
                self.generated_cart_ui.kebabs_layout.addWidget(kebab_group_box, 0, place_holder)
            # Increment the place holder
            if (place_holder == 1):
                place_holder = 0
            else:
                place_holder = 1
            
            
    def get_sel_buttons(self):
        return self.select_button_group

    """------------------------------------------------------------------------------
    Function        : display_pizzas
    Description     : Receives a list of pizzas which then creates a size combobox
                       for pizza size selection, a QCheckBox which allows custom 
                       topping addition and a QPushButton to add the selected item
                       to the cart.
    Args            : pizza_list (retreived from the model_database_dialog class)
    Returns         : Void
    
    ------------------------------------------------------------------------------"""
    def display_pizzas(self, pizza_list):
        pizza_length             = len(pizza_list)
        self.pizza_size          = [None] * pizza_length
        self.pizza_add_button    = [None] * pizza_length
        self.pizza_extra_check_box  = [None] * pizza_length
        for p in range(pizza_length):
            pizza_name = QLabel(pizza_list[p]['name'])
            pizza_size_string = ['9', '12']
            self.pizza_size[p] = QComboBox()
            self.pizza_size[p].addItems(pizza_size_string)
        
            self.pizza_extra_check_box[p] = QCheckBox("Extra")
            self.pizza_add_button[p] = QPushButton("Add")
            vertical_box_layout = QHBoxLayout()
    
            vertical_box_layout.addWidget(pizza_name)
            vertical_box_layout.addWidget(self.pizza_size[p])
            vertical_box_layout.addWidget(self.pizza_extra_check_box[p])
            vertical_box_layout.addWidget(self.pizza_add_button[p])
            
            pizza_group_box = QGroupBox()

            pizza_group_box.setLayout(vertical_box_layout)
            self.generated_cart_ui.pizzas_layout.addWidget(pizza_group_box)
            
            
    """------------------------------------------------------------------------------
    Function        : display_custom_pizza_toppings
    Description     : Receives a list of toppings from the Controller_Cart class
                      it then iterates through all these toppings appending them
                      to the horizantalLayout. It allows the user to specifically
                      choose custom pizza toppings.
    Args            : toppings_list (retreived from the model_database_dialog class)
    Returns         : Void
    
    ------------------------------------------------------------------------------"""
    def display_custom_pizza_toppings(self, toppings_list):
        topping_length = len(toppings_list)
        # Layout variables to display data
        custom_topping_top_layout = QHBoxLayout()
        custom_topping_bot_layout = QHBoxLayout()
        join_layouts              = QVBoxLayout()
        self.layout_into_group         = QGroupBox()
       
        self.custom_topping_options = [None] * topping_length
        for x in range(0, topping_length):
            if x <= 6:
                self.custom_topping_options[x] = QCheckBox(toppings_list[x]['name'])
                custom_topping_top_layout.addWidget(self.custom_topping_options[x])
            else:
                self.custom_topping_options[x] = QCheckBox(toppings_list[x]['name'])
                custom_topping_bot_layout.addWidget(self.custom_topping_options[x])

        join_layouts.addLayout(custom_topping_top_layout)
        join_layouts.addLayout(custom_topping_bot_layout)
        self.layout_into_group.setLayout(join_layouts)
        self.layout_into_group.hide()
        
        
        
    def display_burgers(self, burgers_list):
        burgers_length = len(burgers_list)
        place_holder = 0 
        # Create combobox variables which will be assigned in the loop
        # needs to be dynamic to capture value changed event for each
        # two arrays with length equal to kebab_list size.
        # we will iterate and assign combobox to each one
        for i in range(burgers_length):
            #self.burger_cheese_option[i]     = QComboBox()
            burger_add_button = QPushButton("Select")
            self.burger_add_button_group.addButton(burger_add_button, i)
            
            # Need a groupbox which will hold a bundle of QLabel, QComboBox and QPushbutton
            burger_group_box = QGroupBox()
             
            # Need a layout which will hold nested layouts 
            core = QVBoxLayout()
            top_layout = QVBoxLayout()
            #bottom_layout = QHBoxLayout()
            add_button_holder = QVBoxLayout()
            add_button_holder.addWidget(burger_add_button)
            name = QLabel(burgers_list[i]['name'])
            name.setAlignment(Qt.AlignCenter)
            add_button_holder.setAlignment(Qt.AlignCenter)
            top_layout.addWidget(name)
            #bottom_layout.addWidget(self.burger_cheese_option[i])
            core.addLayout(top_layout)
            #core.addLayout(bottom_layout)
            core.addLayout(add_button_holder)
            
            burger_group_box.setLayout(core)
            
            # Check for row
            if (i == 2) or (i == 3):
                self.generated_cart_ui.burgers_layout_2.addWidget(burger_group_box, 1, place_holder)
            elif (i == 4) or (i == 5):
                self.generated_cart_ui.burgers_layout_2.addWidget(burger_group_box, 2, place_holder)
            elif (i == 6) or (i == 7):
                self.generated_cart_ui.burgers_layout_2.addWidget(burger_group_box, 3, place_holder)
            elif (i == 8) or (i == 9):
                self.generated_cart_ui.burgers_layout_2.addWidget(burger_group_box, 4, place_holder)
            elif (i == 10) or (i == 11):
                self.generated_cart_ui.burgers_layout_2.addWidget(burger_group_box, 5, place_holder)
            elif (i == 11) or (i == 12):  
                self.generated_cart_ui.burgers_layout_2.addWidget(burger_group_box, 6, place_holder)
            elif (i == 13) or (i == 14):  
                self.generated_cart_ui.burgers_layout_2.addWidget(burger_group_box, 7, place_holder)    
            else:
                self.generated_cart_ui.burgers_layout_2.addWidget(burger_group_box, 0, place_holder)
            # Increment the place holder
            if (place_holder == 1):
                place_holder = 0
            else:
                place_holder = 1
    
    
    def get_burger_add_buttons(self):
        return self.burger_add_button_group
        

    def display_drinks(self, drink_list):
        can = "Can"
        bottle = "Bottle"
        drink_len                = len(drink_list)
        self.size_list           = [None] * drink_len 

        for i in range(drink_len):
            drink_group_box      = QGroupBox()
            h_layout             = QHBoxLayout()
            name                 = QLabel(drink_list[i]['name'])
            add_button           = QPushButton("Add")
            self.size_list[i]    = QComboBox()
            # Only coke, diet coke, pepsi and orange tango is available in bootle size
            if drink_list[i]['name'] == "Coca Cola" or drink_list[i]['name'] == "Orange Tango" or drink_list[i]['name'] == "Pepsi" or drink_list[i]['name'] == "Diet Coke":
                self.size_list[i].addItem(can)
                self.size_list[i].addItem(bottle)
            else:
                self.size_list[i].addItem(can)
            self.drinks_add_button_group.addButton(add_button, i)
            h_layout.addWidget(name)
            h_layout.addWidget(self.size_list[i])
            h_layout.addWidget(add_button)
            drink_group_box.setLayout(h_layout)
            
            self.generated_cart_ui.drinks_layout.addWidget(drink_group_box)
        
        
    def get_drink_button(self):
        return self.drinks_add_button_group
    
    def send_data_to_list_view(self, data):
        self.generated_cart_ui.cart_view.addItem(data)
        