import numpy as np
import sys

#Função para pegar uma instância .txt que esteja dentro da pasta Instancias
#e o transforma em uma matriz do tipo Numpy
#Entrada: Uma string com o nome do arquivo que esteja na pasta Instancias
#Saida: Uma matriz do tipo Numpy
def criaMatrizNp(instancia):
    caminho = f"/dev/Grafos/Instancias/{instancia}.txt"

    with open(caminho, 'rb') as f:
        data = np.genfromtxt(f, dtype="int32")

    return data

#Função que retorna o tamanho de uma matriz quadrada utilizando a função numpy.shape
#Entrada: Um matriz do tipo Numpy
#Saida: Retorna uma lista com o tamanho n x m. lista[n, m]. Posicao[0] = n, Posicao[1] = m
def tamanhoMatrizNp(matriz):
    tamanho = [np.shape(matriz)[0], np.shape(matriz)[1]]
    return tamanho

#Função que gera um arquivo .txt contendo o nome da instancia e o tamanho de sua matriz
#Entrada: [1]Nome da Instancia; [2]Array de 2 elementos contendo o tamanho da matriz
#Saida: Arquivo .txt
def geraArquivoMatrizNp(instancia, tamanho):
    texto = str(instancia) + " " + str(tamanho[0]) + " " + str(tamanho[1])
    arquivo = open(f"/dev/Grafos/Resultados/result{instancia.capitalize()}.txt", "w")
    arquivo.writelines(texto + "\n")
    arquivo.close
    print(texto)
    
#Função main onde será chamada as outras funções para a execução do programa
def main(instancia):
    matriz = criaMatrizNp(instancia)
    tamanho = tamanhoMatrizNp(matriz)
    geraArquivoMatrizNp(instancia, tamanho)

#Chamada da funcão main
#Parâmetros: [1]Instancia
if __name__ == "__main__":
    main(str(sys.argv[1]))