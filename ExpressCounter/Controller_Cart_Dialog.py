"""------------------------------------------------------------------------------
FILE        : Controller_Cart_Dialog 
DATE        : 10-12-2015
AUTHOR      : Murat Sert
DESCRIPTION : This class is instanced upon new order click event by the user.
              It initializes the View_Cart_Custom class which calls the generated 
              class View_Cart_Generated to display the cart dialog UI. 
              The main purpose of this class is to handle user Events.
              The class is instanced directly by the Controller_Main_Menu class upon 
              new order request.
              
------------------------------------------------------------------------------"""
import Model_Database_Dialog   
import Controller_Customer_Dialog   
import Controller_Cart_Toppings   
import Controller_Cart_Addon                                                                  
from Crypto.Util.number import size
from __builtin__ import classmethod

"""------------------------------------------------------------------------------
                     Development Diary
    ------------------------------------------------------------------------------
    Date             Notes
    13/12/2015       New View_Cart_Custom architecture is implemented. NOw calling 
                     this method directly rather than View_Cart_Generated.
    10/12/2015       Class created, issues importing the view class unable to 
                     resolve
              
-------------------------------------------------------------------------------"""

import View_Cart_Custom
from PyQt4.QtCore import Qt , pyqtSlot, pyqtSignal
from PyQt4.Qt import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox,\
    QComboBox, QPushButton, QMessageBox, QMainWindow, QListWidgetItem,\
    QListWidget, pyqtSlot


