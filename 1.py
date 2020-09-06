import sys,os
import curses
import prints                              #adding libraries and files
import login
import register
import time

def main(stdscr):
    
    curses.curs_set(0)
    curses.mousemask(1)                                         #activing the mouse and set a color 
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)


    stdscr.addstr(0, 0, prints.print_column())
    stdscr.addstr(1, 0, prints.print_row())
    stdscr.addstr(2, 0, prints.print_row())                 #print main menu
    stdscr.addstr(3, 0, prints.print_time())
    stdscr.addstr(4, 0, prints.print_row())
    stdscr.addstr(5, 0, prints.print_row())
    stdscr.addstr(6, 0, prints.print_column())
    stdscr.addstr(11, 0, "Login")			#getting the login/register from the shell
    stdscr.addstr(12, 0, "Register")
    tss = "click on Login or Register OR"
    tss1 = "write L/l for login or R/r for Register: "
    stdscr.addstr(8, 0, tss)
    stdscr.addstr(9, 0, tss1)
    stdscr.addstr(7, 0, "press Q/q for exit")

    while True :
	stdscr.refresh()
	key = stdscr.getch()								#handeling keyboard and mouse
	if key != curses.KEY_MOUSE :
	    stdscr.addstr(9, len(tss1)+1, str(chr(key)))

	    if str(chr(key)) == "l" or str(chr(key)) == "L":
	        stdscr.attron(curses.color_pair(1))
	        stdscr.addstr(11, 0, "Login")					#define each work for each character and making them red when clicking or typing
	        stdscr.attroff(curses.color_pair(1))
	        stdscr.refresh()
	        stdscr.clear()
		time.sleep(1)
	        login.login(stdscr)

	    elif str(chr(key)) == "r" or str(chr(key)) == "R":
	        stdscr.attron(curses.color_pair(1))
	        stdscr.addstr(12, 0, "Register")
	        stdscr.attroff(curses.color_pair(1))
	        stdscr.refresh()
	        stdscr.clear()
		time.sleep(1)
	        register.register(stdscr)

	    elif str(chr(key)) == "q" or str(chr(key)) == "Q":
		stdscr.clear()
		stdscr.refresh()
		stdscr.attron(curses.color_pair(1))
		stdscr.addstr(9, 0, "Want to Exit? Y/N")
		stdscr.attroff(curses.color_pair(1))
		time.sleep(1)
		key = stdscr.getch()
		if str(chr(key)) == "Y" or str(chr(key)) == "y":
		    time.sleep(1)
		    exit()
		elif str(chr(key)) == "N" or str(chr(key)) == "n" :
		    stdscr.clear()
		    curses.curs_set(0)
		    curses.mousemask(1)
		    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
		    stdscr.addstr(0, 0, prints.print_column())
		    stdscr.addstr(1, 0, prints.print_row())
		    stdscr.addstr(2, 0, prints.print_row())
		    stdscr.addstr(3, 0, prints.print_time())
		    stdscr.addstr(4, 0, prints.print_row())
		    stdscr.addstr(5, 0, prints.print_row())
		    stdscr.addstr(6, 0, prints.print_column())
		    stdscr.addstr(11, 0, "Login")
		    stdscr.addstr(12, 0, "Register")
		    tss = "click on Login or Register OR"
		    tss1 = "write L/l for login or R/r for Register: "
		    stdscr.addstr(8, 0, tss)
		    stdscr.addstr(9, 0, tss1)
		    stdscr.refresh()
		    continue

	
	elif key == curses.KEY_MOUSE :
	    _, x, y, _, _ = curses.getmouse()
	    
	    if y == 11 and x in range(5):
		stdscr.attron(curses.color_pair(1))
		stdscr.addstr(11, 0, "Login")
		stdscr.attroff(curses.color_pair(1))
		stdscr.refresh()
		time.sleep(1)						#mouse defining
		stdscr.clear()
		login.login(stdscr)
		
	    if y == 12 and x in range(8):
		stdscr.attron(curses.color_pair(1))
		stdscr.addstr(12, 0, "Register")
		stdscr.attroff(curses.color_pair(1))	
		stdscr.refresh()
		time.sleep(1)
		stdscr.clear()	
		register.register(stdscr)

    stdscr.getch()

curses.wrapper(main)
