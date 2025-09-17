def converter(x):
    if isinstance(x, str):
        return ord(x.upper()) - 65
    return chr(x + 65)


def defineTamMatriz():
    arq = input("Digite o nome do arquivo de entrada com extensao na pasta DATA:\n")
    arq = "entrada.txt" #apagar dps LEMBRAR!!!!!!!!!!!!!!!!!!!

    vetorLetras = set() #permite inserir uma vez em so
    
    with open("data/" + arq, "r") as arquivo:
        for linha in arquivo:
            origem, destino, peso = linha.strip().split(",")
            vetorLetras.add(origem.strip())
            vetorLetras.add(destino.strip())
            print(f"origem: {origem} destino: {destino} peso: {peso}")

    listaletras = sorted(list(vetorLetras))# o set n deixa ordenar pq e uma hash kk
    return listaletras


def adicionaArestas():
    letrasVert = defineTamMatriz()
    tam = len(letrasVert)
    matriz = [[0] * (tam + 1) for _ in range(tam + 1)]

    for i in range(tam):
        matriz[0][i + 1] = converter(letrasVert[i])
        matriz[i + 1][0] = converter(letrasVert[i])

    return matriz
