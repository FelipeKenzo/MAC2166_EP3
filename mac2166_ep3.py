def opcao0(n, tabuleiro):
    """Opcao 1"""

def opcao1():
    """Opcao 2"""
    
def opcao2():
    """Opcao 1"""

def ladrilho(pmax):
    """Funcao recursiva que verifica se existe
       uma sequencia de pmax movimentos da
       configuracao atual ate final """

    existe = False

    return existe

def main():
    opcao = int(input("Opcao de jogo: "))
    n = int(input("Tamanho do tabuleiro: "))

    print("Tabuleiro inicial: ")

    tabuleiro=[]
    for i in range(n):
            tabuleiro[i][] = list(map(int, input().split()))
    
    print("\n")
    for i in range(n):
        for j in range(n):
            print(tabuleiro[i][j], " ")
    print("\n")

    if (opcao == 0):
        opcao0()
    elif (opcao == 1):
        opcao1()
    elif (opcao == 2):
        opcao2()

main()