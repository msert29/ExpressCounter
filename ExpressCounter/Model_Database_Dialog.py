"""------------------------------------------------------------------------------
FILE        : Model_Database
DATE        : 08-12-2015
AUTHOR      : Murat Sert
DESCRIPTION : The purpose of this class is to establish a connection with the 
              database. It inherits QSqlDatabase which allows direct Sql queries
              to the database and rather than returning displayable data, 
              it returns raw data which then can be used to display dynamically
              rather than in a table form.
              
------------------------------------------------------------------------------"""
                                                                                

"""------------------------------------------------------------------------------
                     Development Diary
----------------------------------------------------------------------------------
    Date             Notes
    13/12/2015       Successfully retreived a list of items, all functions working 
                     correctly as expected.
    12/12/2015       Implemented methods which will fetch items from database such
                     as Burgers, Pizzas, Kebabs and others. 
    09/12/2015       Missing drivers installed and correction to apache2+MySql 
                     has been applied. A connection with database established.
                     
    08/12/2015       Created the class, issues with connecting to the database.
                     
              
-------------------------------------------------------------------------------"""

from PyQt4.Qt import QSqlDatabase, QMessageBox, QSqlQuery
from PyQt4 import QtCore, QtSql
import sys
from PyQt4 import QtGui


class Model_Database_Dialog(QSqlDatabase):
    def __init__(self):
        super(Model_Database_Dialog, self).__init__()
        
    """------------------------------------------------------------------------------
    Function           : establish_connection
    Description        : This function establishes a connection with the database.
                         It will print an error if it fails to connect to the database.
                         It provies confidential information of the mysql database 
                         such as username, password, databasename and hostname, all must match
                         for a valid connection.
                         It is called once in Controller_Main_Menu at start of the program.
                         Any other connection request causes it to reset a connection which 
                         will cause a performance loss. 
    Parameters         : None
    Returns            : Void
    ------------------------------------------------------------------------------"""
    def establish_connection(self):
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("localhost")
        db.setDatabaseName("expresscounter")
        db.setUserName("root")
        db.setPassword("express")
        if (db.open()==False):     
            QMessageBox.critical(None, "Database Error", db.lastError().text())   




    """------------------------------------------------------------------------------
    Function           : get_custom_sauces
    Description        : This function does a query into the database selecting all
                         entries with type kebab and size small.
                         The reason why were only selecting small sized kebabs is 
                         because all items have small and large sizes. We want to 
                         keep the menu simple without too much data. The only difference
                         is the price which is worked out in the calculate price method below.
                         This method is called in the add_to_cart slot in Controller_Cart_Dialog.
                         It then iterates through the results appending each result to
                         a dynamic array. 
                         This function is directly called by Controller_Cart_Dialog
    Parameters         : none
    Returns            : list_of_kebabs_array (Which is used by Controller_Cart_Dialog
    ------------------------------------------------------------------------------""" 
     
    def get_kebabs(self):
        list_of_kebabs_array = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Products` WHERE `product_type` LIKE 'Kebab' AND `product_size` LIKE 'Small' ORDER BY `product_id` ASC""")
        while (query.next()):
            kebab_dict = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(4).toString()}
            list_of_kebabs_array.append(kebab_dict)
        return list_of_kebabs_array

    """------------------------------------------------------------------------------
    Function           : get_pizzas
    Description        : This function does a query into the database selecting 
                         items with type = 'Pizza' and then stores
                         the returned information in a dictionary. For each item iteration
                         it appends the dictionary to a dynamic array which is returned.
    Parameters         : none
    Returns            : list_of_pizza_array (Which is used by Controller_Cart_Dialog
    ------------------------------------------------------------------------------"""
    def get_pizzas(self):
        list_of_pizza_array = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Products` WHERE `product_type` LIKE 'Pizza' AND `product_size` LIKE '9' ORDER BY `product_id` ASC""")
        while (query.next()):
            pizza_dict = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(4).toString()}
            list_of_pizza_array.append(pizza_dict)
        return list_of_pizza_array
        
    """------------------------------------------------------------------------------
    Function           : get_burgers
    Description        : This function does a query into the database selecting
                         items with type = 'Burger' and then stores
                         the returned information in a dictionary. For each item iteration
                         it appends the dictionary to a dynamic array which is returned.
    Parameters         : none
    Returns            : list_of_burgers_array (Which is used by Controller_Cart_Dialog
    ------------------------------------------------------------------------------"""
    def get_burgers(self):
        list_of_burgers_array = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Products` WHERE `product_type` LIKE 'Burger' AND `product_size` LIKE 'Small' ORDER BY `product_id` ASC""")
        while (query.next()):
            burger_dict = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(3).toString()}
            list_of_burgers_array.append(burger_dict)
        return list_of_burgers_array
        

        
    """------------------------------------------------------------------------------
    Function           : get_others
    Description        : This function does a query into the database selecting
                         items with type = 'Other' and then stores
                         the returned information in a dictionary. For each item iteration
                         it appends the dictionary to a dynamic array which is returned.
    Parameters         : none
    Returns            : list_of_kebabs_array (Which is used by Controller_Cart_Dialog
    ------------------------------------------------------------------------------"""    
    def get_others(self):
        list_of_others_array = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Items` WHERE `type` LIKE `other` """)
        while (query.next()):
            other_dict = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(3).toString()}
            list_of_others_array.append(other_dict)
            return list_of_others_array
        
    """------------------------------------------------------------------------------
    Function           : get_price
    Description        : This function does a query into the database selecting
                         items with name = 'product_name' and size = product_size
                         It returns the price of the matching entry. It is called by
                         the add_to_cart slot form the Controller_Cart_Dialog class.
    Parameters         : product_name, product_size
    Returns            : Price
    ------------------------------------------------------------------------------"""    
    def get_price(self, product_name, product_size):
        query = QSqlQuery()
        query.prepare("""SELECT `product_price` FROM `Products` WHERE `product_name` LIKE ? AND `product_size` LIKE ?""")
        query.bindValue(0, product_name)
        query.bindValue(1, product_size)
        query.exec_()
        while (query.next()):
            return query.value(0).toString()
    
    """------------------------------------------------------------------------------
    Function           : get_custom_salads
    Description        : This function does a query into the database selecting all
                         entries in the Salads table.
                         It then iterates through the results appending each result to
                         a dynamic array. 
                         This function is directly called by Controller_Cart_Dialog
    Parameters         : none
    Returns            : list_of_salads_array (Which is used by Controller_Cart_Dialog
    ------------------------------------------------------------------------------"""  
    def get_custom_salads(self):
        list_of_salads_array = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Salads`""")
        while (query.next()):
            list_of_salads_array.append(query.value(1).toString())
        return list_of_salads_array
        
    """------------------------------------------------------------------------------
    Function           : get_custom_sauces
    Description        : This function does a query into the database selecting all
                         entries in the Sauces table.
                         It then iterates through the results appending each result to
                         a dynamic array. 
                         This function is directly called by Controller_Cart_Dialog
    Parameters         : none
    Returns            : list_of_sauces_array (Which is used by Controller_Cart_Dialog
    ------------------------------------------------------------------------------"""  
    def get_custom_sauces(self):
        list_of_sauces_array = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Sauces` """)
        while (query.next()):
            list_of_sauces_array.append(query.value(1).toString())
        return list_of_sauces_array   
        
        
    """------------------------------------------------------------------------------
    Function           : get_pizza_toppings
    Description        : This function does a query into the database selecting all
                         entries in the Toppings table.
                         It then iterates through the results saving each to a dictionary
                         Each dictionary is then apppending to a dynamic array. 
                         This array is returned
                         This function is directly called by Controller_Cart_Dialog
    Parameters         : none
    Returns            : list_of_toppings_array (Which is used by Controller_Cart_Dialog)
    ------------------------------------------------------------------------------"""  
    def get_pizza_toppings(self):
        list_of_toppings_array = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Toppings` WHERE `size` = 9""")
        while (query.next()):
            topping_dict = {'id': query.value(0).toString(), 'name': query.value(1).toString(), 'size':query.value(2).toString(), 'price': query.value(3).toString()}
            list_of_toppings_array.append(topping_dict)
        return list_of_toppings_array
    
    """ ------------------------------------------------------------------------------
    Function           : get_pizza_topping_price
    Description        : This function does a query into the database aiming to retreive
                         the price of the given topping. Toppings can be either 0.90 pence
                         or pound 1 depending on pizza size. Therefore we will need to distinguish
                         between pizza toppings. 
    Parameters         : topping_name (name of the pizza topping) size (size of the pizza topping
                            which can be 9 or 12 in lieue with pizza size)
    Returns            :  query.value(0).toString() (returned query result from database)
    ------------------------------------------------------------------------------"""  
    
    
    def get_pizza_topping_price(self, topping_name, size):
        query = QSqlQuery()
        query.exec_("""SELECT `price` FROM `Toppings` WHERE `topping_name` LIKE ? AND `size` = ? """)
        while (query.next()):
            return query.value(0).toString()
         
         
    """------------------------------------------------------------------------------
    Function           : get_all_items
    Description        : This function retrieves all items in the Items table.
                         It is used as a debug function to print the data to he console.
    Parameters         : none
    Returns            : NOne
    ------------------------------------------------------------------------------"""    
    def get_all_items(self):
        array_of_items = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Items` """) 
        while (query.next()):
            deneme = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(3).toString()}
            array_of_items.append(deneme)
            print "ID:" + query.value(0).toString()
            print "Type: " + query.value(1).toString()
            print "Name: " + query.value(2).toString()
            print "Price: "+ query.value(3).toString()
        return array_of_items