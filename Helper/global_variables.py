from Helper.button_helper import Button
 
WIDTH = 1366
HEIGHT = 768

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEAL = (0, 128, 128)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
LIGHT_BUTTON = (170, 170, 170)
DARK_BUTTON = (100, 100, 100)

button_start = Button(10, 100, 100, 50, WHITE, DARK_BUTTON, "START", 18)
button_reset = Button(110, 100, 100, 50, WHITE, DARK_BUTTON, "RESET", 18)

button_bubble_sort = Button(275, 50, 100, 50, WHITE, DARK_BUTTON, "BUBBLE", 18)
button_selection_sort = Button(275, 100, 100, 50, WHITE, DARK_BUTTON, "SELECTION", 18)
button_insertion_sort = Button(375, 50, 100, 50, WHITE, DARK_BUTTON, "INSERTION", 18)
button_merge_sort = Button(375, 100, 100, 50, WHITE, DARK_BUTTON, "MERGE", 18)
button_quick_sort = Button(475, 50, 100, 50, WHITE, DARK_BUTTON, "QUICK", 18)
button_heap_sort = Button(475, 100, 100, 50, WHITE, DARK_BUTTON, "HEAP", 18)
button_radix_sort = Button(575, 50, 100, 50, WHITE, DARK_BUTTON, "RADIX", 18)
button_todo4 = Button(575, 100, 100, 50, WHITE, DARK_BUTTON, "TODO4", 18)

button_20 = Button(800, 50, 100, 50, WHITE, DARK_BUTTON, "20", 18)
button_50 = Button(800, 100, 100, 50, WHITE, DARK_BUTTON, "50", 18)
button_75 = Button(900, 50, 100, 50, WHITE, DARK_BUTTON, "75", 18)
button_100 = Button(900, 100, 100, 50, WHITE, DARK_BUTTON, "100", 18)

button_slow = Button(1125, 50, 100, 50, WHITE, DARK_BUTTON, "SLOW", 18)
button_medium = Button(1125, 100, 100, 50, WHITE, DARK_BUTTON, "MEDIUM", 18)
button_fast = Button(1225, 50, 100, 50, WHITE, DARK_BUTTON, "FAST", 18)
button_instant = Button(1225, 100, 100, 50, WHITE, DARK_BUTTON, "NO DELAY", 18)