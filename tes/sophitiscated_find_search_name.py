
import sqlite3

import pathlib
import os

def startconnection():

    sql = """
    CREATE TABLE IF NOT EXISTS 'Contoh' (
    'No' INT,
    'Nama Kode Barang' TEXT
    )
    """

    cursor.execute(sql)
    # connect.close()

def query():
    path_of_database = pathlib.Path.cwd()/"PySDS/AppsSDS/db/riasec.db"
    print (path_of_database)
    connect = sqlite3.connect(path_of_database)
   
    cursor = connect.cursor()
    sql = """
    SELECT * FROM 'fileedit'
    """
    cursor.execute(sql)
    data = []
    datas = cursor.fetchall()

    for x in datas:
        data.append(x[0])
    
    connect.close()

    return data
# data = ["Arif","Ahmad","Asep","Ajang","Ajun","Alek","Bambang","Bayu","Baim","Beni","Beben","Berlin","Bedu"]

def goapps():


    # startconnection()
    data = query()
    finish = "Y"

    while finish == "Y" or finish == "y":
        carinama = input("Cari nama disini\n")
        y = len(carinama)
        data_search = []
        for x in range(len(data)):
            if carinama.upper() == data[x][0:y].upper(): 
                print (data[x])
                data_search.append(data[x])
        # print (data_search)
        finish = input("Lanjut ?(y/n)\n")
    
    return data_search

if __name__ == "__main__":
    os.chdir("..")
    # goapps()    
    print (goapps())
    pass