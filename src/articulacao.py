from src.grafo import Grafo

class Articulacao (Grafo):
    def __init__(self, vertices):
        super().__init__(vertices)

    def encontraArticulacao(grafo):
        visitados = [False] * grafo.V
        pai = [None] * grafo.V
        profundidade = [float("inf")] * grafo.V
        low = [float("inf")] * grafo.V

        for i in range(grafo.V):
            if not visitados[i]:
                grafo.dfs(i, visitados, pai, profundidade, low)
        return grafo.articulaçoes