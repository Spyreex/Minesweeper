import pygame
import random
import time
from tkinter import *
sys.setrecursionlimit(100000)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MOREWHITE = (150, 150, 150)

VIOLET = (148, 0, 211)
INDIGO = (75, 0, 130)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)
RED = (255, 0, 0)

DARKERRED = (155, 0, 0)


def grid():
    global starty
    global startx
    global start2
    starty = int(entryY.get())
    startx = int(entryX.get())
    start2 = int(entryBomb.get())
    WIDTH = HEIGHT = int(entryWidth.get())
    MARGIN = int(entryMargin.get())
    startHelp = entryStartHelp.get()

    buttonRecord.grid_remove()
    buttonHelp.grid_remove()

    global layout
    layout = []
    for row in range(starty):
        # Add an empty array that will hold each cell
        # in this row
        layout.append([])
        for column in range(startx):
            layout[row].append(0)  # Append a cell
    count = initiate()
    where(startHelp, WIDTH, HEIGHT, MARGIN)
    startGame(WIDTH, HEIGHT, MARGIN, count)


def initiate():
    count = 0
    for row in range(starty):
        for column in range(startx):
            randomInt = random.randint(1, start2)
            if randomInt == 1:
                bomb = 9
                count += 1
            else:
                bomb = 0
            layout[row][column] = bomb
    if starty*startx/start2 > count:
        count = initiate()

    bombLeft.set(count)
    labelBombLeft.update()
    return count


def initiate2(WIDTH, HEIGHT, MARGIN, startHelp):
    count = 0
    for row in range(starty):
        for column in range(startx):
            randomInt = random.randint(1, start2)
            if randomInt == 1:
                bomb = 9
                count += 1
            else:
                bomb = 0
            layout[row][column] = bomb
    if starty*startx/start2 > count:
        count = initiate2(WIDTH, HEIGHT, MARGIN, startHelp)

    bombLeft.set(count)
    labelBombLeft.update()
    where(startHelp, WIDTH, HEIGHT, MARGIN)
    startGame(WIDTH, HEIGHT, MARGIN, count)


def where(startHelp, WIDTH, HEIGHT, MARGIN):
    for row in range(starty):
        for column in range(startx):
            onlyCheck = 0
            if row == 0:
                onlyCheck += 1
            elif row == starty-1:
                onlyCheck += 4
            if column == 0:
                onlyCheck += 2
            elif column == startx-1:
                onlyCheck += 8
            if layout[row][column] == 9:
                check(row, column, onlyCheck, WIDTH, HEIGHT, MARGIN, startHelp)
            else:
                layout[row][column] = check(row, column, onlyCheck, WIDTH, HEIGHT, MARGIN, startHelp)
    if startHelp == 'Y':
        startHelper(WIDTH, HEIGHT, MARGIN, startHelp)

# WARNING: SPAGHETTI CODE BELOW, DIRECTIONS ARE NOT WHAT THEY ARE SUPPOSED TO BE


