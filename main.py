import pygame 
import numpy as np
import sys
sys.path.append(".")
import winsound
import time
from Helper.button_helper import Button
from Helper.text_helper import drawText, drawTextcenter
from Helper.input_helper import InputBox
from Helper.input_generator import generate_random_input
from Helper.global_variables import *
from Algorithms.bubble_sort import bubble_sort
from Algorithms.selection_sort import selection_sort
from Algorithms.insertion_sort import insertion_sort
from Algorithms.merge_sort import merge_sort
from Algorithms.heap_sort import heap_sort
from Algorithms.quick_sort import quick_sort
from Algorithms.radix_sort import radix_sort
from Display.display import update_display, show

pygame.init() 

win = pygame.display.set_mode((WIDTH, HEIGHT)) 

# setting title to the window 
pygame.display.set_caption("Sorting Algorithms Visualizer") 

def main(win):
    # infinite loop 
    height = []

    color_height = []
    already_generated = 0
    already_sorted = 0
    algorithm = "None"
    speed = "None"
    number_of_elements = 0
    current_numswaps = 0
    start_time = 0
    elapsed_time = 0

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

            if(button_heap_sort.check() == True):
                button_heap_sort.background_color = LIGHT_BUTTON
            else:
                button_heap_sort.background_color = DARK_BUTTON

            if(button_merge_sort.check() == True):
                button_merge_sort.background_color = LIGHT_BUTTON
            else:
                button_merge_sort.background_color = DARK_BUTTON

            if(button_quick_sort.check() == True):
                button_quick_sort.background_color = LIGHT_BUTTON
            else:
                button_quick_sort.background_color = DARK_BUTTON

            if(button_radix_sort.check() == True):
                button_radix_sort.background_color = LIGHT_BUTTON
            else:
                button_radix_sort.background_color = DARK_BUTTON

            if(button_20.check() == True):
                button_20.background_color = LIGHT_BUTTON
            else:
                button_20.background_color = DARK_BUTTON

            if(button_50.check() == True):
                button_50.background_color = LIGHT_BUTTON
            else:
                button_50.background_color = DARK_BUTTON

            if(button_75.check() == True):
                button_75.background_color = LIGHT_BUTTON
            else:
                button_75.background_color = DARK_BUTTON

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
                        for i in range(len(height)):
                            color_height.append(TURQUOISE)
                        already_generated = 1

                    if(algorithm == "Bubble Sort"):
                        start_time = time.time()
                        current_numswaps = bubble_sort(win, height, color_height, 0, algorithm, number_of_elements, speed)
                        elapsed_time = time.time() - start_time
                        update_display(win, height, color_height, current_numswaps, algorithm, number_of_elements, speed, elapsed_time, False)

                    if(algorithm == "Insertion Sort"):
                        start_time = time.time()
                        current_numswaps = insertion_sort(win, height, color_height, 0, algorithm, number_of_elements, speed)
                        elapsed_time = time.time() - start_time
                        update_display(win, height, color_height, current_numswaps, algorithm, number_of_elements, speed, elapsed_time, False)

                    if(algorithm == "Selection Sort"):
                        start_time = time.time()
                        current_numswaps = selection_sort(win, height, color_height, 0, algorithm, number_of_elements, speed)
                        elapsed_time = time.time() - start_time
                        update_display(win, height, color_height, current_numswaps, algorithm, number_of_elements, speed, elapsed_time, False)

                    if(algorithm == "Heap Sort"):
                        start_time = time.time()
                        current_numswaps = heap_sort(height, color_height, win, 0, algorithm, number_of_elements, speed)
                        elapsed_time = time.time() - start_time
                        update_display(win, height, color_height, current_numswaps, algorithm, number_of_elements, speed, elapsed_time, False)

                    if(algorithm == "Merge Sort"):
                        start_time = time.time()
                        current_numswaps = merge_sort(height, 0, len(height), color_height, win, 0, algorithm, number_of_elements, speed)
                        elapsed_time = time.time() - start_time
                        update_display(win, height, color_height, current_numswaps, algorithm, number_of_elements, speed, elapsed_time, False)

                    if(algorithm == "Quick Sort"):
                        start_time = time.time()
                        current_numswaps = quick_sort(height, 0, len(height) - 1, color_height, win, 0, algorithm, number_of_elements, speed)
                        elapsed_time = time.time() - start_time
                        update_display(win, height, color_height, current_numswaps, algorithm, number_of_elements, speed, elapsed_time, False)

                    if(algorithm == "Radix Sort"):
                        start_time = time.time()
                        current_numswaps = radix_sort(height, color_height, win, 0, algorithm, number_of_elements, speed)
                        elapsed_time = time.time() - start_time
                        update_display(win, height, color_height, current_numswaps, algorithm, number_of_elements, speed, elapsed_time, False)

                if(button_reset.check() == True):
                    algorithm = "None"
                    number_of_elements = 0
                    speed = "None"
                    already_generated = 0
                    already_sorted = 0
                    color_height = []
                    height = []

                if(button_bubble_sort.check() == True):
                    algorithm = "Bubble Sort"

                if(button_insertion_sort.check() == True):
                    algorithm = "Insertion Sort"

                if(button_selection_sort.check() == True):
                    algorithm = "Selection Sort"

                if(button_merge_sort.check() == True):
                    algorithm = "Merge Sort"

                if(button_heap_sort.check() == True):
                    algorithm = "Heap Sort"

                if(button_quick_sort.check() == True):
                    algorithm = "Quick Sort"

                if(button_radix_sort.check() == True):
                    algorithm = "Radix Sort"

                if(button_20.check() == True):
                    number_of_elements = 9

                if(button_50.check() == True):
                    number_of_elements = 50

                if(button_75.check() == True):
                    number_of_elements = 75
                
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
    
            update_display(win, height, color_height, current_numswaps, algorithm, number_of_elements, speed, elapsed_time, False)

main(win)