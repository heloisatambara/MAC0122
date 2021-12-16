
 # função para leitura dos arquivos
def func(arq):
    matriz = [] #declaro vetor
    texto = arq.readlines() #quebra as linhas do arquivo em vetores 
    
    for i in range(len(texto)):  # percorre os vetores
        texto[i] = texto[i].replace('\n', '').split(',')  # tira os '\n' e quebra nas vírgulas
        texto[i][1] = texto[i][1].split(' ') 

        
    return texto





def primo(a): # devolve os divisores de um número
    a = int(a)
    divisores = []
    for i in range(a):
        if i != 0 and i != a - 1:
            if a % (i + 1 )== 0:
                divisores.append(i+1)
    return divisores


def hash(a, M):
    s = 0
    # s conterá a soma dos valores numéricos dos caracteres
    for chr in a:
        s = s + ord(chr)
    return s % M


def hash2(a):
    k = 2
    div = primo(a)
    while k < a:
        if k in div: 
            k += 1
        else: break # para quando k e a forem primos entre si

    return k # valor da função - passo

    
def insere_hash(a, x, ind):
    M = len(a)
    cont = 0
    i = hash(x, M)
    k = hash2(M)
    # procura a próxima posição livre
    while a[i] != None:
        if x in a[i]:
            a[i].append(ind) # x já está na tabela, adiciona seu novo índice 
            return -1 
        cont += 1 # conta os elementos da tabela
        if cont == M: return -2 # tabela cheia
        i = (i + k) % M # tabela circular
    # achamos uma posição livre - coloque x nesta posição junto da sua posição na tabela original
    a[i] = [x, ind]
    return i


def busca_hash(a, x):
    M = len(a)
    cont = 0
    i = hash(x, M)
    k = hash2(M)
    # procura x a partir da posição i
    while a[i] == None or a[i][0] != x:
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
        if arq == 'fim': 
            break
        else:
            arq = open(arq, 'r')
             # Ler o arquivo de origem e colocar em TABarq
            TABarq = func(arq)
            tmax = 2*len(TABarq)#*len(TABarq[0][1])
            TAB = tmax * [None]
            for k in range(len(TABarq)):
                for j in range(len(TABarq[k][1])):
                    insere_hash(TAB, TABarq[k][1][j], k)
            print(TAB)
        
        while True:
            search = str.capitalize(input('Procurar nome: ')) # capitalize ajusta o valor de maiúsculas e minúsculas
            if search == 'Fim':
                arq.close() # fecha o arquivo para abrir um próximo
                break
            else: print(busca_hash(TAB, search))

main()
