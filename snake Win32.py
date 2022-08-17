import curses
import os
import time
from copy import copy
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
os.system('title Snake (On CMD)')
os.system('mode con: cols=60 lines=30')
os.system('color 0a')
while True:
    print ("    Y")
    print ("  .-^-.")
    print (" /     \      .- ~ ~ -.")
    print ("()     ()    /   _ _   `.                     _ _ _")
    print (" \_   _/    /  /     \   \                . ~  _ _  ~ .")
    print ("   | |     /  /       \   \             .' .~       ~-. `.")
    print ("   | |    /  /         )   )           /  /             `.`.")
    print ("   \ \_ _/  /         /   /           /  /                `'")
    print ("    \_ _ _.'         /   /           (  ( ")
    print ("                    /   /             \  \ ")
    print ("                   /   /               \  \ ")
    print ("                  /   /                 )  ) ")
    print ("                 (   (                 /  / ")
    print ("                  `.  `.             .'  / ")
    print ("                    `.   ~ - - - - ~   .' ")
    print ("                       ~ . _ _ _ _ . ~ ")

    print ("                                  _  ")
    print ("                                 | | ")
    print ("                  ___ _ __   __ _| | _____ ")
    print ("                 / __| '_ \ / _` | |/ / _ \ ")
    print ("                 \__ \ | | | (_| |   <  __/ ")
    print ("                 |___/_| |_|\__,_|_|\_\___| ")
    print ("Snake On CMD")
    print ("built in python")
    print (" ")
    input("Press Enter To Play ")
    curses.initscr()
    finestra = curses.newwin(30, 60, 0, 0)
    finestra.keypad(True)
    finestra.border(0)
    finestra.timeout(10)
    snake = [[15,13], [15,12], [15,11]]
    cibo = [5,35]
    doveGuardo = KEY_DOWN
    punti = 0
    finestra.addch(cibo[0], cibo[1], '*')
    while True:
        finestra.addstr(0, 14, 'Points: ' + str(punti) + ' ')
        tasto = finestra.getch()
        if tasto !=-1:
            doveGuardo = tasto
        nuovaTesta = copy(snake[0])
        if doveGuardo == KEY_DOWN:
            nuovaTesta[0] += 1
        elif doveGuardo == KEY_UP:
            nuovaTesta[0] -= 1
        elif doveGuardo == KEY_RIGHT:
            nuovaTesta[1] += 1
        elif doveGuardo == KEY_LEFT:
            nuovaTesta[1] -= 1
    
        snake.insert(0, nuovaTesta)
        if snake [0][0] == 0 or snake[0][0] == 29 or snake[0][1] == 0 or snake[0][1] == 59:
            break
        if snake [0] in snake[1:]:
            break
        if snake[0] == cibo:
            cibo= []
            punti += 1
            while cibo == []:
                cibo = [randint(1, 28), randint(1,58)]
                if cibo in snake:
                    cibo = []
            finestra.addch(cibo[0], cibo [1], '*')
    
        else:
            ultimoPezzo = snake.pop()
            finestra.addch(ultimoPezzo[0], ultimoPezzo[1], ' ')

            finestra.addch(snake[0][0], snake [0][1], '*')
    curses.endwin()
    os.system('cls')
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("     _____                         ____                  ")
    print ("    / ____|                       / __ \                 ")
    print ("   | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __  ")
    print ("   | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| ")
    print ("   | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |    ")
    print ("    \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|    ")
    print("                         Points: " +str(punti))
    print (" ")
    print ("Thanks For playing")
    time.sleep(1)
    input("Press Enter to back to home ")
    os.system('cls')
