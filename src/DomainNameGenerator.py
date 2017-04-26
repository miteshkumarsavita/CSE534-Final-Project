import random
from RandomStringGenerator import RandomStringGenerator


'''
returns a list of domain names
'''
def generateDomainNames(count, levels, nTLD, seed):
    pass


def createDomainNameFile(filename, config):
    #TODO: Mitesh
    generateDomainNames(config['nNames'], config['levels'], config['nTLD'], config['seeds'][0])

def createDomainNameFileIfNotExists(config):
        filename = Filenames.getDomainNamesFilename(config)
        if not os.path.exists(filename):
            createDomainNameFile(filename, config)