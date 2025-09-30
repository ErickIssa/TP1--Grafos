import heapq  # para fila de prioridade o heappop sempre retorna o no com a menor distancia atual

def menorCaminhoDijkstra(grafo, inicio, fim):
    V = grafo.V
    dt = [float("inf")] * V #o iesimo elemento guarda a dist calculada entre o vertice origem e o vertice i, os menores caminhos
    rot = [None] * V #vetor que guarda as posicoes de onde passei para ter o menor caminho
    visitados = [False] * V

    dt[inicio] = 0
    fila = [(0, inicio)]  # fila pioridade

    while fila:
        distAtual, u = heapq.heappop(fila) #retira no menor dist

        if visitados[u]:
            continue
        visitados[u] = True

        if u == fim:  # no atual = no destino
            break

        for v, peso in grafo.grafo[u]: #basicamente verifica se por outro caminho é menor
            peso = int(peso)
            if not visitados[v] and dt[u] + peso < dt[v]:
                dt[v] = dt[u] + peso
                rot[v] = u
                heapq.heappush(fila, (dt[v], v))

    # Reconstroi o caminho pelo fim e analisando o vetor rot
    caminho = []
    atual = fim
    while atual is not None:
        caminho.append(atual)
        atual = rot[atual]
    caminho.reverse()

    return dt[fim], caminho