class Cart_Controller_Class(QDialog):
    new_product_inserted = pyqtSignal()
    shopping_list = []
    def __init__(self):
        super(Cart_Controller_Class, self).__init__()
        
        
        #self.burger_addon_dialog = Controller_Cart_Addon.Controller_Cart_Addon("Burger")
        
        # Holds the total price of the cart
        self.total_price = 0.00
        
        
        self.cart_view_init = View_Cart_Custom.View_Cart_Custom()
        self.cart_view_init.setupUI(self)
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        """ Retrieve a list of products from the model_database """
        kebabs_list  = self.database.get_kebabs()
        pizzas_list  = self.database.get_pizzas()
        burgers_list = self.database.get_burgers()
        others_list  = self.database.get_others()
        self.__drinks_list  = self.database.get_drinks()
        self.others_select_handle()
        #remove the declarations below to clean the code, p.s. update the x_list in order for it to work
        self.__kebabs_list = kebabs_list
        self.__pizzas_list = pizzas_list
        self.__burgers_list = burgers_list
        
        # A list of custom salads and sauces used by burger and kebab options
        salad_list    = self.database.get_custom_salads()
        sauce_list    = self.database.get_custom_sauces()
        
        # used to clear the checkboxes by clear_salad_sauce_checkbox method
        self.__salad_list_private = self.database.get_custom_salads()
        self.__sauce_list_private = self.database.get_custom_salads()
        
        # A custom event installed on the 
        # QListWidget item which will print 
        # the last item in the cart to the 
        # QListWidget. It is emitted once a product is inserted to the cart
        self.new_product_inserted.connect(self.new_item_inserted_event)
        
        # Cart section user event handling
        self.handle_cart_clicks()
        self.handle_clear_cart_button()
        self.handle_cart_confirm_button()
        
        """---------------------------------------------------------------------------------
        |
        |
        |                                   Kebab Section
        |
        |
        ---------------------------------------------------------------------------------"""

        # Since we have a list of kebab, sauce and salad options
        # We can populate the QTabBar with products.
        # But we first need to check if we do have any kebab_list returned
        if (len(self.__kebabs_list) > 0):         
            self.cart_view_init.display_kebabs(self.__kebabs_list)
            
            
            self.handle_add_button()
        else:
            QMessageBox.critical(None, "No Kebabs returned!", "No Kebab products where found, please check your database entries!")   
            
            """---------------------------------------------------------------------------------
            |
            |
            |                                   Pizza Section
            |
            |
            ---------------------------------------------------------------------------------"""
        if (len(pizzas_list) > 0):
            # Variables used to store size and custom topping selections
            self.__pizza_size = [None] * len(pizzas_list)
            self.__custom_topping_list = []
        
            # Get a list of toppings from the database and send it to View_Cart_Custom to be displayed
            toppings_list = self.database.get_pizza_toppings()
            self.cart_view_init.display_pizzas(pizzas_list)
            self.cart_view_init.display_custom_pizza_toppings(toppings_list)
            self.__custom_topping_option     = self.cart_view_init.custom_topping_options
            self.__toppings_list             = self.database.get_pizza_toppings()
            # Extract the global variables from View Cart Custom to be
            # used for user triggered events
            pizza_size_combobox      = self.cart_view_init.pizza_size
            pizza_extra_check_box    = self.cart_view_init.pizza_extra_check_box
            pizza_add_button         = self.cart_view_init.pizza_add_button
            # Get the custom layout box to display options if Extra box is ticked
            self.__pizza_toppings_group_box = self.cart_view_init.layout_into_group
            
            #Initialize pizza sizes in case user doesn't make a selection
            self.initialize_pizza_size(pizzas_list)
            # User event handling
            self.handle_pizza_size_selection(pizza_size_combobox)
            self.handle_pizza_extra_checkbox_selection(pizza_extra_check_box)
            
            self.handle_pizza_add_button(pizza_add_button, pizzas_list)
        else:
            QMessageBox.critical(None, "No Pizzas returned!", "No Pizza products where found, please check your database connection and entries!")    
            """---------------------------------------------------------------------------------
            |
            |
            |                                   Burger Section
            |
            |
            ---------------------------------------------------------------------------------"""
            
        if (len(burgers_list) > 0):
            # Three fixed sized arrays which will hold cheese, salad and sauce selection for each burger
            # They have to be private thus self__ declared making it viewable by this class only
            # These arrays will be initialized preventing any errors if the user doesn't make
            # any salad, cheese or sauce selection.

            self.cart_view_init.display_burgers(burgers_list)
        else:
            QMessageBox.critical(None, "No Burgers returned!", "No Burger products where found, please check your database connection and entries!")    
        
        if (len(self.__drinks_list)> 0):
            self.cart_view_init.display_drinks(self.__drinks_list)
            self.handle_drink_size()
        else:
            QMessageBox.critical(None, "No Drinks returned!", "No Drink products where found, please check your database connection and entries!")    


    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Kebab Section : Add to Cart button related methods
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""
        
    """------------------------------------------------------------------------------
    Function    :   handle_add_button
    Description :   This function handles events when the add button has been clicked.
                    It receives an array of add_button_x of type QPushButton, one 
                    for each corresponding kebab. It also receives a kebabs_list array
                    and depending on the add_button_x clicked event, it connect to
                    the add_to_cart slot supplying the kebab_list[x]['name'], salad[x]
                    sauce[x] as parameters. The kebab_list
                    and add_x are corresponding arrays as add_x is populated with 
                    kebab_list array in View_Cart_Custom class.
    Parameters  :   add_x (An array of Pushbuttons received from View_Cart_Custom and 
                    kebabs_list (received from Model_Database_Dialog.
    Returns     :   Void
    
    ------------------------------------------------------------------------------"""  
        
    def handle_drink_size(self):
        buttons = self.cart_view_init.get_drink_button()
        buttons.buttonClicked[int].connect(self.get_size)
                   
    def get_size(self, number):
        self.add_to_cart_other_drink("Drink", self.__drinks_list[number]['name'], self.cart_view_init.size_list[number].currentText())
        
    def others_select_handle(self):
        gen_view = self.cart_view_init.generated_cart_ui # in order to shorten linking we've typecasted it to gen_view
        gen_view.rc_chips.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.rc_chips.text(), "Standard"))
        gen_view.nuggets6.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.nuggets6.text(), "Standard"))
        gen_view.nuggets12.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.nuggets12.text(), "Standard"))
        gen_view.salad_pitta.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.salad_pitta.text(), "Standard"))
        gen_view.humus.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.humus.text(), "Standard"))
        gen_view.chocolate_cake.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.chocolate_cake.text(), "Standard"))
        gen_view.meat_chips.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.meat_chips.text(), "Standard"))
        gen_view.cmeat_chips.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.cmeat_chips.text(), "Standard"))
        gen_view.wedges.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.wedges.text(), "Standard"))
        gen_view.chips_cheese.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.chips_cheese.text(), "Standard"))
        gen_view.chips_gravy.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.chips_gravy.text(), "Standard"))
        gen_view.chips_curry.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.chips_curry.text(), "Standard"))
        gen_view.s_chips.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.s_chips.text(), "Standard"))
        gen_view.l_chips.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.l_chips.text(), "Standard"))
        gen_view.o_rings.clicked.connect(lambda : self.add_to_cart_other_drink("Other", gen_view.o_rings.text(), "Standard"))

    pyqtSlot(str)
    def add_to_cart_other_drink(self, product_type, name, size):
        if product_type == "Other":
            name = name.replace('&&', '&')
        price = self.database.get_price(name, size)
        self.add_to_cart_method(product_type, name, price, size)

        
    def handle_add_button(self):
        sel_buttons = self.cart_view_init.get_sel_buttons()
        burger_add_buttons = self.cart_view_init.get_burger_add_buttons()
        try:
            sel_buttons.buttonClicked[int].connect(self.load_addon)
            burger_add_buttons.buttonClicked[int].connect(self.burger_addon_load)
        except IndexError:
            QMessageBox.critical(None, "Kebab Index Error", "Error while getting the price of kebab:")   
            
    def load_addon(self, number):
        self.kebab_addon_dialog = Controller_Cart_Addon.Controller_Cart_Addon(self.__kebabs_list[number]['type'], \
                                    self.__kebabs_list[number]['name'], "Small", self.__kebabs_list[number]['price'], self.__kebabs_list[number]['id'])
        self.kebab_addon_dialog.show()
        self.kebab_addon_dialog.kebab_added.connect(self.custom_kebab)
    
    pyqtSlot(str, str, str, str, float, str, str, str)
    def custom_kebab(self, product_type, size, name, kebab_type, price, salad, sauce, p_id):
        self.add_to_cart_method(product_type, size, name, kebab_type, price, salad, sauce, p_id)
    """------------------------------------------------------------------------------
    Function    :   add_to_cart (slot)
    Description :   This slot is executed once the add button of any kebab is clicked.
                    It is currently outputting the selection messages.
    Parameters  :   name(kebab name), salad (salad selection), sauce(sauce selection)
                    It also calls the get_price method from MOdel Database Dialog class
                    supplying the name and size of the item added. The database does a search
                    returning the price of the specified product.
                    kebabs_list (received from Model_Database_Dialog.
    Returns     :   Void
    
    TODO        :   Implement a cart class which shall be executed once items are inserted into the database
    
    ------------------------------------------------------------------------------""" 
        
    def burger_addon_load(self, number):
        self.burger_addon_dialog = Controller_Cart_Addon.Controller_Cart_Addon(self.__burgers_list[number]['type'], \
                        self.__burgers_list[number]['name'], "Small", self.__burgers_list[number]['price'], self.__burgers_list[number]['id'])
        self.burger_addon_dialog.show()
        self.burger_addon_dialog.burger_added.connect(self.custom_burger)
        
    #product_type, name, cheese, price, salad, sauce, p_id
    pyqtSlot(str, str, str, float, str, str, str)
    def custom_burger(self, product_type, name, cheese, price, salad, sauce, p_id):
        self.add_to_cart_method(product_type, name, cheese, price, salad, sauce, p_id)    
    
    """--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    |  Pizza Section User Triggered Event handling Code
    |  
    |  Any event triggered by the user in relation to the Pizza section will be handle in this section of the code
    |
    |  Global variables such as self.pizza_size, self.pizza_add_button, self.pizza_extra_check_box are used in order to detect user triggered events on these objects.
    |  These global variables are declared in the View_Cart_Custom class
    |--------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
    
    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Pizza Section : Pizza Size combobox related methods
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""  
    
    def initialize_pizza_size(self, pizza_list):
        for x in range(0, len(pizza_list)):
            self.__pizza_size[x] = '9'
    
    def handle_pizza_size_selection(self, pizza_size_combobox):
        try:
            pizza_size_combobox[0].activated[str].connect(lambda: self.set_pizza_size_selection(0, pizza_size_combobox[0].currentText()))
            pizza_size_combobox[1].activated[str].connect(lambda: self.set_pizza_size_selection(1, pizza_size_combobox[1].currentText()))
            pizza_size_combobox[2].activated[str].connect(lambda: self.set_pizza_size_selection(2, pizza_size_combobox[2].currentText()))
            pizza_size_combobox[3].activated[str].connect(lambda: self.set_pizza_size_selection(3, pizza_size_combobox[3].currentText()))
            pizza_size_combobox[4].activated[str].connect(lambda: self.set_pizza_size_selection(4, pizza_size_combobox[4].currentText()))
            pizza_size_combobox[5].activated[str].connect(lambda: self.set_pizza_size_selection(5, pizza_size_combobox[5].currentText()))
            pizza_size_combobox[6].activated[str].connect(lambda: self.set_pizza_size_selection(6, pizza_size_combobox[6].currentText()))
            pizza_size_combobox[7].activated[str].connect(lambda: self.set_pizza_size_selection(7, pizza_size_combobox[7].currentText()))
            pizza_size_combobox[8].activated[str].connect(lambda: self.set_pizza_size_selection(8, pizza_size_combobox[8].currentText()))
            pizza_size_combobox[9].activated[str].connect(lambda: self.set_pizza_size_selection(9, pizza_size_combobox[9].currentText()))
           
        except IndexError:
            QMessageBox.critical(None, "Pizza size Index Error", "Error while handling pizza size selection! index out of range")   

    @pyqtSlot(int, int)
    def set_pizza_size_selection(self, pizza_number, size):
        self.__pizza_size[pizza_number] = size
        
    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Pizza Section : 'Extra' Checkbox related methods
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""    
    
    """-----------------------------------------------------------------------------
    Function    : handle_pizza_extra_checkbox_selection
    Description : The pizza section contains a checkbox 'Extra', which allows user to 
                  pick custom pizza toppings. Each pizza options contains this checkbox.
                  extra_checkbox_toggle method is called which checks the state of the 
                  passed checkbox and if it is checked, it shows the groupbox (declared 
                  in View_Cart_Custom which holds the custom toppings list), and then 
                  sets all other extra checkbox to disabled state. If the Checkbox is 
                  unchecked it then hides the groupbox, and then sets other Extra checkbox 
                  to enable state.
                  
    Parameters  : pizza_extra_checkbox (a list of 'Extra' checkboxes declared 
                  in View_Cart_Custom class.
    returns     : Void
    ------------------------------------------------------------------------------"""    
    def handle_pizza_extra_checkbox_selection(self, pizza_extra_checkbox):
        try:
            pizza_extra_checkbox[0].stateChanged.connect(lambda: self.extra_checkbox_toggle(0, pizza_extra_checkbox[0].checkState(), pizza_extra_checkbox))
            pizza_extra_checkbox[1].stateChanged.connect(lambda: self.extra_checkbox_toggle(1, pizza_extra_checkbox[1].checkState(), pizza_extra_checkbox))
            pizza_extra_checkbox[2].stateChanged.connect(lambda: self.extra_checkbox_toggle(2, pizza_extra_checkbox[2].checkState(), pizza_extra_checkbox))
            pizza_extra_checkbox[3].stateChanged.connect(lambda: self.extra_checkbox_toggle(3, pizza_extra_checkbox[3].checkState(), pizza_extra_checkbox))
            pizza_extra_checkbox[4].stateChanged.connect(lambda: self.extra_checkbox_toggle(4, pizza_extra_checkbox[4].checkState(), pizza_extra_checkbox))
            pizza_extra_checkbox[5].stateChanged.connect(lambda: self.extra_checkbox_toggle(5, pizza_extra_checkbox[5].checkState(), pizza_extra_checkbox))
            pizza_extra_checkbox[6].stateChanged.connect(lambda: self.extra_checkbox_toggle(6, pizza_extra_checkbox[6].checkState(), pizza_extra_checkbox))
            pizza_extra_checkbox[7].stateChanged.connect(lambda: self.extra_checkbox_toggle(7, pizza_extra_checkbox[7].checkState(), pizza_extra_checkbox))
            pizza_extra_checkbox[8].stateChanged.connect(lambda: self.extra_checkbox_toggle(8, pizza_extra_checkbox[8].checkState(), pizza_extra_checkbox))
            pizza_extra_checkbox[9].stateChanged.connect(lambda: self.extra_checkbox_toggle(9, pizza_extra_checkbox[9].checkState(), pizza_extra_checkbox))
        except IndexError:
            QMessageBox.critical(None, "Pizza Extra checkbox index error!", "The value of the pizza extra checkbox is out of range!")
        
    
    """-----------------------------------------------------------------------------
    Function    : extra_checkbox_toggle
    Description : This method checks the state of the passed Pizzas Extra checkbox.
                  If it is checked, groupbox is shown, and other Extra checkbox is
                  set to disabled state.
                  If it is unchecked, groupbox is hidden, and the previously 
                  disabled checkbox is re-enabled.
                  
    Parameters  : pizza_number (Number of the pizza i.e. 0 - 9), state (state of passed
                  checkbox) and pizza_extra_checkbox (a list of extra checkboxes for 
                  each pizza)
    returns     : Void
    ------------------------------------------------------------------------------"""
    @pyqtSlot(int)
    def extra_checkbox_toggle(self, pizza_number, state, pizza_extra_checkbox):
        
        toppings_list = self.database.get_pizza_toppings()
        pizzas_list   = self.database.get_pizzas()
        self.controller_cart_toppings = Controller_Cart_Toppings.Controller_Cart_Toppings(pizza_extra_checkbox, toppings_list, self.__pizza_size[pizza_number], \
                                                                        pizzas_list[pizza_number]['name'], pizzas_list[pizza_number]['id'])
        if state == Qt.Checked:
            self.disable_other_extra_checkboxes(pizza_number, pizza_extra_checkbox)
            self.controller_cart_toppings.show()
            self.controller_cart_toppings.custom_pizza_inserted.connect(self.custom_pizza)
            self.controller_cart_toppings.no_custom_toppings.connect(self.default_pizza)
        elif state == Qt.Unchecked:
            self.enable_all_extra_checkboxes(pizza_extra_checkbox)
        else:
            QMessageBox.critical(None, "Invalid checkbox state!", "The extra checkbox is in an unkown state")


    pyqtSlot(str, str, str, float, str, str)
    def custom_pizza(self, product_type, size, name, price, toppings, pizza_id):
        self.add_to_cart_method(product_type, size, name, str(price), str(toppings), pizza_id)


    pyqtSlot(str, str, str, unicode, str)
    def default_pizza(self, product_type, size, name, price, pizza_id):
        self.add_to_cart_method(product_type, size, name, str(price), pizza_id)
        
    """ 
    Once an Extra checkbox is selected for a pizza, then all other checkboxes 
    for the other pizzas must be disabled.
    """
    @pyqtSlot(int)
    def disable_other_extra_checkboxes(self, pizza_number, pizza_extra_checkbox):
        for x in range(0, len(pizza_extra_checkbox)):
            if x != pizza_number:
                pizza_extra_checkbox[x].setEnabled(False)
                
    """
    If the extra check box is unchecked, then we need to re-enable rest of the 
    checkboxes to enabled state.
    """
    @pyqtSlot(int)
    def enable_all_extra_checkboxes(self, pizza_extra_checkbox):
        for x in range(0, len(pizza_extra_checkbox)):
            pizza_extra_checkbox[x].setEnabled(True)
        
        # As the user made the selection and therefore disabled the Extra checkbox
        # we will need to clear the toppings list 
        #self.clear_selected_checkboxes()
        
        
        
        
    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Pizza Section : Custom Topping related methods
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""
        
    
    
    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Pizza Section : Add to Cart related methods
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""
    
    def handle_pizza_add_button(self, pizza_add_button, pizzas_list):
        try:
            pizza_add_button[0].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[0], pizzas_list[0]['name'], pizzas_list[0]['id']))
            pizza_add_button[1].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[1], pizzas_list[1]['name'], pizzas_list[1]['id']))
            pizza_add_button[2].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[2], pizzas_list[2]['name'], pizzas_list[2]['id']))
            pizza_add_button[3].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[3], pizzas_list[3]['name'], pizzas_list[3]['id']))
            pizza_add_button[4].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[4], pizzas_list[4]['name'], pizzas_list[4]['id']))
            pizza_add_button[5].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[5], pizzas_list[5]['name'], pizzas_list[5]['id']))
            pizza_add_button[6].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[6], pizzas_list[6]['name'], pizzas_list[6]['id']))
            pizza_add_button[7].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[7], pizzas_list[7]['name'], pizzas_list[7]['id']))
            pizza_add_button[8].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[8], pizzas_list[8]['name'], pizzas_list[8]['id']))
            pizza_add_button[9].clicked.connect(lambda : self.add_to_cart_pizza(self.__pizza_size[9], pizzas_list[9]['name'], pizzas_list[9]['id']))
        except IndexError:
            QMessageBox.critical(None, "Kebab Index Error", "Error while getting the price of kebab:")   


        
    """------------------------------------------------------------------------------
    Function    :   add_to_cart (slot)
    Description :   This slot is executed once the add button of any kebab is clicked.
                    It is currently outputting the selection messages.
    Parameters  :   name(kebab name), salad (salad selection), sauce(sauce selection)
                    It also calls the get_price method from MOdel Database Dialog class
                    supplying the name and size of the item added. The database does a search
                    returning the price of the specified product.
                    kebabs_list (received from Model_Database_Dialog.
    Returns     :   Void
    
    TODO        :   Implement a cart class which shall be executed once items are inserted into the database
    
    ------------------------------------------------------------------------------""" 
    @pyqtSlot(str, str)
    def add_to_cart_pizza(self, size, name, id):
        price = self.database.get_price(name, size)
        self.add_to_cart_method("Pizza", size, name, price, id)
        
        
        
    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Burgers Section Start
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""
    
    
    def add_to_cart_method(self, *args):
        if (args[0] == "Kebab"):
            self.kebab_added(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
        elif (args[0] == "Pizza"):
            # Check if custom toppings requested 
            # remember size doesnt start from 0
            if (len(args) > 5):
                self.pizza_added(args[0], args[1], args[2], args[3], args[4], args[5])
            else:
                self.pizza_added(args[0], args[1], args[2], args[3], args[4])
        elif (args[0] == "Burger"):
            self.burger_added(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
        elif (args[0] == "Other") or (args[0] == "Drink"):
            self.drink_other_added(args[0], args[1], args[2], args[3])
        else:
            QMessageBox.critical(None, "Unkown product Type passed!", "Unkown type has been passed!")
         
        # A new product has been added to the cart
        # emit the signal which will update the cart_view in generated
        # view here
        self.new_product_inserted.emit()

        # At this stage we need to clear the seleced custom sauce and salad 
        #self.clear_salad_sauce_checkboxes(self.__sauce_list_from_custom, self.__salad_list_from_custom, self.__salad_list_private, self.__sauce_list_private)
        #self.clear_burger_salad_sauce_checkboxes(self.cart_view_init.custom_burger_sauce_options, 
         #                                        self.cart_view_init.custom_burger_salad_options, self.__salad_list_private, self.__sauce_list_private)
            
   
    @pyqtSlot()
    def new_item_inserted_event(self):
        pound = u'\xa3'
        self.send_data_to_list_view()
        self.total_price_display = self.cart_view_init.get_total_price()
        self.total_price_display.setText(pound + str(float(self.total_price)) + "0")

    def send_data_to_list_view(self):
        if len(self.shopping_list) > 0:
            data = self.get_value_of_item(self.shopping_list[-1])
            list_view_item = QListWidgetItem(data)
            self.cart_view_init.send_data_to_list_view(list_view_item)
        
        
    def get_value_of_item(self, item):
        if item.type == "Kebab":
            return (str(item.size) + " " + item.name + " \n" + " -" + item.kebab_type + "\n" + " -" + item.salad + "\n -" + item.sauce)
        elif item.type == "Burger":
            return (item.name + " with " + item.cheese +  "\n" + " -" + item.salad + "\n -" + item.sauce)
        elif item.type == "Pizza":
            try:
                return (str(item.size) + " " + item.name + "\n - Extra: " + item.toppings)
            except AttributeError:
                    pass
                    return (str(item.size) + " " + item.name)
        elif item.type == "Other":
            return item.name
        elif item.type == "Drink":
            return item.size + " of " + item.name
        else:
            QMessageBox.critical(None, "Unkown product Type passed!", "Unkown type has been passed!")
            
        
    def pizza_added(self, product_type, size, name, price, *args):
        product = Product()
        product.type = product_type
        product.size = size
        product.name = name
        product.price = price
        if len(args) > 1:
            product.toppings = args[0]
            product.id       = args[1]
        else:
            product.id       = args[0]        
        self.shopping_list.append(product)
       
        self.total_price = self.total_price + float(price)
        
    def kebab_added(self, product_type, size, name, kebab_type, price, salad, sauce, p_id):
        product = Product()
        product.type = product_type
        product.size  = size
        product.name  = name
        product.kebab_type = kebab_type
        product.price = price
        product.salad = salad
        product.sauce = sauce
        product.id    = p_id
        self.shopping_list.append(product)
        self.total_price = float(self.total_price) + float(price)
        
        
    def burger_added(self,  product_type, name, cheese, price, salad, sauce, p_id):
        product = Product()
        product.type = product_type
        product.name   = name
        product.cheese = cheese
        product.price  = price
        product.salad  = salad
        product.sauce  = sauce
        product.id     = p_id
        self.shopping_list.append(product)
        self.total_price = float(self.total_price) + float(price)
        
        
    def other_added(self, product_type, name, price, p_id):
        product = Product()
        product.type = product_type
        product.name  = name
        product.price = price
        product.id    = p_id
        self.shopping_list.append(product)
        self.total_price = self.total_price + float(price)
            
    def drink_other_added(self, product_type, name, price, size):
        product = Product()
        product.type = product_type
        product.name = name
        product.size = size
        product.price = price
        self.shopping_list.append(product)
        self.total_price = float(self.total_price) + float(price)
        
    def handle_cart_clicks(self):
        self.cart_view_init.generated_cart_ui.cart_view.itemClicked.connect(lambda : self.remove_item_from_cart(self.cart_view_init.generated_cart_ui.cart_view.currentRow()))
        
        
        
    pyqtSlot(int)
    def remove_item_from_cart(self, row):
        # Initialize pound sign and get the total price display edit 
        # from the view
        pound = u'\xa3'
        self.total_price_display = self.cart_view_init.get_total_price()
        # Remove the selected item from the cart
        self.cart_view_init.generated_cart_ui.cart_view.takeItem(row)
        # We need to deduct the price before removing it from our list
        # If there are no items in list, the price is always set to 0.00
        # Else deduct the price of the removed item 
        if (len(self.shopping_list) > 0):
            self.total_price = self.total_price - float(self.shopping_list[row].price)
            self.total_price_display.setText(pound + str(float(self.total_price)) + "0")
        else:
            self.total_price = 0.00
            self.total_price_display.setText(pound + str(float(self.total_price)) + "0")
        # remove it from the shopping list which holds all the items
        self.shopping_list.pop(row)
        
        
    """
    Function    : handle_clear_cart_button
    Description : Upon user cart clear request, clear the cart content
    """    
    def handle_clear_cart_button(self):
        self.cart_view_init.generated_cart_ui.pushButton.clicked.connect(self.clear_cart)
        
    @pyqtSlot()
    def clear_cart(self):
        self.cart_view_init.generated_cart_ui.cart_view.clear()
        
        # if the cart is empty and user clicks cancel we presume to cancel the whole order and close dialog
        if (len(self.shopping_list) < 1):
            self.close()
        # clear all the products in the array
        # but check that the list isn't empty else it will cause an index error
        if (len(self.shopping_list) > 0):
            self.total_price = 0.00
            pound = u'\xa3'
            self.total_price_display = self.cart_view_init.get_total_price()
            self.total_price_display.setText(pound + str(float(self.total_price)) + "0")
            del self.shopping_list[:]
        self.total_price = 0.00
        
        
        
    def handle_cart_confirm_button(self):
        self.cart_view_init.generated_cart_ui.pushButton_2.clicked.connect(self.cart_confirmed)
        
    pyqtSlot()
    def cart_confirmed(self):
        # check if cart is not empty
        if len (self.shopping_list) > 0:
            self.customer_dialog = Controller_Customer_Dialog.Controller_Customer_Dialog(self, self.shopping_list, self.total_price)
            self.customer_dialog.exec_()
        else:
            QMessageBox.critical(None, "Cart is empty!", "Cart data is confirmed however cart list is empty! Please add products to continue!")
    
# Python strcut equavilant
# will hold product details
class Product(object):
    pass
