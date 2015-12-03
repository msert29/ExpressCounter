'''
Created on Dec 3, 2015
Purpose: This class will be the base class which will establish a connection with the local database.
Subclasses which are going to need interaction with the database will firstly need to inherent from this class.
@author: murat

'''
from PyQt4.Qt import QSqlDatabase, QMessageBox
from PyQt4.QtSql import *
import sys


class DatabaseConnection(QSqlDatabase):
    def __init__(self, params):
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("localhost")
        db.setPort(3306)
        db.setDatabaseName("expresscounter")
        db.setUserName("root")
        db.setPassword("express")
        
        if (db.open()==False):     
            QMessageBox.critical(None, "Database Error",
                db.lastError().text())   
        
        query = QSqlQuery()
        query.exec_("""INSERT INTO `products` VALUES('kebab', 'Small Doner', 4.90""")
        print "Here"