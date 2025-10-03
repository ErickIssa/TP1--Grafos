from src.grafo import *
from src.articulacao import *
from src.passeioTuristico import *
from src.conectividade import *

def criaGrafobyTxt(arq): #constroi grafo apartir do arqv de txt
    g = Grafo(defineQntdVertices(arq))
    with open("data/" + arq, "r") as arquivo:
        for linha in arquivo:
            origem, destino, peso = linha.strip().split(",")
            g.adiciona_aresta(converter(origem), converter(destino), peso)
            #print(f"origem: {origem} destino: {destino} peso: {peso}")
    return g

def converterParaArticulacao(g):
    novo = Articulacao(g.V)
    for u in g.grafo:
        for v, peso in g.grafo[u]:
            if u < v:
                novo.adiciona_aresta(u, v, peso)
    return novo


def converterParaConectividade(g):
    novo = Conectividade(g.V)
    for u in g.grafo:
        for v, peso in g.grafo[u]:
            if u < v:
                novo.adiciona_aresta(u, v, peso)
    return novo



def menu():
        
   

    while True:
        opcao = (input("Digite o nome do arquivo de texto que está na pasta DATA com sua extensão(Exemplo: entrada.txt)(0 para sair):"))
        arq = opcao #APAGAR ISSO DPS E COLOCAR UMA VERIFICAÇÃO PARA CASO DE ERRADO USAR UM ARQV GENERICO
        try:  
            g = criaGrafobyTxt(arq)
            break
        except :
            if opcao == "0":
                print("-------Execucao Encerrada---------")
                return
            print("arquivo inválido, tente novamente (lembre-se de adicionar o .txt no final)")
        
            


    
    while True:
        print("\n===== MENU =====")
        print("1 - Retornar o número de cidades no grafo")
        print("2 - Retornar a quantidade de estradas no grafo")
        print("3 - Retornar os vizinhos de uma cidade fornecida")
        print("4 - Determinar a quantidade de vizinhos de uma cidade fornecida")
        print("5 - Calcular o menor caminho entre duas cidades escolhidas")
        print("6 - Verificar se a rede é conexa")
        print("7 - Identificar cidades críticas (articulação)")
        print("8 - Verificar se existe passeio turístico (ciclo >= 4)")
        print("9 - Exibir exemplo de passeio turístico (se existir)")
        print("10 - Digitar um novo nome do arquivo de texto (na pasta DATA com sua extensão):")
        print("0 - Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opcao Invalida -- Digite um Numero Valido:")
            continue

        match opcao:
            case 1:
                print("A quantidade de cidades é de: ", g.V)
            case 2:
                print("A quantidade de Arestas é:", g.contaArestas());
            case 3:
                cidade = input("Digite a Letra que representa a cidade:")
                print("As cidades vizinhas são: %s" % g.buscaVizinhos(cidade))
            case 4:
               letraVizinhos = input("Digite a Letra que representa a cidade:") 
               print("A quantidade de vizinhos do vertice (%s) é de %d cidade(s) " % (letraVizinhos, g.quantidadeVizinhos(letraVizinhos)))

            case 5:
                origem = input("Digite a cidade de origem: ")
                destino = input("Digite a cidade de destino: ")

                dist, caminho = menorCaminhoDijkstra(g, converter(origem), converter(destino))
                caminho_letras = [converter(c) for c in caminho]

                if dist == float("inf"):
                    print(f"Não existe caminho de {origem} até {destino}.")
                else:
                    print(f"Menor distância de {origem} até {destino} = {dist}")
                    print("Caminho:", " -> ".join(caminho_letras))

            
            case 6:
                gConect = converterParaConectividade(g)
                vertices, pai, conectados = gConect.verificaConectividade(0)
                #print("Árvore DFS (arestas):", vertices)
                print("O grafo é conexo?", conectados)

            case 7:
                gArt = converterParaArticulacao(g)
                aps = gArt.encontraArticulacao()
                print("Pontos de articulação:", aps)
            case 8:
                verificaSeTemPasseio(g)
                print()
            case 9:
                ExemploDePasseio(g)
                print()
            case 10:
                arq = (input("Digite o nome do arquivo de texto que está na pasta DATA com sua extensão:"))
                g = criaGrafobyTxt(arq)
            case 0:
                print("-------Execucao Encerrada---------")
                break
            
            case _:
                print("/////Opcao Invalida/////")
