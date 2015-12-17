import View_Cart_Generated
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt , pyqtSlot, pyqtSignal
from PyQt4.Qt import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox,\
    QComboBox, QPushButton, QCheckBox, QObject, QEvent
    
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
        self.generated_cart_ui = View_Cart_Generated.Ui_Dialog()
        
    def setupUI(self, dialog):
        self.generated_cart_ui.setupUi(dialog)
    
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
        # Create combobox variables which will be assigned in the loop
        # needs to be dynamic to capture value changed event for each
        # two arrays with length equal to kebab_list size.
        # we will iterate and assign combobox to each one
        self.salad_options = [None] * kebabs_length
        self.sauce_options = [None] * kebabs_length
        self.add_button_x  = [None] * kebabs_length
        self.size_options  = [None] * kebabs_length

        for i in range(kebabs_length):
            salad_options_str = ['All Salad', 'L/O/R/W', 'No Salad', 'Custom Salad']
            sauce_options_str = ['Chilli Sauce', 'Garlic Mayo', 'Mayo', 'BBQ', 'No Sauce', 'Custom Sauce']
            size_options_str  = ['Small', 'Large']
            self.salad_options[i]    = QComboBox()
            self.sauce_options[i]    = QComboBox()
            self.size_options[i]     = QComboBox()
            self.salad_options[i].addItems(salad_options_str)
            self.sauce_options[i].addItems(sauce_options_str)
            self.size_options[i].addItems(size_options_str)
            self.add_button_x[i] = QPushButton("Add")
            
            # Need a groupbox which will hold a bundle of QLabel, QComboBox and QPushbutton
            kebab_group_box = QGroupBox()
             
            # Need a layout which will hold nested layouts 
            core = QVBoxLayout()
            top_layout = QVBoxLayout()
            bottom_layout = QHBoxLayout()
            add_button_holder = QVBoxLayout()
            add_button_holder.addWidget(self.add_button_x[i])
            name = QLabel(kebabs_list[i]['name'])
            name.setAlignment(Qt.AlignCenter)
            add_button_holder.setAlignment(Qt.AlignCenter)
            top_layout.addWidget(name)
            bottom_layout.addWidget(self.size_options[i])
            bottom_layout.addWidget(self.salad_options[i])
            bottom_layout.addWidget(self.sauce_options[i])
            core.addLayout(top_layout)
            core.addLayout(bottom_layout)
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
            
            
            
    """------------------------------------------------------------------------------
    Function           : display_salads_options
    Description        : This function retrieves a list of custom salad variables from
                         the Controller_Cart_Dialog class. It then creates 
                         dynamic variables to store each check box thus allowing user
                         to select specific salad options. 
                         This function is called directly by the Controller_Cart_Dialog.
    Parameters         : salad_list (A list of salad options available fetched by 
                         databaseConnection class, get_custom_salads method, which is 
                         retrieved by Controller_Cart_Dialog and passed to this function.
    Returns            : Void
    ------------------------------------------------------------------------------"""
    def display_salad_options(self, salad_list):
        tmp_holder = QHBoxLayout()
        tmp_group = QGroupBox()
        salads_length = len(salad_list)
        self.custom_salad_options = [None] * salads_length
        for x in range(0, salads_length):
            self.custom_salad_options[x] = QCheckBox(salad_list[x])
            tmp_holder.addWidget(self.custom_salad_options[x])
        tmp_group.setLayout(tmp_holder)
        self.generated_cart_ui.custom_salads_layout.addWidget(tmp_group)
        
    """------------------------------------------------------------------------------
    Function           : display_sauce_options
    Description        :This function retrieves a list of custom salad variables from
                        the Controller_Cart_Dialog class. It then creates 
                        dynamic variables to store each check box thus allowing user
                        to select specific sauce options. 
                        This function is called directly by the Controller_Cart_Dialog.
    Args                : sauce_list (A list of sauce options available fetched by 
                         databaseConnection class, get_custom_salads method, which is 
                         retrieved by Controller_Cart_Dialog and passed to this function.
    Returns             : Void
    ------------------------------------------------------------------------------"""
    def display_sauce_options(self, sauce_list):
        tmp_holder = QHBoxLayout()
        tmp_group = QGroupBox()
        sauces_length = len(sauce_list)
        self.custom_sauce_options = [None] * sauces_length
        for x in range(0, sauces_length):
            self.custom_sauce_options[x] = QCheckBox(sauce_list[x])
            tmp_holder.addWidget(self.custom_sauce_options[x])
        tmp_group.setLayout(tmp_holder)
        self.generated_cart_ui.custom_sauces_layout.addWidget(tmp_group)
        
        
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
        layout_into_group         = QGroupBox()
       
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
        layout_into_group.setLayout(join_layouts)
        self.generated_cart_ui.horizontalLayout.addWidget(layout_into_group)
