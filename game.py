import pygame
from calcs import dijkstra
from button import button

# Colours
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,128)
orange = (255,165,0)

# Grid dimensions
width = 20
height = 20

margin = 5

# Dijkstra parameters
start = (0,0)
finish = (19,19)
queue = [[0,start]]
wall = []
startLen = []
finishLen = []

# Button Parameters
startButton = False
finishButton = False
clearButton = False

# Creating the board
grid = []
for i in range(21):
    grid.append([])
    for j in range(21):
        if (j,i) in wall:
            grid[i].append(1)

        else:
            grid[i].append(0)


#finishx = int(input("Finish x: "))
#finishy = int(input("Finish y: "))
#finish = (4,4)

pygame.init()

# Creating the button
dijkstra_button = button(red,700,150,50,25,"Dijkstra")
start_button = button(green,700,200,50,25,"Start")
finish_button = button(blue,700,250,50,25,"Finish")
clear_button = button(orange,700,300,50,25,"Clear")

WINDOW_SIZE = [1200,540]
screen = pygame.display.set_mode(WINDOW_SIZE)
#DISPLAYSURF = pygame.display.set_mode((400, 300), pygame.FULLSCREEN)

pygame.display.set_caption("Pathfinder Algorithm")
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)


            if pos[0] > 700 and pos[0] < 750 and pos[1] > 150 and pos[1] < 175:
                startButton = False
                finishButton = False

                queue = [[0,start]]
                path = dijkstra(queue,wall,finish)

                for i in range(1,len(path)):
                    grid[path[i][1]][path[i][0]] = 3
                    print(path)

            elif pos[0] > 700 and pos[0] < 750 and pos[1] > 200 and pos[1] < 225:
                startButton = not startButton
                finishButton = False

            elif pos[0] > 700 and pos[0] < 750 and pos[1] > 250 and pos[1] < 275:
                startButton = False
                finishButton = not finishButton

            elif pos[0] > 700 and pos[0] < 750 and pos[1] > 300 and pos[1] < 325:

                walls = []

                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        grid[i][j] = 0
                

            elif (grid[row][column] == 0):
                            
                if startButton:
                    grid[row][column] = 2
                    start = (column,row)
                    startLen.append(start)

                    if len(startLen) != 1:
                        grid[startLen[0][1]][startLen[0][0]] = 0
                        startLen = [start]
                    

                elif finishButton:
                    grid[row][column] = 3
                    finish = (column,row)
                    finishLen.append(finish)

                    if len(finishLen) != 1:
                        grid[finishLen[0][1]][finishLen[0][0]] = 0
                        finishLen = [finish]

                else:
                    grid[row][column] = 1
                    wall.append((column,row))

            else:
                grid[row][column] = 0
                #wall.remove((column,row)) #Fix walls

    screen.fill(black)

    #pygame.draw.rect(screen, green, (600,150,100,50),"Dijkstra")

    
    for i in range(21):
        for j in range(21):

            if grid[i][j] == 0 or clear:
                colour = white

            elif grid[i][j] == 1:
                colour = red

            elif grid[i][j] == 2:
                colour = green

            elif grid[i][j] == 3:
                colour = blue
                
            pygame.draw.rect(screen,colour,[(margin + width) * j + margin,(margin + height) * i + margin,width,height])

    clear = False

    
    # 60 fps
    clock.tick(60)

    # Update the screen
    dijkstra_button.draw(screen)

    if startButton:
        start_button.draw(screen,orange)
    elif not startButton:
        start_button.draw(screen)

    if finishButton:
        finish_button.draw(screen,orange)
    elif not finishButton:
        finish_button.draw(screen)
        
    clear_button.draw(screen)
    pygame.display.update()

pygame.quit()
