from Display.display import update_display
from Helper.global_variables import *

def partition(arr, low, high, color_height, win, numswaps, algorithm, number_of_elements, speed):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            color_height[i] = RED
            color_height[j] = RED
            update_display(win, arr, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
            color_height[i] = TURQUOISE
            color_height[j] = TURQUOISE
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    color_height[i+1] = RED
    color_height[high] = RED
    update_display(win, arr, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
    color_height[i+1] = TURQUOISE
    color_height[high] = TURQUOISE
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
 
def quick_sort(arr, low, high, color_height, win, numswaps, algorithm, number_of_elements, speed):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high, color_height, win, numswaps, algorithm, number_of_elements, speed)
 
        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi-1, color_height, win, numswaps, algorithm, number_of_elements, speed)
        quick_sort(arr, pi+1, high, color_height, win, numswaps, algorithm, number_of_elements, speed)