import pygame
from Helper.global_variables import *
from Helper.text_helper import drawTextcenter, drawText

pygame.init()

def update_display(win, height, numswaps, algorithm, number_of_elements, speed):
    
    win.fill((0, 0, 0)) 
    
    # call show method to display the list items 
    show(win, height, number_of_elements) 

    drawTextcenter("Number of swaps: " + str(numswaps), pygame.font.SysFont('Calibri', 20), win, 100, 25, WHITE)
    drawTextcenter("Algorithm used: " + algorithm, pygame.font.SysFont('Calibri', 20), win, 375, 25, WHITE)
    drawTextcenter("Number of elements: " + str(number_of_elements), pygame.font.SysFont('Calibri', 20), win, 900, 25, WHITE)
    drawTextcenter("Algorithm speed: " + speed, pygame.font.SysFont('Calibri', 20), win, 1225, 25, WHITE)

    button_start.draw(win)
    button_reset.draw(win)
    button_bubble_sort.draw(win)
    button_insertion_sort.draw(win)
    button_selection_sort.draw(win)
    button_merge_sort.draw(win)
    button_20.draw(win)
    button_50.draw(win)
    button_75.draw(win)
    button_100.draw(win)
    button_slow.draw(win)
    button_medium.draw(win)
    button_fast.draw(win)
    button_instant.draw(win)

    # create a time delay 
    delay = 0
    if(speed == "Slow"):
        delay = 50
    if(speed == "Medium"):
        delay = 25
    if(speed == "Fast"):
        delay = 10
    if(speed == "No delay"):
        delay = 0
    pygame.time.delay(delay) 
    
    # update the display 
    pygame.display.update() 

# method to show the list of height 
def show(win, height, number_of_elements): 
      
    if(number_of_elements != -1 and len(height) != 0):

        maximum_value = max(height)
        step = (WIDTH/len(height))

        for i in range(len(height)): 
    
            x = Button(step * (i+1), HEIGHT, -(step-10), -(height[i]/maximum_value)*3*HEIGHT/4, BLACK, TURQUOISE, str(height[i]), int(round(step - 20)))
            x.draw(win)
            #font = pygame.font.SysFont('Arial', int(round(step - 13)))
            #text = font.render(str(height[i]), False, (255, 0, 0))
            #rectangle = pygame.draw.rect(win, (255, 255, 0), (step * (i+1), HEIGHT, -(step-10), -(height[i]/maximum_value)*3*HEIGHT/4)) 
            #text_rect = text.get_rect(center=(step * (i+1) - (step-10)/2, HEIGHT - 10))
            #win.blit(text, text_rect)