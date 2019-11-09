import sys,os
import curses

chapters = [
    "Hello world",
    "Inroduction to variables",
    "Learn functions",
    "For loops for the win",
]

def print_chapter(chapter_id):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Epic")

def draw_menu(stdscr):
    stdscr.clear()
    stdscr.refresh()
    current_selection = 0

    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

    k = 0
    while k != ord('q'):
        i = 0
        for chapter in chapters:
            color_pair = 1
            if current_selection == i:
                color_pair = 2
            stdscr.attron(curses.color_pair(color_pair))
            text_row = "* {}".format(chapter)
            stdscr.addstr(i, 0, text_row)
            stdscr.attroff(curses.color_pair(color_pair))
            i += 1
        k = stdscr.getch()
        if k == curses.KEY_UP:
            if current_selection == 0:
                current_selection = len(chapters) - 1
            else:
                current_selection = current_selection - 1
        elif k == curses.KEY_DOWN:
            if current_selection == len(chapters) - 1:
                current_selection = 0
            else:
                current_selection = current_selection + 1
        elif k in [curses.KEY_ENTER, 10, 13]:
            return current_selection
        stdscr.refresh()

def main():
    current_selection = curses.wrapper(draw_menu)
    if current_selection is not None:
        print_chapter(current_selection)

if __name__ == "__main__":
    main()