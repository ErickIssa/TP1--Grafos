from src.grafo import *
        

def verificaSeTemPasseio(g: Grafo) -> bool:

    visitados: list(bool) = [False] * 26


    for i in g.grafo:
        
        caminho = [-1]

        if posteriorTemCiclo(g,None,i,visitados,caminho):

            print("Existe pelo menos um passeio turístico.")
            return True
        
    print("Não existe passeio turístico com pelo menos 4 cidades.")
    return False

def ExemploDePasseio(g:Grafo):

    visitados: list(bool) = [False] * 26

    for i in g.grafo:

        caminho = [-1]

        if posteriorTemCiclo(g,None,i,visitados,caminho):

            for i in range(len(caminho)):

                if(i==0):
                    print(str(converter(caminho[i])) , end = " ")
                elif(i == len(caminho)-1):
                    print("-> " + str(converter(caminho[i])) + " " + "-> " + str(converter(caminho[0])))
                else:
                    print("-> " + str(converter(caminho[i])) , end = " ")

            return
        
    print("Não existe passeio turístico com pelo menos 4 cidades.")        


def temCiclo(g:Grafo,pai, atual, lista_visitados: list, caminho:list) -> bool:

    lista_visitados[atual] = True
    caminho.append(atual)

    for i in g.grafo[atual]:

        if(fechouCiclo(lista_visitados,i[0],pai)):
            
            counter = 0 
            while (counter<len(caminho)):
                if caminho[counter] == i[0]:
                    break
                counter+=1
            
            if(len(caminho)-counter >= 4):
                del caminho[:counter]
                return True
            
        elif(posteriorTemCiclo(g,atual,i[0],lista_visitados,caminho)):
            return True

    del caminho[-1]
    return False

def fechouCiclo(visitados: list,posterior: int,anterior:int):
    return visitados[posterior]== True and posterior != anterior

def posteriorTemCiclo(g:Grafo,atual:int,posterior:int,visitados:list,caminho:list):
    return visitados[posterior] == False and temCiclo(g, atual, posterior, visitados, caminho)