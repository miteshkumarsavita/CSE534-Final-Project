import os
import Filenames
import random
import pickle
from RandomStringGenerator import RandomStringGenerator

def generateTLDs(nTLD, seed):
    tlds = []
    r = RandomStringGenerator(seed, 3)
    for i in range(0, nTLD):
        tlds.append(r.getNext())
    return tlds

'''
returns a list of domain names
'''
def generateDomainNames(count, levels, nTLD, seed):
    domainNames = []
    tlds = generateTLDs(nTLD, seed)
    r = RandomStringGenerator(seed)
    for i in range(0, count):
        name = ''
        for j in range(0, levels-1):
            name = name + r.getNext() + '.'
        t = 0
        for char in r.getNext():
            t += ord(char)
        t = t%nTLD
        name = name + tlds[t]
        domainNames.append(name)
    return {'domainNames': domainNames, 'TLDs':tlds}

def createDomainNameFile(filename, config):
    ans = generateDomainNames(config['nNames'], config['levels'], config['nTLD'], config['seedNames'])
    f = open(filename, 'wb')
    f.truncate()
    pickle.dump(ans, f)
    f.close()

def createDomainNameFileIfNotExists(config):
        filename = Filenames.getDomainNamesFilename(config)
        if not os.path.exists(filename):
            createDomainNameFile(filename, config)
