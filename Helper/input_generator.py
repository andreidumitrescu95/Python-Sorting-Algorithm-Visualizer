import math
import random

def generate_random_input(size):

    randomList = []
    for i in range(size):
        number = random.randint(5,1000)
        randomList.append(number)
    return randomList