import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "123",
	database = "members" )		#if any database from the past exist his codes remove them to have a new/better code 

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

mycursor.execute("DROP TABLE students")
mycursor.execute("DROP TABLE lessons")
mycursor.execute("DROP TABLE dr")
mycursor.execute("DROP TABLE admin")
mycursor.execute("DROP TABLE rank")
mycursor.execute("DROP TABLE waitings")
mycursor.execute("DROP TABLE waitingl")
mycursor.execute("DROP TABLE arzesh")
