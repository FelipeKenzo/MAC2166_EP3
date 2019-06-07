def main():
    opcao = int(input("Opcao de jogo: "))
    n = int(input("Tamanho do tabuleiro: "))

    if (opcao == 0):
        opcao0(n)
    elif (opcao == 1):
        opcao1(n)
    elif (opcao == 2):
        opcao2(n)

def opcao0(n):
    """Opcao 0"""
    
    print("Tabuleiro inicial:", end = " ")
    tabInicial = tabuleiro(n)

    print("Tabuleiro final:", end = " ")
    tabFinal = tabuleiro(n)

    iguais = True
    for i in range(n):
        for j in range(n):
            if (tabInicial[i][j] != tabFinal[i][j]):
                iguais = False

    if (iguais):
        print("SIM")
    else:
        print("NAO")

def opcao1(n):
    """Opcao 1"""
    
def opcao2(n):
    """Opcao 2"""

def tabuleiro(n):
    """Inicializa um tabuleiro"""
    
    #inicialização do tabuleiro (matriz) nxn
    tabuleiro=[[0 for i in range(n)] for j in range(n)]
    
    #entrada de dados pelo usuário (não há validação de inputs)
    for i in range(n):
        row = input("")
        for j in range(n):
            tabuleiro[i][j] = int(row.split()[j])

    for i in range(n):
        for j in range(n):
            print(tabuleiro[i][j], end=" ")
        print("")
    
    return tabuleiro

def ladrilho(pmax):
    """Funcao recursiva que verifica se existe
       uma sequencia de pmax movimentos da
       configuracao atual ate final """

    existe = False

    return existe

#executa o programa em si
main()