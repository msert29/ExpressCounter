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
        self.establish_connection()
        self.query = QSqlQuery() # Will hold CRUD operations to the database
        #self.get_kebabs()
       
        self.Get_Items()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #
    # Function : Establish a connection with the local database server.
    #            This function is called prior making querys. It will output an error message on failure of Database connection error.
    #
    #---------------------------------------------------------------------------------------------------------------------------------------------
    def establish_connection(self):
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("localhost")
        db.setDatabaseName("expresscounter")
        db.setUserName("root")
        db.setPassword("express")
        if (db.open()==False):     
            QMessageBox.critical(None, "Database Error", db.lastError().text())   


    def Get_Items(self):
        self.query.exec_("""SELECT * FROM `Items`""")
        i = 0;
        while (self.query.next()):
            print self.query.value(1).toString()
            i += 1
        #query.exec_("""INSERT INTO `expresscounter`.`products` (`id`, `type`, `name`, `price`) VALUES (NULL, 'kebab', 'Small Doner', '4.30');""")
        
    def get_pizzas(self):
        self.query.exec_("""SELECT * FROM `Items` WHERE `type` LIKE `pizza` """)
        return self.query
    
    def get_burgers(self):
        self.query.exec_("""SELECT * FROM `Items` WHERE `type` LIKE `burger` """)
        return self.query
    
    def get_kebabs(self):
        query = QSqlQuery()
        query.exec_("""SELECT * FROM `Items` WHERE `type` LIKE 'Kebab'""")
        while (query.next()):
            print query.value(2).toString()
            print "here"
        
    def get_other(self):
        self.query.exec_("""SELECT * FROM `Items` WHERE `type` LIKE `other` """)
        return self.query   
    
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Model_Database()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
    
    
