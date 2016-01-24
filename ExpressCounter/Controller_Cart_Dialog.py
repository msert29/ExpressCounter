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
    QListWidget


class Cart_Controller_Class(QDialog):
    new_product_inserted = pyqtSignal()
    shopping_list = []
    def __init__(self):
        super(Cart_Controller_Class, self).__init__()
        
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
        
        

        # Need to store all custom selected salads and sauces into an array
        self.__custom_salad_array = []
        self.__custom_sauce_array = []
        
        self.__cat_salad_list_to_string = ""
        self.__cat_sauce_list_to_string = ""
        """ 
            For each kebab option, a salad and sauce selection from a 
            combobox is available. If the user doesn't select a custom
            salad/sauce option, we store the selected Item in the combobox.
            We initiliaze these three fixed sized arrays in case the user doesn't 
            make a change in selection 
        """
        self.__kebab_type = [None] * len(kebabs_list)
        self.__salad      = [None] * len(kebabs_list)
        self.__sauce      = [None] * len(kebabs_list)
        self.__kebab_size =  [None] * len(kebabs_list)
        
        
        # Since we have a list of kebab, sauce and salad options
        # We can populate the QTabBar with products.
        # But we first need to check if we do have any kebab_list returned
        if (len(kebabs_list) > 0):         
            self.cart_view_init.display_kebabs(kebabs_list)
            self.cart_view_init.display_salad_options(salad_list)
            self.cart_view_init.display_sauce_options(sauce_list)
            """ 
                Make sure we initiliaze each array with first default value
                i.e. All Salad and Chilli sauce selection must be selected 
                because they are displayed and until the user changes combobox index
                the value will not be updated i.e. it will be null, therefore keep 
                the default value of all salad and chilli sauce as user might not 
                make a selection 
            """
            self.initiliaze_salad_sauce_size_array(self.__salad, self.__sauce, kebabs_list)
            
            """ 
            salad_options and sauce_options are global variables from the View_Cart_Custom Class
            They are a list of Comboboxes holding values of salad and sauce selection
            They are neccesary for the handle_salad/sauce_selection functions
            therefore they are retreived and passed to these functions
            
            Salad_option_from_custom is a combobox selection whereas salad_list_from_custom is
            a list of all salad options displayed as checkboxes. Respectively for the sauce option.
            
            """
            """ FIX ME
            these global variables in the custom view can be converted into local variable in the 
            __init__ function and then be returned via get_x_options. This is for imporvemented purposes"""
            self.__type_options_from_custom         = self.cart_view_init.wrap_pitta
            self.__salad_options_from_custom        = self.cart_view_init.salad_options
            self.__sauce_options_from_custom        = self.cart_view_init.sauce_options
            self.__size_options_from_custom         = self.cart_view_init.size_options
            
            self.__add_x_button_from_custom         = self.cart_view_init.add_button_x
            self.__salad_list_from_custom           = self.cart_view_init.custom_salad_options
            self.__sauce_list_from_custom           = self.cart_view_init.custom_sauce_options
            self.handle_kebab_type_selection(self.__type_options_from_custom)
            self.handle_sauce_selection(self.__sauce_options_from_custom)
            self.handle_salad_selection(self.__salad_options_from_custom)
            self.handle_size_selection(self.__size_options_from_custom)
            self.handle_custom_salad_selection(self.__salad_list_from_custom, salad_list)
            self.handle_custom_sauce_selection(self.__sauce_list_from_custom, sauce_list)
            self.handle_add_button(self.__add_x_button_from_custom, kebabs_list)
            
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
            # A string which will hold custom toppings in one string
            self.__cat_toppings = ""
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
            self.handle_custom_topping_selection(toppings_list)
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
            self.__burger_salad_list  = [None] * len(burgers_list)
            self.__burger_sauce_list  = [None] * len(burgers_list)
            self.__burger_cheese_list = [None] * len(burgers_list)
            
            # And two dynamic arrays for custom salad and sauce list
            self.__burger_custom_salad_list = []
            self.__burger_custom_sauce_list = []
            
            self.__cat_burger_custom_salad = ""
            self.__cat_burger_custom_sauce = ""
            
            self.cart_view_init.display_burgers(burgers_list)
            self.initialize_burger_options(burgers_list)
            self.cart_view_init.display_burger_salad_options(salad_list)
            self.cart_view_init.display_burger_sauce_options(sauce_list)
            # Burgers are initiliazed, now get Combobox and buttons for each burger option
            burger_salad_option   = self.cart_view_init.burger_salad_options
            burger_sauce_option   = self.cart_view_init.burger_sauce_options
            burger_cheese_option  = self.cart_view_init.burger_cheese_option
            
            
            
            self.handle_burger_salad_selection(burger_salad_option)
            self.handle_burger_sauce_selection(burger_sauce_option)
            self.handle_burger_cheese_selection(burger_cheese_option)
            
            self.handle_burger_custom_sauce_selection(self.cart_view_init.custom_burger_sauce_options, sauce_list)
            self.handle_burger_custom_salad_selection(self.cart_view_init.custom_burger_salad_options, salad_list)
            
            self.handle_burger_add_button(self.cart_view_init.burger_add_button, burgers_list)
        else:
            QMessageBox.critical(None, "No Burgers returned!", "No Burger products where found, please check your database connection and entries!")    
        
        
        
        
        
        
    """--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    |  Kebab Section User Triggered Event handling Code
    |  
    |  Any event triggered by the user in relation to the Kebab section will be handle in this section of the code
    |
    |  Global variables such as self.salad_options, self.sauce_options, self.add_button_x and self.size_options are used (which is declared in View_Cart_Custom
    |  in order to detect user triggered events on these objects.
    |
    |--------------------------------------------------------------------------------------------------------------------------------------------------------------------"""   

    
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
        
    def handle_add_button(self, add_x, kebabs_list):
        try:
            add_x[0].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[0], kebabs_list[0]['name'], self.__kebab_type[0], self.__salad[0], self.__sauce[0], kebabs_list[0]['id']))
            add_x[1].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[1], kebabs_list[1]['name'], self.__kebab_type[1], self.__salad[1], self.__sauce[1], kebabs_list[1]['id']))
            add_x[2].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[2], kebabs_list[2]['name'], self.__kebab_type[2], self.__salad[2], self.__sauce[2], kebabs_list[2]['id']))
            add_x[3].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[3], kebabs_list[3]['name'], self.__kebab_type[3], self.__salad[3], self.__sauce[3], kebabs_list[3]['id']))
            add_x[4].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[4], kebabs_list[4]['name'], self.__kebab_type[4], self.__salad[4], self.__sauce[4], kebabs_list[4]['id']))
            add_x[5].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[5], kebabs_list[5]['name'], self.__kebab_type[5], self.__salad[5], self.__sauce[5], kebabs_list[5]['id']))
            add_x[6].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[6], kebabs_list[6]['name'], self.__kebab_type[6], self.__salad[6], self.__sauce[6], kebabs_list[6]['id']))
            add_x[7].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[7], kebabs_list[7]['name'], self.__kebab_type[7], self.__salad[7], self.__sauce[7], kebabs_list[7]['id']))
            add_x[8].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[8], kebabs_list[8]['name'], self.__kebab_type[8], self.__salad[8], self.__sauce[8], kebabs_list[8]['id']))
            add_x[9].clicked.connect(lambda : self.add_to_cart_kebab(self.__kebab_size[9], kebabs_list[9]['name'], self.__kebab_type[9], self.__salad[9], self.__sauce[9], kebabs_list[9]['id']))
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
    @pyqtSlot(str, str, str, str)
    def add_to_cart_kebab(self, size, name, kebab_type, salad, sauce, id):
        price = self.database.get_price(name, size)
       
        
        if (len(self.__custom_salad_array) > 0):
            self.__cat_salad_list_to_string = " ".join(self.__custom_salad_array)
        if (len(self.__custom_sauce_array) > 0):
            self.__cat_sauce_list_to_string = " ".join(self.__custom_sauce_array)
            
            
    
        
        # both custom salad and sauce requested therefore pass them as sald and sauce
        if ((salad == "Custom Salad") and (sauce == "Custom Sauce")):
            if (len(self.__custom_salad_array) > 0):  
                if (len(self.__custom_sauce_array) > 0):
                    self.add_to_cart_method("Kebab", size, name, kebab_type, price, self.__cat_salad_list_to_string, self.__cat_sauce_list_to_string, id)
                else:
                    QMessageBox.critical(None, "Custom salad and sauce selected but sauce empty list", "Custom Salad and sauce option has been selected but no sauce option is selected!")
            else:
                QMessageBox.critical(None, "Custom salad and sauce selected but salad is empty list", "Custom Salad and sauce option has been selected but no salad  is selected!")
        #only sauce is requested therefore pass custom sauce and keep salad as combobox value
        elif ((salad != "Custom Salad") and (sauce == "Custom Sauce")):
            if (len(self.__custom_sauce_array) > 0):
                self.add_to_cart_method("Kebab", size, name, kebab_type, price, salad, self.__cat_sauce_list_to_string, id)
            else:
                QMessageBox.critical(None, "Custom sauce is selected but not specified!", "Custom sauce option is selected but no custom sauce selection has been specified!")
        # only salad is requested therefore pass sauce as combobox value
        elif ((salad == "Custom Salad") and (sauce != "Custom Sauce")):
            if (len(self.__custom_salad_array) > 0):
                self.add_to_cart_method("Kebab", size, name, kebab_type, price, self.__cat_salad_list_to_string, sauce, id)
            else:
                QMessageBox.critical(None, "Custom salad is selected but not specified!", "Custom salad option is selected but no custom salad selection has been specified!")
        # both not requested therefore pass combobx values for each
        elif ((salad != "Custom Salad") and (sauce != "Custom Sauce")):
            self.add_to_cart_method("Kebab", size, name, kebab_type, price, salad, sauce, id)
        else:
            QMessageBox.critical(None, "Invalid custom salad/sauce condition", "Whislt supplying parameters to shopping list, else branch executed!")
                    
    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Kebab Section : Common salad, sauce and size selection related method. All belong to QComboBox group.
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""
    
    """------------------------------------------------------------------------------
    Function    : initialiaze_salad_sauce_size_array
    Description : This function recieves three fixed sized arrays whom hold salad
                  sauce and size selection for each kebab. It initiliazes each 
                  selection with a default value of "all Salad", "chilli sauce" and 
                  "small" values. The reason for this is because the value of each salad
                  sauce and size will only get update if the user will make a change in
                  combobox. Therefore we will need to initilize the default values
                  in case user will not make any changes to the combobox.
                         
    Parameters  : self.__salads, self.__sauce (fixed sized arrays holding salad
                  sauce selection for each kebab
                         
    Returns     : Void
    ------------------------------------------------------------------------------"""
    def initiliaze_salad_sauce_size_array(self, salads, sauces, kebabs_list):
        for m in range(0, len(kebabs_list)):
            self.__kebab_type[m] = "Pitta"
        for x in range(0, len(salads)):
            salads[x] = "All Salad"
        for y in range (0, len(sauces)):
            sauces[y] = "Chilli Sauce"
        for z in range(0, len(kebabs_list)):
            self.__kebab_size[z] = "Small"



    def handle_kebab_type_selection(self, type_x):
        try:
            type_x[0].activated[str].connect(lambda : self.set_kebab_type(0, type_x[0].currentText()))
            type_x[1].activated[str].connect(lambda : self.set_kebab_type(1, type_x[1].currentText()))
            type_x[2].activated[str].connect(lambda : self.set_kebab_type(2, type_x[2].currentText()))
            type_x[3].activated[str].connect(lambda : self.set_kebab_type(3, type_x[3].currentText()))
            type_x[4].activated[str].connect(lambda : self.set_kebab_type(4, type_x[4].currentText()))
            type_x[5].activated[str].connect(lambda : self.set_kebab_type(5, type_x[5].currentText()))
            type_x[6].activated[str].connect(lambda : self.set_kebab_type(6, type_x[6].currentText()))
            type_x[7].activated[str].connect(lambda : self.set_kebab_type(7, type_x[7].currentText()))
            type_x[8].activated[str].connect(lambda : self.set_kebab_type(8, type_x[8].currentText()))
            type_x[9].activated[str].connect(lambda : self.set_kebab_type(9, type_x[9].currentText()))    
        except IndexError:
            QMessageBox.critical(None, "Kebab Type Index Error!", "Please check code as we \
            only assign type for ten different kebabs!")                                              
    """------------------------------------------------------------------------------
    Function    : handle_salad_selection
    Description : If the user makes changes to the salad options i.e. selecting 
                  a different salad option, we will need to store this new value
                  of the combobox. therefore this function handles these events
                  where user makes a selection change. 
                  The 0-7 number is the kebab number which is dynamically assigned
                  in the View_Cart_Custom class, which populates the Kebabs tab bar
                  with the data received from the Model_Database_Dialog class and iterates
                  through each data received. The salad_x[0].currentText() gives the current
                  text value selected by the user in the corresponding combobox
                        
    Parameters  : salad_x (a global ComboBox array, which is assigned to each kebab
                  each kebab will its own salad combobox. We need this ComboBox array
                  to determine which Salad ComboBox option is changed and update the 
                  salad option for the corresponding kebab.  
                         
    Returns     : it calls the set_salad method passing the kebab number 0-7 which then
                  sets the corresponding number in self.__salad array declared above.
    ------------------------------------------------------------------------------"""
    def handle_salad_selection(self, salad_x):
        try:
            salad_x[0].activated[str].connect(lambda : self.set_salad(0, salad_x[0].currentText()))
            salad_x[1].activated[str].connect(lambda : self.set_salad(1, salad_x[1].currentText()))
            salad_x[2].activated[str].connect(lambda : self.set_salad(2, salad_x[2].currentText()))
            salad_x[3].activated[str].connect(lambda : self.set_salad(3, salad_x[3].currentText()))
            salad_x[4].activated[str].connect(lambda : self.set_salad(4, salad_x[4].currentText()))
            salad_x[5].activated[str].connect(lambda : self.set_salad(5, salad_x[5].currentText()))
            salad_x[6].activated[str].connect(lambda : self.set_salad(6, salad_x[6].currentText()))
            salad_x[7].activated[str].connect(lambda : self.set_salad(7, salad_x[7].currentText()))
            salad_x[8].activated[str].connect(lambda : self.set_salad(8, salad_x[8].currentText()))
            salad_x[9].activated[str].connect(lambda : self.set_salad(9, salad_x[9].currentText()))
        except IndexError:
            QMessageBox.critical(None, "Salad Index Error", "Error while assigning salad selection!")   
    """------------------------------------------------------------------------------
    Function    : handle_sauce_selection
    Description : If the user makes changes to the sauce options i.e. selecting 
                  a different sauce option, we will need to store this new value
                  of the combobox. therefore this function handles these events
                  where user makes a selection change. 
                  The 0-7 number is the kebab number which is dynamically assigned
                  in the View_Cart_Custom class, which populates the Kebabs tab bar
                  with the data received from the Model_Database_Dialog class and iterates
                  through each data received. The sauce_x[0].currentText() gives the current
                  text value selected by the user in the corresponding combobox
                         
    Parameters  : sauce_x (a global ComboBox array, which is assigned to each kebab
                  each kebab will its own sauce combobox. We need this ComboBox array
                  to determine which Salad ComboBox option is changed and update the 
                  salad option for the corresponding kebab.  
                         
    Returns     : it calls the set_sauce method passing the kebab number 0-7 which then
                  sets the corresponding number in self.__sauce array declared above.
    ------------------------------------------------------------------------------"""
    def handle_sauce_selection(self, sauce_x):
        try:
            sauce_x[0].activated[str].connect(lambda : self.set_sauce(0, sauce_x[0].currentText()))
            sauce_x[1].activated[str].connect(lambda : self.set_sauce(1, sauce_x[1].currentText()))
            sauce_x[2].activated[str].connect(lambda : self.set_sauce(2, sauce_x[2].currentText()))
            sauce_x[3].activated[str].connect(lambda : self.set_sauce(3, sauce_x[3].currentText()))
            sauce_x[4].activated[str].connect(lambda : self.set_sauce(4, sauce_x[4].currentText()))
            sauce_x[5].activated[str].connect(lambda : self.set_sauce(5, sauce_x[5].currentText()))
            sauce_x[6].activated[str].connect(lambda : self.set_sauce(6, sauce_x[6].currentText()))
            sauce_x[7].activated[str].connect(lambda : self.set_sauce(7, sauce_x[7].currentText()))
            sauce_x[8].activated[str].connect(lambda : self.set_sauce(8, sauce_x[8].currentText()))
            sauce_x[9].activated[str].connect(lambda : self.set_sauce(9, sauce_x[9].currentText()))
        except IndexError:
            QMessageBox.critical(None, "Sauce Index Error", "Error while assigning sauce selection!")   


    def handle_size_selection(self, size_x):
        try:
            size_x[0].activated[str].connect(lambda : self.set_size(0, size_x[0].currentText()))
            size_x[1].activated[str].connect(lambda : self.set_size(1, size_x[1].currentText()))
            size_x[2].activated[str].connect(lambda : self.set_size(2, size_x[2].currentText()))
            size_x[3].activated[str].connect(lambda : self.set_size(3, size_x[3].currentText()))
            size_x[4].activated[str].connect(lambda : self.set_size(4, size_x[4].currentText()))
            size_x[5].activated[str].connect(lambda : self.set_size(5, size_x[5].currentText()))
            size_x[6].activated[str].connect(lambda : self.set_size(6, size_x[6].currentText()))
            size_x[7].activated[str].connect(lambda : self.set_size(7, size_x[7].currentText()))
            size_x[8].activated[str].connect(lambda : self.set_size(8, size_x[8].currentText()))
            size_x[9].activated[str].connect(lambda : self.set_size(9, size_x[9].currentText()))
        except IndexError:
            QMessageBox.critical(None, "Size Index Error", "Error while assigning Size selection!")  

        
    @pyqtSlot(int, str)
    def set_size(self, number, value): 
        self.__kebab_size[number] = value 
        
    
    @pyqtSlot(int, str)
    def set_kebab_type(self, number, type_selection):
        self.__kebab_type[number] = type_selection
        
    """------------------------------------------------------------------------------
    Function    : set_salad (slot)
    Description : If a new salad option is selected by the user in the View_Cart_Custom
                  class via ComboBox, the handle_salad_selection connects the corresponding
                  salad var selection to this slot. The private variable self.__salad declared
                  above is assigned witht the corresponding kebab number. So self.__salad 
                  and salad_x variable which is received from the View_Cart_Custom is of same size.
                  Therefore the corresponding kebab salad selection is stored in the local array here.
    Parameters  : number (NUmber of the corresponding kebab) salad(Salad option selected)
    returns     : void
    ------------------------------------------------------------------------------"""
    @pyqtSlot(int, str)
    def set_salad(self, number, salad):
        # Each kebab has a number which will be assigned if a selection is made
        self.__salad[number] = salad


        

    """------------------------------------------------------------------------------
    Function    : set_sauce(slot)
    Description : If a new sauce option is selected by the user in the View_Cart_Custom
                  class via ComboBox, the handle_salad_selection connects the corresponding
                  sauce var selection to this slot. The private variable self.__salad declared
                  above is assigned witht the corresponding kebab number. So self.__salad 
                  and salad_x variable which is received from the View_Cart_Custom is of same size.
                  Therefore the corresponding kebab sauce selection is stored in the local array here.
    Parameters  : number (Number of the corresponding kebab) sauce(sauce option selected)
    returns     : void
    ------------------------------------------------------------------------------"""
    @pyqtSlot(int, str)
    def set_sauce(self, number, sauce):
        self.__sauce[number] = sauce
        
    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Kebab Section : Custom salad and sauce selectio relation methods
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""    
    
        
    """------------------------------------------------------------------------------
    Function    : handle_custom_salad_selection
    Description : The custom salads options listed as checkboxes in the kebab and burger 
                  section are connected to slots in this function. Any check/uncheck event
                  triggers a connection to the custom_salad_add function which appends or
                  removes the given checkbox from the self.__custom_salad_array dynamic array.
                  
    Parameters  : salad_var (The dynamically asigned salad checkboxes which are populated in
                  View_Cart_Custom class. 
                  salad_list (A list of available salad options fetched from the 
                  Model_Database_Dialog class. Which is also used to pass the checkbox text 
                  dynamically without specifying it for each.
    returns     : triggers custom_salad_added slot.
    ------------------------------------------------------------------------------"""
    def handle_custom_salad_selection(self, salad_var, salad_list):
        try:
            salad_var[0].stateChanged.connect(lambda : self.custom_salad_added(salad_list[0], salad_var[0].checkState()))
            salad_var[1].stateChanged.connect(lambda : self.custom_salad_added(salad_list[1], salad_var[1].checkState()))
            salad_var[2].stateChanged.connect(lambda : self.custom_salad_added(salad_list[2], salad_var[2].checkState()))
            salad_var[3].stateChanged.connect(lambda : self.custom_salad_added(salad_list[3], salad_var[3].checkState()))
            salad_var[4].stateChanged.connect(lambda : self.custom_salad_added(salad_list[4], salad_var[4].checkState()))
            salad_var[5].stateChanged.connect(lambda : self.custom_salad_added(salad_list[5], salad_var[5].checkState()))
            salad_var[6].stateChanged.connect(lambda : self.custom_salad_added(salad_list[6], salad_var[6].checkState()))
        except IndexError:
            QMessageBox.critical(None, "Salad Index Error", "Handling custom salad selection index error! Max value of index is:" + str(len(salad_list)))   


    @pyqtSlot(str, int)
    def custom_salad_added(self, salad_option, state):
        if (state == Qt.Checked):
            #print (salad_option + " is added!")
            self.__custom_salad_array.append(salad_option)
        elif (state == Qt.Unchecked):
            # Remove the option selected but we will need the row number
            #print (salad_option + " is removed!")
            row_no = self.__custom_salad_array.index(salad_option)
            self.__custom_salad_array.pop(row_no)
            self.__cat_salad_list_to_string = ""

        else:
            print (salad_option + " is in an unknown state!")
            
            
    """------------------------------------------------------------------------------
    Function    : handle_custom_sauce_selection
    Description : The custom sauce options listed are as checkboxes in the kebab and burger 
                  section are connected to slots in this function. Any check/uncheck event
                  triggers a connection to the custom_sauce_add function which appends or
                  removes the given checkbox from the self.__custom_sauce_array dynamic array.
                  
    Parameters  : sauce_var (The dynamically asigned salad checkboxes which are populated in
                  View_Cart_Custom class. 
                  sauce_list (A list of available sauce options fetched from the 
                  Model_Database_Dialog class. Which is also used to pass the checkbox text 
                  dynamically without specifying it for each.
    returns     : triggers custom_sauce_added slot.
    ------------------------------------------------------------------------------"""
    
    def handle_custom_sauce_selection(self, sauce_var, sauce_list):
        try:
            sauce_var[0].stateChanged.connect(lambda : self.custom_sauce_added(sauce_list[0], sauce_var[0].checkState()))
            sauce_var[1].stateChanged.connect(lambda : self.custom_sauce_added(sauce_list[1], sauce_var[1].checkState()))
            sauce_var[2].stateChanged.connect(lambda : self.custom_sauce_added(sauce_list[2], sauce_var[2].checkState()))
            sauce_var[3].stateChanged.connect(lambda : self.custom_sauce_added(sauce_list[3], sauce_var[3].checkState()))
            sauce_var[4].stateChanged.connect(lambda : self.custom_sauce_added(sauce_list[4], sauce_var[4].checkState()))
            sauce_var[5].stateChanged.connect(lambda : self.custom_sauce_added(sauce_list[5], sauce_var[5].checkState()))
            sauce_var[6].stateChanged.connect(lambda : self.custom_sauce_added(sauce_list[6], sauce_var[6].checkState()))
        except IndexError:
            QMessageBox.critical(None, "Sauce Index Error", "Handling custom salad selection index error! Max value of index is:" + str(len(sauce_list)))   


    @pyqtSlot(str, int)
    def custom_sauce_added(self, sauce_option, state):
        if (state == Qt.Checked):
            #print (sauce_option + " is Added")
            self.__custom_sauce_array.append(sauce_option)
        elif (state == Qt.Unchecked):
            #print (sauce_option + " is Removed")
            row_no = self.__custom_sauce_array.index(sauce_option)
            self.__custom_sauce_array.pop(row_no)
            self.__cat_sauce_list_to_string = ""
        else:
            print (sauce_option + " is in an unknown state!")
            
    
    
    
    """ We will need to clear the custom salad and sauce checkboxes once the user adds them to the cart """
    def clear_salad_sauce_checkboxes(self, sauce_var, salad_var, salad_list, sauce_list):
        for x in range (0, len(salad_list)):
            if (salad_var[x].checkState() == Qt.Checked):
                salad_var[x].toggle()
        
        for y in range (0, len (sauce_list)):
            if (sauce_var[y].checkState() == Qt.Checked):
                sauce_var[y].toggle()
            
        # Clear the strings which hold custom salad and sauce choices
        del self.__custom_salad_array[:]
        del self.__custom_sauce_array[:]
        self.__cat_sauce_list_to_string = ""
        self.__cat_salad_list_to_string = ""
        
        
    def clear_burger_salad_sauce_checkboxes(self, sauce_var, salad_var, salad_list, sauce_list):
        for x in range (0, len(salad_list)):
            if (salad_var[x].checkState() == Qt.Checked):
                salad_var[x].toggle()
        
        for y in range (0, len (sauce_list)):
            if (sauce_var[y].checkState() == Qt.Checked):
                sauce_var[y].toggle()
            
        # Clear the strings which hold custom salad and sauce choices
        del self.__burger_custom_salad_list[:]
        del self.__burger_custom_sauce_list[:]
        self.__cat_burger_custom_salad = ""
        self.__cat_burger_custom_sauce = ""
        
        
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
        if state == Qt.Checked:
            self.__pizza_toppings_group_box.show()
            self.disable_other_extra_checkboxes(pizza_number, pizza_extra_checkbox)
        elif state == Qt.Unchecked:
            self.__pizza_toppings_group_box.hide()
            self.enable_all_extra_checkboxes(pizza_extra_checkbox)
        else:
            QMessageBox.critical(None, "Invalid checkbox state!", "The extra checkbox is in an unkown state")

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
        self.clear_selected_checkboxes()
        
        
        
        
    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Pizza Section : Custom Topping related methods
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""
        
    """-----------------------------------------------------------------------------
    Function    : handle_custom_topping_selection
    Description : This method is called in the Pizza section above which handles
                  user click events on custom toppings checkboxes.
                  
    Parameters  : topping_list (A list of toppings retreived from the database)
    returns     : Void
    ------------------------------------------------------------------------------"""    
    def handle_custom_topping_selection(self, topping_list):
        self.__custom_topping_option[0].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[0].checkState(), topping_list[0]['name']))
        self.__custom_topping_option[1].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[1].checkState(), topping_list[1]['name']))
        self.__custom_topping_option[2].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[2].checkState(), topping_list[2]['name']))
        self.__custom_topping_option[3].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[3].checkState(), topping_list[3]['name']))
        self.__custom_topping_option[4].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[4].checkState(), topping_list[4]['name']))
        self.__custom_topping_option[5].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[5].checkState(), topping_list[5]['name']))
        self.__custom_topping_option[6].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[6].checkState(), topping_list[6]['name']))
        self.__custom_topping_option[7].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[7].checkState(), topping_list[7]['name']))
        self.__custom_topping_option[8].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[8].checkState(), topping_list[8]['name']))
        self.__custom_topping_option[9].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[9].checkState(), topping_list[9]['name']))
        self.__custom_topping_option[10].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[10].checkState(), topping_list[10]['name']))
        self.__custom_topping_option[11].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[11].checkState(), topping_list[11]['name']))
        self.__custom_topping_option[12].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[12].checkState(), topping_list[12]['name']))
        self.__custom_topping_option[13].stateChanged.connect(lambda : self.set_topping(self.__custom_topping_option[13].checkState(), topping_list[13]['name']))

    
    @pyqtSlot(int, str)
    def set_topping(self, state, selected_topping):
        if state == Qt.Checked:
            self.__custom_topping_list.append(selected_topping)
        elif state == Qt.Unchecked:
            #print ("Removed" + selected_topping)
            rowNo = self.__custom_topping_list.index(selected_topping)
            self.__custom_topping_list.pop(rowNo)
            # Clear concatenated list as well as we pass the value of this to shopping list
            self.__cat_toppings = ""
        else:
            QMessageBox.critical(None, "Invalid topping checkbox state!", "The topping checkbox is in an unkown state")
            
    def clear_selected_checkboxes(self):
        for x in range(0, len(self.__custom_topping_option)):
            if (self.__custom_topping_option[x].checkState() == Qt.Checked):
                self.__custom_topping_option[x].toggle()
                
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
        
        #check if any toppings requested and update the price accordingly
        if (len(self.__custom_topping_list) > 0):
            topping_price = self.calculate_topping_price(size)
            price = float(price) + topping_price
            # concatenate the toppings into one string 
            self.__cat_toppings = " ".join(self.__custom_topping_list)
            
            # Now send it to the shopping list
            self.add_to_cart_method("Pizza", size, name, price, self.__cat_toppings, id)
        else:
            self.add_to_cart_method("Pizza", size, name, price, id)
        
        
        
    """
    A list of custom toppings requested by the user therefore calculate the price of the toppings requested.
    """
    def calculate_topping_price(self, size):
        if (size == '9'):
            plus = (len(self.__custom_topping_list) * 0.90)
            return float(plus)
        elif (size == '12'):
            plus = (len(self.__custom_topping_list) * 1)
            return float(plus)
        else:
            QMessageBox.critical(None, "Price Error", "Pizza Custom topping price update error! unkown size!: " + str(size))


    
    
    """--------------------------------------------------------------------------------------------------------------------------------------------------------
    |
    | Burgers Section Start
    |
    --------------------------------------------------------------------------------------------------------------------------------------------------------"""
    # Initialize the combobox variables with first values
    def initialize_burger_options(self, burgers_list):
        for x in range (0, len(burgers_list)):
            self.__burger_salad_list[x]  = "All Salad"
            self.__burger_sauce_list[x]  = "Chilli Sauce"
            self.__burger_cheese_list[x] = "No Cheese"
    
    
    
    def handle_burger_salad_selection(self, burger_salad_option):
        try: 
            burger_salad_option[0].activated.connect(lambda : self.set_burger_salad(0, burger_salad_option[0].currentText()))
            burger_salad_option[1].activated.connect(lambda : self.set_burger_salad(1, burger_salad_option[1].currentText()))
            burger_salad_option[2].activated.connect(lambda : self.set_burger_salad(2, burger_salad_option[2].currentText()))
            burger_salad_option[3].activated.connect(lambda : self.set_burger_salad(3, burger_salad_option[3].currentText()))
            burger_salad_option[4].activated.connect(lambda : self.set_burger_salad(4, burger_salad_option[4].currentText()))
            burger_salad_option[5].activated.connect(lambda : self.set_burger_salad(5, burger_salad_option[5].currentText()))
            burger_salad_option[6].activated.connect(lambda : self.set_burger_salad(6, burger_salad_option[6].currentText()))
        except IndexError:
            QMessageBox.critical(None, "Burger salad Index error!", "Index error has been raised in Burger salad change option event !")
            
            
    def handle_burger_sauce_selection(self, burger_sauce_option):
        try:
            burger_sauce_option[0].activated.connect(lambda : self.set_burger_sauce(0, burger_sauce_option[0].currentText()))
            burger_sauce_option[1].activated.connect(lambda : self.set_burger_sauce(1, burger_sauce_option[1].currentText()))
            burger_sauce_option[2].activated.connect(lambda : self.set_burger_sauce(2, burger_sauce_option[2].currentText()))
            burger_sauce_option[3].activated.connect(lambda : self.set_burger_sauce(3, burger_sauce_option[3].currentText()))
            burger_sauce_option[4].activated.connect(lambda : self.set_burger_sauce(4, burger_sauce_option[4].currentText()))
            burger_sauce_option[5].activated.connect(lambda : self.set_burger_sauce(5, burger_sauce_option[5].currentText()))
            burger_sauce_option[6].activated.connect(lambda : self.set_burger_sauce(6, burger_sauce_option[6].currentText()))
        except IndexError:
            QMessageBox.critical(None, "Burger sauce Index error!", "Index error has been raised in Burger sauce change option event !")


    def handle_burger_cheese_selection(self, burger_cheese_option):
        try:
            burger_cheese_option[0].activated.connect(lambda : self.set_burger_cheese_selection(0, burger_cheese_option[0].currentText()))
            burger_cheese_option[1].activated.connect(lambda : self.set_burger_cheese_selection(1, burger_cheese_option[1].currentText()))
            burger_cheese_option[2].activated.connect(lambda : self.set_burger_cheese_selection(2, burger_cheese_option[2].currentText()))
            burger_cheese_option[3].activated.connect(lambda : self.set_burger_cheese_selection(3, burger_cheese_option[3].currentText()))
            burger_cheese_option[4].activated.connect(lambda : self.set_burger_cheese_selection(4, burger_cheese_option[4].currentText()))
            burger_cheese_option[5].activated.connect(lambda : self.set_burger_cheese_selection(5, burger_cheese_option[5].currentText()))
            burger_cheese_option[6].activated.connect(lambda : self.set_burger_cheese_selection(6, burger_cheese_option[6].currentText()))
         
        except IndexError:
            QMessageBox.critical(None, "Burger sauce Index error!", "Index error has been raised in Burger sauce change option event !")

    def handle_burger_custom_sauce_selection(self, burger_custom_sauce_list, sauce_list):
        try:
            burger_custom_sauce_list[0].stateChanged.connect(lambda : self.set_burger_custom_sauce(sauce_list[0], burger_custom_sauce_list[0].checkState()))
            burger_custom_sauce_list[1].stateChanged.connect(lambda : self.set_burger_custom_sauce(sauce_list[1], burger_custom_sauce_list[1].checkState()))
            burger_custom_sauce_list[2].stateChanged.connect(lambda : self.set_burger_custom_sauce(sauce_list[2], burger_custom_sauce_list[2].checkState()))
            burger_custom_sauce_list[3].stateChanged.connect(lambda : self.set_burger_custom_sauce(sauce_list[3], burger_custom_sauce_list[3].checkState()))
            burger_custom_sauce_list[4].stateChanged.connect(lambda : self.set_burger_custom_sauce(sauce_list[4], burger_custom_sauce_list[4].checkState()))
            burger_custom_sauce_list[5].stateChanged.connect(lambda : self.set_burger_custom_sauce(sauce_list[5], burger_custom_sauce_list[5].checkState()))
            burger_custom_sauce_list[6].stateChanged.connect(lambda : self.set_burger_custom_sauce(sauce_list[6], burger_custom_sauce_list[6].checkState()))
        except IndexError:
            QMessageBox.critical(None, "Burger custom sauce Index Error", "Index error raised during custom sauce selection")
    
    def handle_burger_custom_salad_selection(self, burger_custom_salad_list, sauce_list):
        try:
            burger_custom_salad_list[0].stateChanged.connect(lambda : self.set_burger_custom_salad(sauce_list[0], burger_custom_salad_list[0].checkState()))
            burger_custom_salad_list[1].stateChanged.connect(lambda : self.set_burger_custom_salad(sauce_list[1], burger_custom_salad_list[1].checkState()))
            burger_custom_salad_list[2].stateChanged.connect(lambda : self.set_burger_custom_salad(sauce_list[2], burger_custom_salad_list[2].checkState()))
            burger_custom_salad_list[3].stateChanged.connect(lambda : self.set_burger_custom_salad(sauce_list[3], burger_custom_salad_list[3].checkState()))
            burger_custom_salad_list[4].stateChanged.connect(lambda : self.set_burger_custom_salad(sauce_list[4], burger_custom_salad_list[4].checkState()))
            burger_custom_salad_list[5].stateChanged.connect(lambda : self.set_burger_custom_salad(sauce_list[5], burger_custom_salad_list[5].checkState()))
            burger_custom_salad_list[6].stateChanged.connect(lambda : self.set_burger_custom_salad(sauce_list[6], burger_custom_salad_list[6].checkState()))
        except IndexError:
            QMessageBox.critical(None, "Burger custom salad Index Error", "Index error raised during custom salad selection")
    
    
    
    def handle_burger_add_button(self, burger_add_button, burger_list):
        try:
            burger_add_button[0].clicked.connect(lambda : self.add_to_cart_burger(0, burger_list[0]['name'], burger_list[0]['id']))
            burger_add_button[1].clicked.connect(lambda : self.add_to_cart_burger(1, burger_list[1]['name'], burger_list[1]['id']))
            burger_add_button[2].clicked.connect(lambda : self.add_to_cart_burger(2, burger_list[2]['name'], burger_list[2]['id']))
            burger_add_button[3].clicked.connect(lambda : self.add_to_cart_burger(3, burger_list[3]['name'], burger_list[3]['id']))
            burger_add_button[4].clicked.connect(lambda : self.add_to_cart_burger(4, burger_list[4]['name'], burger_list[4]['id']))
            burger_add_button[5].clicked.connect(lambda : self.add_to_cart_burger(5, burger_list[5]['name'], burger_list[5]['id']))
            burger_add_button[6].clicked.connect(lambda : self.add_to_cart_burger(6, burger_list[6]['name'], burger_list[6]['id']))
        except IndexError:
            QMessageBox.critical(None, "Burger add button index error", "Index Error raised while handling burger add request!")
    
    
    pyqtSlot(str)
    def set_burger_salad(self, burger_number, salad_choice):
        self.__burger_salad_list[burger_number] = salad_choice
    
        
    pyqtSlot(str)
    def set_burger_sauce(self, burger_number, sauce_choice):
        self.__burger_sauce_list[burger_number] = sauce_choice
        #print ("Sauce Choice: " + sauce_choice)
    
    pyqtSlot(str)
    def set_burger_cheese_selection(self, burger_number, cheese_choice):
        self.__burger_cheese_list[burger_number] = cheese_choice
    
        
    pyqtSlot(str)
    def set_burger_custom_sauce(self, burger_custom_sauce, state):
        if (state == Qt.Checked):
            
            self.__burger_custom_sauce_list.append(burger_custom_sauce)
        elif (state == Qt.Unchecked):
            
            row_no = self.__burger_custom_sauce_list.index(burger_custom_sauce)
            self.__burger_custom_sauce_list.pop(row_no)
        else:
            QMessageBox.critical(None, "Burger custom sauce checkbox unkown", "Burger custom sauce checkbox is in an unknown state!")
            
    pyqtSlot(str)
    def set_burger_custom_salad(self, burger_custom_salad, state):
        if (state == Qt.Checked):
            self.__burger_custom_salad_list.append(burger_custom_salad)
        elif (state == Qt.Unchecked):
            row_no = self.__burger_custom_salad_list.index(burger_custom_salad)
            self.__burger_custom_salad_list.pop(row_no)
        else:
            QMessageBox.critical(None, "Burger custom salad checkbox unkown", "Burger custom salad checkbox is in an unknown state!")
            
            
    pyqtSlot(str)
    def add_to_cart_burger(self, burger_number, burger_name, id):
        price = self.database.get_price(burger_name, "Small")
        
        if (self.__burger_cheese_list[burger_number] == "Cheese"):
            price = float(price) + 0.20
        
        
        # Check if the custom salad/sauce list is populated 
        # concatenate them into one string if they are 
        if (len (self.__burger_custom_salad_list) > 0):
            self.__cat_burger_custom_salad = " ".join(self.__burger_custom_salad_list)
        
        if (len (self.__burger_custom_sauce_list) > 0):
            self.__cat_burger_custom_sauce = " ".join(self.__burger_custom_sauce_list)
        
        
        # both custom salad and sauce requested therefore pass them as salad and sauce
        if ((self.__burger_salad_list[burger_number] == "Custom Salad") and (self.__burger_sauce_list[burger_number] == "Custom Sauce")):
            if (len(self.__burger_custom_salad_list) > 0):  
                if (len(self.__burger_custom_sauce_list) > 0):
                    self.add_to_cart_method("Burger", burger_name, self.__burger_cheese_list[burger_number], 
                                            price, self.__cat_burger_custom_salad, self.__cat_burger_custom_sauce, id)
                else:
                    QMessageBox.critical(None, "1 Custom salad and sauce selected but sauce empty list", 
                                         "Custom Salad and sauce option has been selected but no sauce option is selected!")
            else:
                QMessageBox.critical(None, "2 Custom salad and sauce selected but salad is empty list", 
                                     "Custom Salad and sauce option has been selected but no salad  is selected!")
        #only sauce is requested therefore pass custom sauce and keep salad as combobox value
        elif ((self.__burger_salad_list[burger_number] != "Custom Salad") and (self.__burger_sauce_list[burger_number] == "Custom Sauce")):
            if (len(self.__burger_custom_sauce_list) > 0):
                self.add_to_cart_method("Burger", burger_name, self.__burger_cheese_list[burger_number], 
                                        price, self.__burger_salad_list[burger_number], self.__cat_burger_custom_sauce, id)
            else:
                QMessageBox.critical(None, "3 Custom sauce is selected but not specified!", 
                                     "Custom sauce option is selected but no custom sauce selection has been specified!")
        # only salad is requested therefore pass sauce as combobox value
        elif ((self.__burger_salad_list[burger_number] == "Custom Salad") and (self.__burger_sauce_list[burger_number] != "Custom Sauce")):
            if (len(self.__burger_custom_salad_list) > 0):
                self.add_to_cart_method("Burger", burger_name, self.__burger_cheese_list[burger_number], 
                                        price, self.__cat_burger_custom_salad, self.__burger_sauce_list[burger_number], id)                
            else:
                QMessageBox.critical(None, "4 Custom salad is selected but not specified!", "Custom salad option is selected but no custom salad selection has been specified!")
        # both not requested therefore pass combobx values for each
        elif ((self.__burger_salad_list[burger_number] != "Custom Salad") and ( self.__burger_sauce_list[burger_number] != "Custom Sauce")):
            self.add_to_cart_method("Burger", burger_name, self.__burger_cheese_list[burger_number], 
                                    price, self.__burger_salad_list[burger_number], self.__burger_sauce_list[burger_number], id)       
        else:
            QMessageBox.critical(None, "5 Invalid custom salad/sauce condition", "Whislt supplying parameters to shopping list, else branch executed!")
            
        
    
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
        elif (args[0] == "Other"):
            print ("Other passed")
        else:
            QMessageBox.critical(None, "Unkown product Type passed!", "Unkown type has been passed!")
         
        # A new product has been added to the cart
        # emit the signal which will update the cart_view in generated
        # view here
        self.new_product_inserted.emit()

        # At this stage we need to clear the seleced custom sauce and salad 
        self.clear_salad_sauce_checkboxes(self.__sauce_list_from_custom, self.__salad_list_from_custom, self.__salad_list_private, self.__sauce_list_private)
        self.clear_burger_salad_sauce_checkboxes(self.cart_view_init.custom_burger_sauce_options, 
                                                 self.cart_view_init.custom_burger_salad_options, self.__salad_list_private, self.__sauce_list_private)
            
        
    @pyqtSlot()
    def new_item_inserted_event(self):
        pound = u'\xa3'
        self.send_data_to_list_view()
        self.total_price_display = self.cart_view_init.get_total_price()
        self.total_price_display.setText(pound + str(float(self.total_price)) + "0")
        print ("Total Price: " + str(self.total_price))

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
            return (item.name + str(item.price))
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
