import random
import pickle

class RequestGenerator:
    def __init__(self, filename, subset, seed):
        fileHandle = open(filename, "rb")
        domainNames = pickle.load(fileHandle)
        fileHandle.close()

        self.randomizer = random.Random()
        self.randomizer.seed(seed)

        # only take the first {subset} fraction of requests
        self.domainNames = domainNames['domainNames'][:len(domainNames['domainNames'])*subset]
    
    def getNext(self):
        query = {}
        query['name'] = self.randomizer.choice(self.domainNames)
        return query