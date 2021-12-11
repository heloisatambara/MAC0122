 # função para leitura dos arquivos
def func(arq):
    matriz = [] #declaro vetor
    texto = arq.readlines() #quebra as linhas do arquivo em vetores 
    
    for i in range(len(texto)):  # percorre os vetores
        texto[i] = texto[i].replace('\n', '')  # tira os '\n'
        matriz.append(texto[i].split(','))  # quebra nas vírgulas
        
    return matriz


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


def main():
    while True:
         # Pedir o nome do arquivo de origem (‘fim’: break)
        arq = input('Nome do arquivo de origem: ')
        if arq == 'fim': break
        else: arq = open(arq, 'r')
         # Ler o arquivo de origem e colocar em TAB (já com split(‘,’) dos campos)
        TAB = func(arq)
        
        while True:
            search = input('Procurar nome: ')
            if search == 'fim': break
            else: busca_hash(TAB, search)

main()
