from Display.display import update_display
from Helper.global_variables import *
import math

def divide(number):
    Q, R = divmod(number, 2)
    return Q + R

def merge(a, p, q, r, color_height, win, numswaps, algorithm, number_of_elements, speed):
    (l, ri)=([], [])
    for i in range(p, q):
        l.append(a[i])
    for j in range(q, r):
        ri.append(a[j])
    
    l.append(float('inf'))
    ri.append(float('inf'))
    #print 'l and ri are %s and %s' % (l,ri)
    i=0
    j=0
    for k in range(p, r):
        if l[i] <= ri[j]:
            a[k] = l[i]
            color_height[k] = RED
            update_display(win, a, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
            i += 1
            color_height[k] = TURQUOISE
        else:
            a[k] = ri[j]
            color_height[k] = RED
            update_display(win, a, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
            color_height[k] = TURQUOISE
            j += 1

    #print 'a after merge is %s' % (a)
 
def merge_sort(a, p, r, color_height, win, numswaps, algorithm, number_of_elements, speed):
    #print 'a,P and r are %s, %d and %d' % (a,p,r)
    if p + 1 < r:
        q = divide(r + p)
        merge_sort(a, p, q, color_height, win, numswaps, algorithm, number_of_elements, speed)
        #print 'After MS of %d and %d' % (p,q)
        merge_sort(a, q, r, color_height, win, numswaps, algorithm, number_of_elements, speed)
        #print 'After 2nd MS of %d and %d' % (q+1,r)
        #print 'Before Mer of %d and %d and %d' % (p,q,r)
        merge(a, p, q, r, color_height, win, numswaps, algorithm, number_of_elements, speed)

"""
def merge_sort(array, l_index, r_index, height, color_height, win, numswaps, algorithm, number_of_elements, speed): 

    if len(array) > 1: 
        mid = len(array)//2 # Finding the mid of the heightay 
        L = array[:mid] # Dividing the array elements  
        R = array[mid:] # into 2 halves 
        
        #print("Left index: " + str(l_index) + " right index: " + str(r_index))

        #print("Left array: " + str(L))
        #print("Right array: " + str(R))

        merge_sort(L, 0, mid, height, color_height, win, numswaps, algorithm, number_of_elements, speed) # Sorting the first half
        merge_sort(R, mid+1, len(array), height, color_height, win, numswaps, algorithm, number_of_elements, speed) # Sorting the second half 
        i = j = k = 0

        #print("Left array after merge: " + str(L))
        #print("Right array after merge: " + str(R))

        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R):
            if L[i] < R[j]: 
                #array[k] = L[i]
                height[k] = L[i]
                i+= 1
            else: 
                #array[k] = R[j]
                height[k] = R[j]
                j+= 1
            k+= 1
        
        # Checking if any element was left 
        while i < len(L): 
            #array[k] = L[i] 
            #height[k] = array[k]
            height[k] = L[i]
            update_display(win, array, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
            #update_display(win, height, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
            i+= 1
            k+= 1
        
        while j < len(R): 
            #array[k] = R[j] 
            #height[k] = array[k]
            height[k] = R[j]
            update_display(win, array, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
            #update_display(win, height, color_height, numswaps, algorithm, number_of_elements, speed, 0, True)
            j+= 1
            k+= 1
"""       
        

"""
def merge_sort(height, color_height, win, numswaps, algorithm, number_of_elements, speed): 

    if len(height)>1: 
        m = len(height)//2
        left = height[:m] 
        right = height[m:] 
        left = merge_sort(left, color_height, win, numswaps, algorithm, number_of_elements, speed) 
        right = merge_sort(right, color_height, win, numswaps, algorithm, number_of_elements, speed) 

        height =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                height.append(left[0]) 
                left.pop(0) 
            else: 
                height.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            height.append(i) 
        for i in right: 
            height.append(i) 
        
    return height
"""