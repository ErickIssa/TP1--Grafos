
def defineQntdArestas(arq):
    vetorLetras = set() #permite inserir uma vez em so
    
    with open("data/" + arq, "r") as arquivo:
        for linha in arquivo:
            origem, destino, peso = linha.strip().split(",")
            vetorLetras.add(origem.strip())
            vetorLetras.add(destino.strip())
            print(f"origem: {origem} destino: {destino} peso: {peso}")

    return len(vetorLetras)




def criaMatrizAdcjacencia():
    arq = input("Digite o nome do arquivo de entrada com extensao na pasta DATA:\n")
    arq = "entrada.txt" #apagar dps LEMBRAR!!!!!!!!!!!!!!!!!!!

    matriz = adicionaArestasVertices(arq)
    with open("data/" + arq, "r") as arquivo:
        for linha in arquivo:
            origem, destino, peso = linha.strip().split(",")
            matriz[converter(origem)+1][converter(destino)+1] = int(peso);
    return matriz