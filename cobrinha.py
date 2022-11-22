
import pygame, random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

400
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cobrinha')

cobra = [(200, 200), (210, 200), (220,200)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((000,255,000)) 



my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
pontos = 0

fim_de_jogo = False
while not fim_de_jogo:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
    
        
    
    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        fim_de_jogo = True
        break
    
    
    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            fim_de_jogo = True
            break

    if fim_de_jogo:
        break
    
    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
        
    
    if my_direction == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if my_direction == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if my_direction == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if my_direction == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    

    
    for x in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    

    for pos in cobra:
        screen.blit(cobra_skin,pos)

    pygame.display.update()

