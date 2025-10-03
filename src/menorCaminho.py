import heapq  # para fila de prioridade o heappop sempre retorna o no com a menor distancia atual

def menorCaminhoDijkstra(grafo, inicio, fim):
    V = grafo.V
    dt = [float("inf")] * V  # distâncias
    rot = [None] * V         # predecessores
    visitados = [False] * V

    dt[inicio] = 0
    fila = [(0, inicio)]  # fila de prioridade

    while fila:
        distAtual, u = heapq.heappop(fila)  # nó com menor distância

        if visitados[u]:
            continue
        visitados[u] = True

        if u == fim:  # já chegou no destino
            break

        for v, peso in grafo.grafo[u]:
            peso = int(peso)
            if not visitados[v] and dt[u] + peso < dt[v]:
                dt[v] = dt[u] + peso
                rot[v] = u
                heapq.heappush(fila, (dt[v], v))

    # Se não há caminho até fim
    if dt[fim] == float("inf"):
        return float("inf"), []  

    # Reconstrói o caminho pelo vetor rot
    caminho = []
    atual = fim
    while atual is not None:
        caminho.append(atual)
        atual = rot[atual]
    caminho.reverse()

    return dt[fim], caminho
