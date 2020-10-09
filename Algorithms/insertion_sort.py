from Display.display import update_display
from Helper.global_variables import *

def insertion_sort(win, height, color_height, numswaps, algorithm, number_of_elements, speed): 
  
    # Traverse through 1 to len(height) 
    for i in range(1, len(height)): 
  
        key = height[i] 
        #color_height[i] = GREEN
  
        # Move elements of height[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < height[j] : 
                color_height[i] = GREEN
                height[j + 1] = height[j] 
                j -= 1
                numswaps = numswaps + 1
                color_height[j+1] = RED
                color_height[j] = RED
                update_display(win, height, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
                color_height[j+1] = TURQUOISE
                color_height[j] = TURQUOISE
        height[j + 1] = key 

    for i in range(len(color_height)):
        color_height[i] = PURPLE
    
    return numswaps