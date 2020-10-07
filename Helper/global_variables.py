from Helper.button_helper import Button

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

number_of_elements = -1
algorithm = ''
speed = -1

button_start = Button(25, 50, 100, 50, WHITE, DARK_BUTTON, "START")
button_reset = Button(25, 100, 100, 50, WHITE, DARK_BUTTON, "RESET")

button_bubble_sort = Button(325, 50, 100, 50, WHITE, DARK_BUTTON, "BUBBLE")
button_selection_sort = Button(325, 100, 100, 50, WHITE, DARK_BUTTON, "SELECTION")
button_insertion_sort = Button(425, 50, 100, 50, WHITE, DARK_BUTTON, "INSERTION")
button_merge_sort = Button(425, 100, 100, 50, WHITE, DARK_BUTTON, "MERGE")

button_20 = Button(725, 50, 100, 50, WHITE, DARK_BUTTON, "20")
button_50 = Button(725, 100, 100, 50, WHITE, DARK_BUTTON, "50")
button_100 = Button(825, 50, 100, 50, WHITE, DARK_BUTTON, "100")

button_slow = Button(1125, 50, 100, 50, WHITE, DARK_BUTTON, "SLOW")
button_medium = Button(1125, 100, 100, 50, WHITE, DARK_BUTTON, "MEDIUM")
button_fast = Button(1225, 50, 100, 50, WHITE, DARK_BUTTON, "FAST")
button_instant = Button(1225, 100, 100, 50, WHITE, DARK_BUTTON, "NO DELAY")