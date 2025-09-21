from src.grafo import Grafo

class Conectividade (Grafo):
    def __init__(self, vertices):
        super().__init__(vertices)

    def verificaConectividade(grafo, start=0):
        visitados = [False] * grafo.V
        pai = [None] * grafo.V
        vertices = []

        def dfs(u):
            visitados[u] = True
            for v,peso in grafo.grafo[u]:
                if not visitados[v]:
                    pai[v] = u
                    vertices.append((u, v,peso))
                    dfs(v)
        dfs(start)
        conectados = all(visitados)
        return vertices, pai, conectados
    
