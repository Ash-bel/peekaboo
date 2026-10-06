import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Peekaboo')
clock = pygame.time.Clock()
sky_surface  = pygame.image.load("C:/Users/ANUSHKA DEODHAR/Downloads/Sky.png").convert()
ground_surface = pygame.image.load("C:/Users/ANUSHKA DEODHAR/Downloads/ground.png").convert()
test_font = pygame.font.Font("C:/Users/ANUSHKA DEODHAR/Downloads/Pixeltype.ttf", 50)
text_surface = test_font.render('My Game', False, 'Black')
snail_surface = pygame.image.load("C:/Users/ANUSHKA DEODHAR/Downloads/snail1.png").convert_alpha()
snail_x_position = 600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #draw all elements
    #update everything
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface, (300,50))
    snail_x_position -= 4
    if snail_x_position < -100:
        snail_x_position = 800
    screen.blit(snail_surface,(snail_x_position,250))
    pygame.display.update()
    clock.tick(60)