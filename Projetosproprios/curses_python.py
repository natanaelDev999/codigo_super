import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()

    stdscr.addstr(10,10,"Olá estamos usando o curseS",curses.A_BOLD)

    stdscr.refresh()
    stdscr.getch()

wrapper(main)
input()