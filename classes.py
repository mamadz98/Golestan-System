import db
from db import mycursor


def student_lst():
    lst = []
    mycursor.execute("SELECT * FROM students")
    myresult = mycursor.fetchall()
    for i in myresult:
	lst.append((i[0], i[1], i[2], i[3]))
    return lst
								
def teacher_lst():						#common defs
    lst = []
    mycursor.execute("SELECT * FROM dr")
    myresult = mycursor.fetchall()
    for i in myresult:
	lst.append(i)
    return lst

def lessons_lst():
    lst = []
    mycursor.execute("SELECT * FROM lessons")
    myresult = mycursor.fetchall()
    for i in myresult:
	lst.append(i)
    return lst

class common:

    def edition(self, user):
        flag = True
        mycursor.execute("SELECT * FROM students")
	myresult = mycursor.fetchall()
	for i in myresult:
   	    if i[4] == user :
		flag = False
	mycursor.execute("SELECT * FROM dr")
	myresult = mycursor.fetchall()
	for i in myresult:
   	    if i[4] == user :
		flag = False						#common defs in classes with inheritates from childs
		
        mycursor.execute("SELECT * FROM admin")
	myresult = mycursor.fetchall()
	for i in myresult:
   	    if i[4] == user :
		flag = False							

        if self.status == "P" :
            sql = "UPDATE dr SET user = %s WHERE user = %s"
            mycursor.execute("SELECT user FROM dr")
            myresult = mycursor.fetchall()
            for i in myresult:
                if i == user:
                    flag = False
                    
        if self.status == "S":
            sql = "UPDATE students SET user = %s WHERE user = %s"
            mycursor.execute("SELECT user FROM students")
            myresult = mycursor.fetchall()
            for i in myresult:
                if i == user:
                    flag = False
                    
        if self.status == "A":
            sql = "UPDATE admin SET user = %s WHERE user = %s"
            mycursor.execute("SELECT user FROM admin")
            myresult = mycursor.fetchall()
            for i in myresult:
                if i == user:
                    flag = False
        if flag:
            val = (user, self.user)
            mycursor.execute(sql,val)
            self.user = user
	db.mydb.commit()
        return flag
            

    def change_password(self, newpass):
        if self.status == "P":
            sql = "UPDATE dr SET pass = %s WHERE pass = %s"
        if self.status == "S":
            sql = "UPDATE students SET pass = %s WHERE pass = %s"
        if self.status == "A":
            sql = "UPDATE admin SET pass = %s WHERE pass = %s"
        val = (newpass, self.pss)
        mycursor.execute(sql,val)
        self.pss = newpass
	db.mydb.commit()
        
    def exit(self):
	exit()


class Professor(common):
   
    def __init__(self, teacher):
	self.students = student_lst()
	self.teacher = teacher
	self.number = self.teacher[0]
	self.name = self.teacher[1]
	self.year = self.teacher[2]				#constructor of class professor which making a professor in login			
	self.field = self.teacher[3]
	self.user = self.teacher[4]
	self.pss = self.teacher[5]
	self.status = "P"


    def plesson(self):
	lst = []
        mycursor.execute("SELECT * FROM lessons")
        myresult = mycursor.fetchall()					#defining defs
        for i in myresult:
	    if self.name == i[1]:
		lst.append(i)
        return lst

    def studen(self):
	lst = []
        mycursor.execute("SELECT * FROM rank")
        myresult = mycursor.fetchall()
        for i in myresult:
            if i[3] == self.name:
		lst.append((i[0], i[1], i[2], i[3]))
        return lst

    def erae(self, lesson):
	sqlformula = "INSERT INTO waitingl(lesson, teacher, confirmed) VALUES (%s, %s, %s)"
	mycursor.execute(sqlformula, (lesson, self.name, "No"))
	db.mydb.commit()
	return True

    def grade_s(self, lesson, student, mark):
        sql = "UPDATE rank SET mark = %s WHERE lesson = %s AND user = %s"
        val = (mark, lesson, student)
        mycursor.execute(sql,val)
	db.mydb.commit()

class Student(common):
    
    def __init__(self, student):
	self.student = student
	self.number = self.student[0]
	self.name = self.student[1]
	self.year = self.student[2]
	self.field = self.student[3]					#constructor of class student which making a student in login
	self.user = self.student[4]
	self.pss = self.student[5]
	self.status = "S"

    def slesson(self):
	lst = []
	lst2 = []
	lst3 = []
        mycursor.execute("SELECT * FROM rank")
        myresult = mycursor.fetchall()
        for i in myresult:
	    if self.user == i[0]:
                    lst2.append((i[1],i[3]))
        mylst = lst2
	mycursor.execute("SELECT * FROM lessons")		#defining defs for login and tables
        myresult2 = mycursor.fetchall()
	for i in myresult2:
		lst3.append(i)
        mylst2 = lst3
        a = 0
	b = len(mylst)
	e = len(mylst2)
	d = min(b,e)
	while a < b:
	    c = 0
	    while c < e:
		if mylst != [] and mylst2 != [] :
		    if mylst[a] == mylst2[c] :
		        lst.append(mylst[a])
	        c+=1
	    a+=1
        return lst

    def grade(self):
	lst = []
        mycursor.execute("SELECT * FROM rank")
        myresult = mycursor.fetchall()
        for i in myresult:
	    if self.user == i[0]:
		lst.append((i[1],i[2],i[3],i[4]))
        return lst

    def take_lesson(self, lesson):
        lsen = (self.name, lesson, 0)
        sqlformula = "INSERT INTO rank(user, lesson, ostad, mark) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sqlformula, lsen)
	db.mydb.commit()

    def evaluation(self, teacher, mark):
	formula ="INSERT INTO arzesh(user, teacher, mark) VALUES (%s, %s, %s)"
	esn = (self.user, teacher, mark)
	mycursor.execute(formula, esn)
	db.mydb.commit()
	return True

    


