import curses
import random

texts = {
    1 : "Once upon a time, in a mystical land far beyond the horizon, there existed an ancient forest.",
    2 : "Within this forest, magical creatures roamed freely. Elves with emerald eyes danced under moonlit canopies",
    3 : "Hidden within the gnarled roots were secrets older than time itself. Whispers spoke of forgotten spells",
    4 : "One day, a brave adventurer named Lyra embarked on a quest. Her goal? ",
    5 : "Lyra faced treacherous paths, riddles from ancient spirits, and trials that tested her courage.",
    6 : "At the heart of the forest, she found an ancient oak—the World Tree.",
    7 : "The forest whispered its truth: 'We are all connected. From the tiniest leaf to the brightest star'",
    8 : "And so, Lyra returned to her village, carrying the forest's wisdom. She became a storyteller",
}

def clear(stdscr) -> None: 

    stdscr.clear()
    stdscr.refresh()
    


def add_message(stdscr) -> None:
    clear(stdscr)
    stdscr.addstr(0,0,'welcome to the speed test press any key to start !!')
    stdscr.getkey()




def testspeed(stdscr):
    add_message(stdscr)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    clear(stdscr)
    text = texts[random.randint(1,8)]
    
    global text_list
    text_list = list(text)
    stdscr.addstr(0,0,text) 
    correct = 0
    incorrect = 0
    for i in range(len(text)):
        key = stdscr.getch()  # استخدم getch بدلاً من getkey
        if key == ord(text_list[i]):  # افحص القيم ASCII بدلاً من المفاتيح المباشرة
            stdscr.addstr(0, i, text_list[i], curses.color_pair(1))
            correct += 1
        else:
            stdscr.addstr(0, i, chr(key), curses.color_pair(2))
            incorrect += 1

        stdscr.addstr(3, 0, f'{correct}  chars correct')
        stdscr.addstr(4, 0, f'{incorrect}  chars incorrect')
        stdscr.refresh()
    
    stdscr.getch()

        
        
        
        
    
    


curses.wrapper(testspeed)
