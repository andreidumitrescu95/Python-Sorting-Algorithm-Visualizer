from Display.display import update_display
from Helper.global_variables import *

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

def selection_sort(win, height, color_height, numswaps, algorithm, number_of_elements, speed):

    for i in range(0, len(height) -1):

        min = i

        color_height[i] = GREEN
        for j in range(i+1, len(height)):

            #color_height[j] = GREEN
            #color_height[min] = GREEN
            #update_display(win, height, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)

            if(height[j] < height[min]):

                color_height[j] = RED
                #color_height[min] = RED
                min = j

        numswaps = selection_sort_swap(min, i, height, numswaps)      
        update_display(win, height, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)

        for k in range(0, i+1):
            color_height[k] = PURPLE
        
    color_height[len(height)-1] = PURPLE

    return numswaps