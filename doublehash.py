def primo(a):
    a = int(a)
    divisores = []
    primo = True
    if a == 1:
        primo = False
    for i in range(a):
        if i != 0 and i != a - 1:
            if a % (i + 1 )== 0:
                primo = False
                divisores.append(i+1)
    return divisores


def hash(x, M):
    return x % M # valor da função


def hash2():
    x = 0
    M = 0
    a = hash(x, M)
    k = 2
    div = primo(a)
    while k < a:
        if k in div:
            k =+ 1
        else: break

    return k # valor da função - passo

    
def insere_hash(a, x):
    M = len(a)
    cont = 0
    i = hash(x, M)
    k = hash2()
    # procura a próxima posição livre
    while a[i] != None:
        if a[i] == x: return -1 # valor já existente na tabela
        cont += 1 # conta os elementos da tabela
        if cont == M: return -2 # tabela cheia
        i = (i + k) % M # tabela circular
    # achamos uma posição livre - coloque x nesta posição
    a[i] = x
    return i


def busca_hash(a, x):
    M = len(a)
    cont = 0
    i = hash(x, M)
    k = hash2()
    # procura x a partir da posição i
    while a[i] != x:
        if a[i] == None: return -1 # não achou x, pois há uma vazia
        cont += 1 # conta os elementos da tabela
        if cont == M: return -2; # a tabela está cheia
        i = (i + k) % M # tabela circular
    # encontrou
    return i
