import numpy as np
import itertools
from copy import deepcopy
from readFile import readFile

#Inferencia Bayesiana
def redBayesiana(valores, pregunta):
    #creamos una arreglo con las diferentes probabilidades de los eventos
    probabilidades = []
    #revisamos todas las posibilidades de que ese evento suceda
    for nodo in valores:

        for linea in nodo:
            #print(f'Linea Total: {linea}')
            valor = linea[len(linea) - 1]
            linea = linea[:-1]
            linea
            #print(f'Linea: {linea} Valor {valor}')
            vale = True
            for i in linea:
                if i not in pregunta:
                    vale = False
            if vale:
                probabilidades.append(valor)

    resultado = 1.0
    #print(str(probabilidades))
    for j in probabilidades:
        resultado = float(resultado * float(j))
    return resultado


def normalizar(contadores):
  suma = sum(contadores)
  for i in range(len(contadores)):
    contadores[i] = round(contadores[i]/suma,5)

def getOptions(matrix):
    return np.unique(matrix[:,len(matrix[0])-2])



def resolver(valores,pregunta):
    print(f'La pregunta es {str(pregunta)}')
    opcionesRespuesta = getOptions(valores[len(valores)-1])
    print(str(opcionesRespuesta))
    indicesVariables = []
    contador = 0
    for i in pregunta:
        if i[0].isupper and len(i) == 1:
            print(f'{i} es una variable')
            indicesVariables.append(contador)
        contador +=1
    if len(indicesVariables) == 0:
        resultado = round(redBayesiana(valores, pregunta), 5)
        print(pregunta[len(pregunta)-1])
        print(resultado)
        return resultado

    opcionesVariablesTotal = []
    for i in reversed(indicesVariables):
        opcionesVariable = getOptions(valores[i])
        opcionesVariablesTotal.append(opcionesVariable)
        print(f'Las opciones para la variable {pregunta[i]} son {str(opcionesVariable)}')
        del pregunta[i]
    
    del pregunta[len(pregunta)-1]

    contadores = []
    for i in opcionesRespuesta:
        contador = 0
        print(f'Se calcula para el resultado: {i} ')
        for j in itertools.product(*opcionesVariablesTotal):
            preguntaAux = deepcopy(pregunta)
            for a in range(len(j)):
                preguntaAux.append(j[a])
            preguntaAux.append(i)
            print(f'\tPregunta Parcial {str(preguntaAux)}')
            resultado = round(redBayesiana(valores, preguntaAux), 5)
            contador += resultado
            print(f'\t\tLa probabiliad de esto es de: {resultado}')
        print(f'Probabiliad acumulada es de: {contador}')
        print('_________________________________________________')
        contadores.append(contador)
    

    print("¡RESULTADOS!")
    print(f'Valores sin Normalizar: ')
    print(f'\t{str(contadores)}')

    normalizar(contadores)
    print("Valores Normalizados: ")
    print(f'\t{opcionesRespuesta}')
    print(f'\t{str(contadores)}')
    return contadores



valores = readFile("red.txt")
pregunta = ['none','no','X','attend']
respuesta = resolver(valores,pregunta)
