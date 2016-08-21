#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import datetime
import sys

#importo mi modulos
import db.sqlite as dbMy

#metodo principal
def main():
    conn = None
    try:    
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