def check(row, column, onlyCheck, WIDTH, HEIGHT, MARGIN, startHelp):
    bombCount = 0
    if onlyCheck == 0:
        bombCount = checkLeft(row, column, 9) + checkDown(row, column, 9) + checkDownLeft(row, column, 9) + checkDownRight(row,
        column, 9) + checkRight(row, column, 9) + checkUp(row, column, 9) + checkUpLeft(row, column, 9) + checkUpRight(row, column, 9)
        if bombCount == 8:
            initiate2(WIDTH, HEIGHT, MARGIN, startHelp)
    if onlyCheck == 1:
        bombCount = checkDown(row, column, 9) + checkDownRight(row, column, 9) + checkRight(row, column, 9) + checkUp(row,
        column, 9) + checkUpRight(row, column, 9)
        if bombCount == 5:
            initiate2(WIDTH, HEIGHT, MARGIN, startHelp)
    if onlyCheck == 2:
        bombCount = checkLeft(row, column, 9) + checkDown(row, column, 9) + checkDownLeft(row, column, 9) + checkDownRight(row,
        column, 9) + checkRight(row, column, 9)
        if bombCount == 5:
            initiate2(WIDTH, HEIGHT, MARGIN, startHelp)
    if onlyCheck == 3:
        bombCount = checkDown(row, column, 9) + checkDownRight(row, column, 9) + checkRight(row, column, 9)
        if bombCount == 3:
            initiate2(WIDTH, HEIGHT, MARGIN, startHelp)
    if onlyCheck == 4:
        bombCount = checkLeft(row, column, 9) + checkDown(row, column, 9) + checkDownLeft(row, column, 9) + checkUp(row,
        column, 9) + checkUpLeft(row, column, 9)
        if bombCount == 5:
            initiate2(WIDTH, HEIGHT, MARGIN, startHelp)
    if onlyCheck == 6:
        bombCount = checkLeft(row, column, 9) + checkDown(row, column, 9) + checkDownLeft(row, column, 9)
        if bombCount == 3:
            initiate2(WIDTH, HEIGHT, MARGIN, startHelp)
    if onlyCheck == 8:
        bombCount = checkLeft(row, column, 9) + checkUp(row, column, 9) + checkUpLeft(row, column, 9) + checkUpRight(row,
        column, 9) + checkRight(row, column, 9)
        if bombCount == 5:
            initiate2(WIDTH, HEIGHT, MARGIN, startHelp)
    if onlyCheck == 9:
        bombCount = checkRight(row, column, 9) + checkUp(row, column, 9) + checkUpRight(row, column, 9)
        if bombCount == 3:
            initiate2(WIDTH, HEIGHT, MARGIN, startHelp)
    if onlyCheck == 12:
        bombCount = checkLeft(row, column, 9) + checkUp(row, column, 9) + checkUpLeft(row, column, 9)
        if bombCount == 3:
            initiate2(WIDTH, HEIGHT, MARGIN, startHelp)
    return bombCount


def startHelper(WIDTH, HEIGHT, MARGIN, startHelp):
    zeroList = []
    for row in range(starty):
        for column in range(startx):
            if layout[row][column] == 0:
                if row != 0 and row != starty-1 and column != 0 and column != startx-1:
                    zeroList.append([row, column])
    random.shuffle(zeroList)
    try:
        layout[zeroList[0][0]][zeroList[0][1]] = 99
    except:
        initiate2(WIDTH, HEIGHT, MARGIN, startHelp)


def checkLeft(row, column, number):
    if layout[row-1][column] == number:
        return int(1)
    else:
        return int(0)


def checkUpLeft(row, column, number):
    if layout[row-1][column - 1] == number:
        return int(1)
    else:
        return int(0)


def checkDownLeft(row, column, number):
    if layout[row-1][column + 1] == number:
        return int(1)
    else:
        return int(0)


def checkUp(row, column, number):
    if layout[row][column - 1] == number:
        return int(1)
    else:
        return int(0)


def checkDown(row, column, number):
    if layout[row][column + 1] == number:
        return int(1)
    else:
        return int(0)


def checkUpRight(row, column, number):
    if layout[row+1][column - 1] == number:
        return int(1)
    else:
        return int(0)


def checkRight(row, column, number):
    if layout[row + 1][column] == number:
        return int(1)
    else:
        return int(0)


def checkDownRight(row, column, number):
    if layout[row+1][column + 1] == number:
        return int(1)
    else:
        return int(0)


