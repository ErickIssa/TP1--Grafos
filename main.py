from src.menorcaminho import * #so pra testar como importa

def ler_entrada():

    arq = input("Digite o nome do arquivo de entrada, juntamente com sua extensão que está localizado na pasta data:\n") 
    with open("data/" + arq, "r") as arquivo: #esse "r" e de read pra apenas ler a entrada
        for linha in arquivo:
            origem, destino, peso = linha.split(",")
            peso = int(peso);
            print(f"origem: {origem} destino: {destino} peso: {peso}")

#--------------------------------------------------------------------------------

try:
    ler_entrada();

except FileNotFoundError:
    print(f"Arquivo nao encontrado")



