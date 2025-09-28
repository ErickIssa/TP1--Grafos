from src.conectividade import *
from src.grafo import *
from src.articulacao import *
from src.passeioTuristico import *


def criaGrafobyTxt(arq): #constroi grafo apartir do arqv de txt
    g = Articulacao(defineQntdArestas(arq))
    with open("data/" + arq, "r") as arquivo:
        for linha in arquivo:
            origem, destino, peso = linha.strip().split(",")
            g.adiciona_aresta(converter(origem), converter(destino), peso)
            #print(f"origem: {origem} destino: {destino} peso: {peso}")
    return g


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
        print("0 - Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opcao Invalida -- Digite um Numero Valido:")
            continue

        match opcao:
            case 1:
                print()
            case 2:
                print()
            case 3:
                print()
            case 4:
               letraVizinhos = input("Digite a Letra que representa a cidade:") 
               print("A quantidade de vizinhos do vertice (%s) e %d" % (letraVizinhos, g.quantidadeVizinhos(letraVizinhos)))
            case 5:
               print()
            case 6:
                vertices, pai, conectados = Conectividade.verificaConectividade(g, 0)
                print("O grafo é conexo?", conectados)
            case 7:
                aps = g.encontraArticulacao()
                print("Pontos de articulação:", aps)
            case 8:
                verificaSeTemPasseio(g)
                print()
            case 9:
                ExemploDePasseio(g)
                print()
            case 0:
                print("-------Execucao Encerrada---------")
                break
            case _:
                print("/////Opcao Invalida/////")
