import hashlib

def getHash(obj):
    return int(hashlib.sha256(str(obj).encode('utf-8')).hexdigest(), 16)

def getHashModulo(obj, base):
    return getHash(obj) % base

def getHashChord(obj, m):
    return getHashModulo(obj, 2**m)