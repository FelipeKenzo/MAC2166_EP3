def main():
    opcao = int(input("Opcao de jogo: "))
    n = int(input("Tamanho do tabuleiro: "))

    #Roda a opção 0 <= n <= 2.
    if (opcao == 0):
        opcao0(n)
    elif (opcao == 1):
        opcao1(n)
    elif (opcao == 2):
        opcao2(n)

def opcao0(n):
    """Opção 0."""
    
    #cria o tabuleiro inicial.
    print("Tabuleiro inicial:", end = " ")
    tabInicial = montarTabuleiro(n)
    #imprimir(tabInicial)

    #cria o tabuleiro final.
    print("Tabuleiro final:", end = " ")
    tabFinal = montarTabuleiro(n)
    #imprimir(tabFinal)

    #compara os tabuleiros valor a valor.
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
    """Opção 1."""

    #cria o tabuleiro inicial.
    print("Tabuleiro inicial:", end = " ")
    tabuleiro = montarTabuleiro(n)
    #imprimir(tab)
    
    #localiza a posição do 0 no tabuleiro. Assume que só há um 0.
    for i in range(n):
        for j in range(n):
            if (tabuleiro[i][j] == 0):
                zero = [i, j] #salva as coordenadas do zero.
    
    #print("zero: [",zero[0],"][",zero[1],"]")

    m = int(input("Insira o numero de movimentos: "))

    #inicialização da lista de movimentos
    movimentos = [None for i in range (m)]

    #entrada de dados pelo usuário. Cuidado: se não há o número exato de caracteres, dá pau.
    movimentos = input("Movimentos: ").split()

    # Apenas para debug. Deve ser retirado.
    #print("")
    #for i in range(m):
    #    print(movimentos[i], end = " ")
    #print("")

    for i in range(m):
        mover(movimentos[i], tabuleiro, zero, n)
    
    imprimir(tabuleiro)


def opcao2(n):
    """Opcao 2"""

def montarTabuleiro(n):
    """Monta um tabuleiro."""
    
    #inicialização do tabuleiro (matriz) nxn
    tabuleiro = [[0 for i in range(n)] for j in range(n)]
    
    #entrada de dados pelo usuário (não há validação de inputs)
    for i in range(n):
        linha = input("")
        for j in range(n):
            tabuleiro[i][j] = int(linha.split()[j])

    # Apenas para fins de debug. Deve ser retirado.
    # imrimir(tabuleiro)
    
    return tabuleiro

def mover(movimento, tabuleiro, posicao, n):
    """Move um elemento qualquer de um tabuleiro"""
    # Argumentos são passados por referência :D
    
    # Lembrando que:
    #   0 1 2
    # 0 a b c
    # 1 d e f
    # 2 g h i

    # Apenas para facilitar a leitura
    i = posicao[0] # linha
    j = posicao[1] # coluna

    if (movimento ==  'c'):
        if (i <= 0): #limite superior
            print("NAO")
            return
        aux = tabuleiro[i-1][j]             # copia elemento acima.
        tabuleiro[i-1][j] = tabuleiro[i][j] # sobrescreve o elemento acima.
        tabuleiro[i][j] = aux               # reinsere o elemento.
        posicao[0] = posicao[0] - 1

    elif (movimento ==  'b'):
        if (i >= n - 1): # limite inferior
            print("NAO")
            return
        aux = tabuleiro[i+1][j]             # copia elemento abaixo.
        tabuleiro[i+1][j] = tabuleiro[i][j] # sobrescreve o elemento abaixo.
        tabuleiro[i][j] = aux               # reinsere o elemento.
        posicao[0] = posicao[0] + 1

    elif (movimento ==  'd'):
        if (j >= n - 1): #limite à direita
            print("NAO")
            return
        aux = tabuleiro[i][j+1]             # copia elemento à direita.
        tabuleiro[i][j+1] = tabuleiro[i][j] # sobrescreve o elemento à direita.
        tabuleiro[i][j] = aux               # reinsere o elemento.
        posicao[1] = posicao[1] + 1

    elif (movimento ==  'e'):
        if (j <= 0): #limite superior
            print("NAO")
            return
        aux = tabuleiro[i][j-1]             # copia elemento à esquerda.
        tabuleiro[i][j-1] = tabuleiro[i][j] # sobrescreve o elemento à esquerda.
        tabuleiro[i][j] = aux                 # reinsere o elemento.
        posicao[1] = posicao[1] - 1
    
    #imprimir(tabuleiro)

def imprimir(tabuleiro):
    """Imprime o tabuleiro na tela."""
    print("")
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j], end=" ")
        print("")
    print("")

def ladrilho(pmax):
    """Funcao recursiva que verifica se existe uma sequência de pmax
       movimentos da configuracao atual atá final """

    existe = False

    return existe

#executa o programa em si
main()