import curses
import db
from c_defs import my_input
from db import mycursor				#import libraries and files
import classes
from classes import Student
import time
import login

def register(stdscr):
    stdscr.clear()
    flag = True
    while flag:
	c = 0
	stdscr.refresh()
	uss = my_input(stdscr, 2, 0, "Choose Username: ")
	pss = my_input(stdscr, 3, 0, "Choose Password: ")		#getting info from user
	pss2 = my_input(stdscr, 4, 0, "confirm Password: ")
	if pss == pss2:
	    mycursor.execute("SELECT * FROM students")
	    myresult = mycursor.fetchall()
	    for i in myresult:
   	        if i[4] == uss :
		    stdscr.addstr(6, 0, "ALDREADY USE USERACCOUNT TRY AGAIN!")
		    stdscr.refresh()
		    time.sleep(1)
		    stdscr.clear()
		    continue
	    mycursor.execute("SELECT * FROM dr")
	    myresult = mycursor.fetchall()			#checking in database which the user must be unique 
	    for i in myresult:
   	        if i[4] == uss :
		    stdscr.addstr(6, 0, "ALDREADY USE USERACCOUNT TRY AGAIN!")
		    stdscr.refresh()
		    time.sleep(1)
		    stdscr.clear()
		    continue
	else:
		stdscr.addstr(6, 0, "password Does not match!")
		stdscr.refresh()
	        time.sleep(1)
		stdscr.addstr(7, 0, "Want to exit? Y/N ")
		key = stdscr.getch()
		if str(chr(key)) == "Y" or str(chr(key)) == "y":
		    time.sleep(1)
		    exit()
		elif str(chr(key)) == "N" or str(chr(key)) == "n" :
	            stdscr.clear()
		    continue
		    
		else:
			pass
	
	sqlformula6 = "INSERT INTO waitings(user, pass, confirmed) VALUES (%s, %s, %s)"
	mycursor.execute(sqlformula6, (uss, pss, "No"))
	db.mydb.commit()
        stdscr.addstr(6, 0, "Done! You Registered Successfully")		#storing in database
        stdscr.addstr(7, 0, "wait for your accept from admin!")
        stdscr.refresh()
        time.sleep(2)
        exit()
