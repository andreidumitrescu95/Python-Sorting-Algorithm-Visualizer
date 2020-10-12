from Display.display import update_display
from Helper.global_variables import *

def countingSort(arr, exp1, color_height, win, numswaps, algorithm, number_of_elements, speed):
     
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
        update_display(win, arr, color_height, 0, algorithm, number_of_elements, speed, 0, True)
 
# Method to do Radix Sort
def radix_sort(arr, color_height, win, numswaps, algorithm, number_of_elements, speed):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp, color_height, win, 0, algorithm, number_of_elements, speed)
        exp *= 10

    return 0