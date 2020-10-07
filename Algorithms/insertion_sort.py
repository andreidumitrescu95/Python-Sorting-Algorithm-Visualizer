from Display.display import update_display

def insertion_sort(win, height, numswaps, algorithm, number_of_elements, speed): 
  
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
                update_display(win, height, numswaps, algorithm, number_of_elements, speed)
        height[j + 1] = key 