def check2(row, column, onlyCheck):
    if onlyCheck == 0:
        checkUpLeft2(row, column)
        checkDownLeft2(row, column)
        checkDownRight2(row, column)
        checkUpRight2(row, column)
        checkDown2(row, column)
        checkLeft2(row, column)
        checkRight2(row, column)
        checkUp2(row, column)
    if onlyCheck == 1:
        checkDown2(row, column)
        checkDownRight2(row, column)
        checkRight2(row, column)
        checkUpRight2(row, column)
        checkUp2(row, column)
    if onlyCheck == 2:
        checkLeft2(row, column)
        checkDown2(row, column)
        checkDownLeft2(row, column)
        checkDownRight2(row, column)
        checkRight2(row, column)
    if onlyCheck == 3:
        checkDown2(row, column)
        checkDownRight2(row, column)
        checkRight2(row, column)
    if onlyCheck == 4:
        checkUpLeft2(row, column)
        checkDownLeft2(row, column)
        checkDown2(row, column)
        checkLeft2(row, column)
        checkUp2(row, column)
    if onlyCheck == 6:
        checkDownLeft2(row, column)
        checkDown2(row, column)
        checkLeft2(row, column)
    if onlyCheck == 8:
        checkUpLeft2(row, column)
        checkUpRight2(row, column)
        checkLeft2(row, column)
        checkRight2(row, column)
        checkUp2(row, column)
    if onlyCheck == 9:
        checkUpRight2(row, column)
        checkRight2(row, column)
        checkUp2(row, column)
    if onlyCheck == 12:
        checkUpLeft2(row, column)
        checkLeft2(row, column)
        checkUp2(row, column)


def checkUpRight2(row, column):
    if checkUpRight(row, column, 0) == 1:
        fill(row + 1, column - 1)
    elif layout[row + 1][column - 1] in range(1, 9):
        layout[row + 1][column - 1] += 10


def checkUp2(row, column):
    if checkUp(row, column, 0) == 1:
        fill(row, column-1)
    elif layout[row][column-1] in range(1, 9):
        layout[row][column - 1] += 10


def checkRight2(row, column):
    if checkRight(row, column, 0) == 1:
        fill(row+1, column)
    elif layout[row+1][column] in range(1, 9):
        layout[row + 1][column] += 10


def checkUpLeft2(row, column):
    if checkUpLeft(row, column, 0) == 1:
        fill(row-1, column-1)
    elif layout[row-1][column-1] in range(1, 9):
        layout[row - 1][column - 1] += 10


def checkDownRight2(row, column):
    if checkDownRight(row, column, 0) == 1:
        fill(row+1, column+1)
    elif layout[row+1][column+1] in range(1, 9):
        layout[row + 1][column + 1] += 10


def checkDownLeft2(row, column):
    if checkDownLeft(row, column, 0) == 1:
        fill(row-1, column+1)
    elif layout[row-1][column+1] in range(1, 9):
        layout[row - 1][column + 1] += 10


def checkLeft2(row, column):
    if checkLeft(row, column, 0) == 1:
        fill(row-1, column)
    elif layout[row-1][column] in range(1, 9):
        layout[row - 1][column] += 10


def checkDown2(row, column):
    if checkDown(row, column, 0) == 1:
        fill(row, column+1)
    elif layout[row][column+1] in range(1, 9):
        layout[row][column + 1] += 10


def fill(row, column):
    layout[row][column] += 10
    onlyCheck = 0
    if row == 0:
        onlyCheck += 1
    elif row == starty - 1:
        onlyCheck += 4
    if column == 0:
        onlyCheck += 2
    elif column == startx - 1:
        onlyCheck += 8
    check2(row, column, onlyCheck)


def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!?")
    label = Label(popup, text=msg)
    label.pack()
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


def popup():
    popupmsg('Width: How many tiles wide\nHeigth: How many tiles high\n1 out of ?: 1 out of x tiles is a bomb (has to be above or 2)\nGrid Size: Size of the tiles (numbers will only appear for multiplications of 5 and lower than or 30\nMargin: Space between the tiles\nStart Help Y/N: Get a free gray starting tile for QOL sake (answer only with Y or N')


