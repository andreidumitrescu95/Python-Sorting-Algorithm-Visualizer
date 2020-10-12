from Display.display import update_display
from Helper.global_variables import *

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(height, n, i, color_height, win, numswaps, algorithm, number_of_elements, speed): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and height[i] < height[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and height[largest] < height[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        height[i],height[largest] = height[largest],height[i]  # swap 
        update_display(win, height, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
        # Heapify the root. 
        heapify(height, n, largest, color_height, win, numswaps, algorithm, number_of_elements, speed) 

# The main function to sort an heightay of given size 
def heap_sort(height, color_height, win, numswaps, algorithm, number_of_elements, speed): 
    n = len(height) 

    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(height, n, i, color_height, win, numswaps, algorithm, number_of_elements, speed) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        height[i], height[0] = height[0], height[i]   # swap 
        heapify(height, i, 0, color_height, win, numswaps, algorithm, number_of_elements, speed) 