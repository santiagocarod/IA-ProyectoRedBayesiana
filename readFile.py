import numpy as np

def readFile(name):
    file = open(name,'r')
    values = []
    node = []
    for x in file:
        x = x.rstrip().split(" ")
        if len(x) > 1:
            node.append(x)
        else:
            values.append(node)
            node = []
    values.append(node)
    del values[0]
    retorno = []
    for x in values:
        retorno.append(np.array(x))
    return retorno
    