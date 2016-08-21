#!/usr/bin/python
# -*- coding: utf-8 -*-

#importo modulos de python
import sqlite3
import datetime
import sys

#importo modulos de terceros
from PyQt4 import QtCore, QtGui, uic

#importo mi modulos
import db.sqlite as dbMy

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("UI/mainwindow.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

#metodo principal
def main():
    conn = None
    try:    
        app = QtGui.QApplication(sys.argv)
        MyWindow = MyWindowClass(None)
        MyWindow.show()
        app.exec_()

        conn = sqlite3.connect('data/sqliteDB.db')
        cursor = conn.cursor()    
        
        dbMy.createTables(cursor)
        dbMy.insertDatos(cursor)
        dbMy.deleteDatos(cursor)
        dbMy.updateDatos(cursor)
        
        conn.commit()
        
        dbMy.selectDatos(cursor)

    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)    
    finally:    
        if conn:
            conn.close()

#ejecuto el metodo principal
main()