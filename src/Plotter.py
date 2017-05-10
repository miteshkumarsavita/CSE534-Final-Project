import json
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from Filenames import *
import Experiments
import pickle
import sys

DPI = 500

def getQuantityBeingChanged(config):
    exps = config['experiments'] if 'experiments' in config else None
    if not exps: exps = config['chord']['experiments'] if 'experiments' in config['chord'] else None
    if not exps: exps = config['hierarchical']['experiments'] if 'experiments' in config['hierarchical'] else None
    return list(exps[0])[0]

def plotToFile(xLabel, xData, yLabel, yData, legend, linestyle, color, title, filename):
    #print(xData)
    #print(yData)
    csfont = {'fontname':'Serif'}
    for i in range(len(xData)):
        if xData[i]:
            plt.plot(xData[i], yData[i], linestyle=linestyle[i], color=color[i], label=legend[i], linewidth=3)
    plt.title(title, **csfont, weight='light')
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend(loc=2, prop={'size':6})
    plt.savefig(filename, dpi=DPI, bbox_inches='tight')
    plt.close()

def plotQuantity(title, yLabel, config, funcToGetYDataFromStats, plotTofilename):
    xLabel = quantityBeingChanged = getQuantityBeingChanged(config)
    
    xData = [[], [], [], []]
    yData = [[], [], [], []]
    legendHierarchical = ["Hierarchical DNS, cache off", "Hierarchical DNS, cache on"]
    legendChord = ["Chord, cache off", "Chord, cache on"]
    legend = legendHierarchical + legendChord

    linestyle = ["dotted", "dotted", "solid", "solid"] #"dashed", "dashdot"
    color = ["#d91f1f", "#53de21", "#3424e3", "#e6d327"]
    hExpCacheOff = Experiments.createExperimentsWithCachingParam(config, "hierarchical", False)
    hExpCacheOn = Experiments.createExperimentsWithCachingParam(config, "hierarchical", True)
    cExpCacheOff = Experiments.createExperimentsWithCachingParam(config, "chord", False)
    cExpCacheOn = Experiments.createExperimentsWithCachingParam(config, "chord", True)

    expsList = [hExpCacheOff, hExpCacheOn, cExpCacheOff, cExpCacheOn]
    for i in range(len(expsList)):
        exps = expsList[i]
        for exp in exps:
            x = exp[quantityBeingChanged]
            f = open(getStatsPickleFilename(exp), "rb")
            #print(getStatsPickleFilename(exp))
            stats = pickle.load(f)
            f.close()
            y = funcToGetYDataFromStats(stats)
            xData[i].append(x)
            yData[i].append(y)
            
    print(xData)
    print(yData)
    plotToFile(xLabel, xData, yLabel, yData, legend, linestyle, color, title, plotTofilename)


def print_usage():
    print("Usage: python3 Plotter.py <config>")

def main():
    if len(sys.argv) != 2:
        print_usage()
        exit()
    configFile = open(sys.argv[1])
    configFile = json.load(configFile)

    plotQuantity("Average Throughput", "Throughput (lookups per second)", configFile, 
        lambda stats: stats['client']['throughput'], getThroughputGraphFilename(configFile))

    plotQuantity("Average Latency", "Latency (in milliseconds)", configFile, 
        lambda stats: stats['client']['latencyStats']['mean'], getLatencyGraphFilename(configFile))

    plotQuantity("Resolved by Cache", "Fraction of requests resolved by cache", \
        configFile, lambda stats: stats['client']['resolvedByCache'], getResolvedByCacheFilename(configFile))
    
    plotQuantity("nHops", "Number of hops taken by lookup", \
        configFile, lambda stats: stats['client']['nHops']['mean'], getNHopsFilename(configFile))

main()