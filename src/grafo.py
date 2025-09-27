from src.menorCaminho import *
from collections import defaultdict

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = defaultdict(list)  # lista de adjacência
        self.time = 0                   # contador de tempo DFS (feito pelo algoritmo de referência)
        self.articulaçoes = set()


    def adiciona_aresta(self, u, v,peso=1):
        self.grafo[u].append((v,peso))
        self.grafo[v].append((u,peso))

    def numeroDeCidades(self):
        return self.V

    def dfs(self, u, visitados, pai, profundidade, low):
            filhos = 0
            visitados[u] = True
            self.time += 1
            profundidade[u] = low[u] = self.time

            for v, peso in self.grafo[u]:
                if not visitados[v]:
                    pai[v] = u
                    filhos += 1
                    self.dfs(v, visitados, pai, profundidade, low)

                    # Atualiza o low[u] considerando o filho
                    low[u] = min(low[u], low[v])

                    # Condições para ponto de articulação
                    if pai[u] is None and filhos > 1:
                        self.articulaçoes.add(u)
                    if pai[u] is not None and low[v] >= profundidade[u]:
                        self.articulaçoes.add(u)

                elif v != pai[u]:
                    # Atualiza o low[u] com o pai alcançável
                    low[u] = min(low[u], profundidade[v])

    def quantidadeVizinhos(self, cidade):
        if isinstance(cidade, str): #serve pra verificar se e realmente uma letra que ele tá recebendo
            cidade = converter(cidade)

        return len(self.grafo[cidade])

def converter(x):
    if isinstance(x, str):
        return ord(x.upper()) - 65
    return chr(x + 65)

def defineQntdVertices(arq):
    vetorLetras = set() #permite inserir uma vez em so
    
    with open("data/" + arq, "r") as arquivo:
        for linha in arquivo:
            origem, destino, peso = linha.strip().split(",")
            vetorLetras.add(origem.strip())
            vetorLetras.add(destino.strip())
            print(f"origem: {origem} destino: {destino} peso: {peso}")

    return len(vetorLetras)




