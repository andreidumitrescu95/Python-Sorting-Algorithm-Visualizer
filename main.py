# importing pygame 
import pygame 
import sys
sys.path.append(".")
import winsound
from Helper.button_helper import Button
from Helper.text_helper import drawText, drawTextcenter
from Helper.input_helper import InputBox
from Helper.input_generator import generate_random_input
from Helper.global_variables import *

pygame.init() 
  
# setting window size 
WIDTH = 1366
HEIGHT = 768

# white color 
WHITE = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100)

win = pygame.display.set_mode((WIDTH, HEIGHT)) 
 
# setting title to the window 
pygame.display.set_caption("Sorting Algorithms Visualizer") 

# initial position 
x = 40
y = 40
  
# width of each bar 
width = 10

def merge_sort(height):
    """
    height of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    """
    if len(height) < 2:
        return height

    mid = len(height) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_height = merge_sort(height[:mid])
    right_height = merge_sort(height[mid:])

    return merge(left_height, right_height)

def merge(left, right):
    """
    Traverse both sorted sub-heightays (left and right), and populate the height heightay
    """
    height = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            height.append(left[i])
            i += 1
        else:
            height.append(right[j])
            j += 1
    height += left[i:]
    height += right[j:]

    #update_display(50)

    return height

def insertion_sort(height, numswaps, algorithm, number_of_elements, speed): 
  
    # Traverse through 1 to len(height) 
    for i in range(1, len(height)): 
  
        key = height[i] 
  
        # Move elements of height[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < height[j] : 
                height[j + 1] = height[j] 
                j -= 1
                numswaps = numswaps + 1
                update_display(height, numswaps, algorithm, number_of_elements, speed)
        height[j + 1] = key 

def selection_sort_swap(index1, index2, height, numswaps):
    
    aux = height[index1]
    height[index1] = height[index2]
    height[index2] = aux
    numswaps = numswaps + 1
    return numswaps
    ##if(index1>index2):
    #    winsound.Beep(int(height[index1]/height[index2])*100, 100)
    #else:
    #    winsound.Beep(int(height[index2]/height[index1])*100, 100)

def selection_sort(height, numswaps, algorithm, number_of_elements, speed):

    for i in range(0, len(height) -1):

        min = i

        for j in range(i+1, len(height)):

            if(height[j] < height[min]):

                min = j

        numswaps = selection_sort_swap(min, i, height, numswaps)        
        update_display(height, numswaps, algorithm, number_of_elements, speed)

def bubble_sort_swap(index, height, numswaps):
    
    aux = height[index]
    height[index] = height[index+1]
    height[index+1] = aux
    numswaps = numswaps + 1
    return numswaps   

def bubble_sort(height, numswaps, algorithm, number_of_elements, speed):

    swap_occurred = 0;

    for i in range(len(height)-1):

        for j in range(len(height)-1):

            if(height[i] > height[i+1]):

                swap_occurred = 1;
                
                numswaps = bubble_sort_swap(i, height, numswaps) 
                update_display(height, numswaps, algorithm, number_of_elements, speed)                               
    
    if(swap_occurred == 1):
        bubble_sort(height, numswaps, algorithm, number_of_elements, speed)

def update_display(height, numswaps, algorithm, number_of_elements, speed):

    win.fill((0, 0, 0)) 
    
    # call show method to display the list items 
    show(height, numswaps, number_of_elements) 

    drawTextcenter("Number of swaps: " + str(numswaps), pygame.font.SysFont('Calibri', 20), win, 100, 25, WHITE)
    drawTextcenter("Algorithm used: " + algorithm, pygame.font.SysFont('Calibri', 20), win, 375, 25, WHITE)
    drawTextcenter("Number of elements: " + str(number_of_elements), pygame.font.SysFont('Calibri', 20), win, 750, 25, WHITE)
    drawTextcenter("Algorithm speed: " + speed, pygame.font.SysFont('Calibri', 20), win, 1100, 25, WHITE)

    button_start.draw(win)
    button_reset.draw(win)
    button_bubble_sort.draw(win)
    button_insertion_sort.draw(win)
    button_selection_sort.draw(win)
    button_merge_sort.draw(win)
    button_20.draw(win)
    button_50.draw(win)
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
def show(height, numswaps, number_of_elements): 
      
    if(number_of_elements != -1 and len(height) != 0):

        maximum_value = max(height)
        step = (WIDTH/len(height))

        for i in range(len(height)): 
    
            font = pygame.font.SysFont('Arial', int(round(step - 13)))
            text = font.render(str(height[i]), False, (255, 0, 0))
            rectangle = pygame.draw.rect(win, (255, 255, 0), (step * (i+1), HEIGHT, -(step-10), -(height[i]/maximum_value)*3*HEIGHT/4)) 
            text_rect = text.get_rect(center=(step * (i+1) - (step-10)/2, HEIGHT - 10))
            win.blit(text, text_rect)

