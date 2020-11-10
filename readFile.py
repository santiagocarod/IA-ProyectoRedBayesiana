import numpy as np

def readFile(name):
    file = open(name,'r')
    values = []
    node = []
    for x in file:
        x = x.rstrip().split(" ")
        #print(f'{x} --> {len(x)}')
        if len(x) > 1:
            node.append(x)
        else:
            values.append(node)
            node = []
    values.append(node)
    del values[0]
    retorno = []
    for x in values:
        #print(f'{np.matrix(x)}')
        retorno.append(np.array(x))
    
    
    return retorno
    

'''resultado = readFile("red.txt")
pregunta =resultado[len(resultado)-1].pop()
pregunta[0] = pregunta[0].replace('?','')
print("----------")
print(f'{pregunta}')
print("----------")
print(f'{resultado}')'''