import sys

from MatrizAdjacencias import matrizAdjacencias as ma
from ListaAdjacencias import listaAdjacencias as la

#Função main onde será chamada as outras funções para a execução do programa
def main(instancia):
    matriz = ma.criaMatrizNp(instancia)
    ma.tipoGrafo(matriz)
    lista = la.criaListaAdjacencias(matriz)
    la.tipoGrafoLista(lista)

#Chamada da funcão main
#Parâmetros: [1]Instancia
if __name__ == "__main__":
    main(str(sys.argv[1]))