import random
import pickle

class RequestGenerator:
    def __init__(self, filename, subset, generateNonExistent, seed):
        self.generateNonExistent = generateNonExistent
        fileHandle = open(filename, "rb")
        domainNames = pickle.load(fileHandle)
        fileHandle.close()

        self.randomizer = random.Random()
        self.randomizer.seed(seed)

        # only take the first {subset} fraction of requests
        self.domainNames = domainNames['domainNames'][:int(len(domainNames['domainNames'])*subset)]
    
    def getNext(self):
        query = {}
        name = self.randomizer.choice(self.domainNames)
        if self.generateNonExistent:
            l = name.split(".")
            l[0] = l[0] + 'a'
            name = '.'.join(l)
        query['name'] = name
        return query