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
    QComboBox, QPushButton

class Cart_Controller_Class(QDialog):
    def __init__(self):
        super(Cart_Controller_Class, self).__init__()
        self.cart_view_init = View_Cart_Custom.View_Cart_Custom()
        self.cart_view_init.setupUI(self)
        self.database = Model_Database_Dialog.Model_Database_Dialog()
        
        kebabs_list  = self.database.get_kebabs()
        salad_list   = self.database.get_custom_salads()
        sauce_list   = self.database.get_custom_sauces()
        
        self.pizzas_list  = self.database.get_pizzas()
        self.burgers_list = self.database.get_pizzas()
        self.others_list  = self.database.get_others()
        
        self.cart_view_init.display_kebabs(kebabs_list)
        self.cart_view_init.display_salad_options(salad_list)
        self.cart_view_init.display_sauce_options(sauce_list)





        # Create two arrays which will hold a sauce and salad
        # selection for each corresponding kebab 
        # Values for each array is assign in set_salad and set_sauce
        self.__salad = [None] * len(kebabs_list)
        self.__sauce = [None] * len(kebabs_list)
        """ 
            Make sure we initiliaze each array with first default value
            i.e. All Salad and Chilli sauce selection must be selected 
            because they are displayed and until the user changes combobox index
            the value will not be updated i.e. it will be null, therefore keep 
            the default value of all salad and chilli sauce as user might not 
            make a selection 
        """
        self.initiliaze_salad_sauce_array(self.__salad, self.__sauce)
        
        
        """ 
            salad_x and sauce_x are global variables from the View_Cart_Custom Class
            They are a list of Comboboxes holding values of salad and sauce selection
            They are neccesary for the handle_salad/sauce_selection functions
            therefore they are retreived and passed to these functions
        """
        salad_x = self.cart_view_init.salad_x
        sauce_x = self.cart_view_init.sauce_x
        add_x   = self.cart_view_init.add_button_x
        self.handle_sauce_selection(sauce_x)
        self.handle_salad_selection(salad_x)
        self.handle_add_button(add_x, kebabs_list)
        
        
    """------------------------------------------------------------------------------
    Function    :   handle_add_button
    Description :   This function handles events when the add button has been clicked.
                    It receives an array of add_button_x of type QPushButton, one 
                    for each corresponding kebab. It also receives a kebabs_list array
                    and depending on the add_button_x clicked event, it connect to
                    the add_to_cart slot supplying the kebab_list[x]['name'], salad[x]
                    sauce[x] and kebab_list[x]['price'] as parameters. The kebab_list
                    and add_x are corresponding arrays as add_x is populated with 
                    kebab_list array in View_Cart_Custom class.
    Parameters  :   add_x (An array of Pushbuttons received from View_Cart_Custom and 
                    kebabs_list (received from Model_Database_Dialog.
    Returns     :   Void
    
    ------------------------------------------------------------------------------"""  
        
    def handle_add_button(self, add_x, kebabs_list):
        add_x[0].clicked.connect(lambda : self.add_to_cart(kebabs_list[0]['name'], self.__salad[0], self.__sauce[0], kebabs_list[0]['price']))
        add_x[1].clicked.connect(lambda : self.add_to_cart(kebabs_list[1]['name'], self.__salad[1], self.__sauce[1], kebabs_list[1]['price']))
        add_x[2].clicked.connect(lambda : self.add_to_cart(kebabs_list[2]['name'], self.__salad[2], self.__sauce[2], kebabs_list[2]['price']))
        add_x[3].clicked.connect(lambda : self.add_to_cart(kebabs_list[3]['name'], self.__salad[3], self.__sauce[3], kebabs_list[3]['price']))
        add_x[4].clicked.connect(lambda : self.add_to_cart(kebabs_list[4]['name'], self.__salad[4], self.__sauce[4], kebabs_list[4]['price']))
        add_x[5].clicked.connect(lambda : self.add_to_cart(kebabs_list[5]['name'], self.__salad[5], self.__sauce[5], kebabs_list[5]['price']))
        add_x[6].clicked.connect(lambda : self.add_to_cart(kebabs_list[6]['name'], self.__salad[6], self.__sauce[6], kebabs_list[6]['price']))
        add_x[7].clicked.connect(lambda : self.add_to_cart(kebabs_list[7]['name'], self.__salad[7], self.__sauce[7], kebabs_list[7]['price']))

        
    """------------------------------------------------------------------------------
    Function    :   add_to_cart (slot)
    Description :   This slot is executed once the add button of any kebab is clicked.
                    It is currently outputting the selection messages.
    Parameters  :   name(kebab name), salad (salad selection), sauce(sauce selection)
                    and price (item price)
                    kebabs_list (received from Model_Database_Dialog.
    Returns     :   Void
    
    ------------------------------------------------------------------------------""" 
    @pyqtSlot(str, str, str, int)
    def add_to_cart(self, name, salad, sauce, price):
        print "Name: " + name + "\nSalad: " + salad + "\nSauce: " + sauce + "\nPrice: " + str(price)
    """------------------------------------------------------------------------------
    Function    : initialiaze_salad_sauce_array
    Description : This function recieves two fixed sized arrays whom hold salad
                  and sauce selection for each kebab. It initiliazes each 
                  selection with a default value of "all Salad" and "chilli sauce"
                  values. The reason for this is because the value of each salad
                  and sauce will only get update if the user will make a change in
                  combobox. Therefore we will need to initilize the default values
                  in case user will not make any changes to the combobox.
                         
    Parameters  : self.__salads, self.__sauce (fixed sized arrays holding salad
                  sauce selection for each kebab
                         
    Returns     : Void
    ------------------------------------------------------------------------------"""
    def initiliaze_salad_sauce_array(self, salads, sauces):
        for x in range(0, len(salads)):
            salads[x] = "All Salad"
        for y in range (0, len(sauces)):
            sauces[y] = "Chilli Sauce"


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
        