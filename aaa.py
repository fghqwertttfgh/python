import pygame
import random

background = [[0 for _ in range(0,10)] for _ in range(0,22)]
background[0] = [1 for _ in range(0,10)]
all_bolck = [[0,0],[0,-1],[0,1],[0,2]]
select_block = all_bolck
block_initial_pos = [21,5]

def rcol():
    return((random.randint(1,255),random.randint(1,255),random.randint(1,255)))

def new_darw():
    y_drop,x_move = block_initial_pos
    for row,column in select_block:
        row += y_drop
        column += x_move
        pygame.draw.rect(sc,(0,0,0),(column * 25,500 - row * 25,23,23))

def  block_move_down():
    y_drop,x_move = block_initial_pos
    y_drop -= 1
    for row,column in select_block:
        row += y_drop
        column += x_move
        if background[row][column] == 1:
            break
    else:
        block_initial_pos.clear()
        block_initial_pos.extend([y_drop,x_move])

pygame.init()
sc = pygame.display.set_mode((250,500))
jg = 70
while True:
    sc.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if jg > 70:
        block_move_down()
        
        jg = 0
    else:
        jg += 1
    new_darw()
    pygame.time.Clock().tick(200)
    


    pygame.display.update()