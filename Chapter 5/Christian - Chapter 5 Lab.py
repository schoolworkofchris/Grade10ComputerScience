# Christmas Tree Developed By Chris

# Imports
import pygame
pygame.init()


# Colors
TREE_COLOR = (0, 150, 0)
WHITE = (255, 255, 255)
BROWN = (75, 10, 25)
RED = (255, 0, 0)
SKY = (132, 249, 255)

# Vars
done = False

# Window Managment
res = (1920, 1080)
window = pygame.display.set_mode(res)
pygame.display.set_caption("Christmas Tree by Christian")
clock = pygame.time.Clock()

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.QUIT
        elif event.type == pygame.KEYUP:
            print("Up")

    window.fill(WHITE)
    pygame.draw.rect(window, TREE_COLOR, [810, 250, 300, 650], 0)
    pygame.draw.rect(window, SKY, [0, 0, 1920, 725], 0)
    pygame.draw.polygon(window, TREE_COLOR, [[960, 70], [680, 300], [1230, 300]])
    pygame.draw.polygon(window, TREE_COLOR, [[580, 500], [960, 150], [1330, 500]])
    pygame.draw.polygon(window, TREE_COLOR, [[480, 700], [960, 270], [1430, 700]])
    pygame.draw.polygon(window, TREE_COLOR, [[380, 930], [960, 380], [1530, 930]])
    pygame.draw.rect(window, BROWN, [925, 930, 70, 110], 0)
    pygame.draw.circle(window, RED, [950, 200], 35, 0)
    pygame.draw.circle(window, RED, [800, 400], 35, 0)
    pygame.draw.circle(window, RED, [950, 400], 35, 0)
    pygame.draw.circle(window, RED, [1100, 400], 35, 0)
    pygame.draw.circle(window, RED, [875, 600], 35, 0)
    pygame.draw.circle(window, RED, [1025, 600], 35, 0)
    pygame.draw.circle(window, RED, [700, 600], 35, 0)
    pygame.draw.circle(window, RED, [1200, 600], 35, 0)
    pygame.draw.circle(window, RED, [775, 800], 35, 0)
    pygame.draw.circle(window, RED, [1100, 800], 35, 0)
    pygame.draw.circle(window, RED, [950, 800], 35, 0)
    pygame.draw.circle(window, RED, [625, 800], 35, 0)
    pygame.draw.circle(window, RED, [1250, 800], 35, 0)
    pygame.display.flip()


    clock.tick(60)

pygame.QUIT