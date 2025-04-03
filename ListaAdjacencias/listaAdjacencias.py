import numpy as np

# Cria uma lista de adjacências de um grafo representado por uma matriz de adjacências.
# Entrada: matriz de adjacências (arquivo .txt)
# Saída: lista de adjacências (tipo Dictionary)
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

# Cria uma lista de adjacências de um grafo representado por uma matriz de adjacências.
# Entrada: matriz de adjacências (arquivo .txt)
# Saída: lista de adjacências (tipo Dictionary)
def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vi in listaAdj[vj] and vj in listaAdj[vi]:
        # return True
        print("True")
    else:
        # return False
        print("False")

# Insere uma aresta no grafo considerando o par de vértices vi e vj.
# Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam o id do
# vértice)
# Saída: lista de adjacências (tipo Dictionary) com a aresta inserida.
def insereArestaLista(lista, vi, vj):
    tipo = tipoGrafoLista(lista)

    if(tipo == 1 or tipo == 21 or tipo == 31):
        dirigido = True
    
    lista[vi].append(vj)
    lista[vi].sort()
    
    if not dirigido: 
        lista[vj].append(vi)
        lista[vj].sort()

    #return lista
    print(lista)

# Insere um vértice no grafo.
# Entrada: lista de adjacências (tipo Dictionary), vi (número inteiro que indica o id do vértice)
# Saída: lista de adjacências (tipo Dictionary) com o vértice inserido.
def insereVerticeLista(listaAdj):
    listaAdj[len(listaAdj.keys())] = []
    print(listaAdj)

# Remove uma aresta do grafo considerando o par de vértices vi e vj.
# Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam os ids dos vértices)
# Saída: lista de adjacências (tipo Dictionary) com a aresta removida.
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

# Remove um vértice do grafo.
# Entrada: lista de adjacências (tipo Dictionary), v (número inteiro que indica o id do vértice)
# Saída: lista de adjacências (tipo Dictionary) com o vértice removido.
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

# Retorna o valor da densidade do grafo.
# Entrada: lista de adjacências (tipo Dictionary)
# Saída: Float (valor da densidade com precisão de três casas decimais)
def calcDensidadeLista(lista):
    nVertices = len(lista.keys())
    nArestas = 0

    for i in range(0, nVertices):
        nArestas = nArestas + len(lista[i])
    nArestas = nArestas / 2

    densidade = float((2 * nArestas) / (nVertices * (nVertices - 1)))
    print(round(densidade, 3))

# Retorna o tipo do grafo representado por uma dada matriz de adjacências.
# Entrada: matriz de adjacências
# Saída: Integer (0 – simples; 1 – dígrafo; 20 – multigrafo; 21 – multigrafo dirigido; 30 – pseudografo; 31 – pseudografo dirigido)
def tipoGrafoLista(lista):
    dirigido = False
    multi = False
    pseudo = False

    res = 0

    for i in lista:
        for j in  lista[i]:

            if(i not in lista[j]):
                dirigido = True
            
            if(lista[i].count(j) > 1):
                multi = True
            
            if(i in lista[i]):
                pseudo = True
        
    if(dirigido):
        res = 1
    
    if(multi):
        res += 20
    
    if(pseudo):
        if(not multi):
            res += 30
        else:
            res += 10

    #print(res)
    return res