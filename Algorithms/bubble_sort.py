from Display.display import update_display
from Helper.global_variables import *
import winsound
import math

def bubble_sort_swap(index, height, numswaps):

    aux = height[index]
    height[index] = height[index+1]
    height[index+1] = aux
    numswaps = numswaps + 1
    return numswaps  

def bubble_sort(win, height, color_height, numswaps, algorithm, number_of_elements, speed):

    swap_occurred = 0;
    n = len(height)

    for i in range(n-1):

        for j in range(0, n-i-1):
            
            color_height[j] = GREEN
            color_height[j+1] = GREEN
            update_display(win, height, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)

            if(height[j] > height[j+1]):
                
                color_height[j] = RED
                color_height[j+1] = RED
                numswaps = bubble_sort_swap(j, height, numswaps) 
                freq = height[j] - height[j+1]
                #winsound.Beep(abs(freq)*10 + 37, 50)
                update_display(win, height, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)

            color_height[j] = TURQUOISE
            color_height[j+1] = TURQUOISE
        color_height[j+1] = PURPLE
    
    color_height[0] = PURPLE

    return numswaps