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
        cursor.execute("INSERT INTO Caja (empleado_caj, descripcion_caj,valor_caj, fechaHora_caj)VALUES('carolina','se entregan dinero para taxi', 10000, datetime('now'))")
        cursor.execute("INSERT INTO Caja (empleado_caj, descripcion_caj,valor_caj, fechaHora_caj)VALUES('carolina','se entregan dinero para taxi', 5000, datetime('now'))")
        cursor.execute("INSERT INTO Caja (empleado_caj, descripcion_caj,valor_caj, fechaHora_caj)VALUES('carolina','se entregan dinero para taxi', 8000, datetime('now'))")
        cursor.execute("INSERT INTO Caja (empleado_caj, descripcion_caj,valor_caj, fechaHora_caj)VALUES('carolina','se entregan dinero para taxi', 900, datetime('now'))")    
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        print("Datos insertados")

#Metodo que obtiene los datos
def selectDatos(cursor):
    try:
        cursor.execute("SELECT * FROM Caja")
        rows = cursor.fetchall()
        for row in rows:
            print row

    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        print("Datos dentro de la BD actualmente")        

#Metodo que borra datos de la BD
def deleteDatos(cursor):
    try:
        cursor.execute("delete from Caja where Caja.empleado_caj = 'edgardo'")
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        print("Datos dentro de la BD actualmente")  

#Metodo encargado de actualizar datos de la bd
def updateDatos(cursor):
    try:
        cursor.execute("update caja set empleado_caj = 'Carolina Prado' where empleado_caj = 'carolina'")
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        print("Datos Actualizados")

#metodo principal
def main():
    conn = None
    try:    
        conn = sqlite3.connect('data/sqliteDB.db')
        cursor = conn.cursor()    
        createTables(cursor)
        insertDatos(cursor)
        deleteDatos(cursor)
        updateDatos(cursor)
        conn.commit()
        
        selectDatos(cursor)

    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)    
    finally:    
        if conn:
            conn.close()

#ejecuto el metodo principal
main()