from persiantools.jdatetime import JalaliDateTime
import datetime

def do_twice(f):
    f()
    f()
					
def do_four(f):
    do_twice(f)
    print_time()
    do_twice(f)						#printing the jalali time/shamsi in main

def print_column():
    return '+----------------------------------+'

def print_time():
    return "|   %s     |" %(JalaliDateTime.today())

def print_row():
    return "|                                  |"

def print_rows():
    do_four(print_row)

def do_block():
    print_column()
    print_rows()
    print_column()



