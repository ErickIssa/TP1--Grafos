#so pra testar como importa
from src.MatrizAdjacencia import *


#--------------------------------------------------------------------------------

try:
    #ler_entrada();
    #vetorletras = defineTamMatriz();
    matriz = criaMatrizAdcjacencia()
    for linha in matriz:
        print(linha)

except FileNotFoundError:
    print(f"Arquivo nao encontrado")



