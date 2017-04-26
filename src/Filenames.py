from config import *
import os

def getBaseExperimentName(config):
    cachingStr = "cache-on" if config['caching'] else "cache-off"
    chordNodesStr = "_nNodes-" + str(config['nNodes']) if 'nNodes' in config else ""
    return cachingStr + chordNodesStr + "_nReq-" + str(config['nReq']) + "_subset-" + str(config['subset']) + "_levels-" + str(config['levels'])

def createAllFolders(config):
    createFolderIfNotExists(getBaseStatsFolderName(config))
    createFolderIfNotExists(getBaseStatsFolderName(config) + chordFolderName + "/")
    createFolderIfNotExists(getBaseStatsFolderName(config) + hierarchicalFolderName + "/")

    createFolderIfNotExists(getBaseLogsFolderName(config))
    createFolderIfNotExists(getBaseLogsFolderName(config) + chordFolderName + "/")
    createFolderIfNotExists(getBaseLogsFolderName(config) + hierarchicalFolderName + "/")
    
    createFolderIfNotExists(getBaseGraphsFolderName(config))

# ------------  stats ------------------
def getBaseStatsFolderName(config):
    return statsFolder + "/" + config['name'] + "/"
def getStatsFolderName(config):
    return getBaseStatsFolderName(config) + config['type'] + "/"
def getStatsFilename(config):
    return getStatsFolderName(config) + getBaseExperimentName(config) + ".txt"
def getStatsPickleFilename(config):
    return getStatsFolderName(config) + getBaseExperimentName(config) + ".pickle"


# ------------  logs ------------------
def getBaseLogsFolderName(config):
    return logsFolder + "/" + config['name'] + "/"
def getLogsFolderName(config):
    return getBaseLogsFolderName(config) + config['type'] + "/"
def getClientLogFilename(config):
    return getLogsFolderName(config) + getBaseExperimentName(config) + ".client.txt"
def getDNSLogFilename(config):
    return getLogsFolderName(config) + getBaseExperimentName(config) + ".dns.txt"
def getMasterLogFilename(config):
    return getBaseLogsFolderName(config) + "master.txt"


# ------------  graphs ------------------
def getBaseGraphsFolderName(config):
    return graphsFolder + "/" + config['name'] + "/"
def getGraphsFolderName(config):
    return getBaseGraphsFolderName(config)
def getThroughputGraphFilename(config):
    return getGraphsFolderName(config) + "throughput.png"
def getLatencyGraphFilename(config):
    return getGraphsFolderName(config) + "latency.png"
def getMessagePerRequestGraphFilename(config):
    return getGraphsFolderName(config) + "messagesPerRequest.png"


def createFolderIfNotExists(folderName):
    directory = os.path.dirname(folderName)
    if not os.path.exists(directory):
        os.makedirs(directory)