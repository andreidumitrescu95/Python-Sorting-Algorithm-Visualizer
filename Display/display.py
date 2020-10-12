import pygame
from Helper.global_variables import *
from Helper.text_helper import drawTextcenter, drawText

pygame.init()

def update_display(win, height, color_height, numswaps, algorithm, number_of_elements, speed, time, running):
    
    win.fill(BLACK) 
    
    # call show method to display the list items 
    show(win, height, color_height, number_of_elements) 

    for i in range(15):
        pygame.draw.line(win, TURQUOISE, (0, 165+i), (WIDTH, 165+i))
        pygame.draw.line(win, TURQUOISE, (1060+i,0), (1060+i,165))
        pygame.draw.line(win, TURQUOISE, (730+i,0), (730+i,165))
        pygame.draw.line(win, TURQUOISE, (230+i,0), (230+i,165))

    drawTextcenter("Number of swaps: " + str(numswaps), pygame.font.SysFont('Calibri', 20), win, 100, 25, WHITE)
    drawTextcenter("Time elapsed: " + str(format(time, ".1f")) + "s", pygame.font.SysFont('Calibri', 20), win, 100, 75, WHITE)
    drawTextcenter("Algorithm used: " + algorithm, pygame.font.SysFont('Calibri', 20), win, 475, 25, WHITE)
    drawTextcenter("Number of elements: " + str(number_of_elements), pygame.font.SysFont('Calibri', 20), win, 900, 25, WHITE)
    drawTextcenter("Algorithm speed: " + speed, pygame.font.SysFont('Calibri', 20), win, 1225, 25, WHITE)

    button_start.draw(win)
    button_reset.draw(win)
    button_bubble_sort.draw(win)
    button_insertion_sort.draw(win)
    button_selection_sort.draw(win)
    button_merge_sort.draw(win)
    button_heap_sort.draw(win)
    button_quick_sort.draw(win)
    button_radix_sort.draw(win)
    button_todo4.draw(win)
    button_20.draw(win)
    button_50.draw(win)
    button_75.draw(win)
    button_100.draw(win)
    button_slow.draw(win)
    button_medium.draw(win)
    button_fast.draw(win)
    button_instant.draw(win)

    # create a time delay 
    if(running == True):
        delay = 0
        if(speed == "Slow"):
            delay = 5000
            pygame.time.delay(delay)
        if(speed == "Medium"):
            delay = 50
            pygame.time.delay(delay)
        if(speed == "Fast"):
            delay = 25
            pygame.time.delay(delay)
        if(speed == "No delay"):
            delay = 0
            
    # update the display 
    pygame.display.update() 

# method to show the list of height 
def show(win, height, color_height, number_of_elements): 
    
    if(number_of_elements != -1 and len(height) != 0):

        maximum_value = max(height)
        step = (WIDTH/len(height))

        for i in range(len(height)): 
            
            x = Button(step * (i+1), HEIGHT, -(step), -(height[i]/maximum_value)*3*HEIGHT/4, BLACK, color_height[i], str(height[i]), int(round(step - 20)))
            x.draw(win)    