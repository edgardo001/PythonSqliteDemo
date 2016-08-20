#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import datetime
import sys

#Metodo que crea las tablas
def createTables(cursor):
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS Caja(id_caj integer primary key autoincrement, empleado_caj TEXT, descripcion_caj TEXT, valor_caj INT, fechaHora_caj datetime)")
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        print("Tablas generadas")

#Metodo que inserta datos
def insertDatos(cursor):
    try:
        cursor.execute("INSERT INTO Caja (empleado_caj, descripcion_caj,valor_caj, fechaHora_caj)VALUES('edgardo','se entregan dinero para taxi', 10000, datetime('now'))")
        cursor.execute("INSERT INTO Caja (empleado_caj, descripcion_caj,valor_caj, fechaHora_caj)VALUES('edgardo','se entregan dinero para taxi', 5000, datetime('now'))")
        cursor.execute("INSERT INTO Caja (empleado_caj, descripcion_caj,valor_caj, fechaHora_caj)VALUES('edgardo','se entregan dinero para taxi', 8000, datetime('now'))")
        cursor.execute("INSERT INTO Caja (empleado_caj, descripcion_caj,valor_caj, fechaHora_caj)VALUES('edgardo','se entregan dinero para taxi', 900, datetime('now'))")    
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        print("Datos insertados")

#metodo principal
def main():
    conn = None
    try:    
        conn = sqlite3.connect('data/sqliteDB.db')
        cursor = conn.cursor()    
        createTables(cursor)
        insertDatos(cursor)
        conn.commit()

    except sqlite3.Error, e:    
        print "Error %s:" % e.args[0]
        sys.exit(1)    
    finally:    
        if conn:
            conn.close()

#ejecuto el metodo principal
main()