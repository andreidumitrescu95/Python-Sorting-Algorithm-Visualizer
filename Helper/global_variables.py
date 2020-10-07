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

button_start = Button(25, 50, 100, 50, WHITE, DARK_BUTTON, "START", 18)
button_reset = Button(25, 100, 100, 50, WHITE, DARK_BUTTON, "RESET", 18)

button_bubble_sort = Button(325, 50, 100, 50, WHITE, DARK_BUTTON, "BUBBLE", 18)
button_selection_sort = Button(325, 100, 100, 50, WHITE, DARK_BUTTON, "SELECTION", 18)
button_insertion_sort = Button(425, 50, 100, 50, WHITE, DARK_BUTTON, "INSERTION", 18)
button_merge_sort = Button(425, 100, 100, 50, WHITE, DARK_BUTTON, "MERGE", 18)

button_20 = Button(725, 50, 100, 50, WHITE, DARK_BUTTON, "20", 18)
button_50 = Button(725, 100, 100, 50, WHITE, DARK_BUTTON, "50", 18)
button_100 = Button(825, 50, 100, 50, WHITE, DARK_BUTTON, "100", 18)

button_slow = Button(1125, 50, 100, 50, WHITE, DARK_BUTTON, "SLOW", 18)
button_medium = Button(1125, 100, 100, 50, WHITE, DARK_BUTTON, "MEDIUM", 18)
button_fast = Button(1225, 50, 100, 50, WHITE, DARK_BUTTON, "FAST", 18)
button_instant = Button(1225, 100, 100, 50, WHITE, DARK_BUTTON, "NO DELAY", 18)