def records():
    recordwindow = Tk()
    recordwindow.title('Records')

    list = []

    with open('records','r') as file:
        lines = file.readlines()
        for line in lines:
            list.append(line)

        list2 = []

        counter2 = 0

        for x in range(list.count('---\n')):
            list2.append([])
            y = ''
            while y != '---\n':
                y = list[counter2]
                counter2 += 1
                list2[x].append(0)

        counter = 0
        counter4 = 0
        for item in list:
            done = 0
            if counter >= 3:
                if item == '~~~\n':
                    done = 1
                    list2[counter4][counter] = item.strip("~~~\n")
                    counter += 1
            if counter >= 1 and done == 0:
                if item != '---\n' and item != '\n':
                    if item == '~~~\n':
                        done = 1
                        list2[counter4][counter] = '\t'
                        counter += 1
                    else:
                        item = item.replace(':', '|', 1)
                        done = 1
                        list2[counter4][counter] = item.strip("\n") + '     '
                        counter += 1
            if item != '---\n' and done == 0:
                list2[counter4][counter] = item.strip("\n")
                counter += 1
            elif done == 0:
                list2[counter4][counter] = item.strip('---')
                counter4 += 1
                counter = 0


    allitems = ''
    for catagories in list2:
        for ccount in range(len(catagories)):
            allitems += catagories[ccount]

    varRecord = allitems

    Label(recordwindow, text=varRecord, font=('Ariel', 15), justify='left').pack()

    recordwindow.update()
    recordwindow.mainloop()


