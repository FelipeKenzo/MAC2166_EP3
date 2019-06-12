def main():
    opcao = int(input("Opcao de jogo: "))
    n = int(input("Tamanho do tabuleiro: "))

    if (n >= 2):
        #Roda a opção 0 <= opcao <= 2.
        if (opcao == 0):
            opcao0(n)
        elif (opcao == 1):
            opcao1(n)
        elif (opcao == 2):
            opcao2(n)
        #Opção adicionada para entender o algoritmo recursivo
        elif (opcao == 3):
            opcao3(n)


def opcao0(n):
    """Opção 0 (comparação de matrizes)."""
    
    #cria o tabuleiro inicial.
    print("Tabuleiro inicial:", end = " ")
    tabInicial = montarTabuleiro(n)
    #imprimir(tabInicial)

    #cria o tabuleiro final.
    print("Tabuleiro final:", end = " ")
    tabFinal = montarTabuleiro(n)
    #imprimir(tabFinal)

    if (saoIguais(tabInicial, tabFinal)):
        print("SIM")
    else:
        print("NAO")

def opcao1(n):
    """Opção 1 (movimentação)."""

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

    #entrada de dados de movimento pelo usuário.
    movimentos = input("Digite seq mov: ")

    # Apenas para debug. Deve ser retirado.
    #print("")
    #for i in range(m):
    #    print(movimentos[i], end = " ")
    #print("")

    i = 1
    conseguiu = True
    for m in movimentos:
        #print(m)
        if (not mover(m, tabuleiro, zero)):
            conseguiu = False
            print("NAO: ",i)
            break
        #imprimir(tabuleiro)
        i = i + 1
    
    if (conseguiu):
        print("Tabuleiro final:")
        imprimir(tabuleiro)

def opcao2(n):
    """Opção 2 (busca em profundidade)"""

    pmax = int(input("Profundidade maxima: "))

    print("Tabuleiro inicial:", end = " ")
    tabInicial = montarTabuleiro(n)

    print("Tabuleiro final:", end = " ")
    tabFinal = montarTabuleiro(n)

    p = 0
    listaMov = []

    #localiza a posição do 0 no tabuleiro. Assume que só há um 0.
    for i in range(n):
        for j in range(n):
            if (tabInicial[i][j] == 0):
                zero = [i, j] #salva as coordenadas do zero.

    if ladrilho(pmax, tabInicial, tabFinal, p, zero, '', listaMov):
        print("Sucesso!\nMovimentos:", end = " ")
        
        for m in listaMov:
            print (m, end=" ")

        print("")
        imprimir(tabInicial)
    else:
        print("Nao encontrei solucao")

def opcao3(n):
    """Opção de auxílio para entender o ladrilho(..)"""

    tabuleiro = montarTabuleiro(n)

    #localiza a posição do 0 no tabuleiro. Assume que só há um 0.
    for i in range(n):
        for j in range(n):
            if (tabuleiro[i][j] == 0):
                zero = [i, j] #salva as coordenadas do zero.

    while True:
        movimentos = input("Movimento: ")

        if (movimentos == 'q'):
            break

        for m in movimentos:
            mover(m, tabuleiro, zero)
            print("")
            imprimir(tabuleiro)
    
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

def saoIguais(tabuleiroA, tabuleiroB):
    iguais = True
    for i in range(len(tabuleiroA)):
        for j in range(len(tabuleiroA[i])):
            if (tabuleiroA[i][j] != tabuleiroB[i][j]):
                iguais = False
    
    return iguais

