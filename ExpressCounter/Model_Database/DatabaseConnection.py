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


class Model_Database(QSqlDatabase):
    def __init__(self):
        super(Model_Database, self).__init__()
        
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
        query.exec_("""SELECT * FROM `Items` WHERE `type` LIKE `pizza` """)
        while (query.next()):
            pizza_dict = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(3).toString()}
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
        query.exec_("""SELECT * FROM `Items` WHERE `type` LIKE `burger` """)
        while (query.next()):
            burger_dict = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(3).toString()}
            list_of_burgers_array.append(burger_dict)
        return list_of_burgers_array
        
    
    """------------------------------------------------------------------------------
    Function           : get_kebabs
    Description        : This function does a query into the database selecting
                         items with type = 'Kebabs' and then stores
                         the returned information in a dictionary. For each item iteration
                         it appends the dictionary to a dynamic array which is returned.
    Parameters         : none
    Returns            : list_of_kebabs_array (Which is used by Controller_Cart_Dialog
    ------------------------------------------------------------------------------"""
    def get_kebabs(self):
        list_of_kebabs_array = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Items` WHERE `type` LIKE 'Kebab'""")
        while (query.next()):
            kebab_dict = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(3).toString()}
            list_of_kebabs_array.append(kebab_dict)
        return list_of_kebabs_array
        
        
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
    
   
    
    