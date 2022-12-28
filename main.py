import pygame
from pygame.locals import *

def round(map):
    newMap = []
    for i in range(len(map)):
        newMap.append([])
        for j in range(len(map)):
            surround = 0
            # j - 1
            try:
                if map[i-1][j-1] == 1 and i != 0 and j != 0:
                    surround +=1
            except IndexError:
                pass
            try:
                if map[i][j-1] == 1 and j != 0:
                    surround +=1
            except IndexError:
                pass
            try:
                if map[i+1][j-1] == 1 and j != 0:
                    surround +=1
            except IndexError:
                pass
            # j
            try:
                if map[i-1][j] == 1 and i != 0:
                    surround +=1
            except IndexError:
                pass
            try:
                if map[i+1][j] == 1:
                    surround +=1
            except IndexError:
                pass
            # j + 1
            try:
                if map[i-1][j+1] == 1 and i != 0:
                    surround +=1
            except IndexError:
                pass
            try:
                if map[i][j+1] == 1:
                    surround +=1
            except IndexError:
                pass
            try:
                if map[i+1][j+1] == 1:
                    surround +=1
            except IndexError:
                pass

            if map[i][j] == 0:
                if surround == 3:
                    newMap[i].append(1)
                else:
                    newMap[i].append(0)
            else:
                if surround == 2 or surround == 3:
                    newMap[i].append(1)
                else:
                    newMap[i].append(0)

    return newMap

def printMap(map):
    for i in range(len(map)):
        for j in range(len(map)):
            print(map[j][i], end=" ")
        print("\n", end="")
    print("\n")

def newMap(lenght):
    map = []
    for i in range(lenght):
        map.append([])
        for j in range(lenght):
            map[i].append(0)
    return map


def main():
    # variables init
    windowDim = [800, 800]
    backGroundColor = (0, 0, 0)
    backGroundColorTwo = (50, 50, 50)
    cellColor = (255, 255, 255)
    lenght = 40
    map = newMap(lenght)
    delta = 500
    deltaTime = 0
    play = False
    lastTime = pygame.time.get_ticks()

    # pygame init and config
    pygame.init()
    window = pygame.display.set_mode((windowDim[0], windowDim[1]))
    pygame.display.set_caption("window type")  # window's name

    # game loop
    stopped = False  # turn stopped to True to stop the program
    while not(stopped):

        # event browsing loop
        for event in pygame.event.get():

            # app exiting
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                stopped = True
            # ---event---
            if event.type == KEYDOWN and event.key == K_s:
                map = round(map)

            if event.type == KEYDOWN and event.key == K_SPACE:
                play = not(play)

            if event.type == KEYDOWN and event.key == K_DOWN:
                delta +=50

            if event.type == KEYDOWN and event.key == K_e:
                map = newMap(lenght)
                play = False

            if event.type == KEYDOWN and event.key == K_LEFT and lenght >1:
                lenght -= 1
                map = newMap(lenght)
                play = False
                print(lenght)

            if event.type == KEYDOWN and event.key == K_RIGHT and lenght < windowDim[0]:
                lenght += 1
                map = newMap(lenght)
                play = False
                print(lenght)

            if event.type == KEYDOWN and event.key == K_UP and delta >50:
                delta -=50

            if event.type == MOUSEBUTTONDOWN:

                try:
                    if event.button == 1:
                        map[event.pos[0]//(windowDim[0]//lenght)][event.pos[1]//(windowDim[1]//lenght)] = 1
                    elif event.button == 3:
                        map[event.pos[0]//(windowDim[0]//lenght)][event.pos[1]//(windowDim[1]//lenght)] = 0
                except IndexError:
                    print("index out of range")
        # ---update---
        newTime = pygame.time.get_ticks()
        deltaTime += newTime - lastTime
        lastTime = newTime
        if play and deltaTime >= delta:
            map = round(map)
            deltaTime = 0


        # ---draw---
        window.fill(backGroundColor)

        for i in range(lenght):
            for j in range(lenght):
                if (i%2 == 0 and j %2 == 0) or (i%2 == 1 and j %2 == 1):
                    pygame.draw.rect(window, backGroundColorTwo, (windowDim[0]//lenght * j, windowDim[1]//lenght * i, windowDim[0]//lenght, windowDim[1]//lenght))





        for i in range(lenght):
            for j in range(lenght):
                if map [j][i] == 1:
                    pygame.draw.rect(window, cellColor, (windowDim[0]//lenght * j, windowDim[1]//lenght * i, windowDim[0]//lenght, windowDim[1]//lenght))

        # window refresh
        pygame.display.flip()






if __name__ == "__main__":
    main()