def mover(movimento, tabuleiro, posicao):
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
    n = len(tabuleiro)

    if (movimento ==  'c'):
        if (i <= 0): #limite superior
            return False
        aux = tabuleiro[i-1][j]             # copia elemento acima.
        tabuleiro[i-1][j] = tabuleiro[i][j] # sobrescreve o elemento acima.
        tabuleiro[i][j] = aux               # reinsere o elemento.
        posicao[0] = posicao[0] - 1

    elif (movimento ==  'b'):
        if (i >= n - 1): # limite inferior
            return False
        aux = tabuleiro[i+1][j]             # copia elemento abaixo.
        tabuleiro[i+1][j] = tabuleiro[i][j] # sobrescreve o elemento abaixo.
        tabuleiro[i][j] = aux               # reinsere o elemento.
        posicao[0] = posicao[0] + 1

    elif (movimento ==  'd'):
        if (j >= n - 1): #limite à direita
            return False
        aux = tabuleiro[i][j+1]             # copia elemento à direita.
        tabuleiro[i][j+1] = tabuleiro[i][j] # sobrescreve o elemento à direita.
        tabuleiro[i][j] = aux               # reinsere o elemento.
        posicao[1] = posicao[1] + 1

    elif (movimento ==  'e'):
        if (j <= 0): #limite superior
            return False
        aux = tabuleiro[i][j-1]             # copia elemento à esquerda.
        tabuleiro[i][j-1] = tabuleiro[i][j] # sobrescreve o elemento à esquerda.
        tabuleiro[i][j] = aux                 # reinsere o elemento.
        posicao[1] = posicao[1] - 1
    
    return True
    #imprimir(tabuleiro)

def imprimir(tabuleiro):
    """Imprime o tabuleiro na tela."""

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if (tabuleiro[i][j] <= 9):
                print(end = " ")
            print(tabuleiro[i][j], end=" ")
        print("")
    print("")

def ladrilho(pmax, Mat, Matfim, p, pos, mov, ListaMov):
    """Função recursiva que verifica se existe uma sequência de pmax
       movimentos da configuração atual até a final (mínima).
       É, em essência, um algoritmo de busca em largura."""

    #Cada chamada da função percorre um nível da recursão.
    #print(p)

    if (saoIguais(Mat, Matfim)):
        return True

    #Na primeira chamada, não há movimento que desfaça o anterior.
    #Só posso chamar a função após percorrer a profundidade inteira.
    #A única instância que possui conhecimento sobre qual é a profundidade
    # sendo varrida atualmente é a de profundidade 0.

    #Se a matriz não é igual logo quando chamada, temos que a profundidade é
    # necessáriamente >= 1.
    if (p == 0):
        p = 1

    while (p <= pmax):
        if ((mov != 'b') and mover('c', Mat, pos)):
            ListaMov.append('c')
            #print(ListaMov)
            if (p > len(ListaMov)): # se não é a primeira vez testando nessa profundidade
                if (ladrilho(pmax, Mat, Matfim, p, pos, 'c', ListaMov)):
                    return True
            elif (saoIguais(Mat, Matfim)):
                return True
            ListaMov.pop()
            #print(ListaMov)
            mover('b', Mat, pos)

        if ((mov != 'e') and mover('d', Mat, pos)):
            ListaMov.append('d')
            #print(ListaMov)
            if (p > len(ListaMov)): # se não é a primeira vez testando nessa profundidade
                if (ladrilho(pmax, Mat, Matfim, p, pos, 'd', ListaMov)):
                    return True
            elif (saoIguais(Mat, Matfim)):
                return True
            ListaMov.pop()
            #print(ListaMov)
            mover('e', Mat, pos)

        if ((mov != 'c') and mover('b', Mat, pos)):
            ListaMov.append('b')
            #print(ListaMov)
            if (p > len(ListaMov)): # se não é a primeira vez testando nessa profundidade
                if (ladrilho(pmax, Mat, Matfim, p, pos, 'b', ListaMov)):
                    return True
            elif (saoIguais(Mat, Matfim)):
                return True
            ListaMov.pop()
            #print(ListaMov)
            mover('c', Mat, pos)

        if ((mov != 'd') and mover('e', Mat, pos)):
            ListaMov.append('e')
            #print(ListaMov)
            if (p > len(ListaMov)): # se não é a primeira vez testando nessa profundidade
                if (ladrilho(pmax, Mat, Matfim, p, pos, 'e', ListaMov)):
                    return True
            elif (saoIguais(Mat, Matfim)):
                return True
            ListaMov.pop()
            #print(ListaMov)
            mover('d', Mat, pos)
        
        if (len(ListaMov) > 0 ): # se não é o primeiro nível da recursão, não percorro o laço.
            #print('saiu')
            return False
        p += 1
    
    return False

main()