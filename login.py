import curses
import db
from c_defs import my_input
from db import mycursor				#importing nesseseries
import classes
from classes import Student
from classes import Professor
from classes import Admin
import time

def login(stdscr):
    stdscr.clear()
    flag = True
    while flag:
	stdscr.clear()
	uss = my_input(stdscr, 2, 0, "Enter Username: ")
	pss = my_input(stdscr, 3, 0, "Enter Password: ")
	x = 0
	stdscr.refresh()
	
	mycursor.execute("SELECT * FROM students")
	myresult = mycursor.fetchall()
	for i in myresult:								#entering to login from main for each user is diffrent
   	    if i[4] == uss :
		if i[5] == pss:
		    stdscr.addstr(5, 0, "Login successfully!")
		    stdscr.addstr(6, 0, "Hello %s!" %i[1])
		    stdscr.refresh()
		    time.sleep(1)
		    x +=1
		    flag = False
		    menu_s(stdscr, i)

	
		else:
	    	    stdscr.addstr(5, 0, "Your password is incorrect!/n Try again")
		    time.sleep(1)
	    	    stdscr.refresh()
		    continue
	        
	
	
	mycursor.execute("SELECT * FROM dr")
	myresult = mycursor.fetchall()
	for i in myresult:
   	    if i[4] == uss :
		if i[5] == pss:
		    stdscr.addstr(5, 0, "Login successfully!")
		    stdscr.addstr(6, 0, "Hello %s!" %i[1])
		    stdscr.refresh()
		    x +=1
		    time.sleep(1)
		    flag = False
		    menu_l(stdscr, i)
	
		else:
	    	    stdscr.addstr(5, 0, "Your password is incorrect!/n Try again")
		    time.sleep(1)
	    	    stdscr.refresh()
	            continue

	mycursor.execute("SELECT * FROM admin")
	myresult = mycursor.fetchall()
	for i in myresult:
   	    if i[4] == uss :
		if i[5] == pss:
		    stdscr.addstr(5, 0, "Login successfully!")
		    stdscr.addstr(6, 0, "Hello %s!" %i[1])
		    stdscr.refresh()
		    time.sleep(1)
		    x +=1
		    flag = False
		    menu_A(stdscr, i)

	
		else:
	    	    stdscr.addstr(5, 0, "Your password is incorrect!/n Try again")
		    time.sleep(1)
	    	    stdscr.refresh()
		    continue
	    else:
		if x == 0:
		    stdscr.addstr(5, 0, "Your username is incorrect!")
		    stdscr.addstr(6, 0, "Continue? Y/N ")
		    stdscr.refresh()
		    key = stdscr.getch()
		    if key != curses.KEY_MOUSE :
		        if str(chr(key)) == "Y" or str(chr(key)) == "y":
			    stdscr.addstr(1, 0, "Your username is incorrect!")
			    stdscr.refresh()
			    time.sleep(1)
			    stdscr.clear()
			    x+=1
		        elif str(chr(key)) == "N" or str(chr(key)) == "n" :
			    time.sleep(1)
		            exit()

