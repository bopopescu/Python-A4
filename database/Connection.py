from database.Credentials import *
import mysql.connector

mydb = mysql.connector.connect(host=host,
                               user=user,
                               password=password,
                               database=database)
mycursor = mydb.cursor()