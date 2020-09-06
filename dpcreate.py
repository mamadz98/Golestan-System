import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "123" )
							#create database and using acursor/pointer to handeling the database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE members")

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "123",
	database = "members" )

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE students (num INTEGER(10),name VARCHAR(255),year INTEGER(10), field VARCHAR(255), user VARCHAR(255), pass VARCHAR(255))")
mycursor.execute("CREATE TABLE dr (num INTEGER(10),name VARCHAR(255),year INTEGER(10), field VARCHAR(255), user VARCHAR(255), pass VARCHAR(255))")
mycursor.execute("CREATE TABLE admin (num INTEGER(10),name VARCHAR(255),year INTEGER(10), field VARCHAR(255), user VARCHAR(255), pass VARCHAR(255))")
mycursor.execute("CREATE TABLE rank (user VARCHAR(255), lesson VARCHAR(255), field VARCHAR(255),ostad VARCHAR(255),mark INTEGER(10))")
mycursor.execute("CREATE TABLE lessons (leson VARCHAR(255), teacher VARCHAR(255))")					#creating tables
mycursor.execute("CREATE TABLE waitings (user VARCHAR(255), pass VARCHAR(255), confirmed VARCHAR(255))")
mycursor.execute("CREATE TABLE waitingl (lesson VARCHAR(255), teacher VARCHAR(255), confirmed VARCHAR(255))")
mycursor.execute("CREATE TABLE arzesh (user VARCHAR(255), teacher VARCHAR(255), mark INTEGER(10))")
sqlformula = "INSERT INTO students(num, name, year, field, user, pass) VALUES (%s, %s, %s, %s, %s, %s)"
sqlformula2 = "INSERT INTO dr(num, name, year, field, user, pass) VALUES (%s, %s, %s, %s, %s, %s)"
sqlformula3 = "INSERT INTO admin(num, name, year, field, user, pass) VALUES (%s, %s, %s, %s, %s, %s)"
sqlformula4 = "INSERT INTO rank(user, lesson, field, ostad, mark) VALUES (%s, %s, %s, %s, %s)"
sqlformula5 = "INSERT INTO lessons(leson, teacher) VALUES (%s, %s)"

students = [(1, "mahdi mazloum", 1397, "math", "mzlm","12345"),
	    (2, "ali mohammadpour", 1396, "statics", "sas", "asw1"),
	    (3, "masoud shohani", 1398, "math", "hmsj", "1235"),
	    (4, "hamed marvi", 1394, "cs", "hmdmr", "6789")]

lessons = [("an", " asadi      "),
	    ("bp", " kheradpishe"),
	    ("ap", " khorasani  "),
	    ("fa", " molayi     "),
	    ("ca", " rokni      "), 					#datas
	    ("al", " derafshe   "), 
	    ("di", " khaje      ")]

masters = [(1, " asadi      ", 1397, "math", "mzlmw","1d2345"),
	    (2, " molayi     ", 1396, "statics", "ssas", "adsw1"),
	    (3, " derafshe   ", 1398, "math", "hmsaj", "123d5"),
	    (4, " khorasani  ", 1394, "cs", "hmdmar", "678f9")]

ranks = [("mzlm", "bp", "math", " kheradpishe", 19),
	  ("sas", "bp", "statics", " kheradpishe", 14)]

admins =(1, "yasemi", 1365, "sd", "12345785", "fsfsddf")




mycursor.executemany(sqlformula, students)
mycursor.executemany(sqlformula2, masters)
mycursor.execute(sqlformula3, admins)					#adding datas to tables
mycursor.executemany(sqlformula4, ranks)
mycursor.executemany(sqlformula5, lessons)
mydb.commit()			#saving the changes
