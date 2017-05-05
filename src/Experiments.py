import copy

def createBaseConfig(config, type):
    attrsToRemove = ["hierarchical", "chord", "experiments"]
    baseConfig = {}
    for k in config:
        if k not in attrsToRemove:
            baseConfig[k] = config[k]
    for k in config[type]:
        if k != "experiments":
            baseConfig[k] = config[type][k]
    return baseConfig

def createExperimentsWithCaching(config, type, caching):
    result = []
    baseConfig = createBaseConfig(config, type)
    
    exps = config['experiments'] if 'experiments' in config else None
    if not exps: exps = config[type]['experiments'] if 'experiments' in config[type] else None
    
    if exps:
        for exp in exps:
            modifiedConfig = copy.deepcopy(baseConfig)
            modifiedConfig['type'] = type
            modifiedConfig['caching'] = caching
            for k in exp:
                modifiedConfig[k] = exp[k]
            result.append(modifiedConfig)
    return result

def createExperiments(config, type):
    return createExperimentsWithCaching(config, type, True) + createExperimentsWithCaching(config, type, False)