def main(win):
    # infinite loop 
    height = []
    already_generated = 0
    already_sorted = 0
    algorithm = "None"
    speed = "None"
    number_of_elements = 0

    run = True

    while run: 
        
        pygame.display.update()
        # execute flag to start sorting 
        execute = False
        # getting keys pressed 
        keys = pygame.key.get_pressed() 
    
        # iterating events 
        for event in pygame.event.get(): 
            
            # if event is to quit 
            if event.type == pygame.QUIT: 
    
                # making r6un = false so break the while loop 
                run = False

            if(button_start.check() == True):
                button_start.background_color = LIGHT_BUTTON
            else:
                button_start.background_color = DARK_BUTTON

            if(button_reset.check() == True):
                    button_reset.background_color = LIGHT_BUTTON
            else:
                button_reset.background_color = DARK_BUTTON

            if(button_bubble_sort.check() == True):
                button_bubble_sort.background_color = LIGHT_BUTTON
            else:
                button_bubble_sort.background_color = DARK_BUTTON

            if(button_insertion_sort.check() == True):
                button_insertion_sort.background_color = LIGHT_BUTTON
            else:
                button_insertion_sort.background_color = DARK_BUTTON

            if(button_selection_sort.check() == True):
                button_selection_sort.background_color = LIGHT_BUTTON
            else:
                button_selection_sort.background_color = DARK_BUTTON

            if(button_merge_sort.check() == True):
                button_merge_sort.background_color = LIGHT_BUTTON
            else:
                button_merge_sort.background_color = DARK_BUTTON

            if(button_20.check() == True):
                button_20.background_color = LIGHT_BUTTON
            else:
                button_20.background_color = DARK_BUTTON

            if(button_50.check() == True):
                button_50.background_color = LIGHT_BUTTON
            else:
                button_50.background_color = DARK_BUTTON

            if(button_100.check() == True):
                button_100.background_color = LIGHT_BUTTON
            else:
                button_100.background_color = DARK_BUTTON

            if(button_slow.check() == True):
                button_slow.background_color = LIGHT_BUTTON
            else:
                button_slow.background_color = DARK_BUTTON

            if(button_medium.check() == True):
                button_medium.background_color = LIGHT_BUTTON
            else:
                button_medium.background_color = DARK_BUTTON

            if(button_fast.check() == True):
                button_fast.background_color = LIGHT_BUTTON
            else:
                button_fast.background_color = DARK_BUTTON

            if(button_instant.check() == True):
                button_instant.background_color = LIGHT_BUTTON
            else:
                button_instant.background_color = DARK_BUTTON

            if event.type == pygame.MOUSEBUTTONDOWN: 
                
                if(button_start.check() == True and number_of_elements > 0 and algorithm != "None" and speed != "None"):

                    execute = True

                    if(already_generated != 1):
                        height = generate_random_input(number_of_elements)
                        #print(height)
                        already_generated = 1

                    if(algorithm == "Bubble Sort"):
                        bubble_sort(height, 0, algorithm, number_of_elements, speed)

                    if(algorithm == "Insertion Sort"):
                        insertion_sort(height, 0, algorithm, number_of_elements, speed)

                    if(algorithm == "Selection Sort"):
                        selection_sort(height, 0, algorithm, number_of_elements, speed)

                if(button_reset.check() == True):
                    algorithm = "None"
                    number_of_elements = 0
                    speed = "None"
                    already_generated = 0

                if(button_bubble_sort.check() == True):
                    algorithm = "Bubble Sort"

                if(button_insertion_sort.check() == True):
                    algorithm = "Insertion Sort"

                if(button_selection_sort.check() == True):
                    algorithm = "Selection Sort"

                if(button_merge_sort.check() == True):
                    algorithm = "Merge Sort"

                if(button_20.check() == True):
                    number_of_elements = 20

                if(button_50.check() == True):
                    number_of_elements = 40
                
                if(button_100.check() == True):
                    number_of_elements = 100

                if(button_slow.check() == True):
                    speed = "Slow"

                if(button_medium.check() == True):
                    speed = "Medium"

                if(button_fast.check() == True):
                    speed = "Fast"

                if(button_instant.check() == True):
                    speed = "No delay"

        # checking if execute flag is false 
        if execute == False: 
    
            update_display(height, 0, algorithm, number_of_elements, speed)

main(win)