def menu_s(stdscr, student):
    stdscr.clear()
    stdnt = Student(student)		#making a instance of student
    mycursor.execute("SELECT * FROM waitings")
    myresult = mycursor.fetchall()
    for i in myresult:
	if i[0] == stdnt.user and i[2] == "Yes":
	    stdscr.addstr(0, 0, "%s, Your a new user you should complite your data!"%(i[0]))
	    uss = stdnt.user
	    name = my_input(stdscr, 2, 0, "Write your full name : ")
	    year = my_input(stdscr, 3, 0, "Write your incoming year : ")
	    field = my_input(stdscr, 4, 0, "Write your field : ")
	    sql = "UPDATE students SET name = %s WHERE user = %s"
            val = (name, uss)					#in this part if someone register must complete requirements for database/tables then goes to main menu
            mycursor.execute(sql, val)
	    sql = "UPDATE students SET year = %s WHERE user = %s"				#student menu
            val = (int(year), uss)
            mycursor.execute(sql, val)
	    sql = "UPDATE students SET field = %s WHERE user = %s"
            val = (field, uss)
            mycursor.execute(sql, val)
	    stdnt.name = name
	    stdnt.year = year
	    stdnt.field = field
	    sql = """DELETE FROM waitings WHERE user = %s"""
            mycursor.execute(sql, (uss,))
	    stdscr.addstr(8, 0, "Done!")
	    time.sleep(1)
    	    db.mydb.commit()

    stdscr.clear()
    stdscr.addstr(0, 0, "+----------------------------------+")
    stdscr.addstr(1, 0, "|         @Steudent Menu@          |")
    stdscr.addstr(2, 0, "+----------------------------------+")
    stdscr.addstr(3, 0, "|         Doros Akhz Shode         |")
    stdscr.addstr(4, 0, "+----------------------------------+")
    stdscr.addstr(5, 0, "|             Karname              |")
    stdscr.addstr(6, 0, "+----------------------------------+")
    stdscr.addstr(7, 0, "|          Entekhab vahed          |")
    stdscr.addstr(8, 0, "+----------------------------------+")    #main menu for student which suppport mouse
    stdscr.addstr(9, 0, "|         Arzeshyabi Asatid        |")
    stdscr.addstr(10, 0, "+----------------------------------+")
    stdscr.addstr(11, 0, "|         Virayesh etelaat         |")
    stdscr.addstr(12, 0, "+----------------------------------+")
    stdscr.addstr(13, 0, "|         password change          |")
    stdscr.addstr(14, 0, "+----------------------------------+")
    stdscr.addstr(15, 0, "|               Exit               |")
    stdscr.addstr(16, 0, "+----------------------------------+")
    stdscr.addstr(18, 0, "D/d for doros akhz shode")
    stdscr.addstr(18, 27, "K/k for karname")
    stdscr.addstr(19, 0, "E/e for Entekhab Vahed")
    stdscr.addstr(19, 27, "A/a for Arzeshyabi Asatid")
    stdscr.addstr(20, 0, "V/v for Virayesh Etelaat")
    stdscr.addstr(20, 27, "P/p for Password Change")
    stdscr.addstr(21, 0, "Q/q for Exit")
    stdscr.refresh()


    key = stdscr.getch()
    if key != curses.KEY_MOUSE :
        if str(chr(key)) == "D" or str(chr(key)) == "d":
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(18, 0, "D/d for doros akhz shode")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(2)
	    stdscr.clear()
	    lst = stdnt.slesson()
	    cx = len(lst)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+------+-------------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|  Doros Akhz Shode  |")
                cnt = 2
	        stdscr.addstr(cnt, 0, "+------+-------------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  |%s |" %(i[0],i[1]))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+------+-------------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|     page %d of %d    |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+------+-------------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_s(stdscr, stdnt.student)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst)
            call(stdscr, ox, qx, zx, ux, lst)
	
	elif str(chr(key)) == "K" or str(chr(key)) == "k":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(18, 27, "K/k for karname")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(2)
	    stdscr.clear()
	    lst = stdnt.grade()
	    cx = len(lst)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+------+-------------+-------+------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|class |    Master   | Field | Rank |")
                cnt = 2
	        stdscr.addstr(cnt, 0, "+------+-------------+-------+------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  |%s | %s  |  %s  |" %(i[0],i[2],i[1],i[3]))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+------+-------------+-------+------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|             page %d of %d           |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+------+-------------+-------+------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_s(stdscr, stdnt.student)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst)
            call(stdscr, ox, qx, zx, ux, lst)
		
        

	elif str(chr(key)) == "E" or str(chr(key)) == "e":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(19, 0, "E/e for Entekhab Vahed")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(2)
	    stdscr.clear()
	    lst = []
	    ls = []
	    mycursor.execute("SELECT * FROM lessons")
            myresult = mycursor.fetchall()
            for i in myresult:
                ls.append(i[0])
	    cnt = 24
	    stdscr.addstr(2, 0, "The Available lessons :")
	    stdscr.refresh()
	    for i in ls:
	        stdscr.addstr(2, cnt, "%s/" %(i))
	        cnt += 4
            stdscr.refresh()
	    ts = "choose a lesson :"
	    key = my_input(stdscr, 3, 0, ts)
            for i in myresult:
                if key == i[0]:
                   lst.append(i[1])
            cnt = 24
	    stdscr.addstr(4, 0, "The Available masters :")
            for i in lst:
	        stdscr.addstr(4, cnt, "%s" %(i))
	        cnt += 13
	    key2 = my_input(stdscr, 5, 0, "choose master :")
	    a = len(key2)
	    b = 11-a
	    k= " %s" %key2 + " "*b
	    mycursor.execute("SELECT * FROM rank")
            myresult = mycursor.fetchall()
            for i in myresult:
		if i[1] == key and i[3] == k:
		    stdscr.addstr(6, 0, "You have already taken this lesson whith this master!")
		    stdscr.refresh()
            	    time.sleep(2)
	    	    stdscr.clear()
                    menu_s(stdscr, stdnt.student)
            lss = (student[4], key, student[3], k, 00)
            sqlformula = "INSERT INTO rank(user, lesson, field, ostad, mark) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sqlformula, lss)
	    stdscr.addstr(6, 0, "Succssfully added!")
	    stdscr.addstr(7, 0, "Lesson &%s& Master &%s&!"%(key,k))
	    db.mydb.commit()
	    stdscr.refresh()
            time.sleep(2)
	    stdscr.clear()
            menu_s(stdscr, stdnt.student)
		
	elif str(chr(key)) == "A" or str(chr(key)) == "a":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(19, 27, "A/a for Arzeshyabi Asatid")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(2)
	    stdscr.clear()
            lst = stdnt.slesson()
            cnt = 1
            for i in lst:
                stdscr.addstr(cnt, 0, "%s" %(i[1]))
                cnt += 1 
            teacher = my_input(stdscr, cnt+1, 0, "write your teacher: ")
	    a = len(teacher)
	    b = 11-a
	    k= " %s" %teacher + " "*b
            mark = my_input(stdscr, cnt+2, 0, "write your mark: ")
	    mycursor.execute("SELECT * FROM arzesh")
            myresult = mycursor.fetchall()
            for i in myresult:
		if i[1] == k and i[0] == stdnt.user:
		    stdscr.addstr(7, 0, "You have already evaluate this master!")
		    stdscr.refresh()
            	    time.sleep(2)
	    	    stdscr.clear()
                    menu_s(stdscr, stdnt.student)
            if stdnt.evaluation(k, mark) :
                stdscr.addstr(cnt+3, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
            menu_s(stdscr, stdnt.student)


	elif str(chr(key)) == "V" or str(chr(key)) == "v":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(20, 0, "V/v for Virayesh Etelaat")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(2)
	    stdscr.clear()
            uss = my_input(stdscr, 2, 0, "Write your new username: ")
	    if stdnt.edition(uss) :
                stdscr.addstr(3, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
	    else:
		stdscr.addstr(4, 0, "username already taken!")	
		stdscr.refresh()
		time.sleep(2)
            menu_s(stdscr, stdnt.student)

		
        elif str(chr(key)) == "P" or str(chr(key)) == "p":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(20, 27, "P/p for Password Change")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(2)
	    stdscr.clear()
            pss = my_input(stdscr, 2, 0, "Write your new password : ")
            pss2 = my_input(stdscr, 3, 0, "confirm your new password : ")
            if pss == pss2 :
                stdnt.change_password(pss)
                stdscr.addstr(4, 0, "Done!")
                stdscr.refresh()
            time.sleep(2)
            menu_s(stdscr, stdnt.student)



	elif str(chr(key)) == "q" or str(chr(key)) == "Q":
		stdscr.clear()
		stdscr.refresh()
		stdscr.attron(curses.color_pair(1))
		stdscr.addstr(21, 0, "Q/q for Exit")
		stdscr.addstr(22, 0, "Want to Exit? Y/N")
		stdscr.attroff(curses.color_pair(1))
		time.sleep(1)
		key = stdscr.getch()
		if str(chr(key)) == "Y" or str(chr(key)) == "y":
		    time.sleep(1)
		    exit()
	else:
    	    menu_s(stdscr, stdnt.student)



    elif key == curses.KEY_MOUSE :
	_, x, y, _, _ = curses.getmouse()
	    
	if y == 3 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(3, 0, "|         Doros Akhz Shode         |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)					#enterin to submenu and using the built in defs of class and perinting 
	    stdscr.clear()
	    lst = stdnt.slesson()
	    cx = len(lst)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+------+-------------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|  Doros Akhz Shode  |")
                cnt = 2
	        stdscr.addstr(cnt, 0, "+------+-------------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  |%s |" %(i[0],i[1]))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+------+-------------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|     page %d of %d    |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+------+-------------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_s(stdscr, stdnt.student)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst)
            call(stdscr, ox, qx, zx, ux, lst)

	if y == 5 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(5, 0, "|             Karname              |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
	    lst = stdnt.grade()
	    cx = len(lst)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+------+-------------+-------+------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|class |    Master   | Field | Rank |")
                cnt = 2
	        stdscr.addstr(cnt, 0, "+------+-------------+-------+------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  |%s | %s  |  %s  |" %(i[0],i[2],i[1],i[3]))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+------+-------------+-------+------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|             page %d of %d           |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+------+-------------+-------+------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_s(stdscr, stdnt.student)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst)
            call(stdscr, ox, qx, zx, ux, lst)


	if y == 7 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(7, 0, "|          Entekhab vahed          |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
	    lst = []
	    ls = []
	    mycursor.execute("SELECT * FROM lessons")
            myresult = mycursor.fetchall()
            for i in myresult:
                ls.append(i[0])
	    cnt = 24
	    stdscr.addstr(2, 0, "The Available lessons :")
	    stdscr.refresh()
	    for i in ls:
	        stdscr.addstr(2, cnt, "%s/" %(i))
	        cnt += 4
            stdscr.refresh()
	    ts = "choose a lesson :"
	    key = my_input(stdscr, 3, 0, ts)
            for i in myresult:
                if key == i[0]:
                   lst.append(i[1])
            cnt = 24
	    stdscr.addstr(4, 0, "The Available masters :")
            for i in lst:
	        stdscr.addstr(4, cnt, "%s" %(i))
	        cnt += 13
	    key2 = my_input(stdscr, 5, 0, "choose master :")
	    a = len(key2)
	    b = 11-a
	    k= " %s" %key2 + " "*b
	    mycursor.execute("SELECT * FROM rank")
            myresult = mycursor.fetchall()
            for i in myresult:
		if i[1] == key and i[3] == k:
		    stdscr.addstr(6, 0, "You have already taken this lesson whith this master!")
		    stdscr.refresh()
            	    time.sleep(2)
	    	    stdscr.clear()
                    menu_s(stdscr, stdnt.student)
            lss = (student[4], key, student[3], k, 00)
            sqlformula = "INSERT INTO rank(user, lesson, field, ostad, mark) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sqlformula, lss)
	    stdscr.addstr(6, 0, "Succssfully added!")
	    stdscr.addstr(7, 0, "Lesson &%s& Master &%s&!"%(key,k))
	    db.mydb.commit()
	    stdscr.refresh()
            time.sleep(2)
	    stdscr.clear()
            menu_s(stdscr, stdnt.student)
   
	if y == 9 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(9, 0, "|         Arzeshyabi Asatid        |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            lst = stdnt.slesson()
            cnt = 1
            for i in lst:
                stdscr.addstr(cnt, 0, "%s" %(i[1]))
                cnt += 1 
            teacher = my_input(stdscr, cnt+1, 0, "write your teacher: ")
	    a = len(teacher)
	    b = 11-a
	    k= " %s" %teacher + " "*b
            mark = my_input(stdscr, cnt+2, 0, "write your mark: ")
	    mycursor.execute("SELECT * FROM arzesh")
            myresult = mycursor.fetchall()
            for i in myresult:
		if i[1] == k and i[0] == stdnt.user:
		    stdscr.addstr(7, 0, "You have already evaluate this master!")
		    stdscr.refresh()
            	    time.sleep(2)
	    	    stdscr.clear()
                    menu_s(stdscr, stdnt.student)
            if stdnt.evaluation(k, mark) :
                stdscr.addstr(cnt+3, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
            menu_s(stdscr, stdnt.student)


	if y == 11 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(11, 0, "|         Virayesh etelaat         |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
    	    time.sleep(1)
    	    stdscr.clear()
            uss = my_input(stdscr, 2, 0, "Write your new username: ")
	    if stdnt.edition(uss) :
                stdscr.addstr(3, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
	    else:
		stdscr.addstr(4, 0, "username already taken!")	
		stdscr.refresh()
		time.sleep(2)
            menu_s(stdscr, stdnt.student)
            
        if y == 13 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(13, 0, "|         password change          |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            pss = my_input(stdscr, 2, 0, "Write your new password : ")
            pss2 = my_input(stdscr, 3, 0, "confirm your new password : ")
            if pss == pss2 :
                stdnt.change_password(pss)
                stdscr.addstr(4, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
            menu_s(stdscr, stdnt.student)

        if y == 15 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(15, 0, "|               Exit               |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdnt.exit()
	
	else:
	    menu_s(stdscr, stdnt.student)
	


def menu_l(stdscr, teacher):
    tcher = Professor(teacher)
    stdscr.clear()
    stdscr.addstr(0, 0, "+----------------------------------+")
    stdscr.addstr(1, 0, "|         @Professor Menu@         |")
    stdscr.addstr(2, 0, "+----------------------------------+")
    stdscr.addstr(3, 0, "|            My lessons            |")
    stdscr.addstr(4, 0, "+----------------------------------+")
    stdscr.addstr(5, 0, "|            My Students           |")
    stdscr.addstr(6, 0, "+----------------------------------+")
    stdscr.addstr(7, 0, "|             Erae Dars            |")
    stdscr.addstr(8, 0, "+----------------------------------+")    	#main menu for master which suppport mouse
    stdscr.addstr(9, 0, "|           Record numbers         |")
    stdscr.addstr(10, 0, "+----------------------------------+")
    stdscr.addstr(11, 0, "|         Virayesh etelaat         |")
    stdscr.addstr(12, 0, "+----------------------------------+")
    stdscr.addstr(13, 0, "|         password change          |")
    stdscr.addstr(14, 0, "+----------------------------------+")
    stdscr.addstr(15, 0, "|               Exit               |")
    stdscr.addstr(16, 0, "+----------------------------------+")
    stdscr.addstr(18, 0, "D/d for My lessons")
    stdscr.addstr(18, 27, "K/k for My Students")
    stdscr.addstr(19, 0, "E/e for Erae Dars")
    stdscr.addstr(19, 27, "A/a for Record numbers")
    stdscr.addstr(20, 0, "V/v for Virayesh Etelaat")
    stdscr.addstr(20, 27, "P/p for Password Change")
    stdscr.addstr(21, 0, "Q/q for Exit")
    
    stdscr.refresh()


    key = stdscr.getch()
    if key != curses.KEY_MOUSE :
	if str(chr(key)) == "D" or str(chr(key)) == "d":
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(18, 0, "D/d for My lessons")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
	    lst = tcher.plesson()						
	    cx = len(lst)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+------+-------------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|      My lessons    |")
                cnt = 2
	        stdscr.addstr(cnt, 0, "+------+-------------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  |%s |" %(i[0], i[1]))			#enterin to submenu and using the built in defs of class and perinting 
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+------+-------------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|    page %d of %d     |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+------+-------------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_l(stdscr, tcher.teacher)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst)
            call(stdscr, ox, qx, zx, ux, lst)


	elif str(chr(key)) == "K" or str(chr(key)) == "k":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(18, 27, "K/k for My Students")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            mycursor.execute("SELECT * FROM lessons")
            myresult = mycursor.fetchall()
            lst2 = []
	    w = "Your lessons: "
	    cnt = len(w)
            for i in myresult:
		if tcher.name == i[1]:
                	lst2.append(i[0])
	    stdscr.addstr(2, 0, "%s" %w)
            for i in lst2:
                stdscr.addstr(2, cnt, "%s" %i)
                cnt += 3
            lsen = my_input(stdscr, 3, 0, "Write your lesson : ")
            ls = tcher.studen()
            lst3 = []
            for i in ls:
                if i[1] == lsen:
                    lst3.append(i)
	    stdscr.clear()
	    cx = len(lst3)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+--------+------+--------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|      students in %s    |" %lsen)
                cnt = 2
	        stdscr.addstr(cnt, 0, "+--------+------+--------+")
	        cnt = 3
                stdscr.addstr(cnt, 0, "|  user  |lesson| field  |")
                cnt = 4
	        stdscr.addstr(cnt, 0, "+--------+------+--------+")
	        cnt = 5
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  |  %s  |  %s  |" %(i[0],i[1],i[2]))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+--------+------+--------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|      page %d of %d       |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+--------+------+--------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_l(stdscr, tcher.teacher)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst3)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
                            num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst3)
            call(stdscr, ox, qx, zx, ux, lst3)

            

	elif str(chr(key)) == "E" or str(chr(key)) == "e":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(19, 0, "E/e for Erae Dars")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
            time.sleep(1)
	    stdscr.clear()
            lsen = my_input(stdscr, 2, 0, "Write your lesson (in two digits like ---> analyses == an): ")
	    mycursor.execute("SELECT * FROM lessons")
	    myresult = mycursor.fetchall()
	    done = True
	    for i in myresult:
		if tcher.name == i[1] and lsen == i[0]:
		    stdscr.addstr(3, 0, "You have aldready propousing this course!!")
		    stdscr.refresh()
            	    time.sleep(2)
		    done = False
	    if done:
	    	if tcher.erae(lsen):
                	stdscr.addstr(4, 0, "Dars shoma b modiriat erja dade shod!")
                	stdscr.addstr(5, 0, "Darsorat tayid dar menu my lesson ghabel dastrasi ast!")
			stdscr.refresh()
            		time.sleep(2)
            		stdscr.clear()
            menu_l(stdscr, tcher.teacher)
   
	elif str(chr(key)) == "A" or str(chr(key)) == "a":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(19, 27, "A/a for Record numbers")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            lst = tcher.plesson()
            cnt = 0
            for i in lst:
                stdscr.addstr(2, cnt, "%s" %i[0])
                cnt += 3
            les = my_input(stdscr, 3, 0, "write your lesson: ")
            lst2 = tcher.studen()
            lst3 = []
            for i in lst2:
                if i[1] == les :
                    lst3.append(i)
            cn = 5
            for i in lst3:
                stdscr.addstr(cn, 0, "%s" %i[0])
                cn +=1
            uss = my_input(stdscr, cn+1, 0, "Write your student username: ")
            mark = my_input(stdscr, cn+2, 0, "Write student mark: ")
            tcher.grade_s(les, uss, mark)
            stdscr.addstr(cn+3, 0, "Done!")
	    stdscr.refresh()
            time.sleep(2)
            menu_l(stdscr, tcher.teacher)

	    
        elif str(chr(key)) == "V" or str(chr(key)) == "v":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(20, 0, "V/v for Virayesh Etelaat")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            uss = my_input(stdscr, 2, 0, "Write your new username: ")
	    if tcher.edition(uss) :
                stdscr.addstr(3, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
            menu_l(stdscr, tcher.teacher)
            
        elif str(chr(key)) == "P" or str(chr(key)) == "p":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(20, 27, "P/p for Password Change")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            pss = my_input(stdscr, 2, 0, "Write your new password : ")
            pss2 = my_input(stdscr, 3, 0, "confirm your new password : ")
            if pss == pss2:
                tcher.change_password(pss)
                stdscr.addstr(4, 0, "Done!")
                stdscr.refresh()
            time.sleep(2)
            menu_l(stdscr, tcher.teacher)

        elif str(chr(key)) == "q" or str(chr(key)) == "Q":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
            stdscr.addstr(21, 0, "Q/q for Exit")
    	    stdscr.addstr(22, 0, "Want to Exit? Y/N")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    key = stdscr.getch()
	    if str(chr(key)) == "Y" or str(chr(key)) == "y":
		time.sleep(1)
		exit()
	else:
	    menu_l(stdscr, tcher.teacher)
	    
    elif key == curses.KEY_MOUSE :
	_, x, y, _, _ = curses.getmouse()
	    
	if y == 3 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(3, 0, "|            My lessons            |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
	    lst = tcher.plesson()						
	    cx = len(lst)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+------+-------------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|      My lessons    |")
                cnt = 2
	        stdscr.addstr(cnt, 0, "+------+-------------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  |%s |" %(i[0], i[1]))			#enterin to submenu and using the built in defs of class and perinting 
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+------+-------------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|    page %d of %d     |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+------+-------------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_l(stdscr, tcher.teacher)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst)
            call(stdscr, ox, qx, zx, ux, lst)


	if y == 5 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(5, 0, "|            My Students           |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            mycursor.execute("SELECT * FROM lessons")
            myresult = mycursor.fetchall()
            lst2 = []
	    w = "Your lessons: "
	    cnt = len(w)
            for i in myresult:
		if tcher.name == i[1]:
                	lst2.append(i[0])
	    stdscr.addstr(2, 0, "%s" %w)
            for i in lst2:
                stdscr.addstr(2, cnt, "%s" %i)
                cnt += 3
            lsen = my_input(stdscr, 3, 0, "Write your lesson : ")
            ls = tcher.studen()
            lst3 = []
            for i in ls:
                if i[1] == lsen:
                    lst3.append(i)
	    stdscr.clear()
	    cx = len(lst3)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+--------+------+--------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|      students in %s    |" %lsen)
                cnt = 2
	        stdscr.addstr(cnt, 0, "+--------+------+--------+")
	        cnt = 3
                stdscr.addstr(cnt, 0, "|  user  |lesson| field  |")
                cnt = 4
	        stdscr.addstr(cnt, 0, "+--------+------+--------+")
	        cnt = 5
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  |  %s  |  %s  |" %(i[0],i[1],i[2]))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+--------+------+--------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|      page %d of %d       |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+--------+------+--------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_l(stdscr, tcher.teacher)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst3)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
                            num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst3)
            call(stdscr, ox, qx, zx, ux, lst3)

            

	if y == 7 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(7, 0, "|             Erae Dars            |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            lsen = my_input(stdscr, 2, 0, "Write your lesson (in two digits like ---> analyses == an): ")
	    mycursor.execute("SELECT * FROM lessons")
	    myresult = mycursor.fetchall()
	    done = True
	    for i in myresult:
		if tcher.name == i[1] and lsen == i[0]:
		    stdscr.addstr(3, 0, "You have aldready propousing this course!!")
		    stdscr.refresh()
            	    time.sleep(2)
		    done = False
	    if done:
	    	if tcher.erae(lsen):
                	stdscr.addstr(4, 0, "Dars shoma b modiriat erja dade shod!")
                	stdscr.addstr(5, 0, "Darsorat tayid dar menu my lesson ghabel dastrasi ast!")
			stdscr.refresh()
            		time.sleep(2)
            		stdscr.clear()
            menu_l(stdscr, tcher.teacher)
   
	if y == 9 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(9, 0, "|           Record numbers         |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            lst = tcher.plesson()
            cnt = 0
            for i in lst:
                stdscr.addstr(2, cnt, "%s" %i[0])
                cnt += 3
            les = my_input(stdscr, 3, 0, "write your lesson: ")
            lst2 = tcher.studen()
            lst3 = []
            for i in lst2:
                if i[1] == les :
                    lst3.append(i)
            cn = 5
            for i in lst3:
                stdscr.addstr(cn, 0, "%s" %i[0])
                cn +=1
            uss = my_input(stdscr, cn+1, 0, "Write your student username: ")
            mark = my_input(stdscr, cn+2, 0, "Write student mark: ")
            tcher.grade_s(les, uss, mark)
            stdscr.addstr(cn+3, 0, "Done!")
	    stdscr.refresh()
            time.sleep(2)
            menu_l(stdscr, tcher.teacher)

	    
        if y == 11 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(11, 0, "|         Virayesh etelaat         |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            uss = my_input(stdscr, 2, 0, "Write your new username: ")
	    if tcher.edition(uss) :
                stdscr.addstr(3, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
            menu_l(stdscr, tcher.teacher)
            
        if y == 13 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(13, 0, "|         password change          |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            pss = my_input(stdscr, 2, 0, "Write your new password : ")
            pss2 = my_input(stdscr, 3, 0, "confirm your new password : ")
            if pss == pss2:
                tcher.change_password(pss)
                stdscr.addstr(4, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
            menu_l(stdscr, tcher.teacher)

        if y == 15 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(15, 0, "|               Exit               |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    tcher.exit()
	else:
	    menu_l(stdscr, tcher.teacher)

def menu_A(stdscr, admin):
    addmin = Admin(admin)
    stdscr.clear()
    stdscr.addstr(0, 0, "+----------------------------------+")
    stdscr.addstr(1, 0, "|           @Admin Menu@           |")
    stdscr.addstr(2, 0, "+----------------------------------+")
    stdscr.addstr(3, 0, "|             Teachers             |")
    stdscr.addstr(4, 0, "+----------------------------------+")
    stdscr.addstr(5, 0, "|             Students             |")
    stdscr.addstr(6, 0, "+----------------------------------+")
    stdscr.addstr(7, 0, "|              Lessons             |")
    stdscr.addstr(8, 0, "+----------------------------------+")
    stdscr.addstr(9, 0, "|            Tayid Doros           |")
    stdscr.addstr(10, 0, "+----------------------------------+")
    stdscr.addstr(11, 0, "|          Tayid Karbaran          |")		#main menu for admin which suppport mouse
    stdscr.addstr(12, 0, "+----------------------------------+")
    stdscr.addstr(13, 0, "|          Nafarat Bartar          |")
    stdscr.addstr(14, 0, "+----------------------------------+")
    stdscr.addstr(15, 0, "|         Virayesh etelaat         |")
    stdscr.addstr(16, 0, "+----------------------------------+")
    stdscr.addstr(17, 0, "|         password change          |")
    stdscr.addstr(18, 0, "+----------------------------------+")
    stdscr.addstr(19, 0, "|               Exit               |")
    stdscr.addstr(20, 0, "+----------------------------------+")
    stdscr.addstr(22, 0, "T/t for Teachers")
    stdscr.addstr(22, 27, "S/s for Students")
    stdscr.addstr(23, 0, "L/l for lessons")
    stdscr.addstr(23, 27, "D/d for Tayid Doros")
    stdscr.addstr(24, 0, "K/k for  Tayid Karbaran ")
    stdscr.addstr(24, 27, "A/a for Nafarat Bartar")
    stdscr.addstr(25, 0, "V/v for Virayesh Etelaat")
    stdscr.addstr(25, 27, "P/p for Password Change")
    stdscr.addstr(26, 0, "Q/q for Exit")
    stdscr.refresh()


    key = stdscr.getch()
    if key != curses.KEY_MOUSE :
	if str(chr(key)) == "T" or str(chr(key)) == "t":
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(22, 0, "T/t for Teachers")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()					#enterin to submenu and using the built in defs of class and perinting 
	    time.sleep(1)
	    stdscr.clear()
	    lst = addmin.teacherr()
	    cx = len(lst)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
                stdscr.addstr(cnt, 0, "+---+-------------+------+----------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|           Teachers list           |")
                cnt = 2
                stdscr.addstr(cnt, 0, "+---+-------------+------+----------+")
                cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    a = len(i[3])
                    b = 9 - a
                    k = " %s"%i[3]+ " "*b
                    stdscr.addstr(cnt, 0, "| %s |%s | %s |%s|" %(i[0], i[1], i[2], k))
                    cnt += 1
                    stdscr.addstr(cnt, 0, "+---+-------------+------+----------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|           page %d of %d             |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+---+-------------+------+----------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_A(stdscr, addmin.admin)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst)
            call(stdscr, ox, qx, zx, ux, lst)


		
        elif str(chr(key)) == "S" or str(chr(key)) == "s":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(22, 27, "S/s for Students")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            s = addmin.studentt()
	    cx = len(s)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+---+--------------------------+------+----------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|                  Student list                  |")
                cnt = 2
	        stdscr.addstr(cnt, 0, "+---+--------------------------+------+----------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    a = len(i[3])
		    b = 9 - a
		    k = " %s"%i[3]+ " "*b
		    w = len(i[1])
		    x = 24 - w
		    y = " %s"%i[1]+ " "*x
		    z = len(str(i[2]))
		    q = 4 - z
		    l = " %s"%i[2]+ " "*q
                    stdscr.addstr(cnt, 0, "| %s |%s |%s |%s|" %(i[0], y, l, k))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+---+--------------------------+------+----------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|                   page %d of %d                  |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+---+--------------------------+------+----------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_A(stdscr, addmin.admin)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, s)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, s)
            call(stdscr, ox, qx, zx, ux, s)
            

		
        elif str(chr(key)) == "L" or str(chr(key)) == "l":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(23, 0, "L/l for lessons")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            less = addmin.lessonsss()
	    cx = len(less)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
                stdscr.addstr(cnt, 0, "+------+-------------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|     lessons list   |")
                cnt = 2
                stdscr.addstr(cnt, 0, "+------+-------------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  +%s |" %(i[0],i[1]))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+------+-------------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|    page %d of %d     |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+------+-------------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_A(stdscr, addmin.admin)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, less)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
                            num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, less)
            call(stdscr, ox, qx, zx, ux, less)
   
	
        elif str(chr(key)) == "D" or str(chr(key)) == "d":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))    
	    stdscr.addstr(23, 27, "D/d for Tayid Doros")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            less = addmin.pending_l()
	    cnt = 0
            stdscr.addstr(cnt, 0, "+--------+-------------+")
            cnt = 1
            stdscr.addstr(cnt, 0, "|     pending lessons  |")
            cnt = 2
            stdscr.addstr(cnt, 0, "+--------+-------------+")
	    cnt = 3
	    for i in less:
		a = len(i[0])
		b = 7 - a
		k = " %s"%i[0]+ " "*b
	        stdscr.addstr(cnt, 0, "|%s+%s |" %(k,i[1]))
		cnt += 1
                stdscr.addstr(cnt, 0, "+--------+-------------+")
		cnt += 1
	    if less != []:
	    	con = my_input(stdscr, cnt, 0, "type lesson to confirm : ")
 		addmin.accept_lesson(con)
		addmin.request_lesson()
		stdscr.addstr(cnt+2, 0, "Done!")
		stdscr.refresh()
	        time.sleep(2)
	    else:
		stdscr.addstr(cnt+2, 0, "there is no lesson to confirm!")
		stdscr.refresh()
		time.sleep(2)
	    menu_A(stdscr, addmin.admin)
	    
	
        elif str(chr(key)) == "K" or str(chr(key)) == "k":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
            stdscr.addstr(24, 0, "K/k for  Tayid Karbaran ")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            ls = addmin.pending_s()
	    cnt = 0
            stdscr.addstr(cnt, 0, "+------------------+")
            cnt = 1
            stdscr.addstr(cnt, 0, "|pending students  |")
            cnt = 2
            stdscr.addstr(cnt, 0, "+------------------+")
	    cnt = 3
	    for i in ls:
		a = len(i[0])
		b = 16 - a
		k = " %s"%i[0]+ " "*b
	        stdscr.addstr(cnt, 0, "|%s |" %(k))
		cnt += 1
                stdscr.addstr(cnt, 0, "+------------------+")
		cnt += 1
	    if ls != []:
	    	con = my_input(stdscr, cnt, 0, "type username to confirm : ")
 		addmin.accept_client(con)
		stdscr.addstr(cnt+2, 0, "Done!")
		stdscr.refresh()
	        time.sleep(2)
	    else:
		stdscr.addstr(cnt+2, 0, "there is no lesson to confirm!")
		stdscr.refresh()
		time.sleep(2)
	    menu_A(stdscr, addmin.admin)
		
            
        	
        elif str(chr(key)) == "A" or str(chr(key)) == "a":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
            stdscr.addstr(24, 27, "A/a for Nafarat Bartar")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            bst = addmin.best_students()
	    cnt = 0
            stdscr.addstr(cnt, 0, "+----------------+--------+")
            cnt = 1
            stdscr.addstr(cnt, 0, "|      Best  students     |")
            cnt = 2
            stdscr.addstr(cnt, 0, "+----------------+--------+")
	    cnt = 3
	    for i in bst:
		a = len(i[0])
		b = 15 - a
		k = " %s"%i[0]+ " "*b
	        stdscr.addstr(cnt, 0, "|%s|   %s   |" %(k,i[1]))
		cnt += 1
                stdscr.addstr(cnt, 0, "+----------------+--------+")
		cnt += 1
	    stdscr.addstr(cnt+3, 0, "B for back")
	    key = stdscr.getch()
	    if str(chr(key)) == "B" or str(chr(key)) == "b":
		menu_A(stdscr, addmin.admin)
		
        elif str(chr(key)) == "V" or str(chr(key)) == "v":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
            stdscr.addstr(25, 0, "V/v for Virayesh Etelaat")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            uss = my_input(stdscr, 2, 0, "Write your New username: ")
	    if addmin.edition(uss) :
                stdscr.addstr(3, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
            else:
                stdscr.addstr(3, 0, "this user name is taken!")
		time.sleep(2)
            menu_l(stdscr, addmin.admin)
            
        	
        elif str(chr(key)) == "P" or str(chr(key)) == "p":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(25, 27, "P/p for Password Change")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            pss = my_input(stdscr, 2, 0, "Write your new password : ")
            pss2 = my_input(stdscr, 3, 0, "Write your new password : ")
            if pss == pss2:
                addmin.change_password(pss)
                stdscr.addstr(4, 0, "Done!")
                stdscr.refresh()
            time.sleep(2)
            menu_l(stdscr, addmin.admin)

        elif str(chr(key)) == "q" or str(chr(key)) == "Q":
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(21, 0, "Q/q for Exit")
	    stdscr.addstr(22, 0, "Want to Exit? Y/N")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    key = stdscr.getch()
	    if str(chr(key)) == "Y" or str(chr(key)) == "y":
	        time.sleep(1)
		exit()
	else:
	    menu_A(stdscr, addmin.admin)

	    
    elif key == curses.KEY_MOUSE :
	_, x, y, _, _ = curses.getmouse()
	    
	if y == 3 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(3, 0, "|             Teachers             |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()							#enterin to submenu and using the built in defs of class and perinting 
	    time.sleep(1)
	    stdscr.clear()
	    lst = addmin.teacherr()
	    cx = len(lst)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
                stdscr.addstr(cnt, 0, "+---+-------------+------+----------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|           Teachers list           |")
                cnt = 2
                stdscr.addstr(cnt, 0, "+---+-------------+------+----------+")
                cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    a = len(i[3])
                    b = 9 - a
                    k = " %s"%i[3]+ " "*b
                    stdscr.addstr(cnt, 0, "| %s |%s | %s |%s|" %(i[0], i[1], i[2], k))
                    cnt += 1
                    stdscr.addstr(cnt, 0, "+---+-------------+------+----------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|           page %d of %d             |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+---+-------------+------+----------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_A(stdscr, addmin.admin)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, lst)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, lst)
            call(stdscr, ox, qx, zx, ux, lst)


	if y == 5 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(5, 0, "|             Students             |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            s = addmin.studentt()
	    cx = len(s)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
	        stdscr.addstr(cnt, 0, "+---+--------------------------+------+----------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|                  Student list                  |")
                cnt = 2
	        stdscr.addstr(cnt, 0, "+---+--------------------------+------+----------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    a = len(i[3])
		    b = 9 - a
		    k = " %s"%i[3]+ " "*b
		    w = len(i[1])
		    x = 24 - w
		    y = " %s"%i[1]+ " "*x
		    z = len(str(i[2]))
		    q = 4 - z
		    l = " %s"%i[2]+ " "*q
                    stdscr.addstr(cnt, 0, "| %s |%s |%s |%s|" %(i[0], y, l, k))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+---+--------------------------+------+----------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|                   page %d of %d                  |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+---+--------------------------+------+----------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_A(stdscr, addmin.admin)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, s)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
			    num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, s)
            call(stdscr, ox, qx, zx, ux, s)
            

	if y == 7 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(7, 0, "|              Lessons             |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            less = addmin.lessonsss()
	    cx = len(less)
	    ux = (cx//10)+1
	    zx = 1
	    qx = 10
	    ox = 0
	    def call(stdscr, nums, num, srt, end, lst):
                stdscr.clear()
                cnt = 0
                stdscr.addstr(cnt, 0, "+------+-------------+")
                cnt = 1
                stdscr.addstr(cnt, 0, "|     lessons list   |")
                cnt = 2
                stdscr.addstr(cnt, 0, "+------+-------------+")
	        cnt = 3
		if len(lst) <num:
			num = len(lst)
                for it in range(nums, num):
		    i = lst[it]
                    stdscr.addstr(cnt, 0, "|  %s  +%s |" %(i[0],i[1]))
                    cnt += 1
		    stdscr.addstr(cnt, 0, "+------+-------------+")
                    cnt += 1
                stdscr.addstr(cnt, 0, "|    page %d of %d     |"%(srt,end))
                stdscr.addstr(cnt+1, 0, "+------+-------------+")
                stdscr.addstr(cnt+2, 0, "B for Back")
                if end > 1 and srt < end:
                    stdscr.addstr(cnt+2, 13, "/ N for Next")
                if num > 10:
                    stdscr.addstr(cnt+2, 28, "/ P for Prev")
                key = stdscr.getch()
                if key != curses.KEY_MOUSE :
                    if str(chr(key)) == "B" or str(chr(key)) == "b":
                        menu_A(stdscr, addmin.admin)
                    if str(chr(key)) == "N" or str(chr(key)) == "n":
                        nums += 10
                        num += 10
                        srt += 1
                        call(stdscr, nums, num, srt, end, less)
                    if num > 10:
                        if str(chr(key)) == "P" or str(chr(key)) == "p":
                            num -=10
			    nums -= 10
                            if num < 10:
				num = 10
				nums = 0
                            srt -= 1
                            call(stdscr, nums, num, srt, end, less)
            call(stdscr, ox, qx, zx, ux, less)
   
	if y == 9 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(9, 0, "|            Tayid Doros           |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            less = addmin.pending_l()
	    cnt = 0
            stdscr.addstr(cnt, 0, "+--------+-------------+")
            cnt = 1
            stdscr.addstr(cnt, 0, "|     pending lessons  |")
            cnt = 2
            stdscr.addstr(cnt, 0, "+--------+-------------+")
	    cnt = 3
	    for i in less:
		a = len(i[0])
		b = 7 - a
		k = " %s"%i[0]+ " "*b
	        stdscr.addstr(cnt, 0, "|%s+%s |" %(k,i[1]))
		cnt += 1
                stdscr.addstr(cnt, 0, "+--------+-------------+")
		cnt += 1
	    if less != []:
	    	con = my_input(stdscr, cnt, 0, "type lesson to confirm : ")
 		addmin.accept_lesson(con)
		addmin.request_lesson()
		stdscr.addstr(cnt+2, 0, "Done!")
		stdscr.refresh()
	        time.sleep(2)
	    else:
		stdscr.addstr(cnt+2, 0, "there is no lesson to confirm!")
		stdscr.refresh()
		time.sleep(2)
	    menu_A(stdscr, addmin.admin)
	    
        if y == 11 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
            stdscr.addstr(11, 0, "|          Tayid Karbaran          |")
            stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            ls = addmin.pending_s()
	    cnt = 0
            stdscr.addstr(cnt, 0, "+------------------+")
            cnt = 1
            stdscr.addstr(cnt, 0, "|pending students  |")
            cnt = 2
            stdscr.addstr(cnt, 0, "+------------------+")
	    cnt = 3
	    for i in ls:
		a = len(i[0])
		b = 16 - a
		k = " %s"%i[0]+ " "*b
	        stdscr.addstr(cnt, 0, "|%s |" %(k))
		cnt += 1
                stdscr.addstr(cnt, 0, "+------------------+")
		cnt += 1
	    if ls != []:
	    	con = my_input(stdscr, cnt, 0, "type username to confirm : ")
 		addmin.accept_client(con)
		stdscr.addstr(cnt+2, 0, "Done!")
		stdscr.refresh()
	        time.sleep(2)
	    else:
		stdscr.addstr(cnt+2, 0, "there is no lesson to confirm!")
		stdscr.refresh()
		time.sleep(2)
	    menu_A(stdscr, addmin.admin)
		
            
        if y == 13 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(13, 0, "|          Nafarat Bartar          |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            bst = addmin.best_students()
	    cnt = 0
            stdscr.addstr(cnt, 0, "+----------------+--------+")
            cnt = 1
            stdscr.addstr(cnt, 0, "|      Best  students     |")
            cnt = 2
            stdscr.addstr(cnt, 0, "+----------------+--------+")
	    cnt = 3
	    for i in bst:
		a = len(i[0])
		b = 15 - a
		k = " %s"%i[0]+ " "*b
	        stdscr.addstr(cnt, 0, "|%s|   %s   |" %(k,i[1]))
		cnt += 1
                stdscr.addstr(cnt, 0, "+----------------+--------+")
		cnt += 1
	    stdscr.addstr(cnt+3, 0, "B for back")
	    key = stdscr.getch()
	    if str(chr(key)) == "B" or str(chr(key)) == "b":
		menu_A(stdscr, addmin.admin)
		

        if y == 15 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(15, 0, "|         Virayesh etelaat         |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(2)
	    stdscr.clear()
            uss = my_input(stdscr, 2, 0, "Write your New username: ")
	    if addmin.edition(uss) :
                stdscr.addstr(3, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
            else:
                stdscr.addstr(3, 0, "this user name is taken!")
		time.sleep(2)
            menu_l(stdscr, addmin.admin)
            
        if y == 17 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(17, 0, "|         password change          |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    stdscr.clear()
            pss = my_input(stdscr, 2, 0, "Write your new password : ")
            pss2 = my_input(stdscr, 3, 0, "Write your new password : ")
            if pss == pss2:
                addmin.change_password(pss)
                stdscr.addstr(4, 0, "Done!")
                stdscr.refresh()
                time.sleep(2)
            menu_l(stdscr, addmin.admin)

        if y == 19 and x in range(1,35):
    	    stdscr.attron(curses.color_pair(1))
	    stdscr.addstr(19, 0, "|               Exit               |")
	    stdscr.attroff(curses.color_pair(1))
	    stdscr.refresh()
	    time.sleep(1)
	    addmin.exit()
	
	else:
	    menu_A(stdscr, addmin.admin)











                              