class Admin(common):
    def __init__(self, admin):
	self.admin = admin
	self.number = self.admin[0]
	self.name = self.admin[1]
	self.year = self.admin[2]						#constructor of class admin wich making a admin in login
	self.field = self.admin[3]
	self.user = self.admin[4]
	self.pss = self.admin[5]
	self.lessons = []
	self.teachers = []
	self.students = []
	self.status = "A"
    

    def student_lst(self):
        lst = []
        mycursor.execute("SELECT * FROM students")
        myresult = mycursor.fetchall()
        for i in myresult:
	    lst.append((i[0], i[1], i[2], i[3]))
        return lst

    def teacher_lst(self):
        lst = []
        mycursor.execute("SELECT * FROM dr")
        myresult = mycursor.fetchall()
        for i in myresult:
            lst.append((i[0], i[1], i[2], i[3]))
        return lst

    def lessons_lst(self):
        lst = []
        mycursor.execute("SELECT * FROM lessons")
        myresult = mycursor.fetchall()
        for i in myresult:						#defining defs for login and tables
            lst.append(i)
        return lst
    
    def teacherr(self):
	self.teachers = self.teacher_lst()
        return self.teachers
    
    def studentt(self):
	self.students = self.student_lst()
	return self.students

    def lessonsss(self):
	self.lessons = lessons_lst()
        return self.lessons
        
    def request_lesson(self):
	mycursor.execute("SELECT * FROM waitingl")
	myresult = mycursor.fetchall()
	for i in myresult:
	     if i[2] == "Yes":
		n_lesson = i[0]
		n_master = i[1]
		sqlformula = "INSERT INTO lessons(leson, teacher) VALUES (%s, %s)"
        	mycursor.execute(sqlformula, (n_lesson, n_master))
	db.mydb.commit()


    def pending_s(self):
        lst = []
        mycursor.execute("SELECT * FROM waitings")
	myresult = mycursor.fetchall()
	for i in myresult:
            if i[2] == "No" :
                lst.append(i)
        return lst
    
    def accept_client(self, user):
        std = self.pending_s()
        for i in std:
            if i[0]== user:
                pss = i[1]
        sql = "UPDATE waitings SET confirmed = %s WHERE user = %s"
        val = ("Yes", user)
        mycursor.execute(sql, val)
        seq = "SELECT num FROM students"
	mycursor.execute(seq)
	my = mycursor.fetchall()
	x = 1
	for i in my :
	    x+=1
        cnt = x
        sqlformula = "INSERT INTO students(num, name, year, field, user, pass) VALUES (%s, %s, %s, %s, %s, %s)"
        vals = (cnt, "", 0, "", user, pss)
	mycursor.execute(sqlformula, vals)
	db.mydb.commit()

    def pending_l(self):
        lst = []
        mycursor.execute("SELECT * FROM waitingl")
	myresult = mycursor.fetchall()
	if myresult != []:
	    for i in myresult:
                if i[2] == "No" :
                    lst.append(i)
        return lst
    
    def accept_lesson(self, name):
        sql = "UPDATE waitingl SET confirmed = %s WHERE lesson = %s"
        val = ("Yes", name)
        mycursor.execute(sql, val)
	db.mydb.commit()
	
        
        

    def best_students(self):
        mycursor.execute("SELECT * FROM rank")
        myresult = mycursor.fetchall()
        lst = []
        for i in myresult:
            lst.append((i[0],[]))
        for i in myresult :
            for j in lst:
                if j[0] == i[0]:
                    j[1].append(int(i[4]))
        lst2 = []
        for i in lst:
            if i not in lst2:
                lst2.append(i)

        lst3 = []
        def average(lst):
            return sum(lst) / len(lst)
        for i in lst2 :
            a = average(i[1])
            lst3.append((i[0],a))

        a = lst3[0][1]
        cnt = 0
        i = 1
        bst = [lst3[0]]
        while i < len(lst3):
            if lst3[i][1] >= a:
                a = lst3[i][1]
                bst.append(lst3[i])
                
            i +=1
        bst = bst[::-1]
        if len(bst)> 3:
            bst = bst[0:3]
        return bst





















        
        
	
                
        
    
