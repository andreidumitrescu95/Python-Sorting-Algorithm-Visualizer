from Display.display import update_display

def bubble_sort_swap(index, height, numswaps):
    
    aux = height[index]
    height[index] = height[index+1]
    height[index+1] = aux
    numswaps = numswaps + 1
    return numswaps   

def bubble_sort(win, height, numswaps, algorithm, number_of_elements, speed):

    swap_occurred = 0;

    for i in range(len(height)-1):

        for j in range(len(height)-1):

            if(height[i] > height[i+1]):

                swap_occurred = 1;
                
                numswaps = bubble_sort_swap(i, height, numswaps) 
                update_display(win, height, numswaps, algorithm, number_of_elements, speed)           
                #update_display()                    
    
    if(swap_occurred == 1):
        bubble_sort(win, height, numswaps, algorithm, number_of_elements, speed)

    return numswaps