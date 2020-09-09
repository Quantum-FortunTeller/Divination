# -*- coding: utf-8 -*-
"""
Spyder Editor

Bagua 
"""

import sys
import pygame
import time

from pygame.locals import QUIT

clock = pygame.time.Clock()
fps = 60
size = [200, 200]

HEIGHT = 8
WIDTH = 8
MINES = 7

BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)

pygame.init()
size = width, height = 1024, 984
screen = pygame.display.set_mode(size)
window_surface = pygame.display.set_mode((1024,984))


OPEN_SANS = "D:/QiskitHackathon/Divination/Bagua_asset/OpenSans-Regular.tff"
smallFont = pygame.font.Font(OPEN_SANS, 20)
mediumFont = pygame.font.Font(OPEN_SANS, 28)
largeFont = pygame.font.Font(OPEN_SANS, 40)
window_surface.fill((255, 255, 255))
bg = pygame.image.load("D:/QiskitHackathon/Divination/Bagua_asset/64.bmp")

    #INSIDE OF THE GAME LOOP
screen.blit(bg, (0, 0))



head_font = pygame.font.SysFont(None, 60)
button = pygame.Rect(100, 100, 50, 50)
instructions = True

while True:

   
 # Show game instructions
    if instructions:

        # Title
        title = largeFont.render("Quantum-Classic All-In-One Oracle Machine", True, BLACK)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Rules
        rules = [
            "In order to reveal prophecy",
            "First, select a mode",
            "Second, insert a question you wish to be answered",
            "Press REVEAL to get the prophercy:)"
        ]
        for i, rule in enumerate(rules):
            line = smallFont.render(rule, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 110 + 30 * i)
            screen.blit(line, lineRect)

        #Options
        option11 =["Hadamard Gate"]
        option12 =["U3 Gate"]
        option21 =["Just Measure"]
        option22 =["Stay Quantum"]
        option33 =["The Question"]
        for i, options11 in enumerate(option11):            #Hadamard
            line = smallFont.render(options11, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 5), 250 + 30 * i)
            screen.blit(line, lineRect)
        for i, options12 in enumerate(option12):            #U3 Gate
            line = smallFont.render(options12, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 5), 350 + 30 * i)
            screen.blit(line, lineRect)
        for i, options21 in enumerate(option21):            #Just Measure
            line = smallFont.render(options21, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2.5), 250 + 30 * i)
            screen.blit(line, lineRect)
        for i, options22 in enumerate(option22):            #Stay Quantum
            line = smallFont.render(options22, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2.5), 350 + 30 * i)
            screen.blit(line, lineRect)
        for i, options33 in enumerate(option33):            #The Question
            line = smallFont.render(options33, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 1.33), 250 + 30 * i)
            screen.blit(line, lineRect)



        # Play game button
        buttonRect = pygame.Rect((width / 4), (3 / 4) * height, width / 2, 60)
        buttonText = mediumFont.render("REVEAL", True, WHITE)
        buttonTextRect = buttonText.get_rect()
        buttonTextRect.center = buttonRect.center
        pygame.draw.rect(screen, BLACK, buttonRect)
        screen.blit(buttonText, buttonTextRect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if buttonRect.collidepoint(mouse):
                instructions = False
                time.sleep(0.3)
                
    for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    
    buttonRect11 = pygame.Rect((width / 8.9), 275, width / 6, 50)
    buttonRect12 = pygame.Rect((width / 8.9), 375, width / 6, 50)   
    buttonRect21 = pygame.Rect((width / 3.2), 275, width / 6, 50)   
    buttonRect22 = pygame.Rect((width / 3.2), 375, width / 6, 50)                   
    pygame.draw.rect(screen, [80, 90, 80], buttonRect11)  # draw button
    pygame.draw.rect(screen, [80, 90, 80], buttonRect12) 
    pygame.draw.rect(screen, [80, 90, 80], buttonRect21) 
    pygame.draw.rect(screen, [80, 90, 80], buttonRect22) 
    
    buttonRect33 = pygame.Rect((width / 1.8), 275, width / 2.5, 150)
    pygame.draw.rect(screen, [240, 240, 240], buttonRect33) #the quetion button
    
    
    
    pygame.display.update()
    clock.tick(fps)

 
    break

pygame.display.update()

while True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
       