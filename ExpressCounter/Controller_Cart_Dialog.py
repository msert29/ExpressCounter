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
from PyQt4.QtCore import Qt , pyqtSlot
from PyQt4.Qt import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox,\
    QComboBox, QPushButton, QMessageBox


class Cart_Controller_Class(QDialog):
    def __init__(self):
        super(Cart_Controller_Class, self).__init__()
        
        self.cart_view_init = View_Cart_Custom.View_Cart_Custom()
        self.cart_view_init.setupUI(self)
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        
        #kebabs_list  = self.database.get_kebabs()
        kebabs_list  = self.database.get_kebabs()
        salad_list   = self.database.get_custom_salads()
        sauce_list   = self.database.get_custom_sauces()
        
        self.pizzas_list  = self.database.get_pizzas()
        self.burgers_list = self.database.get_pizzas()
        self.others_list  = self.database.get_others()
        
        self.cart_view_init.display_kebabs(kebabs_list)
        self.cart_view_init.display_salad_options(salad_list)
        self.cart_view_init.display_sauce_options(sauce_list)

        # Two arrays which will hold a list of custom selected salad and sauce
        self.__custom_salad_array = []
        self.__custom_sauce_array = []
        
        # Create three arrays which will hold sauce, salad and size
        # selection for each corresponding kebab. 
        # Values for each array is assign in set_salad and set_sauce
        self.__salad = [None] * len(kebabs_list)
        self.__sauce = [None] * len(kebabs_list)
        self.__size =  [None] * len(kebabs_list)

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
            salad_x and sauce_x are global variables from the View_Cart_Custom Class
            They are a list of Comboboxes holding values of salad and sauce selection
            They are neccesary for the handle_salad/sauce_selection functions
            therefore they are retreived and passed to these functions
        """
        self.__salad_x_from_custom        = self.cart_view_init.salad_x
        self.__sauce_x_from_custom        = self.cart_view_init.sauce_x
        self.__size_x_from_custom         = self.cart_view_init.size_x
        
        self.__add_x_button_from_custom   = self.cart_view_init.add_button_x
        self.__salad_list_from_custom     = self.cart_view_init.salads_var
        self.__sauce_list_from_custom     = self.cart_view_init.sauces_var
        self.handle_sauce_selection(self.__sauce_x_from_custom)
        self.handle_salad_selection(self.__salad_x_from_custom)
        self.handle_size_selection(self.__size_x_from_custom)
        self.handle_custom_salad_selection(self.__salad_list_from_custom, salad_list)
        self.handle_custom_sauce_selection(self.__sauce_list_from_custom, sauce_list)
        self.handle_add_button(self.__add_x_button_from_custom, kebabs_list)

        
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
        add_x[0].clicked.connect(lambda : self.add_to_cart(self.__size[0], kebabs_list[0]['name'], self.__salad[1], self.__sauce[1]))
        add_x[1].clicked.connect(lambda : self.add_to_cart(self.__size[1], kebabs_list[1]['name'], self.__salad[1], self.__sauce[1]))
        add_x[2].clicked.connect(lambda : self.add_to_cart(self.__size[2], kebabs_list[2]['name'], self.__salad[2], self.__sauce[2]))
        add_x[3].clicked.connect(lambda : self.add_to_cart(self.__size[3], kebabs_list[3]['name'], self.__salad[3], self.__sauce[3]))
        add_x[4].clicked.connect(lambda : self.add_to_cart(self.__size[4], kebabs_list[4]['name'], self.__salad[4], self.__sauce[4]))
        add_x[5].clicked.connect(lambda : self.add_to_cart(self.__size[5], kebabs_list[5]['name'], self.__salad[5], self.__sauce[5]))
        add_x[6].clicked.connect(lambda : self.add_to_cart(self.__size[6], kebabs_list[6]['name'], self.__salad[6], self.__sauce[6]))
        add_x[7].clicked.connect(lambda : self.add_to_cart(self.__size[7], kebabs_list[7]['name'], self.__salad[7], self.__sauce[7]))

        
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
    def add_to_cart(self, size, name, salad, sauce):
        price = self.database.get_price(name, size)
        print ("Size: " + str(size) + "\nName: " + name + "\nSalad: " + salad + "\nSauce: " + sauce + "\nPrice: " + price)
        self.__cat_salad_list_to_string = " ".join(self.__custom_salad_array)
        self.__cat_sauce_list_to_string = " ".join(self.__custom_sauce_array)
        print (self.__cat_salad_list_to_string)
        print (self.__cat_sauce_list_to_string)
        

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
        for x in range(0, len(salads)):
            salads[x] = "All Salad"
        for y in range (0, len(sauces)):
            sauces[y] = "Chilli Sauce"
        for z in range(0, len(kebabs_list)):
            self.__size[z] = "Small"


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
        salad_x[0].activated[str].connect(lambda : self.set_salad(0, salad_x[0].currentText()))
        salad_x[1].activated[str].connect(lambda : self.set_salad(1, salad_x[1].currentText()))
        salad_x[2].activated[str].connect(lambda : self.set_salad(2, salad_x[2].currentText()))
        salad_x[3].activated[str].connect(lambda : self.set_salad(3, salad_x[3].currentText()))
        salad_x[4].activated[str].connect(lambda : self.set_salad(4, salad_x[4].currentText()))
        salad_x[5].activated[str].connect(lambda : self.set_salad(5, salad_x[5].currentText()))
        salad_x[6].activated[str].connect(lambda : self.set_salad(6, salad_x[6].currentText()))
        salad_x[7].activated[str].connect(lambda : self.set_salad(7, salad_x[7].currentText()))
        
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
        sauce_x[0].activated[str].connect(lambda : self.set_sauce(0, sauce_x[0].currentText()))
        sauce_x[1].activated[str].connect(lambda : self.set_sauce(1, sauce_x[1].currentText()))
        sauce_x[2].activated[str].connect(lambda : self.set_sauce(2, sauce_x[2].currentText()))
        sauce_x[3].activated[str].connect(lambda : self.set_sauce(3, sauce_x[3].currentText()))
        sauce_x[4].activated[str].connect(lambda : self.set_sauce(4, sauce_x[4].currentText()))
        sauce_x[5].activated[str].connect(lambda : self.set_sauce(5, sauce_x[5].currentText()))
        sauce_x[6].activated[str].connect(lambda : self.set_sauce(6, sauce_x[6].currentText()))
        sauce_x[7].activated[str].connect(lambda : self.set_sauce(7, sauce_x[7].currentText()))
    
    def handle_size_selection(self, size_x):
        size_x[0].activated[str].connect(lambda : self.set_size(0, size_x[0].currentText()))
        size_x[1].activated[str].connect(lambda : self.set_size(1, size_x[1].currentText()))
        size_x[2].activated[str].connect(lambda : self.set_size(2, size_x[2].currentText()))
        size_x[3].activated[str].connect(lambda : self.set_size(3, size_x[3].currentText()))
        size_x[4].activated[str].connect(lambda : self.set_size(4, size_x[4].currentText()))
        size_x[5].activated[str].connect(lambda : self.set_size(5, size_x[5].currentText()))
        size_x[6].activated[str].connect(lambda : self.set_size(6, size_x[6].currentText()))
        size_x[7].activated[str].connect(lambda : self.set_size(7, size_x[7].currentText()))
        
        
    @pyqtSlot(int, str)
    def set_size(self, number, value): 
        self.__size[number] = value 
        
        
        
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
            #print (salad_option + " is checked state!")
            self.__custom_salad_array.append(salad_option)
        elif (state == Qt.Unchecked):
            #print (salad_option + " is unchecked state!")
            self.__custom_salad_array.pop(salad_option)

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
            #print sauce_option + " is checked state!"
            self.__custom_sauce_array.append(sauce_option)
        elif (state == Qt.Unchecked):
            #print sauce_option + " is unchecked state!"
            self.__custom_sauce_array.pop(sauce_option)
        else:
            print (sauce_option + " is in an unknown state!")