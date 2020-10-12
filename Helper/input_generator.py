import math
import random
import numpy as np

def generate_random_input(size):

    #randomList = []
    randomList = np.zeros(size)
    for i in range(size):
        #number = random.randint(5,1000)
        randomList[i] = i
    #random.shuffle(randomList)
    np.random.shuffle(randomList)
    return randomList