class Window(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.popupmsg2()


    def popupmsg2(self):
        label = Label(master=self, text="Enter your name.")
        label.grid(row=0, column=1)
        self.entryName = Entry(master=self, width=20)
        self.entryName.grid(row=1, column=1)
        B2 = Button(master=self, text="Submit", command=self.writeRecord)
        B2.grid(row=2, column=0)
        B3 = Button(master=self, text="Restart", command=self.destroy)
        B3.grid(row=2, column=2)


    def writeRecord(self):
        list = []
        list2 = []

        timeEnd = timeTotal.get()
        timings = timeEnd.split(":")
        hours = int(timings[0])
        minutes = int(timings[1])
        seconds = round(int(float(timings[2])))
        millis = (int((float(timings[2]))*1000%1000))
        name = self.entryName.get()

        record = open('records','r')
        lines = record.readlines()
        record.close()

        for line in lines:
            list.append(line)
        counter2 = 0

        for x in range(list.count('---\n')):
            list2.append([])
            y = ''
            while y != '---\n':
                y = list[counter2]
                counter2 += 1
                list2[x].append(0)

        counter = 0
        counter4 = 0
        for item in list:
            list2[counter4][counter] = item.strip("\n")
            counter += 1
            if item == '---\n':
                counter4 += 1
                counter = 0

        counterList = 0
        newCat = 0

        for catagories in list2:
            catagory = catagories[0]
            indi = catagory.split(';')

            if indi[0] == str(startx) and indi[1] == str(starty) and indi[2] == str(start2):
                newCat = 1
                counter3 = 0
                done = 0
                for times in range(2, len(list2[counterList])-3):
                    counter3 += 1
                    indivi = list2[counterList][times].split(":")
                    if hours == int(indivi[1]):
                        if minutes == int(indivi[2]):
                            if seconds == int(indivi[3]):
                                if millis == int(indivi[4]):
                                    list2[counterList][counter3 + 1:counter3 + 1] = [
                                        '{}:{}:{}:{}:{}'.format(name, hours, minutes, seconds, millis)]
                                    done = 1
                                    break
                                elif millis < int(indivi[4]):
                                    list2[counterList][counter3 + 1:counter3 + 1] = [
                                        '{}:{}:{}:{}:{}'.format(name, hours, minutes, seconds, millis)]
                                    done = 1
                                    break
                            elif seconds < int(indivi[3]):
                                list2[counterList][counter3 + 1:counter3 + 1] = [
                                    '{}:{}:{}:{}:{}'.format(name, hours, minutes, seconds, millis)]
                                done = 1
                                break
                        elif minutes < int(indivi[2]):
                            list2[counterList][counter3 + 1:counter3 + 1] = [
                                '{}:{}:{}:{}:{}'.format(name, hours, minutes, seconds, millis)]
                            done = 1
                            break
                    elif hours < int(indivi[1]):
                        list2[counterList][counter3 + 1:counter3 + 1] = [
                            '{}:{}:{}:{}:{}'.format(name, hours, minutes, seconds, millis)]
                        done = 1
                        break
                if done == 0:
                    list2[counterList][counter3 + 2:counter3 + 2] = [
                        '{}:{}:{}:{}:{}'.format(name, hours, minutes, seconds, millis)]
            counterList += 1

        if newCat == 0:
            list2.append([])
            list2[-1].append('{};{};{}'.format(startx, starty, start2))
            list2[-1].append('~~~')
            list2[-1].append('{}:{}:{}:{}:{}'.format(name, hours, minutes, seconds, millis))
            list2[-1].append('~~~')
            list2[-1].append('')
            list2[-1].append('---')

        write = open('records','w')
        string = ''
        for qq in range(len(list2)):
            for alllines in list2[qq]:
                string += str(alllines) + '\n'
        write.write(string)
        write.close()
        self.destroy()


def startGame(WIDTH, HEIGHT, MARGIN, count):

    beginCount = count

    timeMilli = 0
    timerStop = 0

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    # size = [255, 255]
    size = [(WIDTH + MARGIN) * startx + MARGIN, (HEIGHT + MARGIN) * starty + MARGIN]
    screen = pygame.display.set_mode(size)

    # Set title of screen
    pygame.display.set_caption("Minesweeper")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                if event.button == 1:
                    if layout[row][column] == 0 or layout[row][column] == 99:
                        if timeMilli == 0:
                            timeMilli = round(time.time() * 1000)
                        fill(row, column)

                    if layout[row][column] in range(1, 8):
                        if timeMilli == 0:
                            timeMilli = round(time.time() * 1000)
                        layout[row][column] += 10
                    if layout[row][column] == 9:
                        print('you ded')
                        buttonRecord.grid()
                        buttonHelp.grid()
                        timerStop = 1
                        for row in range(starty):
                            for column in range(startx):
                                if layout[row][column] == 9:
                                    layout[row][column] = 100
                if event.button == 3:
                    if layout[row][column] in range(0, 10):
                        layout[row][column] += 20
                        count -= 1
                        bombLeft.set(count)
                        bombCounter = 0
                        for row in range(starty):
                            for column in range(startx):
                                if layout[row][column] == 29:
                                    bombCounter += 1
                        if bombCounter == beginCount and count == 0:
                            timerStop = 1
                            buttonRecord.grid()
                            buttonHelp.grid()
                            window = Window()
                            window.title('Home')
                            window.mainloop()

                    elif layout[row][column] in range(20, 30):
                        layout[row][column] -= 20
                        count += 1
                        bombLeft.set(count)

        # Set the screen background

        screen.fill(BLACK)

        # Draw the grid
        for row in range(starty):
            for column in range(startx):

                clicked = 0
                img = ''
                color = WHITE
                if WIDTH % 5 == 0:

                    if layout[row][column] == 10:
                        color = MOREWHITE
                    if layout[row][column] == 11:
                        clicked = 1
                        try:
                            img = pygame.image.load(str(WIDTH) + '/1.png')
                        except:
                            img = pygame.image.load(str(WIDTH) + '\1.png')
                    if layout[row][column] == 12:
                        clicked = 1
                        try:
                            img = pygame.image.load(str(WIDTH) + '/2.png')
                        except:
                            img = pygame.image.load(str(WIDTH) + '\2.png')
                    if layout[row][column] == 13:
                        clicked = 1
                        try:
                            img = pygame.image.load(str(WIDTH) + '/3.png')
                        except:
                            img = pygame.image.load(str(WIDTH) + '\3.png')
                    if layout[row][column] == 14:
                        clicked = 1
                        try:
                            img = pygame.image.load(str(WIDTH) + '/4.png')
                        except:
                            img = pygame.image.load(str(WIDTH) + '\4.png')
                    if layout[row][column] == 15:
                        clicked = 1
                        try:
                            img = pygame.image.load(str(WIDTH) + '/5.png')
                        except:
                            img = pygame.image.load(str(WIDTH) + '\5.png')
                    if layout[row][column] == 16:
                        clicked = 1
                        try:
                            img = pygame.image.load(str(WIDTH) + '/6.png')
                        except:
                            img = pygame.image.load(str(WIDTH) + '\6.png')
                    if layout[row][column] == 17:
                        clicked = 1
                        try:
                            img = pygame.image.load(str(WIDTH) + '/7.png')
                        except:
                            img = pygame.image.load(str(WIDTH) + '\7.png')
                    if layout[row][column] == 99:
                        color = MOREWHITE
                    if layout[row][column] == 109:
                        color = MOREWHITE
                    if layout[row][column] == 100:
                        color = DARKERRED

                    if layout[row][column] in range(20, 30):
                        color = BLACK
                else:
                    if layout[row][column] == 10:
                        color = MOREWHITE
                    if layout[row][column] == 11:
                        color = VIOLET
                    if layout[row][column] == 12:
                        color = INDIGO
                    if layout[row][column] == 13:
                        color = BLUE
                    if layout[row][column] == 14:
                        color = GREEN
                    if layout[row][column] == 15:
                        color = YELLOW
                    if layout[row][column] == 16:
                        color = ORANGE
                    if layout[row][column] == 17:
                        color = RED
                    if layout[row][column] == 99:
                        color = MOREWHITE
                    if layout[row][column] == 109:
                        color = MOREWHITE
                    if layout[row][column] == 100:
                        color = DARKERRED

                    if layout[row][column] in range(20, 30):
                        color = BLACK

                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

                if clicked == 1:
                    screen.blit(img, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))

        if timeMilli != 0 and timerStop == 0:
            timer = round(time.time() * 1000) - timeMilli
            timeTotal.set("{}:{}:{}.{}".format(timer // 3600000, (timer - timer // 3600000 * 3600000) // 60000,
                                       (timer - timer // 60000 * 60000) // 1000, timer % 1000))
        root.update()

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.

    pygame.quit()


root = Tk()
root.title('Minesweeper')
labelX = Label(root, width=10, text="Width")
entryX = Entry(root, width=10)
labelY = Label(root, width=10, text="Height")
entryY = Entry(root, width=10)
labelBomb = Label(root, width=10, text="1 out of ?")
entryBomb = Entry(root, width=10)
labelWidth = Label(root, width=10, text="Grid Size")
entryWidth = Entry(root, width=10)
labelMargin = Label(root, width=10, text="Margin")
entryMargin = Entry(root, width=10)
labelStartHelp = Label(root, width=10, text="Start Help Y/N")
entryStartHelp = Entry(root, width=10)

labelX.grid(row=0, column=0)
entryX.grid(row=0, column=2)
labelY.grid(row=1, column=0)
entryY.grid(row=1, column=2)
labelBomb.grid(row=2, column=0)
entryBomb.grid(row=2, column=2)
labelWidth.grid(row=3, column=0)
entryWidth.grid(row=3, column=2)
labelMargin.grid(row=5, column=0)
entryMargin.grid(row=5, column=2)
labelStartHelp.grid(row=6, column=0)
entryStartHelp.grid(row=6, column=2)

buttonStart = Button(root, text="Baguette", command=grid)
buttonStart.grid(row=7, column=0)
buttonRecord = Button(root, text="Records", command=records)
buttonRecord.grid(row=7, column=1)
buttonHelp = Button(root, text="?", width=8, command=popup)
buttonHelp.grid(row=7, column=2)
timeTotal = StringVar()
bombLeft = StringVar()
labelTime = Label(root, textvariable=timeTotal, font=("Ariel", 30))
labelTime.grid(row=8, column=1)
timeTotal.set('0:0:0.000')
labelBombLeft = Label(root, textvariable=bombLeft, font=("Ariel", 30))
labelBombLeft.grid(row=9, column=1)
bombLeft.set('0')
root.update()
root.mainloop()
