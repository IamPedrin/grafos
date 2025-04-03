import numpy as np

def criaListaAdjacencias(matriz):
    qtdVertices = np.shape(matriz)[0]
    lista = {}
    for i in range(0, qtdVertices):
        adjacencia = []
        for j in range(0, qtdVertices):
            if(matriz[i][j] > 0):
                adjacencia.append(j)
            if(matriz[i][j] > 1):
                adjacencia.append(j)
        lista[i] = adjacencia

    #print(lista)
    return lista

def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vi in listaAdj[vj] and vj in listaAdj[vi]:
        # return True
        print("True")
    else:
        # return False
        print("False")

def insereArestaLista(listaAdj, vi, vj):
    if(vi != vj):
        listaAdj[vi].append(vj)
        listaAdj[vi].sort()
        listaAdj[vj].append(vi)
        listaAdj[vj].sort()
    else:
        listaAdj[vi].append(vj).append()
        listaAdj[vi].sort()

    #return listaAdj
    print(listaAdj)

def insereVerticeLista(listaAdj):
    listaAdj[len(listaAdj.keys())] = []
    print(listaAdj)

def removeArestaLista(listaAdj, vi, vj):
    dirigido = False
    if((vi in listaAdj[vj] and not vj in listaAdj[vi]) or (vj in listaAdj[vi] and not vi in listaAdj[vj])):
        dirigido = True

    if(not dirigido and vi in listaAdj[vj] and vj in listaAdj[vi]):
        listaAdj[vj].remove(vi)
        listaAdj[vi].remove(vj)

    if(dirigido and vi in listaAdj[vj]):
        listaAdj[vj].remove(vi)

    if(dirigido and vj in listaAdj[vi]):
        listaAdj[vi].remove(vj)

    #return listaAdj
    print(listaAdj)

def removeVerticeLista(listaAdj, v):
    for i in range(len(listaAdj)):
        if v in listaAdj[i]:
            listaAdj[i].remove(v)
        if i != v:
            if v in listaAdj[i]:
                listaAdj[i].remove(v)

    if v in listaAdj.keys():
        del listaAdj[v]

    print(listaAdj)