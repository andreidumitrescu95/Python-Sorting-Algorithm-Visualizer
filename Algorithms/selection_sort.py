from Display.display import update_display

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

def selection_sort(win, height, numswaps, algorithm, number_of_elements, speed):

    for i in range(0, len(height) -1):

        min = i

        for j in range(i+1, len(height)):

            if(height[j] < height[min]):

                min = j

        numswaps = selection_sort_swap(min, i, height, numswaps)        
        update_display(win, height, numswaps, algorithm, number_of_elements, speed, 0)