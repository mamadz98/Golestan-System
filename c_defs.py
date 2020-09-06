import curses

def my_input(stdscr, y, x, n_string):
    curses.echo()
    stdscr.addstr(y, x, n_string)			#defining a common def for student/admin/teacher
    stdscr.refresh()
    m_input = stdscr.getstr(y, len(n_string)+1, 30)
    return m_input
