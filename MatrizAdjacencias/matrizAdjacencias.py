import numpy as np

#Função para pegar uma instância .txt que esteja dentro da pasta Instancias
#e o transforma em uma matriz do tipo Numpy
#Entrada: Uma string com o nome do arquivo que esteja na pasta Instancias
#Saida: Uma matriz do tipo Numpy
def criaMatrizNp(instancia):
    caminho = f"./Instancias/{instancia}.txt"

    with open(caminho, 'rb') as f:
        data = np.genfromtxt(f, dtype="int32")

    return data


#Função que gera um arquivo .txt contendo o nome da instancia e o tamanho de sua matriz
#Entrada: [1]Nome da Instancia; [2]Array de 2 elementos contendo o tamanho da matriz
#Saida: Arquivo .txt
def geraArquivoMatrizNp(instancia, tamanho):
    texto = str(instancia) + " " + str(tamanho[0]) + " " + str(tamanho[1])
    arquivo = open(f"./Resultados/result{instancia.capitalize()}.txt", "w")
    arquivo.writelines(texto + "\n")
    arquivo.close
    print(texto)


# Verifica se os vértices vi e vj são adjacentes.
# Entrada: matriz de adjacências, vi e vj (ambos números inteiros que indica o id do vértice)
# Saída: Boolean (True se os vértices são adjacentes; False caso contrário)
def verificaAdjacencia(matriz, vi, vj):
    if(matriz[vi][vj] > 0):
        #return True
        print("True")
    else:
        #return False
        print("False")


# Insere uma aresta no grafo considerando o par de vértices vi e vj.
# Entrada: matriz de adjacências, vi e vj (ambos são números inteiros que indicam o id do vértice)
# Saída: matriz de adjacências (tipo numpy.ndarray) com a aresta inserida.
def insereAresta(matriz, vi, vj):
    matriz[vi][vj] += 1
    matriz[vj][vi] += 1

    print(matriz)
    return matriz


# Insere um vértice no grafo.
# Entrada: matriz de adjacências, vi (número inteiro que indica o id do vértice)
# Saída: matriz de adjacências (tipo numpy.ndarray) com o vértice inserido.
def insereVertice(matriz):
    nVertices = np.shape(matriz)[0]
    novaLinha = np.zeros(nVertices, dtype=int)
    novaMatriz = np.insert(matriz, nVertices, novaLinha, axis=0)

    novaColuna = np.zeros(nVertices + 1, dtype=int)
    novaMatriz = np.hstack((novaMatriz, np.atleast_2d(novaColuna).T))

    print(novaMatriz)


# Remove um vértice do grafo.
# Entrada: matriz de adjacências, v (número inteiro que indica o id do vértice)
# Saída: matriz de adjacências (tipo numpy.ndarray) com o vértice removido.
def removeVertice(matriz, vi):
  numVertices = np.shape(matriz)[0]
  for i in range(0, numVertices):
    for j in range(0, numVertices):
      matriz[i][vi] = -1
      matriz[vi][j] = -1

  print(np.array(matriz))
  return matriz


# Remove uma aresta do grafo considerando o par de vértices vi e vj.
# Entrada: matriz de adjacências, vi e vj (ambos são números inteiros que indicam os ids dos vértices)
# Saída: matriz de adjacências (tipo numpy.ndarray) com a aresta removida.
def removeAresta(matriz, vi, vj):
    matriz[vi][vj] = 0
    matriz[vj][vi] = 0

    print(matriz)
    return matriz


# Retorna o valor da densidade do grafo conforme seu tipo.
# Entrada: matriz de adjacências
# Saída: Float (valor da densidade com precisão de três casas decimais)
def calculoDensidade(matriz):
    nVertices = np.shape(matriz)[0]
    nArestas = 0
    for i in range(0, nVertices):
        for j in range(0, nVertices):
            if(matriz[i][j] > 0):
                nArestas += 1
    nArestas = nArestas/2
    densidade = float((2 * nArestas) / (nVertices * (nVertices - 1)))
    print(round(densidade, 3))
    return round(densidade, 3)


# Retorna o tipo do grafo representado por uma dada matriz de adjacências.
# Entrada: matriz de adjacências
# Saída: Integer (0 – simples; 1 – dígrafo; 20 – multigrafo; 21 – multigrafo dirigido; 30 – pseudografo; 31 – pseudografo dirigido) 
def tipoGrafo(matriz):
    dirigido = False
    multi = False
    pseudo = False
    res = 0

    nVertices = np.shape(matriz)[0]

    for i in range(0, nVertices):
        for j in range(0, nVertices):
            
            if(matriz[i][j] != matriz[j][i]):
                dirigido = True
            
            if(matriz[i][j] > 1):
                multi = True
            
            if(i == j and matriz[i][j] > 0):
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
    
    print(res)