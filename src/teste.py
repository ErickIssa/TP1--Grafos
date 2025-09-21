from conectividade import *
from grafo import *
from articulacao import *
if __name__ == "__main__":

    g = Articulacao(6)
    g.adiciona_aresta(0, 1)
    g.adiciona_aresta(0, 2)
    g.adiciona_aresta(1, 2)
    g.adiciona_aresta(1, 3)
    g.adiciona_aresta(3, 4)
    g.adiciona_aresta(3, 5)

    aps = g.encontraArticulacao()
    print("Pontos de articulação:", aps)

    g1 = Conectividade(5)
    g1.adiciona_aresta(0, 1)
    g1.adiciona_aresta(1, 2)
    g1.adiciona_aresta(2, 3)
    g1.adiciona_aresta(3, 4)

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