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
from PyQt4.QtSql import QSqlQuery
                                                                                
from PyQt4.QtCore import QDateTime, QTime, QDate
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

from PyQt4.Qt import QSqlDatabase, QMessageBox, QSqlQuery, QVariant, QSqlError
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
        db.setPassword("expresscounter")
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
        
    def get_id(self, name):
        query = QSqlQuery()
        query.prepare("""SELECT `product_id` FROM `Products` WHERE `product_name` LIKE :name""")
        query.bindValue(":name", str(name))
        query.exec_()
        while(query.next()):
            id = query.value(0).toString()
            return id
        
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
        query.exec_("""SELECT * FROM `Products` WHERE `product_type` LIKE 'Other' ORDER BY `product_id` ASC""")
        while (query.next()):
            other_dict = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(3).toString()}
            list_of_others_array.append(other_dict)
        return list_of_others_array
        
        
    def get_drinks(self):
        list_of_drinks = []
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Products` WHERE `product_type` LIKE 'Drink' AND `product_size` LIKE 'can' ORDER BY `product_id` ASC""")
        while (query.next()):
            kebab_dict = {'id': query.value(0).toString(), 'type': query.value(1).toString(), 'name':query.value(2).toString(), 'price': query.value(4).toString()}
            list_of_drinks.append(kebab_dict)
        return list_of_drinks
        
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
    
    
    
    
    
    def insert_all_to_database(self, shopping_list, total_price, customerid):
        
        last_id_no = 0
        last_order_id_query = QSqlQuery()
        last_order_id_query.exec_(""" SELECT `order_id` FROM `Orders`""")
        while (last_order_id_query.next()):
            last_id_no = last_order_id_query.value(0).toString()
         
        # get local time and date
        # generate an order id
        query = QSqlQuery()
        
        
        current_time = QTime()
        current_date = QDate()
    
        last_id_no = int(last_id_no) + 1
        for x in range(0, len(shopping_list)):
            try:
                options = str(shopping_list[x].salad) + " " + str(shopping_list[x].sauce)
            except AttributeError:
                try:
                    options =  str(shopping_list[x].toppings)
                except AttributeError:
                    options = "No Extra toppings"
            
            query.prepare("INSERT INTO `expresscounter`.`Orders` (`order_id` , `customer_id` ,`item_id` , `options` , `total_price` , `date_of_order` , `time_of_order`)"
                            "VALUES (:order_id , :c_id , :i_id , :option , :total_price , :date , :time);")
            query.bindValue(":order_id", str(last_id_no))
            query.bindValue(":c_id", customerid)
            query.bindValue(":i_id", shopping_list[x].id)
            query.bindValue(":option", options)
            query.bindValue(":total_price", total_price)
            query.bindValue(":date", current_date.currentDate())
            query.bindValue(":time", current_time.currentTime())

            query.exec_()
            # Check if we have an error returned and print it if true
            #if (query.lastError()):
            errorstr = str(query.lastError().text())   
            print errorstr 
            #QMessageBox.critical(None, "Error while executing MYSQL Statement! ", "Unable to insert orders into the orders database!" + str(errorstr))
        return last_id_no
            
    def insert_new_customer(self, customer):
        new_customer_data_query = QSqlQuery()
        new_customer_data_query.prepare("INSERT INTO `expresscounter`.`Customers` (`customer_id` , `name` , `address` , `postcode` , `number`)"
                                        "VALUES (:customer_id , :name , :address , :postcode , :number);")
        new_customer_data_query.bindValue(":customer_id", "")
        new_customer_data_query.bindValue(":name", str(customer.name))
        new_customer_data_query.bindValue(":address", str(customer.address))
        new_customer_data_query.bindValue(":postcode", str(customer.postcode))
        new_customer_data_query.bindValue(":number", str(customer.telephone))
        new_customer_data_query.exec_()
        
        error = new_customer_data_query.lastError()
        if (error.type() == QSqlError.NoError):
            QMessageBox.information(None, "Inserted!", "A new customer entry has succesfully been inserted!")
        else:
            QMessageBox.critical(None, "Error!", "Cannot insert the customer into the database")
    
    def get_customer_id(self, name, address, postcode, number):
        search_for_id = QSqlQuery()
        search_for_id.prepare("""SELECT customer_id FROM Customers WHERE name LIKE ? AND address LIKE ? AND postcode LIKE ? AND number LIKE ?""")
        search_for_id.bindValue(0, name)
        search_for_id.bindValue(1, address)
        search_for_id.bindValue(2, postcode)
        search_for_id.bindValue(3, number)
        search_for_id.exec_()
        while(search_for_id.next()):
            customer_id = search_for_id.value(0).toString()
        print "Id: " + str(customer_id)
        return customer_id
    
    """ This function receives the id of the customer and returns the 
        customer details upon finding matching results
        Called from the file_io from contreoller_customer dialog class
    """
    def get_customer_details(self, customer_id):
        search_customer = QSqlQuery()
        search_customer.prepare("""SELECT * FROM Customers WHERE customer_id LIKE ?""")
        search_customer.bindValue(0, customer_id)
        search_customer.exec_()
        while (search_customer.next()):
            customer_details = { 'name' : search_customer.value(1).toString(), 'address' : search_customer.value(2).toString(), \
            'postcode' : search_customer.value(3).toString(),  'telephone' : search_customer.value(4).toString()}
        return customer_details
    
    def search_existing_customer(self, *args):
        # if all inputs are inserted then they will be bigger than one
        
        results_array = []
        
        search_all_q = QSqlQuery()
        if (len(args) > 3):
            name = args[0]
            addr = args[1]
            post = args[2]
            tel  = args[3]
            
            search_all_q.prepare("SELECT * FROM Customers WHERE name LIKE ? AND address LIKE ? AND postcode LIKE ? AND number LIKE ?")
            search_all_q.bindValue(0, name)
            search_all_q.bindValue(1, addr)
            search_all_q.bindValue(2, post)
            search_all_q.bindValue(3, tel)
            search_all_q.exec_()
            while (search_all_q.next()):
                results_dictionary = {'id' : search_all_q.value(0).toString(), 'name' : search_all_q.value(1).toString(), 'address' : search_all_q.value(2).toString(),
                                      'postcode' : search_all_q.value(3).toString(), 'number' : search_all_q.value(4).toString()}
                results_array.append(results_dictionary)
            return results_array
        elif (args[0] == "name"):
            
            name = args[1]
            
            search_all_q.prepare("SELECT * FROM Customers WHERE name LIKE ?")
            search_all_q.bindValue(0, name)
            search_all_q.exec_()
            while (search_all_q.next()):
                results_dictionary = {'id' : search_all_q.value(0).toString(), 'name' : search_all_q.value(1).toString(), 'address' : search_all_q.value(2).toString(),
                                      'postcode' : search_all_q.value(3).toString(), 'number' : search_all_q.value(4).toString()}
                results_array.append(results_dictionary)
            return results_array
            errorstr = str(search_all_q.lastError().text())
            print errorstr
        elif (args[0] == "address"):
            addr = args[1]
            
            search_all_q.prepare("SELECT * FROM `Customers` WHERE address LIKE ?")
            search_all_q.bindValue(0, addr)
            search_all_q.exec_()
            while (search_all_q.next()):
                results_dictionary = {'id' : search_all_q.value(0).toString(), 'name' : search_all_q.value(1).toString(), 'address' : search_all_q.value(2).toString(),
                                      'postcode' : search_all_q.value(3).toString(), 'number' : search_all_q.value(4).toString()}
                results_array.append(results_dictionary)
            return results_array
            errorstr = str(search_all_q.lastError().text())
            print errorstr
        elif (args[0] == "postcode"):
            postcode = args[1]
            
            search_all_q.prepare("SELECT * FROM `Customers` WHERE postcode LIKE ?")
            search_all_q.bindValue(0, postcode)
            search_all_q.exec_()
            while (search_all_q.next()):
                results_dictionary = {'id' : search_all_q.value(0).toString(), 'name' : search_all_q.value(1).toString(), 'address' : search_all_q.value(2).toString(),
                                      'postcode' : search_all_q.value(3).toString(), 'number' : search_all_q.value(4).toString()}
                results_array.append(results_dictionary)
            return results_array
            errorstr = str(search_all_q.lastError().text())
            print errorstr
        elif (args[0] == "tel"):
            tel = args[1]
        
            search_all_q.prepare("SELECT * FROM `Customers` WHERE number LIKE ?")
            search_all_q.bindValue(0, tel)
            search_all_q.exec_()
            while (search_all_q.next()):
                results_dictionary = {'id' : search_all_q.value(0).toString(), 'name' : search_all_q.value(1).toString(), 'address' : search_all_q.value(2).toString(),
                                      'postcode' : search_all_q.value(3).toString(), 'number' : search_all_q.value(4).toString()}
                results_array.append(results_dictionary)
            return results_array
            errorstr = str(search_all_q.lastError().text())
            print errorstr
        else:
            print "Unknown "
            
    
    
    def search_order_by_name(self, customer_name):
        order_result = []
        customer = []
        order_search = QSqlQuery()
        customer_search = QSqlQuery()
        order_id_array = []
        customer_search.prepare("SELECT customer_id FROM Customers WHERE name LIKE ?")
        customer_search.bindValue(0, customer_name)
        customer_search.exec_()
        while (customer_search.next()):
            customer.append(customer_search.value(0).toString())
        
        for x in range(0, len(customer)):
            order_search.prepare("SELECT * FROM Orders WHERE customer_id LIKE ?")
            order_search.bindValue(0, customer[x])
            order_search.exec_()
            while (order_search.next()):
                """ order ids are not unique ie for each product same order id is used 
                for one order. This means that this query will return duplicate entries of
                same order. What we do here is store the order id into a dynamic list, and then
                and then we check that the order id hasn't appeared before, if it has we count the
                query result as duplicate and dont append it to our list. """
                order_id = order_search.value(0).toString()
                order_id_array.append(order_id)
                if (order_id_array.count(order_id) <= 1):
                    product_name = self.get_product_name_by_id(order_search.value(2).toString())
                    customer_details = self.get_customer_by_id(order_search.value(1).toString())
                    order_result_dict = {'id' : order_search.value(0).toString(), 'customer_name' : customer_details['name'], \
                                     'customer_address' : customer_details['address'], 'customer_postcode' : customer_details['postcode'], \
                                     'customer_tel' : customer_details['tel'], \
                                'product_name' : product_name, 'options' : order_search.value(3).toString(), \
                                'price' : order_search.value(4).toString(), 'date' : order_search.value(5).toString(), \
                                'time' : order_search.value(6).toString()}
                    order_result.append(order_result_dict)
        return order_result
    
    
    def search_order_by_address(self, customer_address):
        order_result = []
        customer = []
        order_search = QSqlQuery()
        customer_search = QSqlQuery()
        order_id_array = []
        customer_search.prepare("SELECT customer_id FROM Customers WHERE address LIKE ?")
        customer_search.bindValue(0, customer_address)
        customer_search.exec_()
        while (customer_search.next()):
            customer.append(customer_search.value(0).toString())
        
        for x in range(0, len(customer)):
            order_search.prepare("SELECT * FROM Orders WHERE customer_id LIKE ?")
            order_search.bindValue(0, customer[x])
            order_search.exec_()
            while (order_search.next()):
                """ order ids are not unique ie for each product same order id is used 
                for one order. This means that this query will return duplicate entries of
                same order. What we do here is store the order id into a dynamic list, and then
                and then we check that the order id hasn't appeared before, if it has we count the
                query result as duplicate and dont append it to our list. """
                order_id = order_search.value(0).toString()
                order_id_array.append(order_id)
                if (order_id_array.count(order_id) <= 1):
                    product_name = self.get_product_name_by_id(order_search.value(2).toString())
                    customer_details = self.get_customer_by_id(order_search.value(1).toString())
                    order_result_dict = {'id' : order_search.value(0).toString(), 'customer_name' : customer_details['name'], \
                                     'customer_address' : customer_details['address'], 'customer_postcode' : customer_details['postcode'], \
                                     'customer_tel' : customer_details['tel'], \
                                'product_name' : product_name, 'options' : order_search.value(3).toString(), \
                                'price' : order_search.value(4).toString(), 'date' : order_search.value(5).toString(), \
                                'time' : order_search.value(6).toString()}
                    order_result.append(order_result_dict)
        return order_result
    
    def search_order_by_postcode(self, customer_postcode):
        order_result = []
        customer = []
        order_search = QSqlQuery()
        customer_search = QSqlQuery()
        order_id_array = []
        customer_search.prepare("SELECT customer_id FROM Customers WHERE postcode LIKE ?")
        customer_search.bindValue(0, customer_postcode)
        customer_search.exec_()
        while (customer_search.next()):
            customer.append(customer_search.value(0).toString())
        
        for x in range(0, len(customer)):
            order_search.prepare("SELECT * FROM Orders WHERE customer_id LIKE ?")
            order_search.bindValue(0, customer[x])
            order_search.exec_()
            while (order_search.next()):
                """ order ids are not unique ie for each product same order id is used 
                for one order. This means that this query will return duplicate entries of
                same order. What we do here is store the order id into a dynamic list, and then
                and then we check that the order id hasn't appeared before, if it has we count the
                query result as duplicate and dont append it to our list. """
                order_id = order_search.value(0).toString()
                order_id_array.append(order_id)
                if (order_id_array.count(order_id) <= 1):
                    product_name = self.get_product_name_by_id(order_search.value(2).toString())
                    customer_details = self.get_customer_by_id(order_search.value(1).toString())
                    order_result_dict = {'id' : order_search.value(0).toString(), 'customer_name' : customer_details['name'], \
                                     'customer_address' : customer_details['address'], 'customer_postcode' : customer_details['postcode'], \
                                     'customer_tel' : customer_details['tel'], \
                                'product_name' : product_name, 'options' : order_search.value(3).toString(), \
                                'price' : order_search.value(4).toString(), 'date' : order_search.value(5).toString(), \
                                'time' : order_search.value(6).toString()}
                    order_result.append(order_result_dict)
        return order_result
    
    def search_order_by_tel(self, customer_tel):
        order_result = []
        customer = []
        order_search = QSqlQuery()
        customer_search = QSqlQuery()
        order_id_array = []
        customer_search.prepare("SELECT customer_id FROM Customers WHERE number LIKE ?")
        customer_search.bindValue(0, customer_tel)
        customer_search.exec_()
        while (customer_search.next()):
            customer.append(customer_search.value(0).toString())
        for x in range(0, len(customer)):
            order_search.prepare("SELECT * FROM Orders WHERE customer_id LIKE ?")
            order_search.bindValue(0, customer[x])
            order_search.exec_()
            while (order_search.next()):
                """ order ids are not unique ie for each product same order id is used 
                for one order. This means that this query will return duplicate entries of
                same order. What we do here is store the order id into a dynamic list, and then
                and then we check that the order id hasn't appeared before, if it has we count the
                query result as duplicate and dont append it to our list. """
                order_id = order_search.value(0).toString()
                order_id_array.append(order_id)
                if (order_id_array.count(order_id) <= 1):
                    product_name = self.get_product_name_by_id(order_search.value(2).toString())
                    customer_details = self.get_customer_by_id(order_search.value(1).toString())
                    order_result_dict = {'id' : order_search.value(0).toString(), 'customer_name' : customer_details['name'], \
                                     'customer_address' : customer_details['address'], 'customer_postcode' : customer_details['postcode'], \
                                     'customer_tel' : customer_details['tel'], \
                                'product_name' : product_name, 'options' : order_search.value(3).toString(), \
                                'price' : order_search.value(4).toString(), 'date' : order_search.value(5).toString(), \
                                'time' : order_search.value(6).toString()}
                    order_result.append(order_result_dict)
        return order_result
    
    def search_order_by_id_for_display(self, order_id):
        order_result = []
        order_search = QSqlQuery()
        order_search.prepare("SELECT * FROM Orders WHERE order_id LIKE ?")
        order_search.bindValue(0, order_id)
        order_search.exec_()
        while (order_search.next()):
            if (order_search.isValid()):
                product_name     = self.get_product_name_by_id(order_search.value(2).toString())
                customer_details = self.get_customer_by_id(order_search.value(1).toString())
                product_type             = self.get_product_type_by_id(order_search.value(2).toString())
                order_result_dict = {'id' : order_search.value(0).toString(), 'customer_name' : customer_details['name'], \
                                     'customer_address' : customer_details['address'], 'customer_postcode' : customer_details['postcode'], \
                                     'customer_tel' : customer_details['tel'], \
                                'product_name' : product_name, 'options' : order_search.value(3).toString(), \
                                'price' : order_search.value(4).toString(), 'date' : order_search.value(5).toString(), \
                                'time' : order_search.value(6).toString(), 'product_type' : product_type}
                order_result.append(order_result_dict)
              
        return order_result
        
       
    def search_order_by_id(self, order_id):
        order_result = []
        order_search = QSqlQuery()
        order_search.prepare("SELECT * FROM Orders WHERE order_id LIKE ?")
        order_search.bindValue(0, order_id)
        order_search.exec_()
       
        while (order_search.next()):
            if (order_search.isValid()):
                product_name = self.get_product_name_by_id(order_search.value(2).toString())
                customer_details = self.get_customer_by_id(order_search.value(1).toString())
                order_result_dict = {'id' : order_search.value(0).toString(), 'customer_name' : customer_details['name'], \
                                     'customer_address' : customer_details['address'], 'customer_postcode' : customer_details['postcode'], \
                                     'customer_tel' : customer_details['tel'], \
                                'product_name' : product_name, 'options' : order_search.value(3).toString(), \
                                'price' : order_search.value(4).toString(), 'date' : order_search.value(5).toString(), \
                                'time' : order_search.value(6).toString()}
                order_result.append(order_result_dict)
                return order_result
    
    """ This method is used by Controller_Manager_Dialog to retreive a list of orders placed according
    to a specified date """
    def search_order_by_date(self, date):
        price_count = 0.00
        order_count = 0
        current_id = 0
        tmp_id = 0
        order_result = []
        order_search = QSqlQuery()
        order_search.prepare("SELECT * FROM Orders WHERE date_of_order LIKE ?")
        order_search.bindValue(0, date)
        order_search.exec_()
       
        while (order_search.next()):
            current_id = order_search.value(0).toString()
            """
            Order IDs arent unique therefore price and order count should be calculate correctly
            Here we make a selection of the order id returned by database against a tmp id
            if they dont match, which means that we have a new order id, we store it and then
            append it to our dictionary.
            """
            if (current_id != tmp_id):
                customer_details = self.get_customer_by_id(order_search.value(1).toString())
                price_count = price_count + float(order_search.value(4).toString())
                order_count = order_count + 1
                tmp_id = current_id
                order_result_dict = {'id' : order_search.value(0).toString(), 'customer_name' : customer_details['name'], \
                                'customer_address' : customer_details['address'], 'customer_postcode' : customer_details['postcode'], \
                                'customer_tel' : customer_details['tel'], \
                                'price' : order_search.value(4).toString(), 'date' : order_search.value(5).toString(), \
                                'time' : order_search.value(6).toString(), 'price_count' : price_count, 'order_count' : order_count}
                order_result.append(order_result_dict)
        return order_result
        
        
        
    # As product name is referenced with product id in the orders table
    # we need to retreive the product name in order to print it as product id is un-meaningful
    def get_product_name_by_id(self, product_id):
        product_search = QSqlQuery()
        product_search.prepare("SELECT * FROM Products WHERE product_id LIKE ?")
        product_search.bindValue(0, product_id)
        product_search.exec_()
        while (product_search.next()):
            # Concatenate the size and string values 
            size_name = product_search.value(3).toString() + " " + product_search.value(2).toString()
            return size_name
        
        
    # Product type isn't referenced directly in orders table and 
    # for file i/o in Order View dialog we need product type to distinguish
    # beetween products for correct format of writing to a file waiting to be printed off
    def get_product_type_by_id(self, product_id):
        product_search = QSqlQuery()
        product_search.prepare("SELECT product_type FROM Products WHERE product_id LIKE ?")
        product_search.bindValue(0, product_id)
        product_search.exec_()
        while (product_search.next()):
            # Concatenate the size and string values 
            product_type = product_search.value(0).toString()
            return product_type
        
    # As product name is referenced with product id in the orders table
    # we need to retreive the product name in order to print it as product id is un-meaningful
    def get_customer_by_id(self, customer_id):
        customer_search = QSqlQuery()
        customer_search.prepare("SELECT * FROM Customers WHERE customer_id LIKE ?")
        customer_search.bindValue(0, customer_id)
        customer_search.exec_()
        while (customer_search.next()):
            customer_details = {'id' : customer_search.value(0).toString(), 'name' : customer_search.value(1).toString(), \
                                'address' : customer_search.value(2).toString(), 'postcode' : customer_search.value(3).toString(),\
                                'tel' : customer_search.value(4).toString()}
            return customer_details
        
    """ Manager Sign IN Section -----------------------------------------------------------"""
    def check_manager_details(self, account_name, password):
        manager_search = QSqlQuery()
        manager_search.prepare("SELECT * FROM Manager WHERE name LIKE ? and password LIKE ?")
        manager_search.bindValue(0, account_name)
        manager_search.bindValue(1, password)
        manager_search.exec_()
        while (manager_search.next()):
            if (manager_search.isValid()):
                return True
            else:
                return False
            
            
    def update_customer_details(self, customer_id, name, address, postcode, tel):
        update_details = QSqlQuery()
        update_details.prepare("UPDATE Customers SET name = ?, address = ?, postcode = ?, number = ? WHERE customer_id LIKE ?")
        update_details.bindValue(0, name)
        update_details.bindValue(1, address)
        update_details.bindValue(2, postcode)
        update_details.bindValue(3, tel)
        update_details.bindValue(4, customer_id)
        update_details.exec_()
        result = update_details.lastError()
        if (result.type() == QSqlError.NoError):
            QMessageBox.information(None, "Updated!!", "The customers details have been updated!")
        else:
            QMessageBox.critical(None, "Cannot update details!", "Cannot update the customers details, \
            please refine your search for an existing customer")
            
    
    def delete_customer(self, customer_id):
        
        # Customers whom placed orders cannot be deleted until their orders have also been removed
        # therefore remove the order first and then delete the customer
        
        delete_order = QSqlQuery()
        delete_order.prepare("DELETE FROM Orders WHERE customer_id LIKE ?")
        delete_order.bindValue(0, customer_id)
        delete_order.exec_()
        
        delete_customer = QSqlQuery()
        delete_customer.prepare("DELETE FROM Customers WHERE customer_id LIKE ?")
        delete_customer.bindValue(0, customer_id)
        delete_customer.exec_()
        result = delete_customer.lastError()
        if (result.type() == QSqlError.NoError):
            return True 
        else:
            QMessageBox.critical(None, "Cannot Delete Customer!", result.text())
            return False 
        
    def delete_order_by_date(self, date):
        date_exist = False
        check_date = QSqlQuery()
        check_date.prepare("SELECT * FROM Orders WHERE date_of_order LIKE ?")
        check_date.bindValue(0, date)
        check_date.exec_()
        while (check_date.next()):
            if (check_date.isValid()):
                date_exist = True
            else:
                date_exist = False
    
        if (date_exist):
            delete_date = QSqlQuery()
            delete_date.prepare("DELETE FROM Orders WHERE date_of_order LIKE ?")
            delete_date.bindValue(0, date)
            delete_date.exec_()
            result = delete_date.lastError()
            if (result.type() == QSqlError.NoError):
                return True
            else:
                QMessageBox.critical(None, "Cannot Delete Order!", result.text())
                return False 
        else:
            QMessageBox.critical(None, "Cannot remove it", "The date you've specified cannot be found!")
            return False
        
    def delete_all_orders(self):
        delete_all_orders = QSqlQuery()
        delete_all_orders.prepare("DELETE FROM Orders")
        delete_all_orders.exec_()
        result = delete_all_orders.lastError()
        if (result.type() == QSqlError.NoError):
            return True 
        else:
            QMessageBox.critical(None, "Cannot Delete Orders!", result.text())
            return False 