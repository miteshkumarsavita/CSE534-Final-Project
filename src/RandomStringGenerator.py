from string import ascii_lowercase
import random
from datetime import datetime

class RandomStringGenerator:
    def __init__(self, seed, length=10):
        self.randomizer = random.Random()
        self.randomizer.seed(seed)
        self.length = length

    def getNext(self):
        res = ""
        for i in range(self.length):
            res += self.randomizer.choice(ascii_lowercase)
        return res

'''
r = RandomStringGenerator(34576906584678978)
s = r.getNext()
'''
