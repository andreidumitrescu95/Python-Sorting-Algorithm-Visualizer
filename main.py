# importing pygame 
import pygame 
import sys
import winsound

pygame.init() 
  
# setting window size 
WIDTH = 1366
HEIGHT = 768

# white color 
WHITE = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100)

win = pygame.display.set_mode((WIDTH, HEIGHT)) 
 
# setting title to the window 
pygame.display.set_caption("Sorting Algorithms Visualization") 
  
  
# initial position 
x = 40
y = 40
  
# width of each bar 
width = 10
f = open("inputs.txt", "r")
content = f.read()
print(content)
height = []
i = 0
height = (content.split(","))
height = list(map(int, height))

f.close();

run = True

def merge_sort(height):
    """
    height of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    """
    if len(height) < 2:
        return height

    mid = len(height) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_height = merge_sort(height[:mid])
    right_height = merge_sort(height[mid:])

    return merge(left_height, right_height)

def merge(left, right):
    """
    Traverse both sorted sub-heightays (left and right), and populate the height heightay
    """
    height = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            height.append(left[i])
            i += 1
        else:
            height.append(right[j])
            j += 1
    height += left[i:]
    height += right[j:]

    #update_display(50)

    return height

def insertion_sort(height): 
  
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
                update_display(1)
        height[j + 1] = key 

def selection_sort_swap(index1, index2, height):
    
    aux = height[index1]
    height[index1] = height[index2]
    height[index2] = aux
    ##if(index1>index2):
    #    winsound.Beep(int(height[index1]/height[index2])*100, 100)
    #else:
    #    winsound.Beep(int(height[index2]/height[index1])*100, 100)

def selection_sort(height):

    for i in range(0, len(height) -1):

        min = i

        for j in range(i+1, len(height)):

            if(height[j] < height[min]):

                min = j

        selection_sort_swap(min, i, height)        
        update_display(1)

def bubble_sort_swap(index, height, numswaps):
    
    aux = height[index]
    height[index] = height[index+1]
    height[index+1] = aux
    numswaps = numswaps + 1
    return numswaps   

def bubble_sort(height, numswaps):

    swap_occurred = 0;

    for i in range(len(height)-1):

        for j in range(len(height)-1):

            if(height[i] > height[i+1]):

                swap_occurred = 1;
                
                numswaps = bubble_sort_swap(i, height, numswaps) 
                update_display(1, numswaps)                               
    
    if(swap_occurred == 1):
        bubble_sort(height, numswaps)

def update_display(delay_timer, numswaps):

    win.fill((0, 0, 0)) 
    
    # call show method to display the list items 
    show(height, numswaps) 

    # create a time delay 
    pygame.time.delay(delay_timer) 
    
    # update the display 
    pygame.display.update() 

# method to show the list of height 
def show(height, numswaps): 

    maximum_value = max(height)
    step = (WIDTH/len(height))

    # displaying number of swaps
    font = pygame.font.SysFont('None', 25)
    string = "Number of swaps: " + str(numswaps)
    text = font.render(string, True, WHITE)
    text_rect = text.get_rect(center=(0,0))
    win.blit(text, [0,0])

    string = "Algorithm used: "
    text = font.render(string, True, WHITE)
    text_rect = text.get_rect(center=(350,0))
    win.blit(text, [350,0])
    
    # displaying reset button
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    mouse = pygame.mouse.get_pos() 
    
    text_button = font.render("Reset", True, WHITE)

    if 0 <= mouse[0] <= 140 and 25 <= mouse[1] <= 65: 
        pygame.draw.rect(win,color_light,[0,25,140,40]) 
          
    else: 
        pygame.draw.rect(win,color_dark,[0,25,140,40]) 
    
    win.blit(text_button, (0,30))

    # loop to iterate each item of list 
    for i in range(len(height)): 
  
        # drawing each bar with respective gap 
        font = pygame.font.SysFont('Arial', int(round(step - 13)))
        text = font.render(str(height[i]), False, (255, 0, 0))
        rectangle = pygame.draw.rect(win, (255, 255, 0), (step * (i+1), HEIGHT, -(step-10), -(height[i]/maximum_value)*3*HEIGHT/4)) 
        text_rect = text.get_rect(center=(step * (i+1) - (step-10)/2, HEIGHT - 10))
        win.blit(text, text_rect)

# infinite loop 
while run: 
    
    pygame.display.update()
    # execute flag to start sorting 
    execute = False
  
    # time delay 
    #pygame.time.delay(50) 
  
    # getting keys pressed 
    keys = pygame.key.get_pressed() 
  
    # iterating events 
    for event in pygame.event.get(): 
  
        # if event is to quit 
        if event.type == pygame.QUIT: 
  
            # making r6un = false so break the while loop 
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN: 
              
            mouse = pygame.mouse.get_pos() 
            #if the mouse is clicked on the 
            # button the game is terminated 
            if 0 <= mouse[0] <= 140 and 25 <= mouse[1] <= 65: 
                #pygame.quit() 
                run = False
  
    # if space bar is pressed 
    if keys[pygame.K_SPACE]: 
        # make execute flag to true 
        execute = True
  
    # checking if execute flag is false 
    if execute == False: 
  
        update_display(0, 0)
  
    # if execute flag is true 
    else: 
        bubble_sort(height, 0)
        #selection_sort(height)
        #merge_sort(height)
        #insertion_sort(height)

# exiting the main window 
pygame.quit() 