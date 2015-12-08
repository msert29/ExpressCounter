'''
Created on Dec 3, 2015
Purpose: This class will be the base class which will establish a connection with the local database.
Subclasses which are going to need interaction with the database will firstly need to inherent from this class.
@author: murat

'''
from PyQt4.Qt import QSqlDatabase, QMessageBox, QSqlQuery
from PyQt4 import QtCore, QtSql
import sys
from PyQt4 import QtGui


class Database(QSqlDatabase):
    def __init__(self):
        super(Database, self).__init__()
        self.Establish_Connection()
        self.query = QSqlQuery() # Will hold CRUD operations to the database
        self.get_kebabs()
       
        self.Get_Items()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #
    # Function : Establish a connection with the local database server.
    #            This function is called prior making querys. It will output an error message on failure of Database connection error.
    #
    #---------------------------------------------------------------------------------------------------------------------------------------------
    def Establish_Connection(self):
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
            print self.query.value(2).toString()
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
    ex = Database()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
    
    
