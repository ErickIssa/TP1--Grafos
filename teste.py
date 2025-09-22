from src.conectividade import *
from src.grafo import *
from src.articulacao import *
from src.matrizAdjacencia import *
from src.menu import *

if __name__ == "__main__":

    menu();

    g = Articulacao(6)
    g.adiciona_aresta(converter('A'), converter('B'))
    g.adiciona_aresta(0, 2, 10)
    g.adiciona_aresta(1, 2, 10)
    g.adiciona_aresta(1, 3, 10)
    g.adiciona_aresta(3, 4, 10)
    g.adiciona_aresta(3, 5, 10)

    

    g1 = Conectividade(5)
    g1.adiciona_aresta(0, 1, 10)
    g1.adiciona_aresta(1, 2, 10)
    g1.adiciona_aresta(2, 3, 10)
    g1.adiciona_aresta(3, 4, 10)

    vertices, pai, conectados = g1.verificaConectividade(0)
    #print("Árvore DFS (arestas):", vertices)
    print("O grafo é conexo?", conectados)
    # Grafo desconexo
    g2 = Conectividade(5)
    g2.adiciona_aresta(0, 1)
    g2.adiciona_aresta(2, 3)

    vertices, pai, conectados = g2.verificaConectividade(0)
    #print("\nÁrvore DFS (arestas):", vertices)
    print("O Grafo é conexo?", conectados)
    print("numero: ", g2.numeroDeCidades() )